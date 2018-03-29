# -*- coding:utf-8 -*-

import numpy

class visual_walker:
	def __init__(self, world):
		self.world = world

		self.visuals = []

	def walk(self, entity):
		if not entity:
			return

		self.do_walk(entity)

	def do_walk(self, entity):
#		if not self.is_entity_valid(entity):
#			return
		if not self.filter_entity(entity):
			return

		visual = entity.get_component('visual')
		if visual:
			self.add_visual(visual)

		self.walk_childs(entity)

	def filter_entity(self, entity):
		return bool(entity.get_component('visible'))

	def add_visual(self, visual):
		self.visuals.append(visual)

	def walk_childs(self, entity):
		if not entity.childs:
			return

		for child in entity.childs:
			self.do_walk(child)

