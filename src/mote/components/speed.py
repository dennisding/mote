# -*- coding:utf-8 -*-

from . import component

class speed(component.component):
	def __init__(self, x = 0, y = 0, z = 0):
		super(speed, self).__init__()

		self.x = x
		self.y = y
		self.z = z