# -*- coding:utf-8 -*-

import app

from . import system

class move(system.system):
	reads = ('pos', 'speed')
	writes = ('pos',)

	def __init__(self):
		super(move, self).__init__()

	def tick(self, entity):
		pos = entity.get_component('pos')
		speed = entity.get_component('speed')

		pos.value += (speed.value * app.delta)
