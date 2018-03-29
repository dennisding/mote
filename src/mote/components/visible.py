# -*- coding:utf-8 -*-

from . import component

class visible(component.component):
	def __init__(self, value = True):
		self.value = value