#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sort_util

__author__ = 'ivan'

# SelectionSort function.
# Time: n*n
def selection_sort(list):
	N = len(list)
	for i in range(0, N):
		minInd = i
		for j in range(i, N):
			if list[j] < list[minInd]:
				minInd = j
		sort_util.swap(list, i, minInd)
	#print list
	return list


def main():
	print "-=SELECTION SORT=-"

	list = [5, 2, 6, 3, 1, 4, 7, 9, 0, 8]

	print ' input:' + str(list)
	result = selection_sort(list)
	print 'result:' + str(result)

if __name__ == '__main__':
	main()