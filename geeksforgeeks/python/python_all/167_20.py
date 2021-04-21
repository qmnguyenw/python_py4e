Sort even and odd placed elements in increasing order



Given a list _N_ , the task is to sort all the elements at odd and even
positions in increasing order. After sorting, we need to put all odd
positioned elements together, then all even positioned elements

 **Examples:**

    
    
    **Input :** [3, 2, 7, 6, 8]
    **Output :** 3 7 8 2 6
    **Explanation:**
    Odd position elements in sorted order are 3, 7, 8.
    Even position elements in sorted order are 2, 6.
    
    **Input :** 1 0 2 7 0 0
    **Output :** 0 1 2 0 0 7
    Odd {1, 2, 0}
    Even {0, 7, 0}
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * Initialize two lists to store the odd and even indexed digits.
  * Traverse through all the digits and store the odd indexed digits at _odd_indexes_ list and the even indexed digits at _even_indexes_ list.
  * Print the elements in the odd_indexes list in sorted order.
  * Print the elements in the even_indexes list in the sorted order.

Below is the implementation:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of above approach

#include<bits/stdc++.h>

using namespace std;

 

// function to prin the odd and even indexed digits

void odd_even(int arr[], int n)

{

 

 // lists to store the odd and

 // even positioned digits

 vector<int> odd_indexes;

 vector<int>even_indexes;

 

 // traverse through all the indexes 

 // in the integer

 for (int i = 0; i < n;i++)

 {

 

 // if the digit is in odd_index position

 // append it to odd_position list

 if (i % 2 == 0)

 odd_indexes.push_back(arr[i]);

 

 // else append it to the even_position list

 else

 even_indexes.push_back(arr[i]);

 

 }

 

 // print the elements in the list in sorted order

 sort(odd_indexes.begin(), odd_indexes.end());

 sort(even_indexes.begin(), even_indexes.end());

 

 for(int i = 0; i < odd_indexes.size();i++)

 cout << odd_indexes[i] << " ";

 

 for(int i = 0; i < even_indexes.size(); i++)

 cout << even_indexes[i] << " "; 

 

} 

 

// Driver code

int main()

{

 int arr[] = {3, 2, 7, 6, 8};

 int n = sizeof(arr)/sizeof(arr[0]);

 odd_even(arr, n);

}

 

// This code is contributed by

// Surendra_Gangwar  
  
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

 

class GFG 

{

 

// function to prin the odd and even indexed digits

static void odd_even(int arr[], int n)

{

 

 // lists to store the odd and

 // even positioned digits

 Vector<Integer> odd_indexes = new Vector<Integer>();

 Vector<Integer> even_indexes = new Vector<Integer>();

 

 // traverse through all the indexes 

 // in the integer

 for (int i = 0; i < n;i++)

 {

 

 // if the digit is in odd_index position

 // append it to odd_position list

 if (i % 2 == 0)

 odd_indexes.add(arr[i]);

 

 // else append it to the even_position list

 else

 even_indexes.add(arr[i]);

 

 }

 

 // print the elements in the list in sorted order

 Collections.sort(odd_indexes);

 Collections.sort(even_indexes);

 

 for(int i = 0; i < odd_indexes.size(); i++)

 System.out.print(odd_indexes.get(i) + " ");

 

 for(int i = 0; i < even_indexes.size(); i++)

 System.out.print(even_indexes.get(i) + " "); 

 

} 

 

// Driver code

public static void main(String[] args)

{

 int arr[] = {3, 2, 7, 6, 8};

 int n = arr.length;

 odd_even(arr, n);

}

}

 

// This code is contributed by Rajput-Ji  
  
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

# function to prin the odd and even indexed digits

def odd_even(n):

 

 # lists to store the odd and

 # even positioned digits

 odd_indexes = []

 even_indexes = []

 

 # traverse through all the indexes 

 # in the integer

 for i in range(len(n)):

 

 # if the digit is in odd_index position

 # append it to odd_position list

 if i % 2 == 0: odd_indexes.append(n[i])

 

 # else append it to the even_position list

 else: even_indexes.append(n[i])

 

 # print the elements in the list in sorted order

 for i in sorted(odd_indexes): print(i, end =" ")

 for i in sorted(even_indexes): print(i, end =" ")

 

 

# Driver Code

n = [3, 2, 7, 6, 8]

odd_even(n)  
  
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

 

class GFG 

{

 

// function to prin the odd and even indexed digits

static void odd_even(int []arr, int n)

{

 

 // lists to store the odd and

 // even positioned digits

 List<int> odd_indexes = new List<int>();

 List<int> even_indexes = new List<int>();

 

 // traverse through all the indexes 

 // in the integer

 for (int i = 0; i < n;i++)

 {

 

 // if the digit is in odd_index position

 // append it to odd_position list

 if (i % 2 == 0)

 odd_indexes.Add(arr[i]);

 

 // else append it to the even_position list

 else

 even_indexes.Add(arr[i]);

 

 }

 

 // print the elements in the list in sorted order

 odd_indexes.Sort();

 even_indexes.Sort();

 

 for(int i = 0; i < odd_indexes.Count; i++)

 Console.Write(odd_indexes[i] + " ");

 

 for(int i = 0; i < even_indexes.Count; i++)

 Console.Write(even_indexes[i] + " "); 

 

} 

 

// Driver code

public static void Main(String[] args)

{

 int []arr = {3, 2, 7, 6, 8};

 int n = arr.Length;

 odd_even(arr, n);

}

}

 

// This code is contributed by PrinciRaj1992  
  
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

// PHP implementation of above approach 

 

// function to prin the odd and even 

// indexed digits 

function odd_even($n)

{

 

 // lists to store the odd and

 // even positioned digits 

 $odd_indexes = array();

 $even_indexes = array();

 

 // traverse through all the indexes 

 // in the integer 

 for ($i = 0; $i < sizeof($n); $i++)

 {

 

 // if the digit is in odd_index position 

 // append it to odd_position list 

 if ($i % 2 == 0)

 array_push($odd_indexes, $n[$i]);

 

 // else append it to the even_position list 

 else

 array_push($even_indexes, $n[$i]); 

 

 }

 

 // print the elements in the list in sorted order 

 sort($odd_indexes);

 for ($i = 0; $i < sizeof($odd_indexes); $i++)

 echo $odd_indexes[$i], " ";

 

 sort($even_indexes) ;

 for ($i = 0; $i < sizeof($even_indexes); $i++)

 echo $even_indexes[$i], " ";

}

 

// Driver Code 

$n = array(3, 2, 7, 6, 8);

odd_even($n);

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    3 7 8 2 6
    

**Time Complexity :** O(nlogn)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

