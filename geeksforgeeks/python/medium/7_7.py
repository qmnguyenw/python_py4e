Introduction to Social Networks using NetworkX in Python



 **Prerequisite –**Python Basics ****

Ever wondered how the most popular social networking site Facebook works? How
we are connected with friends using just Facebook? So, Facebook and other
social networking sites work on a methodology called social networks. Social
networking is used in mostly all social media sites such as Facebook,
Instagram, and LinkedIn, etc. It has a significant effect on marketers to
engage customers. Social networks use graphs for creating a network. Their
nodes are people and edges are their connection between each other. Two nodes
with edges connected are friends. Now let’s see an example for understanding
what is social networks.

The network of 50 students in a class

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200704192204/SN1-160x200.png)

The network of 50 people

The most important python library used in social networking is **Networkx.**

##  **NetworkX**

NetworkX is a graph package that is used to create and modify different types
of graphs. It provides a rapid development environment for collaborative,
multidisciplinary projects.

  

  

#### Installation:

    
    
    pip install networkx
    

After starting python, we have to import networkx module:

    
    
    import networkx as nx
    

#### Basic inbuilt graph types are:

  *  **Graph:** This type of graph stores nodes and edges and edges are un-directed. It can have self-loops but cannot have parallel edges.
  *  **Di-Graph:** This type of graph is the base class for directed graphs. It can have nodes and edges and edges are directed in nature. It can have self-loops but parallel edges are not allowed in Di-Graph.
  *  **Multi-Graph:** This type of graph is an undirected graph class that can store multi or parallel edges. It can have self-loops as well. Multi-edges are multiple edges between 2 nodes.
  *  **Multi-DiGraph:** This type of graph is a directed graph class that can store multi edges. It can have self-loops as well. Multi-edges are multiple edges between 2 nodes.

#### Example of Graph creation :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import networkx library

import networkx as nx

 

# create an empty undirected graph 

G = nx.Graph()

 

# adding edge in graph G

G.add_edge(1, 2)

G.add_edge(2, 3, weight=0.9)  
  
---  
  
 __

 __

#### Drawing of graph:

Drawing can be done using Matplotlib.pyplot library.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import matplotlib.pyplot library

import matplotlib.pyplot as plt

 

# import networkx library

import networkx as nx

 

# create a cubical empty graph

G = nx.cubical_graph()

 

# plotting the graph

plt.subplot(122)

 

# draw a graph with red 

# node and vlue edge color

nx.draw(G, pos = nx.circular_layout(G), 

 node_color = 'r',

 edge_color = 'b')  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200704201402/SN2.png)

Circular Graph

####  **Graph Edge Removal:**

To remove an edge from the graph, use the **remove_edge()** method of graph
object.

>  **Syntax:** G.remove_edge(u, v)  
>
>
> **Parameters:**
>
>  
>
>
>  
>
>
>   *  **u:** first node  
>
>   * **v:** second node  
>
>

>
> **Return** : None

 **Graph Node Removal:**

To remove a node from the graph, use the **remove_node()** method of graph
object.

>  **Syntax:** G.remove_node(u)
>
>  **Parameter:** Node to remove  
>
>
> **Return:** None

#### Show the Adjacent vertices:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import networkx library

import netwokx as nx

 

# create an empty undirected graph

G = nx.Graph()

 

# add edge to the graph

G.add_edge('1', '2')

G.add_edge('2', '3')

 

# print the adjacent vertices

print(G.adj)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'1': {'2': {}}, '2': {'1': {}, '3': {}}, '3': {'2': {}}}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

