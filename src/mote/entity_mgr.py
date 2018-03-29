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
		for reads, group in self.groups.items():
			if self.has_components(entity, reads):
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
				yield entity

				if not entity.is_dirty():
					new_group.append(entity)
				elif entity.is_reset():
					continue
				else:
					if self.has_components(entity, reads):
						new_group.append(entity)
			else:
				if self.has_components(entity, reads):
					yield entity

					if not entity.is_reset():
						new_group.append(entity)

		self.groups[group_id] = new_group

	def has_components(self, entity, components):
		entity_component = set(entity.components)
		return entity_component.issuperset(components)


