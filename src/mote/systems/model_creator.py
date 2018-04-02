# -*- encoding:utf-8 -*-

import numpy

from OpenGL import GLUT
from OpenGL import GL as gl
from OpenGL.GL import *

from . import system
from ..render import program

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

		print('size==', glGetBufferParameteriv(GL_ARRAY_BUFFER, GL_BUFFER_SIZE))

#		program = self.create_shader()
		program = self.create_program()

		glEnableVertexAttribArray(0)
		glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
#		glUseProgram(program)
		program.use()

		glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None);
		glDrawArrays(GL_TRIANGLES, 0, 3)
		glDisableVertexAttribArray(0)

		import app
		app.win.swap_buffer()

	def create_program(self):
		vs = b'''
#version 430 core
layout(location = 0) in vec3 vertexPosition_modelspace;

uniform mat4 mvp;
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
		p = program.gen_program('test.vs', vs, 'test.ps', ps )
		return p
