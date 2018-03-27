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

		pos.x += speed.x * app.delta
		pos.y += speed.y * app.delta
		pos.z += speed.z * app.delta

		print('move pos', pos.x, pos.y, pos.z)