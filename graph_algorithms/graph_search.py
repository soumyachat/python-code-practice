'''
Test code for graph search using DFS and BFS
'''

import depth_first_search as dfs
from graph import *
import random
import time

def main():
	G  = generateRandomGraph(1000)
	#print G
	tStart = time.time()
	dfs.DFS(G)
	print "\n\n Total time for DFS = ", time.time() - tStart, " secs."

def generateRandomGraph(num_vertices):
	p = 0.01		# probability of an edge
	G = Graph()
	for i in range(num_vertices):
		G.addVertex(i)
	
	edges = [(i,j) for i in xrange(num_vertices) for j in xrange(num_vertices) if random.random()<p]

	for (i,j) in edges:
		G.addEdge(i,j,1)

	return G


if __name__=="__main__":
	main()
