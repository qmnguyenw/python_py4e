Why Prim’s and Kruskal’s MST algorithm fails for Directed Graph?



 **Pre-requisites:**

  * Graph and its representations
  * Greedy Algorithms | Set 5 (Prim’s Minimum Spanning Tree (MST))
  * Kruskal’s Minimum Spanning Tree Algorithm | Greedy Algo-2

Given a directed graph **D = < V, E >**, the task is to find the minimum
spanning tree for the given directed graph

 **Example:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200316173940/Untitled-Diagram66-3.jpg)

But the Prim’s Minimum Spanning Tree and Kruskal’s algorithm fails for
directed graphs. Let us see why

 **Why Prim’s Algorithm Fails for Directed Graph ?**

  

  

Prim’s algorithm assumes that all vertices are connected. But in a directed
graph, every node is not reachable from every other node. So, Prim’s algorithm
fails due to this reason.  
 **For Example:**  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200320001817/Untitled-Diagramksh.png)

As it is visible in the graph, no node is reachable from node 4. Directed
graphs fail the requirement that all vertices are connected.

 **Why Kruskal’s Algorithm fails for directed graph ?**  
In Kruskal’s algorithm, In each step, it is checked that if the edges form a
cycle with the spanning-tree formed so far. But Kruskal’s algorithm fails to
detect the cycles in a directed graph as there are cases when there is no
cycle between the vertices but Kruskal’s Algorithm assumes it to cycle and
don’t take consider some edges due to which Kruskal’s Algorithm fails for
directed graph.  
 **For example:**  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200320002247/Untitled-Diagramksjd.png)  
This graph will be reported to contain a cycle with the Union-Find method, but
this graph has no cycle.

The equivalent of minimum spanning tree in directed graphs is, “Minimum
Spanning Arborescence”(also known as optimum branching) can be solved by
Edmonds’ algorithm with a running time of O(EV). This algorithm is directed
analog of the minimum spanning tree problem.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

