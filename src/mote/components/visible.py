# -*- coding:utf-8 -*-

from . import component

class visible(component.component):
	def __init__(self):
		self.world_transform = None
		self.vertex = None
		self.program = None
