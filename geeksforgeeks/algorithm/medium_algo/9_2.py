Sum of all Submatrices of a Given Matrix



Given a **NxN** **2-D** matrix, the task to find the sum of all the
submatrices.  
 **Examples:**  

    
    
    **Input :**  arr[] = {{1, 1},
                      {1, 1}};
    **Output :** 16
    **Explanation** : 
    Number of sub-matrices with 1 elements = 4
    Number of sub-matrices with 2 elements = 4
    Number of sub-matrices with 3 elements = 0
    Number of sub-matrices with 4 elements = 1
    
    Since all the entries are 1, the sum becomes
    sum = 1 * 4 + 2 * 4 + 3 * 0 + 4 * 1 = 16
    
    **Input :** arr[] = {{1, 2, 3},
                     {4, 5, 6},
                     {7, 8, 9}}
    **Output :** 500

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Simple Solution:** A naive solution is to generate all the possible
submatrices and sum up all of them.  
The time complexity of this approach will be O(n6).  
 **Efficient Solution :** For each element of the matrix, let us try to find
the number of sub-matrices, the element will lie in.  
This can be done in O(1) time. Let us suppose the index of an element be (X,
Y) in 0 based indexing, then the number of submatrices (Sx, y) for this
element will be in can be given by the formula **S x, y = (X + 1) * (Y + 1) *
(N – X) * (N – Y) **. This formula works, because we just have to choose two
different positions on the matrix that will create a submatrix that envelopes
the element. Thus, for each element, ‘sum’ can be updated as **sum += (S x, y)
* Arrx, y**.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the sum of all

// possible submatrices of a given Matrix

#include <iostream>

#define n 3

using namespace std;

// Function to find the sum of all

// possible submatrices of a given Matrix

int matrixSum(int arr[][n])

{

 // Variable to store

 // the required sum

 int sum = 0;

 // Nested loop to find the number

 // of submatrices, each number belongs to

 for (int i = 0; i < n; i++)

 for (int j = 0; j < n; j++) {

 // Number of ways to choose

 // from top-left elements

 int top_left = (i + 1) * (j + 1);

 // Number of ways to choose

 // from bottom-right elements

 int bottom_right = (n - i) * (n - j);

 sum += (top_left * bottom_right * arr[i][j]);

 }

 return sum;

}

// Driver Code

int main()

{

 int arr[][n] = { { 1, 1, 1 },

 { 1, 1, 1 },

 { 1, 1, 1 } };

 cout << matrixSum(arr);

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

// Java program to find the sum of all

// possible submatrices of a given Matrix

class GFG

{

 static final int n = 3;

 // Function to find the sum of all

 // possible submatrices of a given Matrix

 static int matrixSum(int arr[][])

 {

 // Varialbe to store

 // the required sum

 int sum = 0;

 // Nested loop to find the number

 // of submatrices, each number belongs to

 for (int i = 0; i < n; i++)

 {

 for (int j = 0; j < n; j++)

 {

 // Number of ways to choose

 // from top-left elements

 int top_left = (i + 1) * (j + 1);

 // Number of ways to choose

 // from bottom-right elements

 int bottom_right = (n - i) * (n - j);

 sum += (top_left * bottom_right * arr[i][j]);

 }

 }

 return sum;

 }

 // Driver Code

 public static void main(String[] args)

 {

 int arr[][] = {{1, 1, 1},

 {1, 1, 1},

 {1, 1, 1}};

 System.out.println(matrixSum(arr));

 }

}

// This code contributed by Rajput-Ji  
  
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

# Python3 program to find the sum of all

# possible submatrices of a given Matrix

n = 3

# Function to find the sum of all

# possible submatrices of a given Matrix

def matrixSum(arr) :

 

 # Variable to store the required sum

 sum = 0;

 # Nested loop to find the number of

 # submatrices, each number belongs to

 for i in range(n) :

 for j in range(n) :

 # Number of ways to choose

 # from top-left elements

 top_left = (i + 1) * (j + 1);

 # Number of ways to choose

 # from bottom-right elements

 bottom_right = (n - i) * (n - j);

 sum += (top_left * bottom_right *

 arr[i][j]);

 return sum;

# Driver Code

if __name__ == "__main__" :

 arr = [[ 1, 1, 1 ],

 [ 1, 1, 1 ],

 [ 1, 1, 1 ]];

 print(matrixSum(arr))

 

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

// C# program to find the sum of all

// possible submatrices of a given Matrix

using System;

class GFG

{

static int n = 3;

// Function to find the sum of all

// possible submatrices of a given Matrix

static int matrixSum(int [,]arr)

{

 // Varialbe to store the

 // required sum

 int sum = 0;

 // Nested loop to find the number of 

 // submatrices, each number belongs to

 for (int i = 0; i < n; i++)

 {

 for (int j = 0; j < n; j++)

 {

 // Number of ways to choose

 // from top-left elements

 int top_left = (i + 1) * (j + 1);

 // Number of ways to choose

 // from bottom-right elements

 int bottom_right = (n - i) * (n - j);

 sum += (top_left * bottom_right * arr[i, j]);

 }

 }

 return sum;

}

// Driver Code

public static void Main()

{

 int [,]arr = {{1, 1, 1},

 {1, 1, 1},

 {1, 1, 1}};

 Console.WriteLine(matrixSum(arr));

}

}

// This code contributed by vt_m..  
  
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

// PHP program to find the sum of all

// possible submatrices of a given Matrix

// Function to find the sum of all

// possible submatrices of a given Matrix

function matrixSum($arr)

{

 $n = 3;

 

 // Variable to store the required sum

 $sum = 0;

 // Nested loop to find the number

 // of submatrices, each number belongs to

 for ($i = 0; $i < $n; $i++)

 for ($j = 0; $j < $n; $j++)

 {

 // Number of ways to choose

 // from top-left elements

 $top_left = ($i + 1) * ($j + 1);

 // Number of ways to choose

 // from bottom-right elements

 $bottom_right = ($n - $i) * ($n - $j);

 $sum += ($top_left * $bottom_right *

 $arr[$i][$j]);

 }

 return $sum;

}

// Driver Code

$arr = array(array(1, 1, 1),

 array(1, 1, 1),

 array(1, 1, 1));

echo matrixSum($arr);

// This code is contributed

// by Akanksha Rai

?>  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// JavaScript program to find the sum of all

// possible submatrices of a given Matrix

let n = 3;

// Function to find the sum of all

// possible submatrices of a given Matrix

function matrixSum(arr)

{

 // Variable to store

 // the required sum

 let sum = 0;

 // Nested loop to find the number

 // of submatrices, each number belongs to

 for (let i = 0; i < n; i++)

 for (let j = 0; j < n; j++) {

 // Number of ways to choose

 // from top-left elements

 let top_left = (i + 1) * (j + 1);

 // Number of ways to choose

 // from bottom-right elements

 let bottom_right = (n - i) * (n - j);

 sum += (top_left * bottom_right * arr[i][j]);

 }

 return sum;

}

// Driver Code

let arr = [[ 1, 1, 1 ],

 [ 1, 1, 1 ],

 [ 1, 1, 1 ]] ;

 document.write(matrixSum(arr));

 

// This code is contributed by todaysgaurav

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    100

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

