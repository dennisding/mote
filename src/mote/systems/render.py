# -*- coding:utf-8 -*-

from . import system

class render(system.system):
	reads = ('pos', 'visual', 'visible')
	def pre_tick(self):
		pass

	def post_tick(self):
		pass

	def tick(self, entity):
		return
		print('render!!!!!!!!', entity)
