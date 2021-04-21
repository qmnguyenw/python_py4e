Find the cordinates of the fourth vertex of a rectangle with given 3 vertices



Given an **N * M** grid. It contains exactly three **‘*’** and every other
cell is a **‘.’** where ‘*’ denotes a vertex of a rectangle. The task is to
find the coordinates of the fourth (missing) vertex (1-based indexing).

 **Examples:**

>  **Input:** grid[][] = {“*.*”, “*..”, “…”}  
>  **Output:** 2 3  
> (1, 1), (1, 3) and (2, 1) are the given coordinates of the rectangle where
> (2, 3) is the missing coordinate.
>
>  **Input:** grid[][] = {“*.*”, “..*”}  
>  **Output:** 2 1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Find the coordinates of the 3 vertices by iterating through the
given grid. Since a rectangle consists of 2 X-coordinates and 2 Y-coordinates
and 4 vertices, every X-coordinate and Y-coordinate should occur exactly
twice. We can count how many times each X and Y coordinate occurs in the 3
given vertices and the 4th one will have coordinates that occur only once.

  

  

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

 

// Function that return the coordinates

// of the fourth vertex of the rectangle

pair<int, int> findFourthVertex(int n, int m, string s[])

{

 map<int, int> row, col;

 for (int i = 0; i < n; i++)

 for (int j = 0; j < m; j++)

 

 // Save the coordinates of the given

 // vertices of the rectangle

 if (s[i][j] == '*') {

 row[i]++;

 col[j]++;

 }

 int x, y;

 for (auto tm : row)

 if (tm.second == 1)

 x = tm.first;

 for (auto tm : col)

 if (tm.second == 1)

 y = tm.first;

 

 // 1-based indexing

 return make_pair(x + 1, y + 1);

}

 

// Driver code

int main()

{

 string s[] = { "*.*", "*..", "..." };

 int n = sizeof(s) / sizeof(s[0]);

 int m = s[0].length();

 

 auto rs = findFourthVertex(n, m, s);

 cout << rs.first << " " << rs.second;

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

import java.util.Map;

 

class GfG

{

 

 // Function that return the coordinates 

 // of the fourth vertex of the rectangle 

 static Pair<Integer, Integer> findFourthVertex(int n, 

 int m, String s[]) 

 { 

 HashMap<Integer, Integer> row = new HashMap<>(); 

 HashMap<Integer, Integer> col = new HashMap<>(); 

 

 for (int i = 0; i < n; i++)

 { 

 for (int j = 0; j < m; j++)

 { 

 

 // Save the coordinates of the given 

 // vertices of the rectangle 

 if (s[i].charAt(j) == '*') 

 { 

 

 if (row.containsKey(i))

 {

 row.put(i, row.get(i) + 1);

 }

 else

 {

 row.put(i, 1);

 }

 

 if (col.containsKey(j))

 {

 col.put(j, col.get(j) + 1);

 }

 else

 {

 col.put(j, 1);

 } 

 }

 }

 }

 

 int x = 0, y = 0; 

 for (Map.Entry<Integer, Integer> entry : row.entrySet())

 { 

 if (entry.getValue() == 1) 

 x = entry.getKey();

 }

 

 for (Map.Entry<Integer, Integer> entry : col.entrySet())

 { 

 if (entry.getValue() == 1) 

 y = entry.getKey();

 }

 

 // 1-based indexing

 Pair<Integer, Integer> ans = new Pair<>(x + 1, y + 1);

 return ans; 

 } 

 

 // Driver Code 

 public static void main(String []args)

 {

 

 String s[] = { "*.*", "*..", "..." }; 

 int n = s.length; 

 int m = s[0].length(); 

 

 Pair<Integer, Integer> rs = findFourthVertex(n, m, s); 

 System.out.println(rs.first + " " + rs.second);

 }

}

 

class Pair<A, B> 

{

 A first;

 B second;

 

 public Pair(A first, B second) 

 {

 this.first = first;

 this.second = second;

 }

}

 

// This code is contributed by Rituraj Jain   
  
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

 

# Function that return the coordinates 

# of the fourth vertex of the rectangle 

def findFourthVertex(n, m, s) :

 

 row = dict.fromkeys(range(n), 0)

 col = dict.fromkeys(range(m), 0)

 

 for i in range(n) :

 for j in range(m) : 

 

 # Save the coordinates of the given 

 # vertices of the rectangle 

 if (s[i][j] == '*') :

 row[i] += 1; 

 col[j] += 1; 

 

 for keys,values in row.items() : 

 if (values == 1) :

 x = keys; 

 

 for keys,values in col.items() : 

 if (values == 1) :

 y = keys; 

 

 # 1-based indexing 

 return (x + 1, y + 1) ;

 

# Driver code 

if __name__ == "__main__" :

 

 s = [ "*.*", "*..", "..." ] 

 n = len(s);

 m = len(s[0]);

 

 rs = findFourthVertex(n, m, s); 

 print(rs[0], rs[1]) 

 

# This code is contributed by Ryuga  
  
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

 

class GfG

{

 

 // Function that return the coordinates 

 // of the fourth vertex of the rectangle 

 static Pair<int, int> findFourthVertex(int n, 

 int m, String []s) 

 { 

 Dictionary<int, int> row = new Dictionary<int, int>();


 Dictionary<int, int> col = new Dictionary<int, int>();


 

 for (int i = 0; i < n; i++)

 { 

 for (int j = 0; j < m; j++)

 { 

 

 // Save the coordinates of the given 

 // vertices of the rectangle 

 if (s[i][j] == '*') 

 { 

 

 if (row.ContainsKey(i))

 {

 row[i] = row[i] + 1;

 }

 else

 {

 row.Add(i, 1);

 }

 

 if (col.ContainsKey(j))

 {

 col[j] = col[j] + 1;

 }

 else

 {

 col.Add(j, 1);

 } 

 }

 }

 }

 

 int x = 0, y = 0; 

 foreach(KeyValuePair<int, int> entry in row)

 { 

 if (entry.Value == 1) 

 x = entry.Key;

 }

 

 foreach(KeyValuePair<int, int> entry in col)

 { 

 if (entry.Value == 1) 

 y = entry.Key;

 }

 

 // 1-based indexing

 Pair<int, int> ans = new Pair<int, int>(x + 1, y +
1);

 return ans; 

 } 

 

 // Driver Code 

 public static void Main(String []args)

 {

 

 String []s = { "*.*", "*..", "..." }; 

 int n = s.Length; 

 int m = s[0].Length; 

 

 Pair<int, int> rs = findFourthVertex(n, m, s); 

 Console.WriteLine(rs.first + " " + rs.second);

 }

}

 

class Pair<A, B> 

{

 public A first;

 public B second;

 

 public Pair(A first, B second) 

 {

 this.first = first;

 this.second = second;

 }

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    2 3
    

**Time Complexity:** O(N * M)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

