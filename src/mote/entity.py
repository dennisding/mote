# -*- encoding:utf-8 -*-

import app
import world

class entity:
	def __init__(self, name):
		self.name = name

		self.components = {}

		self.childs = []

		self.dirty_flag = 0
		self.add_component_flag = 0

	def add_component(self, name, *args, **kwds):
		components = __import__('components.%s'%(name), globals(), locals(), level = 1)
		module = getattr(components, name)
		component_type = getattr(module, name)

		component = component_type(*args, **kwds)

		self.components[name] = component

		self.add_component_flag = app.frame_counter

		world.on_entity_changed(self)

	def get_component(self, name):
		return self.components[name]

	def del_component(self, name):
		self.components.pop(name, None)

		self.dirty_flag = app.frame_counter

	def is_dirty(self):
		return self.dirty_flag == app.frame_counter

	def is_add_component(self):
		return self.add_component_flag == app.frame_counter
