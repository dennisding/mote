# -*- coding:utf-8 -*-

from . import system

from .. import res_mgr

class model_loader(system.system):
	reads = ('model_loader',)
	writes = ('visual', )
	def __init__(self):
		super(model_loader, self).__init__()

	def tick(self, entity):
		print('tick model loader')
		loader = entity.get_component('model_loader')

		entity.del_component('model_loader')

		task_id = res_mgr.gen_task(lambda : self.loading_res(loader.res))
		entity.add_component('visual_creator', task_id = task_id)

	def loading_res(self, res):
		result = {}
		result['info'] = res_mgr.read(res + '/info.1')
		result['mesh'] = res_mgr.read(res + '/mesh.1')
		result['mat'] = res_mgr.read(res + '/mat.1')

		return result
