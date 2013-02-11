#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ivan'


# QuickSort function.
# Time: n*ln(n)
def quick_sort(list, left, right):
	N = len(list)
	if N <= 1:
		return list
	partition(list)
	left = quick_sort(list[0:middle])
	right = quick_sort(list[middle: N])
	return merge(left, right)

# merges two sorted arrays.
def partition(list):
	if (len(list) == 1):
		return
	pivot = list[0]
	i = 0
	j = len(list) - 1
	while i <= j:
		while list[i] >= pivot:
			i += 1
		while list[j] < pivot:
			j -= 1
		#swap
		tmp = list[i]
		list[i] = list[j]
		list[j] = tmp

def main():
	print "-=QUICK SORT=-"

	list = [5, 2, 6, 3, 1, 4, 7, 9, 0, 8]

	#print ' input:' + str(list)
	#print ' input:' + str(list)
	#result = quick_sort(list, 0, len(list) - 1)
	#print 'result:' + str(result)

if __name__ == '__main__':
	main()
