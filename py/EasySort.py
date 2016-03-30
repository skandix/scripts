#!/bin/python
def sort(x,y):
	return cmp(x,y)

unsorted = [3,2,9,4,3,9,2,8,3,4,6,3,2,5,5,1,8,1,5,8]
print "Unsorted; ", unsorted
unsorted.sort(sort)
print "Sorted; ", unsorted
