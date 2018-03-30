# -*- encoding:utf-8 -*-

import numpy

from OpenGL import GLUT
from OpenGL import GL as gl
from OpenGL.GL import *

from . import system

class model_creator(system.system):
	reads = ('model_creator', )
	writes = ('visual', )
	def __init__(self):
		super(model_creator, self).__init__()


	def tick(self, entity):
		creator = entity.get_component('model_creator')

		print('create model!', creator.res)

		self.create_visual(entity)

		entity.del_component('model_creator')

	def create_visual(self, entity):

		glClearColor(0.3, 0.6, 0.3, 1)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		visual = entity.add_component('visual')

		vertex_array = glGenVertexArrays(1)
		glBindVertexArray(vertex_array)

		vertex_buffer = glGenBuffers(1)
		glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
		# buffer
		b = numpy.array([(-1.0, -1, 0), (1, -1, 0), (0, 1, 0)], dtype = numpy.float32)
		glBufferData(GL_ARRAY_BUFFER, b.nbytes, b.tobytes(), GL_STATIC_DRAW)
		print('glerror1',glGetError())

		print('size==', glGetBufferParameteriv(GL_ARRAY_BUFFER, GL_BUFFER_SIZE))

		program = self.create_shader()

		glEnableVertexAttribArray(0)
		print('glerror1',glGetError(), vertex_buffer, vertex_array)
#		glBindVertexArray(vertex_array)
		glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
		print('glerror1',glGetError(), vertex_buffer, vertex_array)
		glUseProgram(program)
		print('glerror1',glGetError(), vertex_buffer, vertex_array)
		glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None);
		print('glerror1',glGetError())
		glDrawArrays(GL_TRIANGLES, 0, 3)
		print('glerror3',glGetError())
		glDisableVertexAttribArray(0)

		import app
		app.win.swap_buffer()

	def create_shader(self):
		vs = b'''
#version 430 core
layout(location = 0) in vec3 vertexPosition_modelspace;
void main(){
  gl_Position.xyz = vertexPosition_modelspace;
  gl_Position.w = 1.0;
}
		'''
		ps = b'''
#version 430 core
out vec3 color;
void main(){
  color = vec3(0.1,0.1,0);
}
'''
		vertex_shader = glCreateShader(GL_VERTEX_SHADER)
		pixel_shader = glCreateShader(GL_FRAGMENT_SHADER)

		glShaderSource(vertex_shader, vs)
		glCompileShader(vertex_shader)

		log = glGetShaderInfoLog(pixel_shader)
		print('vertex_log!!!', log)

		glShaderSource(pixel_shader, ps)
		glCompileShader(pixel_shader)

		log = glGetShaderInfoLog(pixel_shader)
		print('pixel_log!!!', log)

		program = glCreateProgram()
		glAttachShader(program, vertex_shader)
		print('glerror3',glGetError())

		glAttachShader(program, pixel_shader)
		print('glerror3',glGetError())
		glLinkProgram(program)

		print('glerror3',glGetError())

		log = glGetProgramInfoLog(program)
		print('program log!', log)

		glDeleteShader(vertex_shader)
		glDeleteShader(pixel_shader)

		return program
