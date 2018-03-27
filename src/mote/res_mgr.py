# -*- coding:utf-8 -*-

_results = {} # {task_id:res}
_results2 = {}

def pop_res(task_id):
	return _results2.pop(task_id) or _results.pop(task_id)

def has_task_result():
	return bool(_results) or bool(_results2)

def clear_task_result():
	global _results, _results2

	_results, _results2 = _results2, _results
	_results.clear()

def set_task_result(task_id, res):
	assert task_id not in _results

	_results[task_id] = res

def add_null_task_result():
	set_task_result(0, None)

_last_task_id = 0
def gen_task_id():
	global _last_task_id

	_last_task_id += 1
	return _last_task_id

def add_task(task_id, task):
	task()

def read(name):
	return open(name, 'rb').read()