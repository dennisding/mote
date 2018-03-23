# -*- coding:utf-8 -*-

from win import win
from OpenGL.GL import *

class app:
	def __init__(self):
		self.win = win.win('测试')

		self.stop = False

	def start(self):
		self.win.start()

		while True:
			self.tick()
			if self.stop:
				break

		self.win.release()

	def tick(self):
		# process events
		self.process_events()
		self.update()
		self.render()

	def process_events(self):
		if self.win.process_events():
			self.stop = True

	def update(self):
		pass

	def render(self):
		glClearColor(0.3, 0.3, 0.3, 1)
		glClear(GL_COLOR_BUFFER_BIT)

		self.win.swap_buffer()
