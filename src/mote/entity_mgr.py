# -*- coding:utf-8 -*-

class entity_mgr:
	def __init__(self):
		self.entities = []

		self.groups = {} # {name:[]}

	def add_entity(self, entity):
		assert not entity.is_in_world()
		entity.set_in_world()

		self.on_entity_changed(entity)

	def on_entity_changed(self, entity):
		entity.reset()
		self.entities.append(entity)

		for child in entity.childs:
			self.on_entity_changed(child)

	def del_entity(self, entity):
		assert entity.is_in_world()

		entity.set_in_world(False)
		entity.reset()

		for child in entity.childs:
			self.del_entity(child)

	def do_add_entity(self, entity):
		components = set(entity.components)

		for reads, group in self.groups.items():
			if components.issuperset(reads): # and components.issuperset(writes):
				group.append(entity)

	def post_tick(self):
		for entity in self.entities:
			self.do_add_entity(entity)

		self.entities = []

	def add_entity_group(self, reads, writes):
		group_id = reads

		self.groups[group_id] = []

	def iter_entities(self, reads, writes):
		group_id = reads

		group = self.groups[group_id]
		new_group = []

		for entity in group:
			if not entity.is_dirty():
#				new_group.append(entity)
				yield entity

				if not entity.is_dirty():
					new_group.append(entity)
			else:
				components = set(entity.components)
				if components.issuperset(reads): # and components.issuperset(writes):
					yield entity

					if not entity.is_reset():
						new_group.append(entity)

		self.groups[group_id] = new_group
