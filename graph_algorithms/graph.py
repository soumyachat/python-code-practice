'''
The GRAPH data structure
'''


class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}
	
	def addNeighbor(self, nbr, weight = 1):
		self.connectedTo[nbr] = weight
	def getId(self):
		return self.id

	def __str__(self):
		return str(self.id) 

	
class Graph:
	def __init__(self):
		self.num_vertices = 0
		self.vertex_list = {}
	
	def addVertex(self, key):
		new_vertex = Vertex(key)
		self.num_vertices += 1
		self.vertex_list[key] = new_vertex


	def addEdge(self, f, t, cost = 1):
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

	def __str__(self):
		print "Vertices: ", self.vertex_list.keys()
		print "Edges: "
		for v in self.vertex_list.values():
			for j in v.connectedTo:
				print v,", ", j, ": ",v.connectedTo[j]
		return "**** Elements if the Graph ****" 
		#return str(self.id) + ' connected to: ' + str( [x.id for x in self.connectedTo])



#### ======== end of graph data structure =====

