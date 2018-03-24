# -*- encoding:utf-8 -*-

class entity:
	def __init__(self, name):
		self.name = name

		self.components = {}

		self.childs = []

	def add_component(self, name, *args, **kwds):
		components = __import__('components.%s'%(name), globals(), locals(), level = 1)
		module = getattr(components, name)
		component_type = getattr(module, name)

		component = component_type(*args, **kwds)

		assert name not in self.components
		self.components[name] = component

