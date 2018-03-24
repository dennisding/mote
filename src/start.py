# -*- coding:utf-8 -*-

from mote import entity

import world

def add_camera():
	e = entity.entity('camera')

	e.add_component('pos', 0.1, 0.2, 0.3)
	e.add_component('input_ctrl')
	e.add_component('move', 1, 0, 0, 0.4)

	world.add_entity(e)

def start():
	print('logic start')

	add_camera()