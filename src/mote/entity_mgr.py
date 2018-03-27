# -*- coding:utf-8 -*-

class entity_mgr:
	def __init__(self):
		self.changed_entities = []

		self.groups = {} # {name:[]}

	def add_entity(self, entity):
		components = set(entity.components)

		for (reads, writes), group in self.groups.items():
			if components.issuperset(reads) and components.issuperset(writes):
				group.append(entity)

	def post_tick(self):
		for entity in self.changed_entities:
			self.add_entity(entity)

		self.changed_entities = []

	def on_entity_changed(self, entity):
		self.changed_entities.append(entity)

	def del_entity(self, entity):
		pass

	def add_entity_group(self, reads, writes):
		group_id = (reads, writes)

		self.groups[group_id] = []

	def iter_entities(self, reads, writes):
		group_id = (reads, writes)

		group = self.groups[group_id]
		new_group = []

		for entity in group:
			if not entity.is_dirty():
				new_group.append(entity)
				yield entity
			else:
				components = set(entity.components)
				if components.issuperset(reads) and components.issuperset(writes):
					if not entity.is_add_component():
						new_group.append(entity)
					yield entity

		self.groups[group_id] = new_group
