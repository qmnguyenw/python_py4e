Choose atleast two elements from array such that their GCD is 1 and cost is
minimum



Given two integer arrays **arr[]** and **cost[]** where **cost[i]** is the
cost of choosing **arr[i]**. The task is to choose a subset with at least two
elements such that the GCD of all the elements from the subset is 1 and the
cost of choosing those elements is as minimum as possible then print the
minimum cost.  
 **Examples:**  

> **Input:** arr[] = {5, 10, 12, 1}, cost[] = {2, 1, 2, 6}  
> **Output:** 4  
> {5, 12} is the required subset with cost = 2 + 2 = 4  
>  **Input:** arr[] = {50, 100, 150, 200, 300}, cost[] = {2, 3, 4, 5, 6}  
> **Output:** -1  
> No subset possible with gcd = 1  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** Add GCD of any two elements to a map, now for every element
**arr[i]** calculate its gcd with all the gcd values found so far (saved in
the map) and update **map[gcd] = min(map[gcd], map[gcd] + cost[i])**. If in
the end, map doesn’t contain any entry for **gcd = 1** then print **-1** else
print the stored minimum cost.  
Below is the implementation of the above approach:  

## C++

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

// Function to return the minimum cost required

int getMinCost(int arr[], int n, int cost[])

{

 // Map to store <gcd, cost> pair where

 // cost is the cost to get the current gcd

 map<int, int> mp;

 mp.clear();

 mp[0] = 0;

 for (int i = 0; i < n; i++) {

 for (auto it : mp) {

 int gcd = __gcd(arr[i], it.first);

 // If current gcd value already exists in map

 if (mp.count(gcd) == 1)

 // Update the minimum cost

 // to get the current gcd

 mp[gcd] = min(mp[gcd], it.second + cost[i]);

 else

 mp[gcd] = it.second + cost[i];

 }

 }

 // If there can be no sub-set such that

 // the gcd of all the elements is 1

 if (mp[1] == 0)

 return -1;

 else

 return mp[1];

}

// Driver code

int main()

{

 int arr[] = { 5, 10, 12, 1 };

 int cost[] = { 2, 1, 2, 6 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << getMinCost(arr, n, cost);

 return 0;

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

// Java implementation of the approach

import java.util.*;

import java.util.concurrent.ConcurrentHashMap;

class GFG{

 

// Function to return the minimum cost required

static int getMinCost(int arr[], int n, int cost[])

{

 

 // Map to store <gcd, cost> pair where

 // cost is the cost to get the current gcd

 Map<Integer,Integer> mp = new ConcurrentHashMap<Integer,Integer>();

 mp.clear();

 mp.put(0, 0);

 

 for (int i = 0; i < n; i++) {

 for (Map.Entry<Integer,Integer> it : mp.entrySet()){

 int gcd = __gcd(arr[i], it.getKey());

 

 // If current gcd value already exists in map

 if (mp.containsKey(gcd))

 

 // Update the minimum cost

 // to get the current gcd

 mp.put(gcd, Math.min(mp.get(gcd), it.getValue() + cost[i]));

 

 else

 mp.put(gcd,it.getValue() + cost[i]);

 }

 }

 

 // If there can be no sub-set such that

 // the gcd of all the elements is 1

 if (!mp.containsKey(1))

 return -1;

 else

 return mp.get(1);

}

static int __gcd(int a, int b) 

{ 

 return b == 0? a:__gcd(b, a % b); 

}

// Driver code

public static void main(String[] args)

{

 int arr[] = { 5, 10, 12, 1 };

 int cost[] = { 2, 1, 2, 6 };

 int n = arr.length;

 

 System.out.print(getMinCost(arr, n, cost));

}

}

// This code is contributed by PrinciRaj1992  
  
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

# Python3 implementation of the approach

from math import gcd as __gcd

# Function to return the minimum cost required

def getMinCost(arr, n, cost):

 # Map to store <gcd, cost> pair where

 # cost is the cost to get the current gcd

 mp = dict()

 mp[0] = 0

 for i in range(n):

 for it in list(mp):

 gcd = __gcd(arr[i], it)

 # If current gcd value

 # already exists in map

 if (gcd in mp):

 # Update the minimum cost

 # to get the current gcd

 mp[gcd] = min(mp[gcd],

 mp[it] + cost[i])

 else:

 mp[gcd] = mp[it] + cost[i]

 # If there can be no sub-set such that

 # the gcd of all the elements is 1

 if (mp[1] == 0):

 return -1

 else:

 return mp[1]

# Driver code

arr = [ 5, 10, 12, 1]

cost = [ 2, 1, 2, 6]

n = len(arr)

print(getMinCost(arr, n, cost))

# This code is contributed by Mohit Kumar  
  
---  
  
 __

 __

## C#

 __

 __  
 __

 __

 __  
 __  
 __

// C# implementation of the approach

using System;

using System.Collections.Generic;

using System.Linq;

class GFG

{

 static int __gcd(int a, int b) 

 { 

 return b == 0? a:__gcd(b, a % b); 

 }

 // Function to return the minimum cost required

 static int getMinCost(int[] arr, int n, int[] cost)

 {

 // Map to store <gcd, cost> pair where

 // cost is the cost to get the current gcd

 Dictionary<int, int> mp = new Dictionary<int, int>();

 mp.Add(0, 0);

 for (int i = 0; i < n; i++)

 {

 foreach (int it in mp.Keys.ToList())

 {

 int gcd = __gcd(arr[i], it);

 // If current gcd value already exists in map

 if(mp.ContainsKey(gcd))

 {

 // Update the minimum cost

 // to get the current gcd

 mp[gcd] = Math.Min(mp[gcd], mp[it] + cost[i]);

 }

 else

 {

 mp.Add(gcd, mp[it] + cost[i]);

 }

 } 

 }

 // If there can be no sub-set such that

 // the gcd of all the elements is 1

 if (mp[1] == 0)

 {

 return -1;

 }

 else

 {

 return mp[1];

 } 

 }

 // Driver code

 static public void Main ()

 {

 int[] arr = { 5, 10, 12, 1 };

 int[] cost = { 2, 1, 2, 6 };

 int n = arr.Length;

 Console.WriteLine(getMinCost(arr, n, cost));

 }

}

// This code is contributed by avanitrachhadiya2155  
  
---  
  
 __

 __

 **Output:**

    
    
    4

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

