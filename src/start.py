# -*- coding:utf-8 -*-

import app
import world

from mote import entity

camera = None
counter = 0

def key_callback(key, pressed):
	zdelta = 0
	xdelta = 0

	speed = 1

	if pressed:
		if key == 'A':
			xdelta -= speed
		elif key == 'D':
			xdelta += speed
		elif key == 'W':
			zdelta += speed
		elif key == 'S':
			zdelta -= speed

	if zdelta or xdelta:
		camera.add_component('speed', x = xdelta, z = zdelta)
	else:
		camera.del_component('speed')

#	global counter
#	counter += 1
#	if counter == 4:
#		world.del_entity(camera)
#		print('del entity', camera.is_reset(), camera.is_dirty())
#	if counter == 7:
#		print('readd entity')
#		world.add_entity(camera)

def add_camera():
	global camera
	camera = entity.entity('camera')

	camera.add_component('pos', 0.1, 0.2, 0.3)
#	camera.add_component('speed', z = 1)

	world.add_entity(camera)

def add_model():
	e = entity.entity('model')

	e.add_component('pos')

	e.add_component('model_loader', res = 'char/test.model')

	world.add_entity(e)

def start():
	print('logic start')

	app.key_callback = key_callback

	add_camera()
	add_model()