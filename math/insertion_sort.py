#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sort_util

__author__ = 'ivan'

# SelectionSort function.
# Time: n*n
def insertion_sort(list):
	N = len(list)
	for i in range(0, N):
		for j in range(i, 0, -1):
			if list[j] < list[j - 1]:
				sort_util.swap(list, j, j - 1)
	return list


def main():
	print "-=INSERTION SORT=-"

	list = [5, 2, 6, 3, 1, 4, 7, 9, 0, 8]

	print ' input:' + str(list)
	result = insertion_sort(list)
	print 'result:' + str(result)

if __name__ == '__main__':
	main()