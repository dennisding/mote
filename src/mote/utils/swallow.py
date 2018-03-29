# -*- coding:utf-8 -*-

class swallow( object ):
	def __getattr__(self, name):
		return self

	def __setattr__(self, name, value):
		return self

	def __delattr__(self, name, value):
		return self

	def __nonzero__(self):
		return False

	def __call__(self, *argv, **kwds):
		return self

	def __contains__(self, item):
		return False

	def __iter__(self):
		return self

	def __add__(self, other):
		return self

	def __rmul__(self, other):
		return self

	def next(self):
		raise StopIteration()