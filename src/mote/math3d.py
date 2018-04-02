# -*- coding:utf-8 -*-

import math
import numpy

_identity = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))

def vec3(x = 0, y = 0, z = 0):
	return numpy.array((x, y, z), dtype = numpy.float32)

def vec(x = 0, y = 0, z = 0):
	return numpy.array((x, y, z), dtype = numpy.float32)

def matrix(args = None):
	args = args or _identity

	return numpy.array(args, dtype = numpy.float32)

def translation(x = 0, y = 0, z = 0):
	data = ((1, 0, 0, x), (0, 1, 0, y), (0, 0, 1, z), (0, 0, 0, 1))
	return matrix(data)

def get_translation(m):
	return vec(m[0,3], m[1,3], m[2,3])

def scale(x = 1, y = 1, z = 1):
	data = ((x, 0, 0, 0), (0, y, 0, 0), (0, 0, z, 0), (0, 0, 0, 1))
	return matrix(data)

def rotate_roll_yaw_pitch(roll = 0, yaw = 0, pitch = 0):
	cos = math.cos
	sin = math.sin

	a = pitch
	b = yaw
	c = roll

	row1 = (cos(c)*cos(b), -sin(c)*cos(a)+cos(c)*sin(b)*sin(a), sin(c)*sin(a)+cos(c)*sin(b)*cos(a), 0)
	row2 = (sin(c)*cos(b), cos(c)*cos(a)+sin(c)*sin(b)*sin(a), -cos(c)*sin(a)+sin(c)*sin(b)*cos(a), 0)
	row3 = (-sin(b), cos(b)*sin(a), cos(b)*cos(a), 0)

	return matrix([row1, row2, row3, (0, 0, 0, 1)])

if __name__ == '__main__':
	hpi = math.pi / 2
	v = vec(0, 0, 0)
	t = translation(10, 0, 0)
	r = rotate_roll_yaw_pitch(hpi)

	v = t.dot(v)

	result = r.dot(v)
