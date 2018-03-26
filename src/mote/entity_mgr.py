# -*- coding:utf-8 -*-

class entity_mgr:
	def __init__(self):
		self.entities = []

	def add_entity(self, entity):
		self.entities.append(entity)

		for child in entity.childs:
			self.add_entity(child)

	def del_entity(self, entity):
		pass

	def get_entities_by_component(self, reads, writes):
		for entity in self.entities:
			components = set(entity.components)
			if components.issuperset(reads) and components.issuperset(writes):
				yield entity
