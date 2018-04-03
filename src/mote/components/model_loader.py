# -*- coding:utf-8 -*-

from . import component

from .. import res_mgr

class model_loader(component.component):
	def __init__(self, res):
		super(model_loader, self).__init__()

		self.res = res
