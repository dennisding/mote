# -*- coding:utf-8 -*-

from . import math3d
from . import entity_mgr
from . import blackboard

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
		self.blackboard = blackboard.blackboard()

	def init_systems(self):
		self.add_system('move')
		self.add_system('model_loader')
#		self.add_system('model_creator')
		self.add_system('visual_creator')

	def tick(self):
		self.pre_tick()

		for system in self.systems:
			self.tick_system(system)

		self.post_tick()

	def pre_tick(self):
		self.update_transform()

	def update_transform(self):
		transform = math3d.matrix()

		# update the pos
		self.blackboard.scene and self.blackboard.scene.set_parent_transform(transform)
		self.blackboard.gui and self.blackboard.gui.set_parent_transform(transform)

	def post_tick(self):
		self.entity_mgr.post_tick()

		self.update_transform()

	def tick_system(self, system):
		if not system.pre_tick():
			return

		for entity in self.entity_mgr.iter_entities(system.reads, system.writes):
			system.tick(entity)

		system.post_tick()

	def add_system(self, name):
		systems = __import__('systems.%s'%(name), globals(), locals(), (), 1)
		module = getattr(systems, name)
		system_type = getattr(module, name)

		system = system_type()
		self.systems.append(system)

	# script call
	def add_entity(self, entity):
		self.entity_mgr.add_entity(entity)

	def del_entity(self, entity):
		self.entity_mgr.del_entity(entity)

	def on_entity_changed(self, entity):
		self.entity_mgr.on_entity_changed(entity)

	def set_gui_root(self, entity):
		self.blackboard.gui = entity

	def set_scene(self, scene):
		self.blackboard.scene = scene