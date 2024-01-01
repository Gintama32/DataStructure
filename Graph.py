#implementing vertex class with vertex name as value and  a list to contain its adjacent vertices
from queue import Queue
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
#bfs implementation
    def bfs(starting_vertex):
        queue = Queue()
        visted_vertices = {}
        visted_vertices[starting_vertex.value] = True
        queue.put(starting_vertex)
        while queue.not_empty:
            current_vertex = queue.get()
            print(current_vertex.value)
            for vtx in current_vertex.adjacent_vertices:
                if vtx.value not in visted_vertices:
                    visted_vertices[vtx.value] = True
                    queue.put(vtx)



            
#list of vertices we'll be working with.

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
if __name__ == '__main__':
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
    alice.dfs()
    alice.bfs()