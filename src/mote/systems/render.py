# -*- coding:utf-8 -*-

from . import system

class render(system.system):
	reads = ('pos', 'visual', 'visible')

	def post_tick(self):
		pass

	def tick(self, entity):
		print('render tick', entity)
