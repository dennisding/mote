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

		for system in self.systems:
			self.entity_mgr.add_entity_group(system.reads, system.writes)

	def init(self):
		self.last_time = time.perf_counter()

	def init_systems(self):
		self.add_system('move')
		self.add_system('render')

	def tick(self):
		now = time.perf_counter()
		delta = now - self.last_time

		self.pre_tick()

		for system in self.systems:
			self.tick_system(delta, system)

		self.post_tick()

		self.last_time = now

	def pre_tick(self):
		pass

	def post_tick(self):
		self.entity_mgr.post_tick()

	def tick_system(self, delta, system):
		system.pre_tick()

		for entity in self.entity_mgr.iter_entities(system.reads, system.writes):
			system.tick(delta, entity)

		system.post_tick()

	def add_system(self, name):
		systems = __import__('systems.%s'%(name), globals(), locals(), (), 1)
		module = getattr(systems, name)
		system_type = getattr(module, name)

		system = system_type()
		self.systems.append(system)

	def add_entity(self, entity):
		self.entity_mgr.add_entity(entity)

	def on_entity_changed(self, entity):
		self.entity_mgr.on_entity_changed(entity)