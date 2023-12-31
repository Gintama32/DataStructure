#implementing vertex class with vertex name as value and  a list to contain its adjacent vertices
class Vertex():
    def __init__(self,value):
        self.value= value
        self.adjacent_vertices = []
    #method to add adjacent vertices of vertex
    def add_adjacent_vertices(self,vertices):
        for vertex in vertices:
            if vertex not in self.adjacent_vertices:
                self.adjacent_vertices.append(vertex)
    #depth first search traversal, we print vertex to show our traversal path
    def dfs(self,visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = {}
        visited_vertices[self.value] = True
        print(self.value)
        for vtx in self.adjacent_vertices:
            if vtx.value not in visited_vertices:
                vtx.dfs(visited_vertices)
            
#list of vertices we'll be working with.
vertices = ['Alice', 'Bob','Irene', 'Cynthia', 'Marco','David']
alice = Vertex('Alice')
bob = Vertex('Bob')
irene = Vertex('Irene')
cynthia = Vertex('Cynthia')
marco = Vertex('Marco')
david = Vertex('David')
#adding adjacent vertices
alice.add_adjacent_vertices([bob, cynthia])
bob.add_adjacent_vertices([alice, irene])
cynthia.add_adjacent_vertices([alice,marco,david])
irene.add_adjacent_vertices([bob])
marco.add_adjacent_vertices([cynthia, david])
david.add_adjacent_vertices([cynthia, marco])
#the traversal of dfs from irene, make sure to check the graph and the output of this dfs
irene.dfs()
"""
this is graph that we have created using Vertex class and by adding adjacent vertices
              Alice
            /      \
          /         \ 
        Bob         Cynthia
        |             |    \
        |             |     \
        Irene       David--- Marco
"""