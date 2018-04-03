# -*- coding:utf-8 -*-

from . import component

from .. import math3d

class speed(component.component):
	def __init__(self, x = 0, y = 0, z = 0):
		super(speed, self).__init__()

		self.value = math3d.vec(x, y, z)