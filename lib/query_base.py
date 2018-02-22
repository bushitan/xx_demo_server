#coding:utf-8
class QueryBase(object):
	def __init__(self,model = None):
		self.model = model
		print self.model
	def _PackList(self,_pack_fun,query_filter):
		_list = []
		for q in query_filter:
			_list.append( _pack_fun(q) )
		return _list

	def _PackDict(self,*args, **kwargs):
		pass

	def IsExists(self, *args, **kwargs):
		return self.model.objects.filter(*args, **kwargs).exists()

	def Add(self,*args,**kwargs):
		_m = self.model(*args,**kwargs)
		_m.save()
		return self._PackDict(_m)

	def Get(self,*args,**kwargs):
		_m = self.model.objects.get(*args,**kwargs)
		return self._PackDict(_m)

	def Filter(self,*args,**kwargs):
		_m = self.model.objects.filter(*args,**kwargs)
		return self._PackList( self._PackDict,_m)

	def Update(self,*args,**kwargs):
		pass

	def Delete(self,*args,**kwargs):
		_m = self.model.delete(*args,**kwargs)
		_m.save()
		return self._PackDict(_m)