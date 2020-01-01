#-*- coding: UTF-8 -*-
import json
from plone.memoize.instance import memoize
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import ISiteRoot
from cms.policy import _

from cms.theme.interfaces import IThemeSpecific
from cms.db.browser.sysajax_listings import SysAjaxListingView,Ajaxsearch
from cms.db.contents.wuyunfolder import IWuyunfolder


class FrontpageView(SysAjaxListingView):     
       
    @memoize
    def getPathQuery(self,objid=None,justchildrens=True):
        """返回 知识库目录
        """
        query = {}
        kb = self.getWuyunfolder()
        path = "/".join(kb.getPhysicalPath())
        if justchildrens:
            pathdic = {'depth':1}
            pathdic['query'] = path
            query['path'] = pathdic            
        elif bool(objid):
            query2 = {}
            query2['id'] = objid
            bn = self.catalog()(query2)
            if len(bn) >=1:
                path = bn[0].getPath()
                query['path'] = path
            else:
                query['path'] = path                                             
        else:
            query['path'] = path                             
        return query        
       

    def getWuyunfolder(self):        
        brains = self.catalog()({'object_provides':IWuyunfolder.__identifier__})
        context = brains[0].getObject()
        return context        
        
class Search(Ajaxsearch):    
    
    def __call__(self):    
        searchview = getMultiAdapter((self.context, self.request),name=u"index.html")        
 # datadic receive front ajax post data       
        datadic = self.request.form
        start = int(datadic['start']) # batch search start position
        datekey = int(datadic['datetype'])  # 对应 最近一周，一月，一年……
        size = int(datadic['size'])      # batch search size 

        tag = datadic['tag'].strip()
        sortcolumn = datadic['sortcolumn']
        sortdirection = datadic['sortdirection']
        keyword = (datadic['searchabletext']).strip()

        origquery = searchview.getPathQuery()
        origquery['sort_on'] = sortcolumn  
        origquery['sort_order'] = sortdirection                
 #模糊搜索       
        if keyword != "":
            origquery['SearchableText'] = '*'+keyword+'*'        

        if datekey != 0:
            origquery['created'] = self.Datecondition(datekey)
        # remove repeat values 
        tag = tag.split(',')
        tag = set(tag)
        tag = list(tag)
        all = u"所有".encode("utf-8")
        unclass = u"未分类".encode("utf-8")        
# filter contain "u'所有'"
        tag = filter(lambda x: all not in x, tag)
# recover un-category tag (remove:u"未分类-")
        def recovery(value):
            if unclass not in value:return value
            return value.split('-')[1]
            
        tag = map(recovery,tag)        
        if '0' in tag and len(tag) > 1:
            tag.remove('0')
            rule = {"query":tag,"operator":"and"}
            origquery['Subject'] = rule                      
#totalquery  search all 
        totalquery = origquery.copy()
#origquery provide  batch search        
        origquery['b_size'] = size 
        origquery['b_start'] = start
        # search all                         
        totalbrains = searchview.search_multicondition(totalquery)
        totalnum = len(totalbrains)
        # batch search         
        braindata = searchview.search_multicondition(origquery)
#        brainnum = len(braindata)         
        del origquery 
        del totalquery,totalbrains
#call output function        
        data = self.output(start,size,totalnum, braindata)
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(data)     
            
