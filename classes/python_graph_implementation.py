'''
Basic Implementation of a Graph class
Uses dictionaries to store adjacency lists.
Some functions included.
  add_edge(graph, start, end): Adds an edge to the Graph
'''

# Vertex Class
class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}
	
	def addNeighbor(self, neighbor, weight = 0):
		self.connectedTo[neighbor] = weight 

	def __str__(self):
		return str(self.id) + ' connected to: ' + str( [x.id for x in self.connectedTo])

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self, neighbor):
		return self.connectedTo[neighbor]



''' 
Graph class
'''
class Graph:
	def __init__(self):
		self.num_vertices = 0
		self.vertex_list = {}
	
	def addVertex(self, key):
		self.num_vertices += 1
		new_vertex = Vertex(key)
		self.vertex_list[key] = new_vertex
		return new_vertex

	def addEdge(self, f, t, cost = 0):
		if f not in self.vertex_list:
			new_vertex = self.addVertex(f)
		if t not in self.vertex_list:
			new_vertex = self.addVertex(t)
		self.vertex_list[f].addNeighbor(self.vertex_list[t],cost)
		self.vertex_list[t].addNeighbor(self.vertex_list[f],cost)

	def getVertex(self,n):
		if n in self.vertex_list:
			return self.vertex_list[n]
		else:
			return None
	
	def __contains__(self, n):
		return n in self.vertex_list

	def getVertices(self):
		return self.vertex_list.keys()

	def __iter__(self):
		return iter(self.vertex_list.values())
	





