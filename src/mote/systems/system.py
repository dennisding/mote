# -*- coding:utf-8 -*-

class system:
	reads = ()
	writes = ()

	def __init__(self):
		pass

	def pre_tick(self):
		return True

	def post_tick(self):
		pass

	def tick(self, entity):
		pass
