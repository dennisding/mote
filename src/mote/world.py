# -*- coding:utf-8 -*-

import time

from .systems import process_input

class world:
	def __init__(self, app):
		self.app = app
		self.entities = []
		self.systems = []

		self.init()
		self.init_systems()

		# entity_list

	def init(self):
		self.last_time = time.perf_counter()

	def init_systems(self):
		self.add_system('process_input')

	def tick(self):
		now = time.perf_counter()
		delta = now - self.last_time

		for system in self.systems:
			self.tick_system(delta, system)

		self.last_time = now

	def tick_system(self, delta, system):
		pass

	def add_system(self, name):
		systems = __import__('systems.%s'%(name), globals(), locals(), (), 1)
		module = getattr(systems, name)
		system_type = getattr(module, name)

		system = system_type()
		self.systems.append(system)

	def add_entity(self, entity):
		print('add entity', entity)