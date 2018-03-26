# -*- coding:utf-8 -*-

import time

from . import entity_mgr
from .systems import process_input

class world:
	def __init__(self, app):
		self.app = app
		self.entities = []
		self.systems = []

		self.init()
		self.init_systems()
		self.setup_entity_mgr()

	def setup_entity_mgr(self):
		self.entity_mgr = entity_mgr.entity_mgr()

	def init(self):
		self.last_time = time.perf_counter()

	def init_systems(self):
		self.add_system('move')

	def tick(self):
		now = time.perf_counter()
		delta = now - self.last_time

		for system in self.systems:
			self.tick_system(delta, system)

		self.last_time = now

	def tick_system(self, delta, system):
		entities = self.entity_mgr.get_entities_by_component(system.reads, system.writes)

		for entity in entities:
			system.tick(delta, entity)

	def add_system(self, name):
		systems = __import__('systems.%s'%(name), globals(), locals(), (), 1)
		module = getattr(systems, name)
		system_type = getattr(module, name)

		system = system_type()
		self.systems.append(system)

	def add_entity(self, entity):
#		print('add entity', entity)
		self.entity_mgr.add_entity(entity)