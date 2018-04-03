# -*- coding:utf-8 -*-

from . import component

from .. import res_mgr

class visual_creator(component.component):
	def __init__(self, task_id):
		self.task_id = task_id

	def tick(self):
		pass