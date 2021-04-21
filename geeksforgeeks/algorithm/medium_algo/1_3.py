Single source shortest path between two cities



Given a graph of **N** Nodes and **E** edges in form of **{U, V, W}** such
that there exists an edge between **U and V** with weight **W**. You are given
an integer **K** and source **src** and destination **dst**. The task is to
find the cheapest cost path from given source to destination from **K** stops.

 **Examples:**

>  **Input:** N = 3, edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0,
> dst = 2, k = 1  
>  **Output:** 200  
>  **Explanation:**  
>  The Cheapest Price is from City 0 to City 2. With just one stop, it just
> costs 200 which is our Output.
>
>  **Input:** N = 3, edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0,
> dst = 2, k = 0  
>  **Output:** 500

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1: Using** **Depth First Search**

  

  

  1. Explore the current node and keep exploring its children.
  2. Use a map to store the visited node in pair with stops and distance as value.
  3. Break the recursion tree if the key is present in the map.
  4. Find the answer (minimum cost) for each recursion tree and return it.

Below is the implementation of our approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

using namespace std;

 

// Structure to implement hashing to

// stores pairs in map

struct pair_hash {

 template <class T1, class T2>

 std::size_t

 operator()(const std::pair<T1, T2>& pair) const

 {

 return std::hash<T1>()(pair.first)

 ^ std::hash<T2>()(pair.second);

 }

};

 

// DFS memoization

vector<vector<int> > adjMatrix;

typedef std::pair<int, int> pair1;

unordered_map<pair1, int, pair_hash> mp;

 

// Function to implement DFS Traversal

long DFSUtility(int node, int stops,

 int dst, int cities)

{

 // Base Case

 if (node == dst)

 return 0;

 

 if (stops < 0) {

 return INT_MAX;

 }

 

 pair<int, int> key(node, stops);

 

 // Find value with key in a map

 if (mp.find(key) != mp.end()) {

 return mp[key];

 }

 

 long ans = INT_MAX;

 

 // Traverse adjacency matrix of

 // source node

 for (int neighbour = 0;

 neighbour < cities;

 ++neighbour) {

 

 long weight

 = adjMatrix[node][neighbour];

 

 if (weight > 0) {

 

 // Recursive DFS call for

 // child node

 long minVal

 = DFSUtility(neighbour,

 stops - 1,

 dst, cities);

 

 if (minVal + weight > 0)

 ans = min(ans,

 minVal

 + weight);

 }

 }

 

 mp[key] = ans;

 

 // Return ans

 return ans;

}

 

// Function to find the cheapest price

// from given source to destination

int findCheapestPrice(int cities,

 vector<vector<int> >& flights,

 int src, int dst, int stops)

{

 

 // Resize Adjacency Marix

 adjMatrix.resize(cities + 1,

 vector<int>(cities + 1, 0));

 

 // Traverse flight[][]

 for (auto item : flights) {

 // Create Adjacency Matrix

 adjMatrix[item[0]][item[1]] = item[2];

 }

 

 // DFS Call to find shortest path

 long ans = DFSUtility(src, stops,

 dst, cities);

 

 // Return the cost

 return ans >= INT_MAX ? -1 : (int)ans;

 ;

}

 

// Driver Code

int main()

{

 // Input flight : {Source,

 // Destination, Cost}

 vector<vector<int> > flights

 = { { 4, 1, 1 }, { 1, 2, 3 }, { 0, 3, 2 }, { 0, 4, 10 }, { 3, 1, 1 }, { 1,
4, 3 } };

 

 // vec, n, stops, src, dst

 int stops = 2;

 int totalCities = 5;

 int sourceCity = 0;

 int destCity = 4;

 

 // Function Call

 long ans = findCheapestPrice(

 totalCities, flights,

 sourceCity, destCity,

 stops);

 

 cout << ans;

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

**Time Complexity:** O(V + E), where V is the number of nodes and E is the
edges.  
 **Auxiliary Space:** O(V)

 **Method 2: Using**Breadth-First **** Search

  1. The idea is to use Queue to perform BFS Traversal.
  2. Perform traversal from current node and insert root node in the queue.
  3. Traverse the queue and explore the current node and its siblings. Then insert the siblings of the node in the queue.
  4. While exploring each sibling and keep pushing the entries in the queue if the cost is less and update the minimum cost.
  5. Print the minimum cost after the above traversal.

Below is the implementation of our approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program of the above approach

#include <bits/stdc++.h>

#include <iostream>

#include <queue>

#include <tuple>

#include <unordered_map>

 

using namespace std;

// BSF Memoization

typedef tuple<int, int, int> tupl;

 

// Function to implement BFS

int findCheapestPrice(int cities,

 vector<vector<int> >& flights,

 int src, int dst, int stops)

{

 unordered_map<int,

 vector<pair<int, int> > >

 adjList;

 

 // Traverse flight[][]

 for (auto flight : flights) {

 

 // Create Adjacency Matrix

 adjList[flight[0]].push_back(

 { flight[1], flight[2] });

 }

 

 // < city, distancefromsource > pair

 queue<pair<int, int> >

 q;

 q.push({ src, 0 });

 

 // Store the Result

 int srcDist = INT_MAX;

 

 // Traversing the Matrix

 while (!q.empty() && stops-- >= 0) {

 

 int qSize = q.size();

 

 for (int i = 0; i < qSize; i++) {

 pair<int, int> curr = q.front();

 q.pop();

 

 for (auto next : adjList[curr.first]) {

 

 // If source distance is already

 // least the skip this iteration

 if (srcDist < curr.second

 + next.second)

 continue;

 

 q.push({ next.first,

 curr.second

 + next.second });

 

 if (dst == next.first) {

 srcDist = min(

 srcDist, curr.second

 + next.second);

 }

 }

 }

 }

 

 // Returning the Answer

 return srcDist == INT_MAX ? -1 : srcDist;

}

 

// Driver Code

int main()

{

 // Input flight : {Source,

 // Destination, Cost}

 vector<vector<int> > flights

 = { { 4, 1, 1 }, { 1, 2, 3 }, { 0, 3, 2 }, { 0, 4, 10 }, { 3, 1, 1 }, { 1,
4, 3 } };

 

 // vec, n, stops, src, dst

 int stops = 2;

 int totalCities = 5;

 

 // Given source and destination

 int sourceCity = 0;

 int destCity = 4;

 

 // Function Call

 long ans = findCheapestPrice(

 totalCities, flights,

 sourceCity, destCity,

 stops);

 cout << ans;

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

**Time Complexity:** O(Stops* N * N) where N is the Product of Cities and Size
in Queue  
 **Auxiliary Space:** O(N)

 **Method 3: Using**Dijkstra Algorithm

  

  

  1. Update the distance of all the vertices from the source.
  2. The vertices that are not directly connected from the source are marked with infinity and vertices that are directly connected are updated with the correct distance.
  3. Start from the source, and extract next min vertices. This will ensure the minimum cost.
  4. Do Edge Relaxation at each step: _**D denotes Distance** and **w denotes weights**_
    1. If D[u] + w(u, z) < D[z] then
    2. D[z] = D[u] + w(u, z)

Here is the implementation of our approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

#include <tuple>

using namespace std;

 

typedef tuple<int, int, int> tupl;

long findCheapestPrice(int cities,

 vector<vector<int> >& flights,

 int src, int dst, int stops)

{

 // Adjacency Matrix

 vector<vector<pair<int, int> > > adjList(cities);

 

 // Traverse flight[][]

 for (auto flight : flights) {

 // Create Adjacency Matrix

 adjList[flight[0]].push_back(

 { flight[1], flight[2] });

 }

 

 // Implementing Priority Queue

 priority_queue<tupl, vector<tupl>,

 greater<tupl> >

 pq;

 

 tupl t = make_tuple(0, src, stops);

 pq.push(t);

 

 // While PQ is not empty

 while (!pq.empty()) {

 tupl t = pq.top();

 pq.pop();

 

 if (src == dst)

 return 0;

 

 int cost = get<0>(t);

 int current = get<1>(t);

 int stop = get<2>(t);

 

 if (current == dst)

 

 // Return the Answer

 return cost;

 

 if (stop >= 0) {

 for (auto next : adjList[current]) {

 

 tupl t = make_tuple((cost

 + next.second),

 next.first,

 stop - 1);

 pq.push(t);

 }

 }

 }

 return -1;

}

 

int main()

{

 // Input flight : {Source,

 // Destination, Cost}

 vector<vector<int> > flights

 = { { 4, 1, 1 }, { 1, 2, 3 }, { 0, 3, 2 }, { 0, 4, 10 }, { 3, 1, 1 }, { 1,
4, 3 } };

 

 // vec, n, stops, src, dst

 int stops = 2;

 int totalCities = 5;

 

 // Given source and destination

 int sourceCity = 0;

 int destCity = 4;

 

 // Function Call

 long ans = findCheapestPrice(

 totalCities, flights,

 sourceCity, destCity, stops);

 cout << ans;

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

**Time Complexity:** O(E+V log V) where V is the number of nodes and E is the
edges.  
 **Auxiliary Space:** O(V)

 **Method 4: Using**Bellmon Ford ****

  1. Initialize distances from the source to all vertices as infinite and distance to the source itself as 0.
  2. Do Edge Relaxation at each step: D denotes Distance and w denotes weights
    * If D[u] + w(u, z) < D[z] then D[z] = D[u] + w(u, z)
  3. The algorithm has been modified to solve the given problem instead of relaxing the graph V-1 times, we will do it for the given number of stops.

