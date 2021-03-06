# -*- coding:utf-8 -*-

import sys
import time

from . import win
from . import world
from . import res_mgr
from .render import renderer

def fixed_numpy():
	import numpy

	numpy.float128 = numpy.float64
	numpy.complex256 = numpy.complex128

fixed_numpy()

class app:
	def __init__(self):
		self.win = None
		self.world = None

		self.stop = False
		self.frame_counter = 0
		self.delta = 0

		self.init()

		self.key_callback = None

	def init(self):
		sys.modules['app'] = self

		self.create_win()
		self.create_world()
		self.create_renderer()

		self.init_script()

		self.last_time = time.perf_counter()

	def create_renderer(self):
		self.renderer = renderer.renderer()

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
			now = time.perf_counter()
			self.delta = now - self.last_time

			self.on_new_frame()

			self.tick()
			if self.stop:
				break

			self.frame_counter += 1
			self.last_time = now

		self.win.release()

	def on_new_frame(self):
		res_mgr.on_new_frame()

	def create_win(self):
		self.win = win.win(self, 'test')
		self.win.start()

	def create_world(self):
		self.world = world.world(self)

	def tick(self):
		# process events
		self.process_events()

		self.world.tick()

		self.render()

	def process_events(self):
		if self.win.process_events():
			self.stop = True

	def render(self):
		self.renderer.pre_render()

		self.renderer.render(self.world)

		self.renderer.post_render()

		self.win.swap_buffer()
