# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime
from Products.CMFPlone.interfaces.constrains import ISelectableConstrainTypes
from zope.lifecycleevent import ObjectModifiedEvent
from plone import api
from plone.app.dexterity.behaviors import constrains
from logging import getLogger
from zope import event
from z3c.relationfield import RelationValue
from zope.component import getUtility


from cms.db.tests.base import inputvalues, fire_created_event

logger = getLogger(__name__)


STRUCTURE = [
    {
        'type': 'cms.db.folder',
        'title': u'中医系统',
        'id': 'root',
        'description': u'中医系统',
        'layout': 'folder_contents',
        'children': [
                     {
                      'type': 'cms.db.ormfolder',
                      'title': u'数据库',
                      'id': 'ormfolder',
                      'description': u'数据库',
                      'layout': 'yaoxing_listings',
                     },

                     {
                     'type': 'cms.db.yaofolder',
                     'title': u'药',
                     'id': 'yaofolder',
                     'description': u'药',
                     'layout': 'sysajax_listings',            
                      },                          
                     {
                     'type': 'cms.db.danweifolder',
                     'title': u'单位',
                     'id': 'danweifolder',
                     'description': u'单位',
                     'layout': 'sysajax_listings',            
                      },
                     {
                     'type': 'cms.db.yishengfolder',
                     'title': u'医生',
                     'id': 'yishengfolder',
                     'description': u'医生',
                     'layout': 'sysajax_listings',            
                      },
                     {
                     'type': 'cms.db.bingrenfolder',
                     'title': u'病人',
                     'id': 'bingrenfolder',
                     'description': u'病人',
                     'layout': 'sysajax_listings',            
                      },
                     {
                     'type': 'cms.db.chufangfolder',
                     'title': u'处方',
                     'id': 'chufangfolder',
                     'description': u'处方',
                     'layout': 'sysajax_listings',            
                      },                                                                                                

                ]
}
]



def isNotCurrentProfile(context):
    return context.readDataFile('policy_marker.txt') is None

def setupGroups(context):
    """create emc management groups and management users
    """
    from cms.memberArea.events import BackMemberCreatedEvent
    group = api.group.create(
            groupname='System Administrators',
            title='System Administrators',
            description='EMC System Administrators',
            roles=['SysAdmin',],
            ) 
    group = api.group.create(
            groupname='Secure Staffs',
            title='Secure Staffs',
            description='EMC Secure Staffs',
            roles=['SecStaff', ],
            ) 
    group = api.group.create(
            groupname='Secure Auditors',
            title='Secure Auditors',
            description='EMC Secure Auditors',
            roles=['SecAuditor', ],
            )
    properties= dict(fullname=u'李四'.encode('utf-8'))
    demo = api.user.create(
            username='333010199106113321' ,
            email='lisi@plone.org',
            password='secret$',
            properties=properties
                               )
    if demo != None:
        event.notify(BackMemberCreatedEvent(demo))    
    properties= dict(fullname=u'系统管理员'.encode('utf-8'))
    demo = api.user.create(
            username='111111222222333333' ,
            email='sysadmin@plone.org',
            password='secret$',
            properties=properties
                               )
    if demo != None:
        event.notify(BackMemberCreatedEvent(demo))
    properties= dict(fullname=u'安全管理员'.encode('utf-8'))
    demo = api.user.create(
            username='444444555555666666' ,
            email='secstaff@plone.org',
            password='secret$',
            properties=properties
                               )
    if demo != None:
        event.notify(BackMemberCreatedEvent(demo))
    properties= dict(fullname=u'安全审计员'.encode('utf-8'))
    demo = api.user.create(
            username='777777888888999999' ,
            email='secauditor@plone.org',
            password='secret$',
            properties=properties
                               )
    if demo != None:
        event.notify(BackMemberCreatedEvent(demo))                    
    api.group.add_user(groupname='System Administrators', username='111111222222333333')
    api.group.add_user(groupname='Secure Staffs', username='444444555555666666')
    api.group.add_user(groupname='Secure Auditors', username='777777888888999999')


# def run_after(context):
def post_install(context):
    """post Setuphandler for the profile 'default'
    """
    if isNotCurrentProfile(context):
        return
    # Do something during the installation of this package
#     return
    portal = api.portal.get()
    defaulpage = portal.get('front-page', None)
    if defaulpage is not None:
        api.content.delete(defaulpage)    
    members = portal.get('events', None)
    if members is not None:
        api.content.delete(members)
    members = portal.get('news', None)
    if members is not None:
        api.content.delete(members)
    members = portal.get('Members', None)
    if members is not None:
       members.exclude_from_nav = True
       members.reindexObject()
       # give admin create memberarea
   
    for item in STRUCTURE:
        _create_content(item, portal)

    inputvalues()
    fire_created_event() 

#     setupGroups(context)    

#     try:
#         add_navigator_portlet(context)
#     except:
#         pass
                                                                
def _create_content(item, container):
    new = container.get(item['id'], None)
    if not new:
        new = api.content.create(
            type=item['type'],
            container=container,
            title=item['title'],
            description=item['description'],            
            id=item['id'],
            safe_id=False)
        logger.info('Created item {}'.format(new.absolute_url()))
    if item.get('layout', False):
        new.setLayout(item['layout'])
    if item.get('default-page', False):
        new.setDefaultPage(item['default-page'])
    if item.get('allowed_types', False):
        _constrain(new, item['allowed_types'])
    if item.get('local_roles', False):
        for local_role in item['local_roles']:
            api.group.grant_roles(
                groupname=local_role['group'],
                roles=local_role['roles'],
                obj=new)
    if item.get('publish', False):
        api.content.transition(new, to_state=item.get('state', 'published'))
    new.reindexObject()
    # call recursively for children
    for subitem in item.get('children', []):
        _create_content(subitem, new)


def _constrain(context, allowed_types):
    behavior = ISelectableConstrainTypes(context)
    behavior.setConstrainTypesMode(constrains.ENABLED)
    behavior.setLocallyAllowedTypes(allowed_types)
    behavior.setImmediatelyAddableTypes(allowed_types)
