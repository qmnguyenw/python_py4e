Comparision between Tarjan’s and Kosaraju’s Algorithm



 ** _Tarjan’s Algorithm_** **:** The Tarjan’s Algorithm is an efficient graph
algorithm that is used to find the **Strongly Connected Component** ( **SCC**
) in a directed graph by using only one DFS traversal in linear time
complexity.

 **Working:**

  * Perform a DFS traversal over the nodes so that the sub-trees of the Strongly Connected Components are removed when they are encountered.
  * Then two values are assigned:
    * The first value is the counter value when the node is explored for the first time.
    * Second value stores the lowest node value reachable from the initial node which is not part of another **SCC**.
  * When the nodes are explored, they are pushed into a stack.
  * If there are any unexplored children of a node are left, they are explored and the assigned value is respectively updated.

Below is the program to find the SCC of the given graph using Tarjan’s
Algorithm:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the SCC using

// Tarjan's algorithm (single DFS)

#include <iostream>

#include <list>

#include <stack>

#define NIL -1

using namespace std;

 

// A class that represents

// an directed graph

class Graph {

 // No. of vertices

 int V;

 

 // A dynamic array of adjacency lists

 list<int>* adj;

 

 // A Recursive DFS based function

 // used by SCC()

 void SCCUtil(int u, int disc[],

 int low[], stack<int>* st,

 bool stackMember[]);

 

public:

 // Member functions

 Graph(int V);

 void addEdge(int v, int w);

 void SCC();

};

 

// Constructor

Graph::Graph(int V)

{

 this->V = V;

 adj = new list<int>[V];

}

 

// Function to add an edge to the graph

void Graph::addEdge(int v, int w)

{

 adj[v].push_back(w);

}

 

// Recursive function to finds the SCC

// using DFS traversal

void Graph::SCCUtil(int u, int disc[],

 int low[], stack<int>* st,

 bool stackMember[])

{

 static int time = 0;

 

 // Initialize discovery time

 // and low value

 disc[u] = low[u] = ++time;

 st->push(u);

 stackMember[u] = true;

 

 // Go through all vertices

 // adjacent to this

 list<int>::iterator i;

 

 for (i = adj[u].begin();

 i != adj[u].end(); ++i) {

 // v is current adjacent of 'u'

 int v = *i;

 

 // If v is not visited yet,

 // then recur for it

 if (disc[v] == -1) {

 SCCUtil(v, disc, low,

 st, stackMember);

 

 // Check if the subtree rooted

 // with 'v' has connection to

 // one of the ancestors of 'u'

 low[u] = min(low[u], low[v]);

 }

 

 // Update low value of 'u' only of

 // 'v' is still in stack

 else if (stackMember[v] == true)

 low[u] = min(low[u], disc[v]);

 }

 

 // head node found, pop the stack

 // and print an SCC

 

 // Store stack extracted vertices

 int w = 0;

 

 // If low[u] and disc[u]

 if (low[u] == disc[u]) {

 // Until stack st is empty

 while (st->top() != u) {

 w = (int)st->top();

 

 // Print the node

 cout << w << " ";

 stackMember[w] = false;

 st->pop();

 }

 w = (int)st->top();

 cout << w << "\n";

 stackMember[w] = false;

 st->pop();

 }

}

 

// Function to find the SCC in the graph

void Graph::SCC()

{

 // Stores the discovery times of

 // the nodes

 int* disc = new int[V];

 

 // Stores the nodes with least

 // discovery time

 int* low = new int[V];

 

 // Checks whether a node is in

 // the stack or not

 bool* stackMember = new bool[V];

 

 // Stores all the connected ancestors

 stack<int>* st = new stack<int>();

 

 // Initialize disc and low,

 // and stackMember arrays

 for (int i = 0; i < V; i++) {

 disc[i] = NIL;

 low[i] = NIL;

 stackMember[i] = false;

 }

 

 // Recursive helper function to

 // find the SCC in DFS tree with

 // vertex 'i'

 for (int i = 0; i < V; i++) {

 

 // If current node is not

 // yet visited

 if (disc[i] == NIL) {

 SCCUtil(i, disc, low,

 st, stackMember);

 }

 }

}

 

// Driver Code

int main()

{

 // Given a graph

 Graph g1(5);

 g1.addEdge(1, 0);

 g1.addEdge(0, 2);

 g1.addEdge(2, 1);

 g1.addEdge(0, 3);

 g1.addEdge(3, 4);

 

 // Function Call to find SCC using

 // Tarjan's Algorithm

 g1.SCC();

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    3
    1 2 0
    

**_Kosaraju’s Algorithm_** **:** The Kosaraju’s Algorithm is also a Depth
First Search **** based algorithm which is used to find the **SCC** in a
directed graph in linear time complexity. The basic concept of this algorithm
is that if we are able to arrive at vertex **v** initially starting from
vertex **u** , then we should be able to arrive at vertex **u** starting from
vertex **v** , ****and if this is the situation, we can say and conclude that
vertices **u** and **v** are strongly connected, and they are in the strongly
connected sub-graph.

  

  

 **Working:**

  * Perform a DFS traversal on the given graph, keeping track of the finish times of each node. This process can be performed by using a stack.
  * When the procedure of running the DFS traversal over the graph finishes, put the source vertex on the stack. In this way, the node with the highest finishing time will be at the top of the stack.
  * Reverse the original graph by using an Adjacency List.
  * Then perform another DFS traversal on the reversed graph with the source vertex as the vertex on the top of the stack. When the DFS running on the reversed graph finishes, all the nodes that are visited will form one strongly connected component.
  * If any more nodes are left or remain unvisited, this signifies the presence of more than one strongly connected component on the graph.
  * So pop the vertices from the top of the stack until a valid unvisited node is found. This will have the highest finishing time of all currently unvisited nodes.

Below is the program to find the SCC of the given graph using Kosaraju’s
Algorithm:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print the SCC of the

// graph using Kosaraju's Algorithm

#include <iostream>

#include <list>

#include <stack>

using namespace std;

 

class Graph {

 // No. of vertices

 int V;

 

 // An array of adjacency lists

 list<int>* adj;

 

 // Member Functions

 void fillOrder(int v, bool visited[],

 stack<int>& Stack);

 void DFSUtil(int v, bool visited[]);

 

public:

 Graph(int V);

 void addEdge(int v, int w);

 void printSCCs();

 Graph getTranspose();

};

 

// Constructor of class

Graph::Graph(int V)

{

 this->V = V;

 adj = new list<int>[V];

}

 

// Recursive function to print DFS

// starting from v

void Graph::DFSUtil(int v, bool visited[])

{

 // Mark the current node as

 // visited and print it

 visited[v] = true;

 cout << v << " ";

 

 // Recur for all the vertices

 // adjacent to this vertex

 list<int>::iterator i;

 

 // Traverse Adjacency List of node v

 for (i = adj[v].begin();

 i != adj[v].end(); ++i) {

 

 // If child node *i is unvisited

 if (!visited[*i])

 DFSUtil(*i, visited);

 }

}

 

// Function to get the transpose of

// the given graph

Graph Graph::getTranspose()

{

 Graph g(V);

 for (int v = 0; v < V; v++) {

 // Recur for all the vertices

 // adjacent to this vertex

 list<int>::iterator i;

 for (i = adj[v].begin();

 i != adj[v].end(); ++i) {

 // Add to adjacency list

 g.adj[*i].push_back(v);

 }

 }

 

 // Return the reversed graph

 return g;

}

 

// Function to add an Edge to the given

// graph

void Graph::addEdge(int v, int w)

{

 // Add w to v’s list

 adj[v].push_back(w);

}

 

// Function that fills stack with vertices

// in increasing order of finishing times

void Graph::fillOrder(int v, bool visited[],

 stack<int>& Stack)

{

 // Mark the current node as

 // visited and print it

 visited[v] = true;

 

 // Recur for all the vertices

 // adjacent to this vertex

 list<int>::iterator i;

 

 for (i = adj[v].begin();

 i != adj[v].end(); ++i) {

 

 // If child node *i is unvisited

 if (!visited[*i]) {

 fillOrder(*i, visited, Stack);

 }

 }

 

 // All vertices reachable from v

 // are processed by now, push v

 Stack.push(v);

}

 

// Function that finds and prints all

// strongly connected components

void Graph::printSCCs()

{

 stack<int> Stack;

 

 // Mark all the vertices as

 // not visited (For first DFS)

 bool* visited = new bool[V];

 for (int i = 0; i < V; i++)

 visited[i] = false;

 

 // Fill vertices in stack according

 // to their finishing times

 for (int i = 0; i < V; i++)

 if (visited[i] == false)

 fillOrder(i, visited, Stack);

 

 // Create a reversed graph

 Graph gr = getTranspose();

 

 // Mark all the vertices as not

 // visited (For second DFS)

 for (int i = 0; i < V; i++)

 visited[i] = false;

 

 // Now process all vertices in

 // order defined by Stack

 while (Stack.empty() == false) {

 

 // Pop a vertex from stack

 int v = Stack.top();

 Stack.pop();

 

 // Print SCC of the popped vertex

 if (visited[v] == false) {

 gr.DFSUtil(v, visited);

 cout << endl;

 }

 }

}

 

// Driver Code

int main()

{

 // Given Graph

 Graph g(5);

 g.addEdge(1, 0);

 g.addEdge(0, 2);

 g.addEdge(2, 1);

 g.addEdge(0, 3);

 g.addEdge(3, 4);

 

 // Function Call to find the SCC

 // using Kosaraju's Algorithm

 g.printSCCs();

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    0 1 2 
    3 
    4
    

**_Time Complexity_ :**  
The time complexity of Tarjan’s Algorithm and Kosaraju’s Algorithm will be
**O(V + E)** , where **V** represents the set of vertices and **E** represents
the set of edges of the graph. Tarjan’s algorithm has much lower constant
factors w.r.t Kosaraju’s algorithm. In Kosaraju’s algorithm, the traversal of
the graph is done at least 2 times, so the constant factor can be of double
time. We can print the **SCC** in progress with Kosaraju’s algorithm as we
perform the second DFS. While performing Tarjan’s Algorithm, it requires extra
time to print the **SCC** after finding the head of the **SCCs** sub-tree.

 ** _Summary_ :**  
Both the methods have the same linear time complexity, but the techniques or
the procedure for the **SCC** computations are fairly different. Tarjan’s
method solely depends on the record of nodes in a **DFS** to partition the
graph whereas Kosaraju’s method performs the two DFS (or 3 DFS if we want to
leave the original graph unchanged) on the graph and is quite similar to the
method for finding the topological sorting of a graph.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

