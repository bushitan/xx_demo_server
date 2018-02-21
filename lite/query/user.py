# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
from django.db.models import Q
class QueryUser(QueryBase):
	def _PackDict(self,query_get):
		_dict = {
			'session':query_get.session,
			'logo':query_get.logo,
			'nick_name':query_get.nick_name,
		}
		return _dict

	def Set(self,*args,**kwargs):
		_user = User(*args,**kwargs)
		_user.save()
		return self._PackDict(_user)
	def GetDict(self, *args, **kwargs):
		_query = User.objects.get(*args,**kwargs)
		return self._PackDict(_query)
	def IsExists(self, *args, **kwargs):
		return User.objects.filter(*args, **kwargs).exists()


if __name__ == "__main__":
	query_user = QueryUser()
	print query_user.GetDict(session = "12321321")