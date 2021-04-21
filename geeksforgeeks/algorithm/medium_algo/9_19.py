Clone an undirected graph with multiple connected components



Given an undirected graph with multiple connected components, the task is to
clone the graph. Cloning a graph with a single connected component can be seen
here.

 **Examples:**

    
    
    An example of an undirected graph 
    with 3 connected components:
    

![](https://media.geeksforgeeks.org/wp-content/uploads/Graphs-300x225.jpg)

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:**  
The idea is to follow the same approach posted for cloning connected graph,
but with every node so that we can clone graphs with multiple connected
components.

We are going to use a GraphNode class and a Graph class. The Graph class is
compulsory, since we might have multiple connected components (see example
above), and we cannot deal with them having only a GraphNode as an input. For
the Graph class, what we actually need is a list of GraphNodes. It’s also
possible to make a list of nodes instead of creating a class, both ways work.

  

  

To keep track of the visited nodes, we need a data structure; a map is an
appropriate one, as we can map from the “old” nodes to the “new” ones (the
cloned). So, we are defining a main function, which creates the map, and uses
a helper function to fill it. Once the map is created, a new graph can be
created, using the cloned nodes in the map.  
The helper function is going to put connections between nodes (besides filling
the map). As we are dealing with a whole connected component, a similar
approach to the BFS is going to be followed.

Notice that in the main function, we don’t call the helper function for each
node in the Graph; if the node is stored in the map, it means that we’ve
already visited it and dealt with its connected component, so no need to
repeat the steps again.  
In order to check if the graph has been correctly cloned, we can print the
memory addresses of the nodes, and compare them to see whether we’ve cloned,
or we’ve copied them.

Below is the implementation of the above approach:

## C++14

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <bits/stdc++.h>

using namespace std;

// GraphNode class represents each

// Node of the Graph

class GraphNode

{

 int data;

 list<GraphNode *> children;

 

 // Constructor to initialize the

 // node with value

 public:

 GraphNode(int data)

 {

 this->data = data;

 }

 

 // Function to add a child to the

 // current node

 void addChild(GraphNode *node)

 {

 this->children.push_back(node);

 }

 

 // Function to return a list of children

 // for the current node

 list<GraphNode *> getChildren()

 {

 return children;

 }

 

 // Function to set the node's value

 void setData(int data)

 {

 this->data = data;

 }

 

 // Function to return the node's value

 int getData()

 {

 return data;

 }

};

// Class to represent the graph

class Graph

{

 list<GraphNode *> nodes;

 

 public:

 Graph(){}

 

 // Constructor to set the graph's nodes

 Graph(list<GraphNode *> nodes)

 {

 this->nodes = nodes;

 }

 

 // Function to add a node to the graph

 void addNode(GraphNode *node)

 {

 this->nodes.push_back(node);

 }

 

 // Function to return the list of nodes

 // for the graph

 list<GraphNode *> getNodes()

 {

 return this->nodes;

 }

};

class GFG{

 

// Function to clone the graph

// Function to clone the connected components

void cloneConnectedComponent(GraphNode *node,

 map<GraphNode *,

 GraphNode *> &map;)

{

 queue<GraphNode *> queue;

 queue.push(node);

 

 while (!queue.empty())

 {

 GraphNode *current = queue.front();

 queue.pop();

 GraphNode *currentCloned = NULL;

 

 if (map.find(current) != map.end())

 {

 currentCloned = map[current];

 }

 else

 {

 currentCloned = new GraphNode(

 current->getData());

 map[current] = currentCloned;

 }

 

 list<GraphNode *> children = current->getChildren();

 for(auto child : children)

 {

 if (map.find(child) != map.end())

 {

 currentCloned->addChild(map[child]);

 }

 else

 {

 GraphNode *childCloned = new GraphNode(

 child->getData());

 map[child] = childCloned;

 currentCloned->addChild(childCloned);

 queue.push(child);

 }

 }

 }

}

public:

 Graph *cloneGraph(Graph *graph)

 {

 map<GraphNode *, GraphNode *> mapp;

 for(auto node : graph->getNodes())

 {

 if (mapp.find(node) == mapp.end())

 cloneConnectedComponent(node, mapp);

 }

 Graph *cloned = new Graph();

 for(auto current : mapp)

 cloned->addNode(current.second);

 

 return cloned;

 }

// Function to build the graph

Graph *buildGraph()

{

 

 // Create graph

 Graph *g = new Graph();

 

 // Adding nodes to the graph

 GraphNode *g1 = new GraphNode(1);

 g->addNode(g1);

 GraphNode *g2 = new GraphNode(2);

 g->addNode(g2);

 GraphNode *g3 = new GraphNode(3);

 g->addNode(g3);

 GraphNode *g4 = new GraphNode(4);

 g->addNode(g4);

 GraphNode *g5 = new GraphNode(5);

 g->addNode(g5);

 GraphNode *g6 = new GraphNode(6);

 g->addNode(g6);

 

 // Adding edges

 g1->addChild(g2);

 g1->addChild(g3);

 g2->addChild(g1);

 g2->addChild(g4);

 g3->addChild(g1);

 g3->addChild(g4);

 g4->addChild(g2);

 g4->addChild(g3);

 g5->addChild(g6);

 g6->addChild(g5);

 

 return g;

}

// Function to print the connected components

void printConnectedComponent(GraphNode *node,

 set<GraphNode *> &visited;)

{

 if (visited.find(node) != visited.end())

 return;

 queue<GraphNode *> q;

 q.push(node);

 

 while (!q.empty())

 {

 GraphNode *currentNode = q.front();

 q.pop();

 

 if (visited.find(currentNode) != visited.end())

 continue;

 

 visited.insert(currentNode);

 cout << "Node " << currentNode->getData()

 << " - " << currentNode << endl;

 for(GraphNode *child : currentNode->getChildren())

 {

 cout << "\tNode " << child->getData()

 << " - " << child << endl;

 q.push(child);

 }

 }

}

};

// Driver code

int main()

{

 GFG *gfg = new GFG();

 Graph *g = gfg->buildGraph();

 

 // Original graph

 cout << "\tINITIAL GRAPH\n";

 set<GraphNode *> visited;

 for(GraphNode *n : g->getNodes())

 gfg->printConnectedComponent(n, visited);

 

 // Cloned graph

 cout << "\n\n\tCLONED GRAPH\n";

 Graph *cloned = gfg->cloneGraph(g);

 visited.clear();

 for(GraphNode *node : cloned->getNodes())

 gfg->printConnectedComponent(node, visited);

}

// This code is contributed by sanjeev2552  
  
---  
  
 __

 __

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java implementation of the approach

import java.util.ArrayList;

import java.util.HashMap;

import java.util.HashSet;

import java.util.LinkedList;

import java.util.List;

import java.util.Map;

import java.util.Queue;

import java.util.Set;

// Class to represent the graph

class Graph {

 private List<GraphNode> nodes;

 // Constructor to create an empty ArrayList

 // to store the nodes of the graph

 public Graph()

 {

 this.nodes = new ArrayList<GraphNode>();

 }

 // Constructor to set the graph's nodes

 public Graph(List<GraphNode> nodes)

 {

 this.nodes = nodes;

 this.nodes = new ArrayList<GraphNode>();

 }

 // Function to add a node to the graph

 public void addNode(GraphNode node)

 {

 this.nodes.add(node);

 }

 // Function to return the list of nodes

 // for the graph

 public List<GraphNode> getNodes()

 {

 return this.nodes;

 }

}

// GraphNode class represents each

// Node of the Graph

class GraphNode {

 private int data;

 private List<GraphNode> children;

 // Constructor to initialize the node with value

 public GraphNode(int data)

 {

 this.data = data;

 this.children = new ArrayList<GraphNode>();

 }

 // Function to add a child to the current node

 public void addChild(GraphNode node)

 {

 this.children.add(node);

 }

 // Function to return a list of children

 // for the current node

 public List<GraphNode> getChildren()

 {

 return children;

 }

 // Function to set the node's value

 public void setData(int data)

 {

 this.data = data;

 }

 // Function to return the node's value

 public int getData()

 {

 return data;

 }

}

public class GFG {

 // Function to clone the graph

 public Graph cloneGraph(Graph graph)

 {

 Map<GraphNode, GraphNode> map

 = new HashMap<GraphNode, GraphNode>();

 for (GraphNode node : graph.getNodes()) {

 if (!map.containsKey(node))

 cloneConnectedComponent(node, map);

 }

 Graph cloned = new Graph();

 for (GraphNode current : map.values())

 cloned.addNode(current);

 return cloned;

 }

 // Function to clone the connected components

 private void cloneConnectedComponent(GraphNode node,

 Map<GraphNode, GraphNode> map)

 {

 Queue<GraphNode> queue = new LinkedList<GraphNode>();

 queue.add(node);

 while (!queue.isEmpty()) {

 GraphNode current = queue.poll();

 GraphNode currentCloned = null;

 if (map.containsKey(current)) {

 currentCloned = map.get(current);

 }

 else {

 currentCloned = new GraphNode(current.getData());

 map.put(current, currentCloned);

 }

 List<GraphNode> children = current.getChildren();

 for (GraphNode child : children) {

 if (map.containsKey(child)) {

 currentCloned.addChild(map.get(child));

 }

 else {

 GraphNode childCloned

 = new GraphNode(child.getData());

 map.put(child, childCloned);

 currentCloned.addChild(childCloned);

 queue.add(child);

 }

 }

 }

 }

 // Function to build the graph

 public Graph buildGraph()

 {

 // Create graph

 Graph g = new Graph();

 // Adding nodes to the graph

 GraphNode g1 = new GraphNode(1);

 g.addNode(g1);

 GraphNode g2 = new GraphNode(2);

 g.addNode(g2);

 GraphNode g3 = new GraphNode(3);

 g.addNode(g3);

 GraphNode g4 = new GraphNode(4);

 g.addNode(g4);

 GraphNode g5 = new GraphNode(5);

 g.addNode(g5);

 GraphNode g6 = new GraphNode(6);

 g.addNode(g6);

 // Adding edges

 g1.addChild(g2);

 g1.addChild(g3);

 g2.addChild(g1);

 g2.addChild(g4);

 g3.addChild(g1);

 g3.addChild(g4);

 g4.addChild(g2);

 g4.addChild(g3);

 g5.addChild(g6);

 g6.addChild(g5);

 return g;

 }

 // Function to print the connected components

 public void printConnectedComponent(GraphNode node,

 Set<GraphNode> visited)

 {

 if (visited.contains(node))

 return;

 Queue<GraphNode> q = new LinkedList<GraphNode>();

 q.add(node);

 while (!q.isEmpty()) {

 GraphNode currentNode = q.remove();

 if (visited.contains(currentNode))

 continue;

 visited.add(currentNode);

 System.out.println("Node "

 + currentNode.getData() + " - " + currentNode);

 for (GraphNode child : currentNode.getChildren()) {

 System.out.println("\tNode "

 + child.getData() + " - " + child);

 q.add(child);

 }

 }

 }

 // Driver code

 public static void main(String[] args)

 {

 GFG gfg = new GFG();

 Graph g = gfg.buildGraph();

 // Original graph

 System.out.println("\tINITIAL GRAPH");

 Set<GraphNode> visited = new HashSet<GraphNode>();

 for (GraphNode n : g.getNodes())

 gfg.printConnectedComponent(n, visited);

 // Cloned graph

 System.out.println("\n\n\tCLONED GRAPH\n");

 Graph cloned = gfg.cloneGraph(g);

 visited = new HashSet<GraphNode>();

 for (GraphNode node : cloned.getNodes())

 gfg.printConnectedComponent(node, visited);

 }

}  
  
---  
  
 __

 __

 **Output:**

    
    
    INITIAL GRAPH
    Node 1 - GraphNode@232204a1
        Node 2 - GraphNode@4aa298b7
        Node 3 - GraphNode@7d4991ad
    Node 2 - GraphNode@4aa298b7
        Node 1 - GraphNode@232204a1
        Node 4 - GraphNode@28d93b30
    Node 3 - GraphNode@7d4991ad
        Node 1 - GraphNode@232204a1
        Node 4 - GraphNode@28d93b30
    Node 4 - GraphNode@28d93b30
        Node 2 - GraphNode@4aa298b7
        Node 3 - GraphNode@7d4991ad
    Node 5 - GraphNode@1b6d3586
        Node 6 - GraphNode@4554617c
    Node 6 - GraphNode@4554617c
        Node 5 - GraphNode@1b6d3586
    
    
        CLONED GRAPH
    
    Node 1 - GraphNode@74a14482
        Node 2 - GraphNode@1540e19d
        Node 3 - GraphNode@677327b6
    Node 2 - GraphNode@1540e19d
        Node 1 - GraphNode@74a14482
        Node 4 - GraphNode@14ae5a5
    Node 3 - GraphNode@677327b6
        Node 1 - GraphNode@74a14482
        Node 4 - GraphNode@14ae5a5
    Node 4 - GraphNode@14ae5a5
        Node 2 - GraphNode@1540e19d
        Node 3 - GraphNode@677327b6
    Node 6 - GraphNode@7f31245a
        Node 5 - GraphNode@6d6f6e28
    Node 5 - GraphNode@6d6f6e28
        Node 6 - GraphNode@7f31245a

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

