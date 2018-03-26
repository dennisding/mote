# -*- coding:utf-8 -*-

from mote import entity

import world

def add_camera():
	e = entity.entity('camera')

	e.add_component('pos', 0.1, 0.2, 0.3)
	e.add_component('speed', z = 1)

	world.add_entity(e)

def start():
	print('logic start')

	add_camera()