#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sort_util

__author__ = 'ivan'

# todo:
# QuickSort function.
# Time: n*ln(n
def quick_sort(list):
	quick_sort_impl(list, 0, len(list) - 1)

def quick_sort_impl(list, left, right):
	N = len(list)
	if N <= 1:
		return list
	if (left >= right):
		return list
	pos = partition(list, left, right)
	quick_sort_impl(list, left, pos - 1)
	quick_sort_impl(list, pos + 1, right)

# merges two sorted arrays.
def partition(list, left, right):
	#just take the 1st item.
	pivot = list[0]
	#pivot = list[(left + right) / 2]
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

	sort_util.swap(list, pivot_pos, j)
	return pivot_pos

def main():
	print "-=QUICK SORT=-"

	list = [5, 2, 6, 3, 1, 4, 7, 9, 0, 8]

	print ' input:' + str(list)
	quick_sort(list)
	print 'result:' + str(list)

if __name__ == '__main__':
	main()
