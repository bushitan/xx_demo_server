#coding:utf-8

from django.views.generic import ListView
from lib.message import *
from action.login import *
class Index( ListView):
    def get(self, request, *args, **kwargs):
        try:
            print 11111
            _s_js_code = request.GET.get('js_code',"")
            _s_session = request.GET.get('session',"")
            _login = ActionLogin()
            _login.CheckSession(_s_js_code,_s_session)
            _dict = {
                'MSG':u'登录初始化成狗',
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            a = Exception
            print Exception
            print e
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

    def post(self, request, *args, **kwargs):
        try:
            _str_hash = request.POST['hash']
            _dict = {
                'MSG':u'登录初始化成狗',
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
