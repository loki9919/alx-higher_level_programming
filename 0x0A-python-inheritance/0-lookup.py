#!/usr/bin/python3

"""defines an object attribute lookup func"""
def lookup(obj):
	"""returns the list of available attributes and methods of an object"""
	return (dir(obj))
