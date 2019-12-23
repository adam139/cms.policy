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
                     {
                     'type': 'cms.db.wuyunfolder',
                     'title': u'五运六气',
                     'id': 'chufangfolder',
                     'description': u'五运六气',
                     'layout': 'sysajax_listings',
                     'children': [
                                  {'type': 'cms.db.wuyun',
                                   'title': u'甲子',
                                   'id': '1',
                                   'description': u'甲子年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'乙丑',
                                   'id': '2',
                                   'description': u'乙丑年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丙寅',
                                   'id': '3',
                                   'description': u'丙寅年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丁卯',
                                   'id': '4',
                                   'description': u'丁卯年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'戊辰',
                                   'id': '5',
                                   'description': u'戊辰年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'己巳',
                                   'id': '6',
                                   'description': u'己巳年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'庚午',
                                   'id': '7',
                                   'description': u'庚午年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'辛未',
                                   'id': '8',
                                   'description': u'辛未年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'壬申',
                                   'id': '9',
                                   'description': u'壬申年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'癸酉',
                                   'id': '10',
                                   'description': u'癸酉年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'甲戌',
                                   'id': '11',
                                   'description': u'甲戌年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'乙亥',
                                   'id': '12',
                                   'description': u'乙亥年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丙子',
                                   'id': '13',
                                   'description': u'丙子年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丁丑',
                                   'id': '14',
                                   'description': u'丁丑年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'戊寅',
                                   'id': '15',
                                   'description': u'戊寅年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'己卯',
                                   'id': '16',
                                   'description': u'己卯年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'庚辰',
                                   'id': '17',
                                   'description': u'庚辰年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'辛巳',
                                   'id': '18',
                                   'description': u'辛巳年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'壬午',
                                   'id': '19',
                                   'description': u'壬午年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'癸未',
                                   'id': '20',
                                   'description': u'癸未年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'甲申',
                                   'id': '21',
                                   'description': u'甲申年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'乙酉',
                                   'id': '22',
                                   'description': u'乙酉年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丙戌',
                                   'id': '23',
                                   'description': u'丙戌年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丁亥',
                                   'id': '24',
                                   'description': u'丁亥年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'戊子',
                                   'id': '25',
                                   'description': u'戊子年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'己丑',
                                   'id': '26',
                                   'description': u'己丑年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'庚寅',
                                   'id': '27',
                                   'description': u'庚寅年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'辛卯',
                                   'id': '28',
                                   'description': u'辛卯年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'壬辰',
                                   'id': '29',
                                   'description': u'壬辰年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'癸巳',
                                   'id': '30',
                                   'description': u'癸巳年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'甲午',
                                   'id': '31',
                                   'description': u'甲午年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'乙未',
                                   'id': '32',
                                   'description': u'乙未年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丙申',
                                   'id': '33',
                                   'description': u'丙申年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丁酉',
                                   'id': '34',
                                   'description': u'丁酉年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'戊戌',
                                   'id': '35',
                                   'description': u'戊戌年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'己亥',
                                   'id': '36',
                                   'description': u'己亥年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'庚子',
                                   'id': '37',
                                   'description': u'庚子年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'辛丑',
                                   'id': '38',
                                   'description': u'辛丑年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'壬寅',
                                   'id': '39',
                                   'description': u'壬寅年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'癸卯',
                                   'id': '40',
                                   'description': u'癸卯年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'甲辰',
                                   'id': '41',
                                   'description': u'甲辰年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'乙巳',
                                   'id': '42',
                                   'description': u'乙巳年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丙午',
                                   'id': '43',
                                   'description': u'丙午年五运六气',
                                   'layout': 'base_view'
                                   }, 
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丁未',
                                   'id': '44',
                                   'description': u'丁未年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'戊申',
                                   'id': '45',
                                   'description': u'戊申年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'己酉',
                                   'id': '46',
                                   'description': u'己酉年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'庚戌',
                                   'id': '47',
                                   'description': u'庚戌年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'辛亥',
                                   'id': '48',
                                   'description': u'辛亥年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'壬子',
                                   'id': '49',
                                   'description': u'壬子年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'癸丑',
                                   'id': '50',
                                   'description': u'癸丑年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'甲寅',
                                   'id': '51',
                                   'description': u'甲寅年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'乙卯',
                                   'id': '52',
                                   'description': u'乙卯年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丙辰',
                                   'id': '53',
                                   'description': u'丙辰年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'丁巳',
                                   'id': '54',
                                   'description': u'丁巳年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'戊午',
                                   'id': '55',
                                   'description': u'戊午年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'己未',
                                   'id': '56',
                                   'description': u'己未年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'庚申',
                                   'id': '57',
                                   'description': u'庚申年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'辛酉',
                                   'id': '58',
                                   'description': u'辛酉年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'壬戌',
                                   'id': '59',
                                   'description': u'壬戌年五运六气',
                                   'layout': 'base_view'
                                   },
                                  {'type': 'cms.db.wuyun',
                                   'title': u'癸亥',
                                   'id': '60',
                                   'description': u'癸亥年五运六气',
                                   'layout': 'base_view'
                                   },                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                                  ]            
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
