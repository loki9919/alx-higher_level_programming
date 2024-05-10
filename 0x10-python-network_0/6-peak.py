#!/usr/bin/python3
"""Algorithms for list of integers"""


def find_peak(list_integers):
    """Finds a peak in a list of unsorted integers"""
    if list_integers:
        list_integers.sort(reverse=True)
        return list_integers[0]
