'''
MergeSort
'''

import numpy as np
import math
import time


def mergesort(data):
	
	if len(data)>1:
		mid = len(data)//2

		#print "Splitting...", data
		left_array = data[:mid]
		right_array = data[mid:]

		mergesort(left_array)
		mergesort(right_array)


		i, j, k = 0,0,0

		while(i<len(left_array) and j < len(right_array)):
			if left_array[i]<right_array[j]:
				data[k] = left_array[i]
				i = i+1
			else:
				data[k] = right_array[j]
				j = j+1
			k = k+1
		while i<len(left_array):
			data[k] = left_array[i]
			k = k+1
			i = i+1
		while j < len(right_array):
			data[k] = right_array[j]
			k = k+1
			j = j+1
		#print "Merging", data
		


def main():
	#data = np.random.randint(1,1000,100).tolist()
	data = np.arange(1000,0,-1).tolist()

	print "Original data:\n",data

	tStart = time.time()
	mergesort(data)
	print "Mergesort Time = ", time.time()  - tStart, " secs."

	print "Sorted Data:\n", data


if __name__=="__main__":
	main()


			
