Python Program for Dijkstra’s shortest path algorithm | Greedy Algo-7



Given a graph and a source vertex in the graph, find the shortest paths from
source to all vertices in the given graph.  
Dijkstra’s algorithm is very similar to Prim’s algorithm for minimum spanning
tree. Like Prim’s MST, we generate an _SPT (shortest path tree)_ with a given
source as root. We maintain two sets, one set contains vertices included in
the shortest-path tree, another set includes vertices not yet included in the
shortest-path tree. At every step of the algorithm, we find a vertex that is
in the other set (set of not yet included) and has a minimum distance from the
source.  
Below are the detailed steps used in Dijkstra’s algorithm to find the shortest
path from a single source vertex to all other vertices in the given graph.  
Algorithm  
**1)** Create a set _sptSet_ (shortest path tree set) that keeps track of
vertices included in shortest path tree, i.e., whose minimum distance from
source is calculated and finalized. Initially, this set is empty.  
**2)** Assign a distance value to all vertices in the input graph. Initialize
all distance values as INFINITE. Assign distance value as 0 for the source
vertex so that it is picked first.  
**3)** While _sptSet_ doesn’t include all vertices:

  * Pick a vertex u which is not there in _sptSet_ and has minimum distance value. 
  * Include u to _sptSet_. 
  * Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if the sum of a distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v. 

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for Dijkstra's single

# source shortest path algorithm. The program is

# for adjacency matrix representation of the graph

# Library for INT_MAX

import sys

class Graph():

 def __init__(self, vertices):

 self.V = vertices

 self.graph = [[0 for column in range(vertices)]

 for row in range(vertices)]

 def printSolution(self, dist):

 print("Vertex tDistance from Source")

 for node in range(self.V):

 print(node, "t", dist[node])

 # A utility function to find the vertex with

 # minimum distance value, from the set of vertices

 # not yet included in shortest path tree

 def minDistance(self, dist, sptSet):

 # Initilaize minimum distance for next node

 min = sys.maxsize

 # Search not nearest vertex not in the

 # shortest path tree

 for v in range(self.V):

 if dist[v] < min and sptSet[v] == False:

 min = dist[v]

 min_index = v

 return min_index

 # Funtion that implements Dijkstra's single source

 # shortest path algorithm for a graph represented

 # using adjacency matrix representation

 def dijkstra(self, src):

 dist = [sys.maxsize] * self.V

 dist[src] = 0

 sptSet = [False] * self.V

 for cout in range(self.V):

 # Pick the minimum distance vertex from

 # the set of vertices not yet processed.

 # u is always equal to src in first iteration

 u = self.minDistance(dist, sptSet)

 # Put the minimum distance vertex in the

 # shotest path tree

 sptSet[u] = True

 # Update dist value of the adjacent vertices

 # of the picked vertex only if the current

 # distance is greater than new distance and

 # the vertex in not in the shotest path tree

 for v in range(self.V):

 if self.graph[u][v] > 0 and

 sptSet[v] == False and

 dist[v] > dist[u] + self.graph[u][v]:

 dist[v] = dist[u] + self.graph[u][v]

 self.printSolution(dist)

# Driver program

g = Graph(9)

g.graph = [[0, 4, 0, 0, 0, 0, 0, 8,
0],

 [4, 0, 8, 0, 0, 0, 0, 11, 0],

 [0, 8, 0, 7, 0, 4, 0, 0, 2],

 [0, 0, 7, 0, 9, 14, 0, 0, 0],

 [0, 0, 0, 9, 0, 10, 0, 0, 0],

 [0, 0, 4, 14, 10, 0, 2, 0, 0],

 [0, 0, 0, 0, 0, 2, 0, 1, 6],

 [8, 11, 0, 0, 0, 0, 1, 0, 7],

 [0, 0, 2, 0, 0, 0, 6, 7, 0]

 ]

g.dijkstra(0)

# This code is contributed by Divyanshu Mehta  
  
---  
  
 __

 __

 **Output:**

    
    
    Vertex tDistance from Source
    0 t 0
    1 t 4
    2 t 12
    3 t 19
    4 t 21
    5 t 11
    6 t 9
    7 t 8
    8 t 14

Please refer complete article on Dijkstra’s shortest path algorithm | Greedy
Algo-7 for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

