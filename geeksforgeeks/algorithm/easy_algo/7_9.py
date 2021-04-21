Minimum odd cost path in a matrix



Given a matrix, the task is to find the cost of the minimum path which is odd
to reach the bottom of a matrix. If no such path exists, print -1.  
 **Note:** Only right-bottom, left-bottom and direct bottom moves are allowed.

 **Examples:**

    
    
    Input: mat[] = 
    {{ 1, 2, 3, 4, 6},
    { 1, 2, 3, 4, 5 },
    { 1, 2, 3, 4, 5 },
    { 1, 2, 3, 4, 5 },
    { 100, 2, 3, 4, 5 }
    
    Output: 11
    
    Input: mat[][] = 
    {{1, 5, 2},
    {7, 2, 2},
    {2, 8, 1}}
    
    Output: 5
    
    
    

**Approach:** This problem can be solved using dynamic programming:

* > For the first row (Base case), cost is  
> floor[0][j]=given[0][j] (floor is our cost array and given is our given
> matrix)

* > // For leftmost element  
> if(j==0)  
> floor[i][j]=given[i][j]+min(floor[i-1][j], floor[i-1][j+1]);
>
>  
>
>
>  
>

* > // For rightmost element  
> else if(j == N-1)  
> floor[i][j] = given[i][j] + min(floor[i-1][j], floor[i-1][j-1])

* As any element except leftmost and rightmost is reachable from direct upper or left upper or right upper row’s block. So,  

> else  
> floor[i][j] = a[i][j] + min(floor[i-1][j-1] + floor[i-1][j] +
> floor[i-1][j+1])

At last, return the minimum odd value from the last row. In case it is not
present, return -1.

 **Below is the implementation of above approach:**  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find Minimum

// odd cost path in a matrix

#include <bits/stdc++.h>

#define M 100 // number of rows

#define N 100 // number of columns

using namespace std;

 

// Function to find the minimum cost

int find_min_odd_cost(int given[M][N], int m, int n)

{

 int floor[M][N] = { { 0 }, { 0 } };

 int min_odd_cost = 0;

 int i, j, temp;

 

 for (j = 0; j < n; j++)

 floor[0][j] = given[0][j];

 

 for (i = 1; i < m; i++)

 for (j = 0; j < n; j++) {

 

 // leftmost element

 if (j == 0) {

 floor[i][j] = given[i][j];

 floor[i][j] += min(floor[i - 1][j], floor[i - 1][j + 1]);

 }

 

 // rightmost element

 else if (j == n - 1) {

 floor[i][j] = given[i][j];

 floor[i][j] += min(floor[i - 1][j], floor[i - 1][j - 1]);

 }

 

 // Any element except leftmost and rightmost element of a row

 // is reachable from direct upper or left upper or right upper

 // row's block

 else {

 

 // Counting the minimum cost

 temp = min(floor[i - 1][j], floor[i - 1][j - 1]);

 temp = min(temp, floor[i - 1][j + 1]);

 floor[i][j] = given[i][j] + temp;

 }

 }

 

 min_odd_cost = INT_MAX;

 

 // Find the minimum cost

 for (j = 0; j < n; j++) {

 if (floor[n - 1][j] % 2 == 1) {

 if (min_odd_cost > floor[n - 1][j])

 min_odd_cost = floor[n - 1][j];

 }

 }

 

 if (min_odd_cost == INT_MIN)

 return -1;

 

 return min_odd_cost;

}

 

// Driver code

int main()

{

 int m = 5, n = 5;

 int given[M][N] = { { 1, 2, 3, 4, 6 },

 { 1, 2, 3, 4, 5 },

 { 1, 2, 3, 4, 5 },

 { 1, 2, 3, 4, 5 },

 { 100, 2, 3, 4, 5 } };

 

 cout << "Minimum odd cost is "

 << find_min_odd_cost(given, m, n);

 

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

// Java program to find minimum odd

// cost path in a matrix

public class GFG {

 

 public static final int M = 100 ;

 public static final int N = 100 ;

 

 // Function to find the minimum cost 

 static int find_min_odd_cost(int given[][], int m, int n)


 { 

 int floor[][] = new int [M][N]; 

 int min_odd_cost = 0; 

 int i, j, temp; 

 

 for (j = 0; j < n; j++) 

 floor[0][j] = given[0][j]; 

 

 for (i = 1; i < m; i++) 

 for (j = 0; j < n; j++) { 

 

 // leftmost element 

 if (j == 0) { 

 floor[i][j] = given[i][j]; 

 floor[i][j] += Math.min(floor[i - 1][j], floor[i - 1][j + 1]);


 } 

 

 // rightmost element 

 else if (j == n - 1) { 

 floor[i][j] = given[i][j]; 

 floor[i][j] += Math.min(floor[i - 1][j], floor[i - 1][j - 1]);


 } 

 

 // Any element except leftmost and rightmost element of a row 

 // is reachable from direct upper or left upper or right upper 

 // row's block 

 else { 

 

 // Counting the minimum cost 

 temp = Math.min(floor[i - 1][j], floor[i - 1][j - 1]); 

 temp = Math.min(temp, floor[i - 1][j + 1]); 

 floor[i][j] = given[i][j] + temp; 

 } 

 } 

 

 min_odd_cost = Integer.MAX_VALUE; 

 

 // Find the minimum cost 

 for (j = 0; j < n; j++) { 

 if (floor[n - 1][j] % 2 == 1) { 

 if (min_odd_cost > floor[n - 1][j]) 

 min_odd_cost = floor[n - 1][j]; 

 } 

 } 

 

 if (min_odd_cost == Integer.MIN_VALUE) 

 return -1; 

 

 return min_odd_cost; 

 } 

 // Driver code

 public static void main(String args[])

 {

 int m = 5, n = 5; 

 int given[][] = { { 1, 2, 3, 4, 6 }, 

 { 1, 2, 3, 4, 5 }, 

 { 1, 2, 3, 4, 5 }, 

 { 1, 2, 3, 4, 5 }, 

 { 100, 2, 3, 4, 5 } }; 

 

 System.out.println( "Minimum odd cost is " + find_min_odd_cost(given,
m, n));

 }

 // This Code is contributed by ANKITRAI1

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

# Python3 program to find Minimum

# odd cost path in a matrix

M = 100 # number of rows

N = 100 # number of columns

 

# Function to find the minimum cost

def find_min_odd_cost(given, m, n):

 

 floor = [[0 for i in range(M)] 

 for i in range(N)]

 min_odd_cost = 0

 i, j, temp = 0, 0, 0

 

 for j in range(n):

 floor[0][j] = given[0][j]

 

 for i in range(1, m):

 for j in range(n):

 

 # leftmost element

 if (j == 0):

 floor[i][j] = given[i][j];

 floor[i][j] += min(floor[i - 1][j], 

 floor[i - 1][j + 1])

 # rightmost element

 elif (j == n - 1):

 floor[i][j] = given[i][j];

 floor[i][j] += min(floor[i - 1][j],

 floor[i - 1][j - 1])

 

 # Any element except leftmost and rightmost 

 # element of a row is reachable from direct 

 # upper or left upper or right upper row's block

 else:

 

 # Counting the minimum cost

 temp = min(floor[i - 1][j], 

 floor[i - 1][j - 1])

 temp = min(temp, floor[i - 1][j + 1])

 floor[i][j] = given[i][j] + temp

 

 min_odd_cost = 10**9

 

 # Find the minimum cost

 for j in range(n):

 if (floor[n - 1][j] % 2 == 1):

 if (min_odd_cost > floor[n - 1][j]):

 min_odd_cost = floor[n - 1][j]

 

 

 if (min_odd_cost == -10**9):

 return -1;

 

 return min_odd_cost

 

# Driver code

m, n = 5, 5

given = [[ 1, 2, 3, 4, 6 ],

 [ 1, 2, 3, 4, 5 ],

 [ 1, 2, 3, 4, 5 ],

 [ 1, 2, 3, 4, 5 ],

 [ 100, 2, 3, 4, 5 ]]

 

print("Minimum odd cost is",

 find_min_odd_cost(given, m, n))

 

# This code is contributed by mohit kumar  
  
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

// C# program to find minimum odd

// cost path in a matrix

 

using System;

public class GFG {

 

 public static int M = 100 ;

 public static int N = 100 ;

 

 // Function to find the minimum cost 

 static int find_min_odd_cost(int[,] given, int m, int n) 

 { 

 int[,] floor = new int [M,N]; 

 int min_odd_cost = 0; 

 int i, j, temp; 

 

 for (j = 0; j < n; j++) 

 floor[0,j] = given[0,j]; 

 

 for (i = 1; i < m; i++) 

 for (j = 0; j < n; j++) { 

 

 // leftmost element 

 if (j == 0) { 

 floor[i,j] = given[i,j]; 

 floor[i,j] += Math.Min(floor[i - 1,j], floor[i - 1,j + 1]); 

 } 

 

 // rightmost element 

 else if (j == n - 1) { 

 floor[i,j] = given[i,j]; 

 floor[i,j] += Math.Min(floor[i - 1,j], floor[i - 1,j - 1]); 

 } 

 

 // Any element except leftmost and rightmost element of a row 

 // is reachable from direct upper or left upper or right upper 

 // row's block 

 else { 

 

 // Counting the minimum cost 

 temp = Math.Min(floor[i - 1,j], floor[i - 1,j - 1]); 

 temp = Math.Min(temp, floor[i - 1,j + 1]); 

 floor[i,j] = given[i,j] + temp; 

 } 

 } 

 

 min_odd_cost = int.MaxValue; 

 

 // Find the minimum cost 

 for (j = 0; j < n; j++) { 

 if (floor[n - 1,j] % 2 == 1) { 

 if (min_odd_cost > floor[n - 1,j]) 

 min_odd_cost = floor[n - 1,j]; 

 } 

 } 

 

 if (min_odd_cost == int.MinValue) 

 return -1; 

 

 return min_odd_cost; 

 } 

 // Driver code

 public static void Main()

 {

 int m = 5, n = 5; 

 int[,] given = { { 1, 2, 3, 4, 6 }, 

 { 1, 2, 3, 4, 5 }, 

 { 1, 2, 3, 4, 5 }, 

 { 1, 2, 3, 4, 5 }, 

 { 100, 2, 3, 4, 5 } }; 

 

 Console.Write( "Minimum odd cost is " + 

 find_min_odd_cost(given, m, n));

 }

 

}

   
  
---  
  
__

__

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP program to find Minimum 

// odd cost path in a matrix

$M = 100; $N = 100;

 

// Function to find the minimum cost

function find_min_odd_cost($given, $m, $n)

{

 global $M, $N;

 

 $floor1[$M][$N] = array(array(0), 

 array(0));

 $min_odd_cost = 0;

 

 for ($j = 0; $j < $n; $j++)

 $floor1[0][$j] = $given[0][$j];

 

 for ($i = 1; $i < $m; $i++)

 for ($j = 0; $j < $n; $j++)

 {

 

 // leftmost element

 if ($j == 0)

 {

 $floor1[$i][$j] = $given[$i][$j];

 $floor1[$i][$j] += min($floor1[$i - 1][$j], 

 $floor1[$i - 1][$j + 1]);

 }

 

 // rightmost element

 else if ($j == $n - 1)

 {

 $floor1[$i][$j] = $given[$i][$j];

 $floor1[$i][$j] += min($floor1[$i - 1][$j], 

 $floor1[$i - 1][$j - 1]);

 }

 

 // Any element except leftmost and rightmost

 // element of a row is reachable from direct

 // upper or left upper or right upper row's block

 else

 {

 

 // Counting the minimum cost

 $temp = min($floor1[$i - 1][$j], 

 $floor1[$i - 1][$j - 1]);

 $temp = min($temp, $floor1[$i - 1][$j + 1]);

 $floor1[$i][$j] = $given[$i][$j] + $temp;

 }

 }

 

 $min_odd_cost = PHP_INT_MAX;

 

 // Find the minimum cost

 for ($j = 0; $j < $n; $j++)

 {

 if ($floor1[$n - 1][$j] % 2 == 1)

 {

 if ($min_odd_cost > $floor1[$n - 1][$j])

 $min_odd_cost = $floor1[$n - 1][$j];

 }

 }

 

 if ($min_odd_cost == PHP_INT_MIN)

 return -1;

 

 return $min_odd_cost;

}

 

// Driver code

$m = 5; $n = 5;

$given = array(array(1, 2, 3, 4, 6),

 array(1, 2, 3, 4, 5),

 array(1, 2, 3, 4, 5),

 array(1, 2, 3, 4, 5),

 array(100, 2, 3, 4, 5));

 

echo "Minimum odd cost is " . 

 find_min_odd_cost($given, $m, $n);

 

// This code is contributed by Akanksha Rai

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    Minimum odd cost is 11
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

