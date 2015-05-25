'''
Depth First Seach
'''

from python_graph_implementation import *

def DFS(G,root):
	state = {}
	for v in G:
		state[v] = "White"
	runDFS(root,state)
	state = None


def runDFS(u, state):
	state[u] = "Gray"
	for v in u.getConnections():
		if state[v] == "White":
			runDFS(v,state)
	state[u] = "Black"
	print u.getId()



