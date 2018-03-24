# -*- coding:utf-8 -*-

import sys

from . import win
from . import world
from OpenGL.GL import *

class app:
	def __init__(self):
		self.win = None
		self.world = None

		self.stop = False

		self.init()

	def init(self):
		self.create_win()
		self.create_world()

		self.init_script()

	def init_script(self):
		init_module = __import__('init')
		init_module.init()

	def start_script(self):
		# setup logic module
		sys.modules['world'] = self.world

		start_module = __import__('start')

		start_module.start()

	def start(self):
		self.start_script()

		while True:
			self.tick()
			if self.stop:
				break

		self.win.release()

	def create_win(self):
		self.win = win.win('测试')
		self.win.start()

	def create_world(self):
		self.world = world.world(self)

	def tick(self):
		# process events
		self.process_events()
		self.update()
		self.render()

		self.world.tick()

	def process_events(self):
		if self.win.process_events():
			self.stop = True

	def update(self):
		pass

	def render(self):
		glClearColor(0.3, 0.3, 0.3, 1)
		glClear(GL_COLOR_BUFFER_BIT)

		self.win.swap_buffer()
