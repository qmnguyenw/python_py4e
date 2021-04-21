Most frequent element in Array after replacing given index by K for Q queries



Given an array **arr[]** of size **N** , and **Q** queries of the form **{i,
k}** for which, the task is to print the **most frequent element** in the
array after **replacing arr[i] by k**.  
 **Example :**  

> **Input:** arr[] = {2, 2, 2, 3, 3}, Querry = {{0, 3}, {4, 2}, {0, 4}}  
> **Output:** 3 2 2  
> First query: Setting arr[0] = 3 modifies arr[] = {3, 2, 2, 3, 3}. So, 3 has
> max frequency.  
> Second query: Setting arr[4] = 2, modifies arr[] = {3, 2, 2, 3, 2}. So, 2
> has max frequency.  
> Third query: Setting arr[0] = 4, modifies arr[] = {4, 2, 2, 3, 2}. So, 2 has
> max frequency  
>  **Input:** arr[] = {1, 2, 3, 4, 3, 3} Querry = {{0, 2}, {3, 2}, {2, 4}}  
> **Output:** 3 2 2  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  
For every query, replace arr[i] by K, and traverse over the whole array and
count the frequency of every array element and print the most frequent of
them.  
_**Time Complexity:** O(N * Q)_  
_**Auxiliary Space:** O(N)_  
 **Efficient Approach:**  
The above approach can be optimized by precomputing the frequencies of every
array element and maintain frequency-array element pairings in a set to obtain
the most frequent element in O(1). Follow the steps below to solve the
problem:  

  1. Initialize a map to store frequencies of all array elements, and a set of pairs to store frequency-element pairings. In the set, store the frequencies as negative. This ensures that the first pair stored at the beginning of the set, i.e. s.begin(), is the **{-(maximum frequency), most frequent element}** pairing.
  2. For every query, while removing the array element at ith index, do the following tasks: 
    * Find the frequency of arr[i] from the map, that is **mp[arr[i]].**
    * Remove the pair **{-mp[arr[i]], arr[i]}** from the set.
    * Update the set after decreasing the frequency of **arr[i]** by inserting **{-(mp[arr[i] – 1), arr[i]}** into the set.
    * Decrease the frequency of **arr[i]** in the map.
    * To insert **K** into the array for every query, do the following: 
      * Find the frequency of **K** from the map, that is **mp[K]**.
      * Remove the pair **{-mp[K], K}** from the set.
      * Update the set after increasing the frequency of **K** by inserting **{-(mp[K] + 1), K}** into the set.
      * Increase the frequency of **K** in the map.
    * Finally for each query, extract the pair at the beginning of the set. The **first element** in the set denotes **-(maximum frequency)**. Hence, the second element will be the most frequent element. Print the second element of the pair.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the most

// frequent element after every

// update query on the array

#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

// Function to print the most

// frequent element of array

// along with update querry

void mostFrequent(ll arr[], ll n, ll m,

 vector<vector<ll> > q)

{

 ll i;

 // Stores element->fequencies

 // mappings

 map<ll, ll> mp;

 for (i = 0; i < n; i++)

 mp[arr[i]] += 1;

 // Stores frequencies->element

 // mappings

 set<pair<ll, ll> > s;

 // Store the frequencies in

 // negative

 for (auto it : mp) {

 s.insert(make_pair(-(it.second),

 it.first));

 }

 for (i = 0; i < m; i++) {

 // Index to be modified

 ll j = q[i][0];

 // Value to be inserted

 ll k = q[i][1];

 // Store the frequency of

 // arr[j] and k

 auto it = mp.find(arr[j]);

 auto it2 = mp.find(k);

 // Remove mapping of arr[j]

 // with previous frequency

 s.erase(make_pair(-(it->second),

 it->first));

 // Update mapping with new

 // frequency

 s.insert(make_pair(-((it->second)

 - 1),

 it->first));

 // Update frequency of arr[j]

 // in the map

 mp[arr[j]]--;

 // Remove mapping of k

 // with previous frequency

 s.erase(make_pair(-(it2->second),

 it2->first));

 // Update mapping of k

 // with previous frequency

 s.insert(make_pair(-((it2->second)

 + 1),

 it2->first));

 // Update frequency of k

 mp[k]++;

 // Replace arr[j] by k

 arr[j] = k;

 // Display maximum frequent element

 cout << (*s.begin()).second << " ";

 }

}

// Driver Code

int main()

{

 ll i, N, Q;

 N = 5;

 Q = 3;

 ll arr[] = { 2, 2, 2, 3, 3 };

 vector<vector<ll> > querry = {

 { 0, 3 },

 { 4, 2 },

 { 0, 4 }

 };

 mostFrequent(arr, N, Q, querry);

}  
  
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

// Java program to find the most

// frequent element after every

// update query on the array

import java.util.*;

import java.io.*;

class GFG{

 

// Pair class represents

// a pair of elements

static class Pair

{

 int first, second;

 Pair(int f,int s)

 {

 first = f;

 second = s;

 }

}

// Function to print the most

// frequent element of array

// along with update querry

static void mostFrequent(int arr[], int n, int m,

 ArrayList<Pair> q)

{

 int i;

 // Stores element->fequencies

 // mappings

 HashMap<Integer, Integer> map = new HashMap<>();

 HashMap<Integer, Pair> map1 = new HashMap<>();

 

 for(i = 0; i < n; i++)

 {

 if(!map.containsKey(arr[i]))

 map.put(arr[i], 1);

 else

 map.put(arr[i], map.get(arr[i]) + 1);

 }

 // Stores frequencies->element

 // mappings

 TreeSet<Pair> set = new TreeSet<>(

 new Comparator<Pair>()

 {

 public int compare(Pair p1, Pair p2)

 {

 return p2.first - p1.first;

 }

 });

 // Store the frequencies in

 // bigger to smaller

 for(Map.Entry<Integer,

 Integer> entry : map.entrySet())

 {

 Pair p = new Pair(entry.getValue(),

 entry.getKey());

 set.add(p);

 map1.put(entry.getKey(), p);

 }

 for(i = 0; i < m; i++)

 {

 

 // Index to be modified

 int j = q.get(i).first;

 // Value to be inserted

 int k = q.get(i).second;

 

 // Insert the new Pair

 // with value k if it was

 // not inserted

 if(map1.get(k) == null)

 {

 Pair p = new Pair(0, k);

 map1.put(k, p);

 set.add(p);

 }

 

 // Get the Pairs of

 // arr[j] and k

 Pair p1 = map1.get(arr[j]);

 set.remove(p1);

 Pair p2 = map1.get(k);

 set.remove(p2);

 

 // Decrease the frequency of

 // mapping with value arr[j]

 p1.first--;

 set.add(p1);

 // Update frequency of arr[j]

 // in the map

 map.put(arr[j], map.get(arr[j]) - 1);

 // Increase the frequency of

 // mapping with value k

 p2.first++;

 set.add(p2);

 

 // Update frequency of k

 if(map.containsKey(k))

 map.put(k, map.get(k) + 1);

 else

 map.put(k, 1);

 // Replace arr[j] by k

 arr[j] = k;

 // Display maximum frequent element

 System.out.print(

 set.iterator().next().second + " ");

 }

}

// Driver Code

public static void main(String []args)

{

 int i, N, Q;

 N = 5;

 Q = 3;

 int arr[] = { 2, 2, 2, 3, 3 };

 

 ArrayList<Pair> query = new ArrayList<>();

 query.add(new Pair(0, 3));

 query.add(new Pair(4, 2));

 query.add(new Pair(0, 4));

 

 mostFrequent(arr, N, Q, query);

}

}

// This code is contributed by Ganeshchowdharysadanala  
  
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

# Python program to find the most

# frequent element after every

# update query on the array

from typing import List

from collections import defaultdict

# Function to print the most

# frequent element of array

# along with update querry

def mostFrequent(arr: List[int], n: int, m: int, q:
List[List[int]]) -> None:

 i = 0

 # Stores element->fequencies

 # mappings

 mp = defaultdict(lambda: 0)

 for i in range(n):

 mp[arr[i]] += 1

 # Stores frequencies->element

 # mappings

 s = set()

 # Store the frequencies in

 # negative

 for k, v in mp.items():

 s.add((-v, k))

 for i in range(m):

 # Index to be modified

 j = q[i][0]

 # Value to be inserted

 k = q[i][1]

 # Store the frequency of

 # arr[j] and k

 it = mp[arr[j]]

 it2 = mp[k]

 # Remove mapping of arr[j]

 # with previous frequency

 if (-it, arr[j]) in s:

 s.remove((-it, arr[j]))

 # Update mapping with new

 # frequency

 s.add((-(it - 1), arr[j]))

 # Update frequency of arr[j]

 # in the map

 mp[arr[j]] -= 1

 # Remove mapping of k

 # with previous frequency

 if (-it2, k) in s:

 s.remove((-it2, k))

 # Update mapping of k

 # with previous frequency

 s.add((-(it2 + 1), k))

 # Update frequency of k

 mp[k] += 1

 # Replace arr[j] by k

 arr[j] = k

 # Display maximum frequent element

 print(sorted(s)[0][1])

# Driver Code

if __name__ == "__main__":

 N = 5

 Q = 3

 arr = [2, 2, 2, 3, 3]

 querry = [[0, 3], [4, 2], [0, 4]]

 mostFrequent(arr, N, Q, querry)

# This code is contributed by sanjeev2552  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    3 2 2 

_**Time Complexity:** O(N + (Q * LogN))_  
_**Auxiliary Space:** O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

