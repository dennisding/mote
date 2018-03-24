# -*- coding:utf-8 -*-

from . import component

class move(component.component):
	def __init__(self):
		super(move, self).__init__()

	def tick(self, delta, entities):
		for entity in entities:
			pass