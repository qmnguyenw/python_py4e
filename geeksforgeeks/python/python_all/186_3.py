Python Program for Detect Cycle in a Directed Graph



Given a directed graph, check whether the graph contains a cycle or not. Your
function should return true if the given graph contains at least one cycle,
else return false. For example, the following graph contains three cycles
0->2->0, 0->1->2->0 and 3->3, so your function must return true.

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to detect cycle

# in a graph

 

from collections import defaultdict

 

class Graph():

 def __init__(self, vertices):

 self.graph = defaultdict(list)

 self.V = vertices

 

 def addEdge(self, u, v):

 self.graph[u].append(v)

 

 def isCyclicUtil(self, v, visited, recStack):

 

 # Mark current node as visited and 

 # adds to recursion stack

 visited[v] = True

 recStack[v] = True

 

 # Recur for all neighbours

 # if any neighbour is visited and in 

 # recStack then graph is cyclic

 for neighbour in self.graph[v]:

 if visited[neighbour] == False:

 if self.isCyclicUtil(neighbour, visited, recStack) == True:

 return True

 elif recStack[neighbour] == True:

 return True

 

 # The node needs to be poped from 

 # recursion stack before function ends

 recStack[v] = False

 return False

 

 # Returns true if graph is cyclic else false

 def isCyclic(self):

 visited = [False] * self.V

 recStack = [False] * self.V

 for node in range(self.V):

 if visited[node] == False:

 if self.isCyclicUtil(node, visited, recStack) == True:

 return True

 return False

 

g = Graph(4)

g.addEdge(0, 1)

g.addEdge(0, 2)

g.addEdge(1, 2)

g.addEdge(2, 0)

g.addEdge(2, 3)

g.addEdge(3, 3)

if g.isCyclic() == 1:

 print "Graph has a cycle"

else:

 print "Graph has no cycle"

 

# Thanks to Divyanshu Mehta for contributing this code  
  
---  
  
 __

 __

 **Output:**

    
    
    Graph has a cycle
    

Please refer complete article on Detect Cycle in a Directed Graph for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

