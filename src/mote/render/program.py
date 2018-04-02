# -*- coding:utf-8 -*-

from OpenGL.GL import *

_programs = {} # caches

class program:
	def __init__(self, vs_name, vs, ps_name, ps):
		self.valid = False
		self.vs_name = vs_name
		self.ps_name = ps_name

		self.create_program(vs, ps)

	# public interface
	def use(self):
		print('use program', self.program)
		glUseProgram(self.program)

	def create_program(self, vs_source, ps_source):
		vs = self.create_vertex_shader(vs_source)
		ps = self.create_pixel_shader(ps_source)

		self.program = self.link_program(vs, ps)

		self.release_shader(vs)
		self.release_shader(ps)

		self.program and self.parse_infos()

	def parse_infos(self):
		self.valid = True

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
			print('compile error in: %s\r\n'%(name, log))
			return None

		return shader

	def link_program(self, vs, ps):
		program = glCreateProgram()

		print('attach shader!!!!!!', vs, ps)
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
