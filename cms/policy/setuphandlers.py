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

from cms.db import  Session
from cms.db.orm import YaoWei,YaoXing,JingLuo,Yao
from cms.db.orm import ChuFang,BingRen,DiZhi,DanWei,YiSheng
from cms.db.orm import Yao_ChuFang_Asso,ChuFang_BingRen_Asso

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
            'layout': 'folder_contents'
            }                          

                ]
}
]

def initdb(context):
        "enter initial recorders to db"

        yaowei1 = YaoWei("酸")
        yaowei2 = YaoWei("苦")
        yaowei3 = YaoWei("甘")
        yaowei4 = YaoWei("辛")
        yaowei5 = YaoWei("咸")
        Session.add_all([yaowei1,yaowei2,yaowei3,yaowei4,yaowei5])
        yaoxing1 = YaoXing("大热")
        yaoxing2 = YaoXing("热")
        yaoxing3 = YaoXing("温")
        yaoxing4 = YaoXing("凉")
        yaoxing5 = YaoXing("寒")
        yaoxing6 = YaoXing("大寒")
        Session.add_all([yaoxing1,yaoxing2,yaoxing3,yaoxing4,yaoxing5,yaoxing6])
        jingluo1 = JingLuo("足太阳膀胱经")
        jingluo2 = JingLuo("足阳明胃经")
        jingluo3 = JingLuo("足少阳胆经")
        jingluo4 = JingLuo("足厥阴肝经")
        jingluo5 = JingLuo("足少阴肾经")
        jingluo6 = JingLuo("足太阴脾经")
        Session.add_all([jingluo1,jingluo2,jingluo3,jingluo4,jingluo5,jingluo6])
        yao1 = Yao("白芍")
        yao1.yaowei = yaowei1
        yao1.yaoxing = yaoxing1
        yao1.guijing = [jingluo1]         
        yao2 = Yao("大枣")
        yao2.yaowei = yaowei2
        yao2.yaoxing = yaoxing2
        yao2.guijing = [jingluo2]
        Session.add_all([yao1,yao2])        
        dizhi = DiZhi("中国","湖南","湘潭市","湘潭县云湖桥镇北岸村道林组83号")
        bingren = BingRen('张三',1, date(2015, 4, 2),'13673265899')
        bingren.dizhi = dizhi
        dizhi2 = DiZhi("中国","湖北","十堰市","茅箭区施洋路83号")
        danwei = DanWei("任之堂")
        yisheng = YiSheng('余浩',1, date(2015, 4, 2),'13673265859')
        danwei.yishengs = [yisheng]
        danwei.dizhi = dizhi2
        chufang = ChuFang("桂枝汤","加热稀粥",5)
        yao_chufang = Yao_ChuFang_Asso(yao1,chufang,7,"晒干")
        yao_chufang2 = Yao_ChuFang_Asso(yao2,chufang,10,"掰开")
        chufang_bingren = ChuFang_BingRen_Asso(bingren,chufang,datetime.now())
        yisheng.chufangs = [chufang]
        Session.add_all([dizhi,bingren,danwei,dizhi2,yisheng,chufang,yao_chufang,yao_chufang2,chufang_bingren])                         
        Session.commit()

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
        
    # initial db
    initdb(context) 

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
