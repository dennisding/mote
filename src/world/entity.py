# -*- encoding:utf-8 -*-

class entity:
	def __init__(self):
		self.components = {}
		self.component_changed = False

	def add_component(self, name, component):
		assert name not in self.components

		self.components[name] = component

		self.component_changed = True

	def del_component(self, name):
		self.components.pop(name)

		self.component_changed = True