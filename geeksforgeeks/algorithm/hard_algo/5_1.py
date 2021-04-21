Check if one string can be converted to another



Given two strings **str** and **str1** , the task is to check whether one
string can be converted to other by using the following operation:

  * Convert all the presence of a character by a different character.

For example, if str = “abacd” and operation is to change character ‘a’ to ‘k’,
then the resultant str = “kbkcd”

 **Examples:**

>  **Input:** str = “abbcaa”; str1 = “bccdbb”  
>  **Output:** Yes  
>  **Explanation:** The mappings of the characters are:  
> c –> d  
> b –> c  
> a –> b
>
>  **Input:** str = “abbc”; str1 = “bcca”  
>  **Output:** No  
>  **Explanation:** The mapping of characters are:  
> a –> b  
> b –> c  
> c –> a  
> Here, due to the presence of a cycle, a specific order cannot be found.
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * According to the given operation, every unique character should map to a unique character may be same or different.
  * This can easily be checked by a Hashmap.
  * However, this fails in cases where there is a cycle in mapping and a specific order cannot be determined.
  * One example of such case is _Example 2_ above.
  * Therefore, for mapping, the first and final characters are stored as edges in a hashmap.
  * For finding cycle with the edges, these edges are mapped one by one to a parent and are checked for cycle using Union and Find Algorithm.

Below is the implementation of the above approach.  

## CPP

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach.

#include <bits/stdc++.h>

using namespace std;

int parent[26];

// Function for find

// from Disjoint set algorithm

int find(int x)

{

 if (x != parent[x])

 return parent[x] = find(parent[x]);

 return x;

}

 

// Function for the union

// from Disjoint set algorithm

void join(int x, int y)

{

 int px = find(x);

 int pz = find(y);

 if (px != pz) {

 parent[pz] = px;

 }

}

// Function to check if one string

// can be converted to another.

bool convertible(string s1, string s2)

{

 // All the characters are checked whether

 // it's either not replaced or replaced

 // by a similar character using a map.

 map<int, int> mp;

 

 for (int i = 0; i < s1.size(); i++) {

 if (mp.find(s1[i] - 'a') == mp.end()) {

 mp[s1[i] - 'a'] = s2[i] - 'a';

 }

 else {

 if (mp[s1[i] - 'a'] != s2[i] - 'a')

 return false;

 }

 }

 // To check if there are cycles.

 // If yes, then they are not convertible.

 // Else, they are convertible.

 for (auto it : mp) {

 if (it.first == it.second)

 continue;

 else {

 if (find(it.first) == find(it.second))

 return false;

 else

 join(it.first, it.second);

 }

 }

 return true;

}

 

// Function to initialize parent array

// for union and find algorithm.

void initialize()

{

 for (int i = 0; i < 26; i++) {

 parent[i] = i;

 }

}

// Driver code

int main()

{

 // Your C++ Code

 string s1, s2;

 s1 = "abbcaa";

 s2 = "bccdbb";

 initialize();

 if (convertible(s1, s2))

 cout << "Yes" << endl;

 else

 cout << "No" << endl;

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

// Java implementation of the above approach.

import java.util.*;

 

class GFG

{

 

static int []parent = new int[26];

 

// Function for find

// from Disjoint set algorithm

static int find(int x)

{

 if (x != parent[x])

 return parent[x] = find(parent[x]);

 return x;

}

 

// Function for the union

// from Disjoint set algorithm

static void join(int x, int y)

{

 int px = find(x);

 int pz = find(y);

 if (px != pz)

 {

 parent[pz] = px;

 }

}

// Function to check if one String

// can be converted to another.

static boolean convertible(String s1, String s2)

{

 // All the characters are checked whether

 // it's either not replaced or replaced

 // by a similar character using a map.

 HashMap<Integer,Integer> mp = new HashMap<Integer,Integer>();

 

 for (int i = 0; i < s1.length(); i++) 

 {

 if (!mp.containsKey(s1.charAt(i) - 'a'))

 {

 mp.put(s1.charAt(i) - 'a', s2.charAt(i) - 'a');

 }

 else

 {

 if (mp.get(s1.charAt(i) - 'a') != s2.charAt(i) - 'a')

 return false;

 }

 }

 

 // To check if there are cycles.

 // If yes, then they are not convertible.

 // Else, they are convertible.

 for (Map.Entry<Integer, Integer> it : mp.entrySet())

 {

 if (it.getKey() == it.getValue())

 continue;

 else

 {

 if (find(it.getKey()) == find(it.getValue()))

 return false;

 else

 join(it.getKey(), it.getValue());

 }

 }

 return true;

}

 

// Function to initialize parent array

// for union and find algorithm.

static void initialize()

{

 for (int i = 0; i < 26; i++) 

 {

 parent[i] = i;

 }

}

 

// Driver code

public static void main(String[] args)

{

 

 String s1, s2;

 s1 = "abbcaa";

 s2 = "bccdbb";

 initialize();

 if (convertible(s1, s2))

 System.out.print("Yes" + "\n");

 else

 System.out.print("No" + "\n");

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 implementation of the above approach.

parent = [0] * 256

 

# Function for find

# from Disjoset algorithm

def find(x):

 if (x != parent[x]):

 parent[x] = find(parent[x])

 return parent[x]

 return x

 

# Function for the union

# from Disjoset algorithm

def join(x, y):

 px = find(x)

 pz = find(y)

 if (px != pz):

 parent[pz] = px

 

# Function to check if one string

# can be converted to another.

def convertible(s1, s2):

 

 # All the characters are checked whether

 # it's either not replaced or replaced

 # by a similar character using a map.

 mp = dict()

 

 for i in range(len(s1)):

 if (s1[i] in mp):

 mp[s1[i]] = s2[i]

 else:

 if s1[i] in mp and mp[s1[i]] != s2[i]:

 return False

 

 # To check if there are cycles.

 # If yes, then they are not convertible.

 # Else, they are convertible.

 for it in mp:

 if (it == mp[it]):

 continue

 else :

 if (find(ord(it)) == find(ord(it))):

 return False

 else:

 join(ord(it), ord(it))

 

 return True

 

# Function to initialize parent array

# for union and find algorithm.

def initialize():

 for i in range(256):

 parent[i] = i

 

# Driver code

s1 = "abbcaa"

s2 = "bccdbb"

initialize()

if (convertible(s1, s2)):

 print("Yes")

else:

 print("No")

 

# This code is contributed by mohit kumar 29  
  
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

// C# implementation of the above approach.

using System;

using System.Collections.Generic;

 

class GFG

{

 

static int []parent = new int[26];

 

// Function for find

// from Disjoint set algorithm

static int find(int x)

{

 if (x != parent[x])

 return parent[x] = find(parent[x]);

 return x;

}

 

// Function for the union

// from Disjoint set algorithm

static void join(int x, int y)

{

 int px = find(x);

 int pz = find(y);

 if (px != pz)

 {

 parent[pz] = px;

 }

}

 

// Function to check if one String

// can be converted to another.

static bool convertible(String s1, String s2)

{

 // All the characters are checked whether

 // it's either not replaced or replaced

 // by a similar character using a map.

 Dictionary<int,int> mp = new Dictionary<int,int>();

 

 for (int i = 0; i < s1.Length; i++) 

 {

 if (!mp.ContainsKey(s1[i] - 'a'))

 {

 mp.Add(s1[i] - 'a', s2[i] - 'a');

 }

 else

 {

 if (mp[s1[i] - 'a'] != s2[i] - 'a')

 return false;

 }

 }

 

 // To check if there are cycles.

 // If yes, then they are not convertible.

 // Else, they are convertible.

 foreach(KeyValuePair<int, int> it in mp)

 {

 if (it.Key == it.Value)

 continue;

 else

 {

 if (find(it.Key) == find(it.Value))

 return false;

 else

 join(it.Key, it.Value);

 }

 }

 return true;

}

 

// Function to initialize parent array

// for union and find algorithm.

static void initialize()

{

 for (int i = 0; i < 26; i++) 

 {

 parent[i] = i;

 }

}

 

// Driver code

public static void Main(String[] args)

{

 

 String s1, s2;

 s1 = "abbcaa";

 s2 = "bccdbb";

 initialize();

 if (convertible(s1, s2))

 Console.Write("Yes" + "\n");

 else

 Console.Write("No" + "\n");

}

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

