# -*- encoding:utf-8 -*-

import app
import world

from . import math3d

class entity:
	def __init__(self, name):
		self.name = name

		self.components = {}

		self.childs = []

		self.in_world = False
		self.dirty_flag = 0
		self.reset_flag = 0

	def add_child(self, child):
		self.childs.append(child)

	def add_component(self, name, *args, **kwds):
		components = __import__('components.%s'%(name), globals(), locals(), level = 1)
		module = getattr(components, name)
		component_type = getattr(module, name)

		component = component_type(*args, **kwds)

		if self.is_in_world() and (name not in self.components):
			world.on_entity_changed(self)

		self.components[name] = component

		component.add_to_entity(self)

		return component

	def set_parent_transform(self, parent_transform):
		transform = self.gen_transform(parent_transform)

		visual = self.get_component('visual')
		if visual:
			visual.world_transform = transform

		for child in self.childs:
			child.set_parent_transform(transform)

	def gen_transform(self, parent_transform):
		pos = self.get_component('pos')
		scale = self.get_component('scale')
		rotate = self.get_component('rotate')

		if not (pos or scale or rotate):
			return parent_transform

		last_transform = None
		if pos:
			last_transform = math3d.translation(pos.pos[0], pos.pos[1], pos.pos[2])

		return parent_transform.dot(last_transform)

	def get_component(self, name):
		return self.components.get(name)

	def del_component(self, name):
		self.components.pop(name, None)

		self.set_dirty()

	def set_dirty(self):
		self.dirty_flag = app.frame_counter

	def is_dirty(self):
		return self.dirty_flag == app.frame_counter

	def reset(self):
		self.reset_flag = app.frame_counter
		self.set_dirty()

	def is_reset(self):
		return self.reset_flag == app.frame_counter

	def set_in_world(self, in_world = True):
		self.in_world = in_world

	def is_in_world(self):
		return self.in_world
