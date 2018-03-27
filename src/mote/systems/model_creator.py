# -*- encoding:utf-8 -*-

from . import system

class model_creator(system.system):
	reads = ('model_creator', )
	writes = ('visual', )
	def __init__(self):
		super(model_creator, self).__init__()


	def tick(self, entity):
		creator = entity.get_component('model_creator')

		print('create model!', creator.res)

		entity.del_component('model_creator')