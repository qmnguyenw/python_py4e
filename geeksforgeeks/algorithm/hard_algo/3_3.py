Minimum number of operations required to make two strings equal



Given Two Strings **s1** and **s2** containing only lowercase letters of same
length. The task is to make these strings equal by using the minimum number of
operations. In one operation you can equalize any letter to any other
alphabet.  
 **Examples:**

>  **Input:** S1 = “abb”, S2 = “dad”  
> **Output:** 2  
> a -> d  
> b -> a  
> **Explanation:**  
> Strings after the first operation –  
> S1 = “dbb”, S2 = “ddd”  
> Strings after the second operation –  
> S1 = “ddd”, S2 = “ddd”  
>  **Input:** S1 = “bab”, S2 = “aab”  
> **Output:** 1  
> b -> a  
> **Explanation:**  
> Strings after the first operation –  
> S1 = “aaa”, S2 = “aaa”

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to use the Disjoint set union data structure. Below
is the illustration of the steps:

  * Initialize the parent of each alphabet to itself.
  * Traverse the two strings simultaneously with the help of index and check if the corresponding characters have different parents then merge the string which has less rank in the strings.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// minimum number of operations to

// make two strings equal

#include <bits/stdc++.h>

#define MAX 500001

using namespace std;

int parent[MAX];

int Rank[MAX];

// Function to find out

// parent of an alphabet

int find(int x)

{

 return parent[x] =

 parent[x] == x ? x :

 find(parent[x]);

}

// Function to merge two

// different alphabets

void merge(int r1, int r2)

{

 // Merge a and b using

 // rank compression

 if (r1 != r2) {

 if (Rank[r1] > Rank[r2]) {

 parent[r2] = r1;

 Rank[r1] += Rank[r2];

 }

 else {

 parent[r1] = r2;

 Rank[r2] += Rank[r1];

 }

 }

}

// Function to find the minimum

// number of operations required

void minimumOperations(string s1,

 string s2){

 

 // Initializing parent to i

 // and rank(size) to 1

 for (int i = 1; i <= 26; i++) {

 parent[i] = i;

 Rank[i] = 1;

 }

 

 // We will store our

 // answerin this vector

 vector<pair<char, char> > ans;

 // Traversing strings

 for (int i = 0; i < s1.length(); i++) {

 if (s1[i] != s2[i]) {

 // If they have differnt parents

 if (find(s1[i] - 96) !=

 find(s2[i] - 96)) {

 

 // Find their respective

 // parents and merge them

 int x = find(s1[i] - 96);

 int y = find(s2[i] - 96);

 merge(x, y);

 // Store this in

 // our Answer vector

 ans.push_back({ s1[i], s2[i] });

 }

 }

 }

 // Number of operations

 cout << ans.size() << endl;

 for (int i = 0; i < ans.size(); i++)

 cout << ans[i].first << "->"

 <<ans[i].second << endl;

 

}

// Driver Code

int main()

{

 // Two strings

 // S1 and S2

 string s1, s2;

 s1 = "abb";

 s2 = "dad";

 

 // Function Call

 minimumOperations(s1, s2);

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

// Java implementation to find the

// minimum number of operations to

// make two Strings equal

import java.util.*;

class GFG{

 

static final int MAX = 500001;

static int []parent = new int[MAX];

static int []Rank = new int[MAX];

static class pair

{

 char first, second;

 

 public pair(char first, char second)

 {

 this.first = first;

 this.second = second;

 }

}

// Function to find out

// parent of an alphabet

static int find(int x)

{

 return parent[x] = parent[x] == x ? x :

 find(parent[x]);

}

// Function to merge two

// different alphabets

static void merge(int r1, int r2)

{

 

 // Merge a and b using

 // rank compression

 if (r1 != r2)

 {

 if (Rank[r1] > Rank[r2])

 {

 parent[r2] = r1;

 Rank[r1] += Rank[r2];

 }

 else

 {

 parent[r1] = r2;

 Rank[r2] += Rank[r1];

 }

 }

}

// Function to find the minimum

// number of operations required

static void minimumOperations(String s1,

 String s2)

{

 

 // Initializing parent to i

 // and rank(size) to 1

 for(int i = 1; i <= 26; i++)

 {

 parent[i] = i;

 Rank[i] = 1;

 }

 

 // We will store our

 // answer in this vector

 Vector<pair> ans = new Vector<pair>();

 // Traversing Strings

 for(int i = 0; i < s1.length(); i++)

 {

 if (s1.charAt(i) != s2.charAt(i))

 {

 

 // If they have differnt parents

 if (find(s1.charAt(i) - 96) !=

 find(s2.charAt(i) - 96))

 {

 

 // Find their respective

 // parents and merge them

 int x = find(s1.charAt(i) - 96);

 int y = find(s2.charAt(i) - 96);

 merge(x, y);

 // Store this in

 // our Answer vector

 ans.add(new pair(s1.charAt(i),

 s2.charAt(i)));

 }

 }

 }

 // Number of operations

 System.out.print(ans.size() + "\n");

 for(int i = 0; i < ans.size(); i++)

 System.out.print(ans.get(i).first + "->" +

 ans.get(i).second +"\n");

}

// Driver Code

public static void main(String[] args)

{

 

 // Two Strings

 // S1 and S2

 String s1, s2;

 s1 = "abb";

 s2 = "dad";

 

 // Function call

 minimumOperations(s1, s2);

}

}

// This code is contributed by Princi Singh  
  
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

# Python3 implementation to find the

# minimum number of operations to

# make two strings equal

MAX = 500001

parent = [0] * MAX

Rank = [0] * MAX

# Function to find out

# parent of an alphabet

def find(x):

 

 if parent[x] == x:

 return x

 else:

 return find(parent[x])

# Function to merge two

# different alphabets

def merge(r1, r2):

 # Merge a and b using

 # rank compression

 if(r1 != r2):

 if(Rank[r1] > Rank[r2]):

 parent[r2] = r1

 Rank[r1] += Rank[r2]

 else:

 parent[r1] = r2

 Rank[r2] += Rank[r1]

# Function to find the minimum

# number of operations required

def minimumOperations(s1, s2):

 # Initializing parent to i

 # and rank(size) to 1

 for i in range(1, 26 + 1):

 parent[i] = i

 Rank[i] = 1

 # We will store our

 # answerin this list

 ans = []

 # Traversing strings

 for i in range(len(s1)):

 if(s1[i] != s2[i]):

 # If they have differnt parents

 if(find(ord(s1[i]) - 96) !=

 find(ord(s2[i]) - 96)):

 # Find their respective

 # parents and merge them

 x = find(ord(s1[i]) - 96)

 y = find(ord(s2[i]) - 96)

 merge(x, y)

 # Store this in

 # our Answer list

 ans.append([s1[i], s2[i]])

 # Number of operations

 print(len(ans))

 for i in ans:

 print(i[0], "->", i[1])

 

# Driver code

if __name__ == '__main__':

 # Two strings

 # S1 and S2

 s1 = "abb"

 s2 = "dad"

 

 # Function Call

 minimumOperations(s1, s2)

# This code is contributed by Shivam Singh  
  
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

// C# implementation to find the

// minimum number of operations to

// make two Strings equal

using System;

using System.Collections.Generic;

class GFG{

 

static readonly int MAX = 500001;

static int []parent = new int[MAX];

static int []Rank = new int[MAX];

class pair

{

 public char first, second;

 public pair(char first, char second)

 {

 this.first = first;

 this.second = second;

 }

}

// Function to find out

// parent of an alphabet

static int find(int x)

{

 return parent[x] = parent[x] ==

 x ? x : find(parent[x]);

}

// Function to merge two

// different alphabets

static void merge(int r1, int r2)

{

 // Merge a and b using

 // rank compression

 if (r1 != r2)

 {

 if (Rank[r1] > Rank[r2])

 {

 parent[r2] = r1;

 Rank[r1] += Rank[r2];

 }

 else

 {

 parent[r1] = r2;

 Rank[r2] += Rank[r1];

 }

 }

}

// Function to find the minimum

// number of operations required

static void minimumOperations(String s1,

 String s2)

{

 // Initializing parent to i

 // and rank(size) to 1

 for(int i = 1; i <= 26; i++)

 {

 parent[i] = i;

 Rank[i] = 1;

 }

 // We will store our

 // answer in this vector

 List<pair> ans = new List<pair>();

 // Traversing Strings

 for(int i = 0; i < s1.Length; i++)

 {

 if (s1[i] != s2[i])

 {

 // If they have differnt parents

 if (find(s1[i] - 96) !=

 find(s2[i] - 96))

 {

 // Find their respective

 // parents and merge them

 int x = find(s1[i] - 96);

 int y = find(s2[i] - 96);

 merge(x, y);

 // Store this in

 // our Answer vector

 ans.Add(new pair(s1[i],

 s2[i]));

 }

 }

 }

 // Number of operations

 Console.Write(ans.Count + "\n");

 for(int i = 0; i < ans.Count; i++)

 Console.Write(ans[i].first + "->" +

 ans[i].second + "\n");

}

// Driver Code

public static void Main(String[] args)

{ 

 // Two Strings

 // S1 and S2

 String s1, s2;

 s1 = "abb";

 s2 = "dad";

 // Function call

 minimumOperations(s1, s2);

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    a->d
    b->a
    
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

