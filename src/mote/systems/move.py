# -*- coding:utf-8 -*-

from . import system

class move(system.system):
	reads = ('pos', 'speed')
	writes = ('pos',)

	def __init__(self):
		super(move, self).__init__()

	def tick(self, delta, entity):
		pos = entity.get_component('pos')
		speed = entity.get_component('speed')

		pos.x += speed.x * delta
		pos.y += speed.y * delta
		pos.z += speed.z * delta
