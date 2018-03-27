# coding:utf-8

import glfw

class win:
	def __init__(self, app, name, width = 1024, height = 768):
		self.app = app
		self.name = name

		self.width = width
		self.height = height

		self.win = None

	def start(self):
		assert glfw.init(), 'init glfw'

		self.win = glfw.create_window(self.width, self.height, self.name, None, None)
		glfw.set_key_callback(self.win, self.key_callback)

		assert self.win, 'invalid win'

		glfw.make_context_current(self.win)

	def key_callback(self, win, key, scan_code, action, modes):
		callback = self.app.key_callback

		if not callback:
			return

		if action == glfw.PRESS:
			callback(chr(key), True)
		elif action == glfw.RELEASE:
			callback(chr(key), False)

	def tick(self):
		if glfw.window_should_close(self.win):
			return False

		return True

	def process_events(self):
		glfw.poll_events()
		return glfw.window_should_close(self.win)

	def swap_buffer(self):
		glfw.swap_buffers(self.win)

	def release(self):
		glfw.terminate()
