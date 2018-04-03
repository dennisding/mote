# -*- coding:utf-8 -*-

_results = {} # {task_id:res}
_results2 = {}

_root = 'res/'

_last_task_id = 0
def gen_task_id():
	global _last_task_id

	_last_task_id += 1
	return _last_task_id

def on_new_frame():
	global _results, _results2
	_results, _results2 = _results2, _results

def gen_task(task):
	task_id = gen_task_id()

	_results[task_id] = task()

	return task_id

def get_res(task_id):
	return _results.get(task_id) or _results2.get(task_id)

def read(name):
	return open(_root + name, 'rb').read()