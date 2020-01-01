#-*- coding: UTF-8 -*-
from Products.CMFCore.utils import getToolByName
 
from cms.policy.testing import FunctionalTesting
from plone.app.testing import TEST_USER_ID, login, TEST_USER_NAME, \
    TEST_USER_PASSWORD, setRoles
import json
import hmac
from hashlib import sha1 as sha
from datetime import date
from datetime import datetime
from Products.CMFCore.utils import getToolByName
from cms.db.testing import FUNCTIONAL_TESTING  

from zope.component import getUtility
from zope.interface import alsoProvides
from plone.keyring.interfaces import IKeyManager
from plone.testing.z2 import Browser
import unittest

from cms.theme.interfaces import IThemeSpecific

class TestView(unittest.TestCase):
    
    layer = FunctionalTesting
    def setUp(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ('Manager',))
        portal.invokeFactory('cms.db.folder', 'folder') 
        portal['folder'].invokeFactory('cms.db.wuyunfolder', 'kbfolder')
        portal['folder']['kbfolder'].invokeFactory('cms.db.wuyun', 'f1')
        file = portal['folder']['kbfolder']
       
        file.title = "My File"
        file.description = "This is my file."
        
                
           
        self.portal = portal
    
         
 
    def test_homepage_view(self):
        request = self.layer['request']
        alsoProvides(request, IThemeSpecific)        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'size': '10',
                        'start':'0' ,
                        'sortcolumn':'created',
                        'datetype':"0",
                        'objid':"",
                        'tag':"a,b,c",
                        'sortdirection':'desc',
                        'searchabletext':''                                                                       
                        }
# Look up and invoke the view via traversal
        box = self.portal
        view = box.restrictedTraverse('@@ajax_db_search')
        result = view()       
        self.assertEqual(json.loads(result)['total'],2)       
   