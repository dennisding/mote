# -*- coding:utf-8 -*-

from . import component

class model_creator(component.component):
	def __init__(self, res):
		super(model_creator, self).__init__()

		self.res = res
		print('create model_creator component')
