# -*- coding:utf-8 -*-

import numpy

from . import component

class pos(component.component):
	__slots__ = ('pos',)
	def __init__(self, x = 0, y = 0, z = 0):
		super(pos, self).__init__()

		self.pos = numpy.array((x, y, z))
