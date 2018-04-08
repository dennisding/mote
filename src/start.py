# -*- coding:utf-8 -*-

import app
import world

from mote import entity

camera = None
model = None
counter = 0

def key_callback(key, pressed):
	zdelta = 0
	xdelta = 0

	speed = 0.5

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
#		camera.add_component('speed', x = xdelta, z = zdelta)
		model.add_component('speed', x = xdelta, y = zdelta)
	else:
		model.del_component('speed')
#		camera.del_component('speed')

#	global counter
#	counter += 1
#	if counter == 4:
#		world.del_entity(camera)
#		print('del entity', camera.is_reset(), camera.is_dirty())
#	if counter == 7:
#		print('readd entity')
#		world.add_entity(camera)

def add_camera():
	# add and del component
	global camera
	camera = entity.entity('camera')

	camera.add_component('pos', 0.1, 0.2, 0.3)
#	camera.add_component('speed', z = 1)

	world.add_entity(camera)

def add_model():
	# resource loading
	e = entity.entity('model')

	e.add_component('pos')

	e.add_component('visible')
	e.add_component('model_loader', res = 'char/100')

	world.add_entity(e)
	world.set_scene(e)

	global model
	model = e

def add_gui():
	return
	# layers
	e = entity.entity('dialog')

	e.add_component('pos', x = 1, y = 0.5, z = 3)
	e.add_component('visual')
	e.add_component('visible')

	child = entity.entity('panel')
	child.add_component('pos', x = 2)
	child.add_component('visual')
	child.add_component('visible')

	e.add_child(child)

	world.add_entity(e)

	world.set_gui_root(e)

def start():
	print('logic start')

	app.key_callback = key_callback

	add_camera()
	add_model()
#	add_gui()