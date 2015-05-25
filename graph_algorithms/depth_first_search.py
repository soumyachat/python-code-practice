'''
DFS Implementation. Utilized Graph class
'''
from graph import *

def DFS(G):
	color = {}
	parent = {}
	for v in G:
		color[v] = 'WHITE'
		parent[v] = None
	
	for u in G:
		if color[u]=='WHITE':
			print "\nMoving to new connected component"
			DFS_VISIT(u,color, parent)


def DFS_VISIT(u, color, parent):
	color[u] = 'GREY'

	for v in u.connectedTo:
		if color[v] == 'WHITE':
			parent[v] = u
			DFS_VISIT(v, color, parent)
	color[u] = 'BLACK'
	print u, " has been searched."





