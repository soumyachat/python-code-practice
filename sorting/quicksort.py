'''
Quick Sort
'''


import numpy as np
import time

def quicksort(data, low, high):
	if low<(high-1):
		pivot = partition(data, low, high)
		quicksort(data, low, pivot)
		quicksort(data, pivot+1, high)
	

def partition(data, low, high):
	x = data[high-1]
	j = low - 1
	for i in range(low, high-1):
		if data[i] <= x:
			j = j +1
			swap(data, i,j)
	
	#data[j+1], data[high-1] = data[high-1], data[j+1]
	swap(data, j+1, high-1)
	return (j+1)


def swap(data, i,j):
	data[i], data[j] = data[j], data[i]


def main():
	data = np.random.randint(1,1000,100).tolist()
	#data = np.arange(1000,0,-1).tolist()

	print "Original data:\n",data

	tStart = time.time()
	quicksort(data, 0,len(data) )
	print "Quicksort Time = ", time.time()  - tStart, " secs."

	print "Sorted Data:\n", data


if __name__=="__main__":
	main()
	
	
