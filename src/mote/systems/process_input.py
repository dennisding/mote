# -*- coding:utf-8 -*-

from . import system

class process_input(system.system):
	read_components = ('process_input',)
	write_components = ('pos', )

	def __init__(self):
		pass

	def tick(self, delta, entities):
		print('tick!!!', delta)
		for entity in entities:
			pass
