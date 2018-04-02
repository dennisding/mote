# -*- coding:utf-8 -*-

from . import component

from .. import math3d

class pos(component.component):
	__slots__ = ('pos',)
	def __init__(self, x = 0, y = 0, z = 0):
		super(pos, self).__init__()

		self.pos = math3d.vec(x, y, z)
