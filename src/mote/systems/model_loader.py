# -*- coding:utf-8 -*-

from . import system

from .. import res_mgr

class model_loader(system.system):
	reads = ('model_loader',)
	writes = ('visual', )
	def __init__(self):
		super(model_loader, self).__init__()

	def pre_tick(self):
		return res_mgr.has_task_result()

	def tick(self, entity):
		model_loader = entity.get_component('model_loader')

		if model_loader.task_id:
			res = res_mgr.pop_res(model_loader.task_id)
			print('model loaded', res)
			if res:
				entity.del_component('model_loader')
				entity.add_component('model_creator', res = res)
				res_mgr.add_null_task_result()
			return

		task_id = res_mgr.gen_task_id()
		res_name = model_loader.res

		model_loader.task_id = task_id

		def _loading_task():
			res = {} # {name:res}

			model_res = res_mgr.read(res_name)
			res['model_res'] = model_res

			model_info = self.parse_model_info(model_res)

			res['mesh'] = res_mgr.read(model_info.mesh)
			textures = []
			for name in model_info.textures:
				textures.append(res_mgr.read(name))
			res['tex'] = textures

			res_mgr.set_task_result(task_id, res)

		print('add loading task', task_id)
		res_mgr.add_task(task_id, _loading_task)

	def parse_model_info(self, res):
		class _test:
			def __init__(self):
				self.mesh = 'char/test.mesh'
				self.textures = ['char/test1.txt', 'char/test2.txt']

		return _test()
