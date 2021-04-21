Minimum possible modifications in the matrix to reach destination



Given a matrix of size **N x M** consisting of integers **1, 2, 3** and **4**.  
Each value represents the possible movement from that cell:  

    
    
    1 -> move left
    2 -> move right
    3 -> move up
    4 -> move down.

The task is to find the minimum possible changes required in the matrix such
that there exists a path from **(0, 0)** to **(N-1, M-1)**.  
 **Examples:**  

> **Input :** mat[][] = {{2, 2, 4},  
> {1, 1, 1},  
> {3, 3, 2}};  
> **Output :** 1  
> Change the value of mat[1][2] to 4. So the sequence of moves will be  
> (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2)  
>  **Input :** mat[][] = {{2, 2, 1},  
> {4, 2, 3},  
> {4, 3, 2}}  
> **Output :** 2  
>

**Prerequisites:**  
1\. Djikstra’s Algorithm  
2.0-1 BFS  

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Method 1**  

  

  

  * Let’s consider each cell of the 2D matrix as a node of the weighted graph and each node can has at most four connected nodes(possible four directions). Each edge is weighted as: 
    * weight(U, V) = 0, if the direction of movement of node U points to V, else
    * weight(U, V) = 1
  * Now, this basically reduces to shortest path problem which can be computed using Djikstra’s Algorithm   

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find minimum possible

// changes required in the matrix

#include <bits/stdc++.h>

using namespace std;

// Function to find next possible node

int nextNode(int x, int y, int dir, int N, int M)

{

 if (dir == 1)

 y--;

 else if (dir == 2)

 y++;

 else if (dir == 3)

 x--;

 else

 x++;

 // If node is out of matrix

 if (!(x >= 0 && x < N && y >= 0 && y < M))

 return -1;

 else

 return (x * N + y);

}

// Prints shortest paths from src

// to all other vertices

int dijkstra(vector<pair<int, int> >* adj,

 int src, int dest, int N, int M)

{

 // Create a set to store vertices

 // that are bein preprocessed

 set<pair<int, int> > setds;

 // Create a vector for distances

 // and initialize all distances

 // as infinite (large value)

 vector<int> dist(N * M, INT_MAX);

 // Insert source itself in Set

 // and initialize its distance as 0

 setds.insert(make_pair(0, src));

 dist[src] = 0;

 /* Looping till all shortest

 distance are finalized

 then setds will become empty */

 while (!setds.empty()) {

 // The first vertex in Set

 // is the minimum distance

 // vertex, extract it from set.

 pair<int, int> tmp = *(setds.begin());

 setds.erase(setds.begin());

 // vertex label is stored in second

 // of pair (it has to be done this

 // way to keep the vertices sorted

 // distance (distance must be

 // first item in pair)

 int u = tmp.second;

 // 'i' is used to get all adjacent

 // vertices of a vertex

 vector<pair<int, int> >::iterator i;

 for (i = adj[u].begin();

 i != adj[u].end(); ++i) {

 // Get vertex label and weight

 // of current adjacent of u.

 int v = (*i).first;

 int weight = (*i).second;

 // If there is shorter path from u to v

 if (dist[v] > dist[u] + weight) {

 // If distance of v is not

 // INF then it must be

 // in our set, so removing it

 // and inserting again with

 // updated less distance.

 // Note : We extract only

 // those vertices from Set

 // for which distance is

 // finalized. So for them,

 // we would never reach here

 if (dist[v] != INT_MAX)

 setds.erase(setds.find(

 { dist[v], v }));

 // Updating distance of v

 dist[v] = dist[u] + weight;

 setds.insert(make_pair(dist[v], v));

 }

 }

 }

 // Return the distance

 return dist[dest];

}

// Function to find minimum possible

// changes required in the matrix

int MinModifications(vector<vector<int> >& mat)

{

 int N = mat.size(), M = mat[0].size();

 // Converting given matrix to a graph

 vector<pair<int, int> > adj[N * M];

 for (int i = 0; i < N; i++) {

 for (int j = 0; j < M; j++) {

 // Each cell is a node,

 // with label i*N + j

 for (int dir = 1; dir <= 4; dir++) {

 // Label of node if we

 // move in direction dir

 int nextNodeLabel

 = nextNode(i, j, dir, N, M);

 // If invalid(out of matrix)

 if (nextNodeLabel == -1)

 continue;

 // If direction is same as mat[i][j]

 if (dir == mat[i][j])

 adj[i * N + j].push_back(

 { nextNodeLabel, 0 });

 else

 adj[i * N + j].push_back(

 { nextNodeLabel, 1 });

 }

 }

 }

 // Applying djikstra's algorithm

 return dijkstra(adj, 0,

 (N - 1) * N + M - 1, N, M);

}

// Driver code

int main()

{

 vector<vector<int> > mat = { { 2, 2, 1 },

 { 4, 2, 3 },

 { 4, 3, 2 } };

 // Function call

 cout << MinModifications(mat);

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    2

**Time Complexity :** ![O\(N * M * log\(N * M\)\)
](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
ab7b8eacdb822df603539409994c5b60_l3.png)  
**Method 2**  
Here, edge weights are 0, and 1 only i.e it’s a 0-1 graph. The shortest path
in such graphs can be found using 0-1 BFS.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find minimum

// possible changes required

// in the matrix

#include <bits/stdc++.h>

using namespace std;

// Function to find next possible node

int nextNode(int x, int y, int dir,

 int N, int M)

{

 if (dir == 1)

 y--;

 else if (dir == 2)

 y++;

 else if (dir == 3)

 x--;

 else

 x++;

 // If node is out of matrix

 if (!(x >= 0 && x < N && y >= 0 && y < M))

 return -1;

 else

 return (x * N + y);

}

// Prints shortest distance

// from given source to

// every other vertex

int zeroOneBFS(vector<pair<int, int> >* adj,

 int src, int dest, int N, int M)

{

 // Initialize distances

 // from given source

 int dist[N * M];

 for (int i = 0; i < N * M; i++)

 dist[i] = INT_MAX;

 // Double ended queue to do BFS.

 deque<int> Q;

 dist[src] = 0;

 Q.push_back(src);

 while (!Q.empty()) {

 int v = Q.front();

 Q.pop_front();

 for (auto i : adj[v]) {

 // Checking for the optimal distance

 if (dist[i.first] > dist[v]

 + i.second) {

 dist[i.first] = dist[v]

 + i.second;

 // Put 0 weight edges to front

 // and 1 weight edges to back

 // so that vertices are processed

 // in increasing order of weights.

 if (i.second == 0)

 Q.push_front(i.first);

 else

 Q.push_back(i.first);

 }

 }

 }

 // Shortest distance to

 // reach destination

 return dist[dest];

}

// Function to find minimum possible

// changes required in the matrix

int MinModifications(vector<vector<int> >& mat)

{

 int N = mat.size(), M = mat[0].size();

 // Converting given matrix to a graph

 vector<pair<int, int> > adj[N * M];

 for (int i = 0; i < N; i++) {

 for (int j = 0; j < M; j++) {

 // Each cell is a node

 // with label i*N + j

 for (int dir = 1; dir <= 4; dir++) {

 // Label of node if we

 // move in direction dir

 int nextNodeLabel = nextNode(i, j,

 dir, N, M);

 // If invalid(out of matrix)

 if (nextNodeLabel == -1)

 continue;

 // If direction is same as mat[i][j]

 if (dir == mat[i][j])

 adj[i * N + j].push_back(

 { nextNodeLabel, 0 });

 else

 adj[i * N + j].push_back(

 { nextNodeLabel, 1 });

 }

 }

 }

 // Applying djikstra's algorithm

 return zeroOneBFS(adj, 0,

 (N - 1) * N + M - 1, N, M);

}

// Driver code

int main()

{

 vector<vector<int> > mat = { { 2, 2, 1 },

 { 4, 2, 3 },

 { 4, 3, 2 } };

 // Function call

 cout << MinModifications(mat);

 return 0;

}  
  
---  
  
 __

 __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find minimum

# possible changes required

# in the matrix

from collections import deque

# Function to find next possible node

def nextNode(x, y, dir, N, M):

 if (dir == 1):

 y -= 1

 elif (dir == 2):

 y += 1

 elif (dir == 3):

 x -= 1

 else:

 x += 1

 # If node is out of matrix

 if (not (x >= 0 and x < N and y >= 0 and y <
M)):

 return -1

 else:

 return (x * N + y)

# Prints shortest distance

# from given source to

# every other vertex

def zeroOneBFS(adj, src, dest, N, M):

 

 # Initialize distances

 # from given source

 dist = [10**8] *(N * M)

 # Double ended queue to do BFS.

 Q = deque()

 dist[src] = 0

 Q.append(src)

 while (len(Q) > 0):

 v = Q.popleft()

 for i in adj[v]:

 

 # print(i)

 # Checking for the optimal distance

 if (dist[i[0]] > dist[v] + i[1]):

 dist[i[0]] = dist[v] + i[1]

 

 # Put 0 weight edges to front

 # and 1 weight edges to back

 # so that vertices are processed

 # in increasing order of weights.

 if (i[1] == 0):

 Q.appendleft(i[0])

 else:

 Q.append(i[0])

 # Shortest distance to

 # reach destination

 return dist[dest]

# Function to find minimum possible

# changes required in the matrix

def MinModifications(mat):

 N, M = len(mat), len(mat[0])

 # Converting given matrix to a graph

 adj = [[] for i in range(N * M)]

 for i in range(N):

 for j in range(M):

 

 # Each cell is a node

 # with label i*N + j

 for dir in range(1, 5):

 

 # Label of node if we

 # move in direction dir

 nextNodeLabel = nextNode(i, j, dir, N, M)

 # If invalid(out of matrix)

 if (nextNodeLabel == -1):

 continue

 # If direction is same as mat[i][j]

 if (dir == mat[i][j]):

 adj[i * N + j].append([nextNodeLabel, 0])

 else:

 adj[i * N + j].append([nextNodeLabel, 1])

 # Applying djikstra's algorithm

 return zeroOneBFS(adj, 0, (N - 1) * N + M - 1,
N, M)

# Driver code

if __name__ == '__main__':

 mat = [ [ 2, 2, 1 ],

 [ 4, 2, 3 ],

 [ 4, 3, 2 ] ]

 # Function call

 print (MinModifications(mat))

# This code is contributed by mohit kumar 29.  
  
---  
  
 __

 __

 **Output:**

    
    
    2

**Time Complexity :** ![O\(N * M\)   ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-d90ca27e551dae508f761bc7243f9923_l3.png)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

