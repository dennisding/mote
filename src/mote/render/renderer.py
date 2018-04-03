# -*- coding:utf-8 -*-

from . import visual_walker

from OpenGL.GL import *

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

	def pre_render(self):
		glClearColor(0.0, 0.3, 0.3, 1)
		glClear(GL_COLOR_BUFFER_BIT)

	def post_render(self):
		pass

	def render_visual(self, visual):
		glEnableVertexAttribArray(0)

		glBindVertexArray(visual.vertex_array)

		visual.program.use(self.world, visual)

		glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None);
		glDrawArrays(GL_TRIANGLES, 0, 3)
		glDisableVertexAttribArray(0)
