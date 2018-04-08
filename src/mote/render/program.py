# -*- coding:utf-8 -*-

from .. import math3d

from OpenGL.GL import *

_programs = {} # caches

_uniform_getters = {} # {name:getter}
_uniform_setters = {} # {name:setter}

def register_setters():
	_uniform_setters[GL_FLOAT_MAT4] = glUniformMatrix4fv

def register_getters():
	_uniform_getters[b'mvp'] = lambda world, visual: visual.world_transform.tobytes()
#	_uniform_getters[b'mvp'] = lambda world, visual: math3d.translation(x = 1).tobytes()

register_getters()
register_setters()

class program:
	def __init__(self, vs_name, vs, ps_name, ps):
		self.valid = False
		self.vs_name = vs_name
		self.ps_name = ps_name

		self.create_program(vs, ps)

	# public interface
	def use(self, world, visual):
		glUseProgram(self.program)

		self.setup_uniforms(world, visual)

	def setup_uniforms(self, world, visual):
		for index, getter, setter in self.uniforms:
			setter(index, 1, GL_TRUE, getter(world, visual))

	def create_program(self, vs_source, ps_source):
		vs = self.create_vertex_shader(vs_source)
		ps = self.create_pixel_shader(ps_source)

		self.program = self.link_program(vs, ps)

		self.release_shader(vs)
		self.release_shader(ps)

		self.program and self.parse_infos()

	def parse_infos(self):
		self.valid = True

		self.uniforms = [] # [(index, getter, setter)]
		count = glGetProgramiv(self.program, GL_ACTIVE_UNIFORMS)
		for index in range(count):
			name, _id, type = glGetActiveUniform(self.program, index)
			self.uniforms.append((index, _uniform_getters[name], _uniform_setters[type]))

	def is_valid(self):
		return self.valid

	def create_vertex_shader(self, source):
		return self.compile_shader(self.vs_name, source, GL_VERTEX_SHADER)

	def create_pixel_shader(self, source):
		return self.compile_shader(self.ps_name, source, GL_FRAGMENT_SHADER)

	def compile_shader(self, name, source, type):
		shader = glCreateShader(type)
		glShaderSource(shader, source)
		glCompileShader(shader)

		log = glGetShaderInfoLog(shader)
		if log:
			print('compile error in: %s\r\n%s'%(name, log))
			return None

		return shader

	def link_program(self, vs, ps):
		program = glCreateProgram()

		glAttachShader(program, vs)
		glAttachShader(program, ps)
		glLinkProgram(program)

		log = glGetProgramInfoLog(program)
		if log:
			print('error in linking: %s, %s, \r\n%s'%(self.vs_name, self.ps_name, log))

		return program

	def release_shader(self, shader):
		shader and glDeleteShader(shader)

def gen_program(vs_name, vs, ps_name, ps):
	# get from cache
	id = vs_name, ps_name
	p = _programs.get(id)
	if p:
		return p

	p = program(vs_name, vs, ps_name, ps)

	if not p.is_valid():
		p = None

	_programs[id] = p
	return p

def release_program(program):
	pass
