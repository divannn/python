#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sort_util

__author__ = 'ivan'

# todo:
# QuickSort function.
# Time: n*ln(n)
def quick_sort(list, left, right):
	N = len(list)
	if N <= 1:
		return list
	if (left >= right):
		return list
	pos = partition(list, left, right)
	#if left < pos:
	quick_sort(list, left, pos - 1)
	#if right > pos:
	quick_sort(list, pos + 1, right)

# merges two sorted arrays.
def partition(list, left, right):
	#pivot = list[0]#just take the 1st item.
	pivot = list[(left + right) / 2]
	pivot_pos = -1
	i = left
	j = right
	while i <= j:
		while list[i] < pivot:
			i += 1
		while list[j] > pivot:
			j -= 1
		if i <= j:
			pivot_pos = i
			sort_util.swap(list, i, j)
			i += 1
			j -= 1
	return pivot_pos

def main():
	print "-=QUICK SORT=-"

	list = [5, 2, 6, 3, 1, 4, 7, 9, 0, 8]

	print ' input:' + str(list)
	quick_sort(list, 0, len(list) - 1)
	print 'result:' + str(list)

if __name__ == '__main__':
	main()
