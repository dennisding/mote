# -*- coding:utf-8 -*-

from . import visual_walker

class renderer:
	def __init__(self):
		pass

	def render(self, world):
		self.world = world

		visuals = self.gen_visual_list(world)
		self.render_visuals(visuals)

		self.world = None

	def gen_visual_list(self, world):
		walker = visual_walker.visual_walker(world)

		walker.walk(world.blackboard.gui)
		walker.walk(world.blackboard.scene)

		return walker.visuals

	def render_visuals(self, visuals):
		for visual in visuals:
			self.render_visual(visual)

	def render_visual(self, visual):
		print('render visual', visual)
