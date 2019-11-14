#-*- coding: UTF-8 -*-
from zope.i18nmessageid import MessageFactory

fmt = "%Y-%m-%d %H:%M:%S"
_ = MessageFactory('cms.policy')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
