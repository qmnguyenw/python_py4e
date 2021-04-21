Building an undirected graph and finding shortest path using Dictionaries in
Python



 **Prerequisites:**

  * BFS for a Graph
  * Dictonaries in Python

In this article, we will be looking at how to build an undirected graph and
then find the shortest path between two nodes/vertex of that graph easily
using dictionaries in Python Language.

### Building a Graph using Dictonaries

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200617040109/cool.jpg)

 **Approach:** The idea is to store the adjacency list into the dictionaries,
which helps to store the graph in any format not only in the form of the
integers. Here we have used characters as a reference on those places any
custom objects can also be used.

Below is the implementation of the above approach:  

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 implementation to build a

# graph using Dictonaries

 

from collections import defaultdict

 

# Function to build the graph

def build_graph():

 edges = [

 ["A", "B"], ["A", "E"], 

 ["A", "C"], ["B", "D"],

 ["B", "E"], ["C", "F"],

 ["C", "G"], ["D", "E"]

 ]

 graph = defaultdict(list)

 

 # Loop to iterate over every 

 # edge of the graph

 for edge in edges:

 a, b = edge[0], edge[1]

 

 # Creating the graph 

 # as adjacency list

 graph[a].append(b)

 graph[b].append(a)

 return graph

 

if __name__ == "__main__":

 graph = build_graph()

 

 print(graph)  
  
---  
  
 __

 __

