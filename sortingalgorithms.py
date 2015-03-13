# Quicksort
# Best: O(n log(n))
# Average: O(n log(n))
# Worst: O(n^2)

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more
 
a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = quickSort(a)

# Mergesort
# Best: O(n log(n))
# Pre-sorted: O(n)
# Average: O(n log(n))
# Worst: O(n log(n))
def merge_sort(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result


# Heapsort:
# Best: O(n log(n))
# Average: O(n log(n))
# Worst: O(n log(n))
def heap_sort(lst):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break


# Bubble Sort
# Time: Best - O(n)
# 	  Average/Worst (On^2)
	  # Space: O(1)

def bubble_sort(seq):
	changed = True
	while changed:
		changed = False
		for i in xrange(len(seq-1)):
			if seq[i] > seq [i+1]:
				seq[i], seq[i+1]  = seq [i+1], seq[i]
				changed = True
		return seq


# Insertion Sort
# Best: O(n)
# Average/Worst O(n^2)
# Space: O(1)

def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

Select Sort:

Bucket Sort:

Radix Sort:

