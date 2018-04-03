# -*- coding:utf-8 -*-

import numpy

from . import system

from .. import res_mgr
from ..render import program

from OpenGL.GL import *

class visual_creator(system.system):
	reads = ('visual_creator', )
	writes = ('visual')

	def tick(self, entity):
		print('tick visual creator')
		creator = entity.get_component('visual_creator')

		res = res_mgr.get_res(creator.task_id)
		if not res:
			return

		visual = entity.add_component('visual')
		self.fill_visual(res, visual)

		entity.del_component('visual_creator')

	def fill_visual(self, res, visual):
		visual.vertex_array = self.create_vertex_array(res)
		visual.program = self.create_program(res)

	def create_vertex_array(self, res):
		vertex_array = glGenVertexArrays(1)
		glBindVertexArray(vertex_array)

		vertex_buffer = glGenBuffers(1)
		glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)

		b = numpy.array([(-1.0, -1, 0), (1, -1, 0), (0, 1, 0)], dtype = numpy.float32)
		glBufferData(GL_ARRAY_BUFFER, b.nbytes, b.tobytes(), GL_STATIC_DRAW)

		return vertex_array

	def create_program(self, res):
		vs = b'''
#version 430 core
layout(location = 0) in vec3 vertexPosition_modelspace;

uniform mat4 mvp;
void main(){
  gl_Position.xyzw = mvp * vec4(vertexPosition_modelspace, 1);
 // gl_Position.w = 1.0;
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