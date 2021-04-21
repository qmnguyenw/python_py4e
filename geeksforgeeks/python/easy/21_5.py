Find the number of operations required to make all array elements Equal



Given an array of **N** integers, the task is to find the number of operations
required to make all elements in the array equal. In one operation we can
distribute equal weights from the maximum element to the rest of the array
elements. If it is not possible to make the array elements equal after
performing the above operations then print -1.

 **Examples** :

>  **Input** : arr = [1, 6, 1, 1, 1];  
>  **Output** : 4  
>  **Explanation** : Since arr becomes **[2, 2, 2, 2, 2]** after distribution
> from max element.
>
>  **Input** : arr = [2, 2, 3];  
>  **Output** : -1  
>  **Explanation** : Here arr becomes [3, 3, 1] after distribution.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Algorithm** :

  

  

  * Declare temporary variable to store number of times operation is performed.
  * Find maximum element of the given array and store its index value.
  * Check if all the elements are equal to the maximum element after n subtractions.
  * Again check that each element is equal to other elements and return n.

Below is the implementation of above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the number

//of operations required to make 

//all array elements Equal 

#include<bits/stdc++.h>

using namespace std;

 

//Function to find maximum 

//element of the given array 

int find_n(int a[],int n)

{ 

 int j = 0, k = 0, s = 0; 

 

 int x = *max_element(a, a + n); 

 int y = *min_element(a, a + n); 

 for (int i = 0; i < n; i++) 

 { 

 if (a[i] == x)

 { 

 s = i; 

 break; 

 } 

 

 } 

 for (int i =0;i<n;i++) 

 { 

 if (a[i] != x && a[i] <= y && a[i] != 0) 

 { 

 a[j] += 1; 

 a[s] -= 1; 

 x -= 1; 

 k += 1; 

 j += 1; 

 } 

 else if (a[i] != 0) 

 { 

 j += 1; 

 } 

 } 

 

 for (int i = 0; i < n; i++) 

 { 

 if (a[i] != x) 

 { 

 k = -1; 

 break; 

 } 

 } 

 return k; 

 } 

 

// Driver Code 

int main() 

{ 

 

 int a[] = {1, 6, 1, 1, 1}; 

 int n = sizeof(a)/sizeof(a[0]);

 cout << (find_n(a, n)); 

 

 return 0;

} 

 

// This code contributed by princiraj1992  
  
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

// Java program to find the number

//of operations required to make 

//all array elements Equal 

 

import java.util.Arrays;

 

class GFG {

 

//Function to find maximum 

//element of the given array 

 static int find_n(int[] a) {

 int j = 0, k = 0, s = 0;

 

 int x = Arrays.stream(a).max().getAsInt();

 int y = Arrays.stream(a).min().getAsInt();

 for (int i : a) {

 if (a[i] == x) {

 s = i;

 break;

 }

 

 }

 for (int i : a) {

 if (i != x && i <= y && i != 0) {

 a[j] += 1;

 a[s] -= 1;

 x -= 1;

 k += 1;

 j += 1;

 } else if (i != 0) {

 j += 1;

 }

 }

 

 for (int i : a) {

 if (a[i] != x) {

 k = -1;

 break;

 }

 }

 return k;

 }

//Driver Code 

 

 public static void main(String[] args) {

 

 int[] a = {1, 6, 1, 1, 1};

 System.out.println(find_n(a));

 }

 

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

# Python program to find the number

# of operations required to make

# all array elements Equal

 

# Function to find maximum 

# element of the given array

def find_n(a):

 j, k = 0, 0

 

 x = max(a)

 for i in range(len(a)):

 if(a[i] == x):

 s = i

 break

 

 for i in a:

 if(i != x and i <= min(a) and i !='\0'):

 a[j] += 1

 a[s] -= 1

 x -= 1

 k += 1

 j += 1

 elif(i != '\0'):

 j += 1

 

 for i in range(len(a)): 

 if(a[i] != x):

 k = -1

 break

 

 return k

 

# Driver Code 

a = [1, 6, 1, 1, 1]

print (find_n(a))  
  
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

// C# program to find the number

// of operations required to make 

// all array elements Equal 

using System;

using System.Linq;

 

class GFG

{

 

// Function to find maximum 

// element of the given array 

static int find_n(int []a)

{

 int j = 0, k = 0, s = 0;

 

 int x = a.Max();

 int y = a.Min();

 foreach(int i in a) 

 {

 if (a[i] == x)

 {

 s = i;

 break;

 }

 

 }

 

 foreach (int i in a) 

 {

 if (i != x && i <= y && i != 0)

 {

 a[j] += 1;

 a[s] -= 1;

 x -= 1;

 k += 1;

 j += 1;

 } 

 

 else if (i != 0)

 {

 j += 1;

 }

 }

 

 foreach (int i in a) 

 {

 if (a[i] != x)

 {

 k = -1;

 break;

 }

 }

 return k;

}

 

// Driver Code 

public static void Main()

{

 int[] a = {1, 6, 1, 1, 1};

 Console.Write(find_n(a));

}

}

 

// This code contributed by 29AjayKumar  
  
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

// PHP program to find the number of 

// operations required to make all 

// array elements Equal

 

// Function to find maximum element of 

// the given array

function find_n(&$a)

{

 $j = 0; 

 $k = 0;

 

 $x = max($a);

 for ($i = 0; $i < sizeof($a); $i++)

 {

 if($a[$i] == $x)

 {

 $s = $i;

 break;

 }

 }

 

 for($i = 0; $i < sizeof($a); $i++)

 {

 if($a[$i] != $x and $a[$i] <= min($a) and

 $a[$i] !=0)

 {

 $a[$j] += 1;

 $a[$s] -= 1;

 $x -= 1;

 $k += 1;

 $j += 1;

 }

 else if($a[$i] != 0)

 $j += 1;

 } 

 

 for($i = 0; $i < sizeof($a); $i++)

 {

 if($a[$i] != $x)

 {

 $k = -1;

 break;

 }

 }

 return $k;

}

 

// Driver Code 

$a = array(1, 6, 1, 1, 1);

echo(find_n($a));

 

// This code is contributed by 

// Shivi_Aggarwal

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

**Time complexity** : O(n)

![competitive-programming-img](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200604102100/GFG-CP-Article-2.png)

My Personal Notes _arrow_drop_up_

Save

