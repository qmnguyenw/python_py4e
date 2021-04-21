Minimum number of stacks possible using boxes of given capacities



Given **N** boxes with their capacities which denotes the total number of
boxes that it can hold above it. You can stack up the boxes one over the other
as long as the total number of boxes above each box is less than or equal to
its capacity. Find the minimum number of stacks that can be made by using all
the boxes.  
 **Examples:**  

> **Input:** arr[] = {0, 0, 1, 1, 2}  
> **Output:** 2  
> First stack (top to bottom): 0 1 2  
> Second stack (top to bottom): 0 1  
>  **Input:** arr[] = {1, 1, 4, 4}  
> **Output:** 1  
> All the boxes can be put on a single stack.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Let’s have a map in which map[X] denotes the number of boxes
with capacity X available with us. Let’s build stacks one by one. Initially
the size of the stack would be 0, and then we iterate through the map greedily
choosing as many boxes of current capacity as we can.  
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

// Function to return the count

// of minimum stacks

int countPiles(int n, int a[])

{

 // Keep track of occurrence

 // of each capacity

 map<int, int> occ;

 // Fill the occurrence map

 for (int i = 0; i < n; i++)

 occ[a[i]]++;

 // Number of piles is 0 initially

 int pile = 0;

 // Traverse occurrences in increasing

 // order of capacities.

 while (occ.size()) {

 // Adding a new pile

 pile++;

 int size = 0;

 unordered_set<int> toRemove;

 // Traverse all piles in increasing

 // order of capacities

 for (auto tm : occ) {

 int mx = tm.first;

 int ct = tm.second;

 // Number of boxes of capacity mx

 // that can be added to current pile

 int use = min(ct, mx - size + 1);

 // Update the occurrence

 occ[mx] -= use;

 // Update the size of the pile

 size += use;

 if (occ[mx] == 0)

 toRemove.insert(mx);

 }

 // Remove capacities that are

 // no longer available

 for (auto tm : toRemove)

 occ.erase(tm);

 }

 return pile;

}

// Driver code

int main()

{

 int a[] = { 0, 0, 1, 1, 2 };

 int n = sizeof(a) / sizeof(a[0]);

 cout << countPiles(n, a);

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

import java.util.HashMap;

import java.util.HashSet;

class GFG

{

 // Function to return the count

 // of minimum stacks

 static int countPiles(int n, int[] a)

 {

 // Keep track of occurrence

 // of each capacity

 HashMap<Integer,

 Integer> occ = new HashMap<>();

 // Fill the occurrence map

 for (int i = 0; i < n; i++)

 occ.put(a[i], occ.get(a[i]) == null ? 1 :

 occ.get(a[i]) + 1);

 // Number of piles is 0 initially

 int pile = 0;

 // Traverse occurrences in increasing

 // order of capacities.

 while (!occ.isEmpty())

 {

 // Adding a new pile

 pile++;

 int size = 0;

 HashSet<Integer> toRemove = new HashSet<>();

 // Traverse all piles in increasing

 // order of capacities

 for (HashMap.Entry<Integer,

 Integer> tm : occ.entrySet())

 {

 int mx = tm.getKey();

 int ct = tm.getValue();

 // Number of boxes of capacity mx

 // that can be added to current pile

 int use = Math.min(ct, mx - size + 1);

 // Update the occurrence

 occ.put(mx, occ.get(mx) - use);

 // Update the size of the pile

 size += use;

 if (occ.get(mx) == 0)

 toRemove.add(mx);

 }

 // Remove capacities that are

 // no longer available

 for (int tm : toRemove)

 occ.remove(tm);

 }

 return pile;

 }

 // Driver Code

 public static void main(String[] args)

 {

 int[] a = { 0, 0, 1, 1, 2 };

 int n = a.length;

 System.out.println(countPiles(n, a));

 }

}

// This code is contributed by

// sanjeev2552  
  
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

# Function to return the count

# of minimum stacks

def countPiles(n, a):

 

 # Keep track of occurrence

 # of each capacity

 occ = dict()

 # Fill the occurrence map

 for i in a:

 if i in occ.keys():

 occ[i] += 1

 else:

 occ[i] = 1

 # Number of piles is 0 initially

 pile = 0

 # Traverse occurrences in increasing

 # order of capacities.

 while (len(occ) > 0):

 # Adding a new pile

 pile += 1

 size = 0

 toRemove = dict()

 # Traverse all piles in increasing

 # order of capacities

 for tm in occ:

 mx = tm

 ct = occ[tm]

 # Number of boxes of capacity mx

 # that can be added to current pile

 use = min(ct, mx - size + 1)

 # Update the occurrence

 occ[mx] -= use

 # Update the size of the pile

 size += use

 if (occ[mx] == 0):

 toRemove[mx] = 1

 

 # Remove capacities that are

 # no longer available

 for tm in toRemove:

 del occ[tm]

 

 return pile

# Driver code

a = [0, 0, 1, 1, 2]

n = len(a)

print(countPiles(n, a))

# This code is contributed

# by Mohit Kumar  
  
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

using System.Collections;

using System.Collections.Generic;

using System.Linq;

class GFG

{

 // Function to return the count

 // of minimum stacks

 static int countPiles(int n, int[] a)

 {

 // Keep track of occurrence

 // of each capacity

 Dictionary<int,

 int> occ = new Dictionary<int,int>();

 // Fill the occurrence map

 for (int i = 0; i < n; i++)

 {

 if(!occ.ContainsKey(a[i]))

 {

 occ[a[i]]=0;

 }

 occ[a[i]]++;

 }

 // Number of piles is 0 initially

 int pile = 0;

 // Traverse occurrences in increasing

 // order of capacities.

 while(occ.Count!=0)

 {

 // Adding a new pile

 pile++;

 int size = 0;

 HashSet<int> toRemove = new HashSet<int>();

 Dictionary<int,int> tmp = occ;

 // Traverse all piles in increasing

 // order of capacities

 foreach(var tm in occ.Keys.ToList())

 {

 int mx = tm;

 int ct = occ[tm];

 // Number of boxes of capacity mx

 // that can be added to current pile

 int use = Math.Min(ct, mx - size + 1);

 // Update the occurrence

 occ[mx]-= use;

 // Update the size of the pile

 size += use;

 if (occ[mx] == 0)

 toRemove.Add(mx);

 }

 occ = tmp;

 

 // Remove capacities that are

 // no longer available

 foreach(int tm in toRemove.ToList())

 occ.Remove(tm);

 }

 return pile;

 }

 // Driver Code

 public static void Main(string[] args)

 {

 int[] a = { 0, 0, 1, 1, 2 };

 int n = a.Length;

 Console.WriteLine(countPiles(n, a));

 }

}

//// This code is contributed by rutvik_56.  
  
---  
  
 __

 __

 **Output:**

    
    
    2

**Time Complexity:** O(NlogN)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

