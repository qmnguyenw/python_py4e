Minimize the sum calculated by repeatedly removing any two elements and
inserting their sum to the Array



Given **N** elements, you can remove any two elements from the list, note
their sum and add the sum to the list. Repeat these steps while there are more
than a single element in the list. The task is to minimize the sum of these
chosen sum in the end.  
 **Examples:**  

> **Input:** arr[] = {1, 4, 7, 10}  
> **Output:** 39  
> Choose 1 and 4, Sum = 5, arr[] = {5, 7, 10}  
> Choose 5 and 7, Sum = 17, arr[] = {12, 10}  
> Choose 12 and 10, **Sum = 39** , arr[] = {22}  
>  **Input:** arr[] = {1, 3, 7, 5, 6}  
> **Output:** 48  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** In order to minimize the sum, the elements that gets chosen at
every step must the minimum elements from the list. In order to do that
efficiently, a priority queue can be used. At every step, while there are more
than a single element in the list, choose the minimum and the second minimum,
remove them from the list add their sum to the list after updating the running
sum.  
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

#include<bits/stdc++.h>

using namespace std;

// Function to return the minimized sum

int getMinSum(int arr[], int n)

{

 int i, sum = 0;

 // Priority queue to store the elements of the array

 // and retrieve the minimum element efficiently

 priority_queue<int, vector<int>, greater<int> > pq;

 // Add all the elements

 // to the priority queue

 for (i = 0; i < n; i++)

 pq.push(arr[i]);

 // While there are more than 1 elements

 // left in the queue

 while (pq.size() > 1)

 {

 // Remove and get the minimum

 // element from the queue

 int min = pq.top();

 pq.pop();

 // Remove and get the second minimum

 // element (currently minimum)

 int secondMin = pq.top();

 

 pq.pop();

 // Update the sum

 sum += (min + secondMin);

 // Add the sum of the minimum

 // elements to the queue

 pq.push(min + secondMin);

 }

 // Return the minimized sum

 return sum;

}

// Driver code

int main()

{

 int arr[] = { 1, 3, 7, 5, 6 };

 int n = sizeof(arr)/sizeof(arr[0]);

 cout << (getMinSum(arr, n));

}

// This code is contributed by mohit  
  
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

import java.util.PriorityQueue;

class GFG

{

 // Function to return the minimized sum

 static int getMinSum(int arr[], int n)

 {

 int i, sum = 0;

 // Priority queue to store the elements of the array

 // and retrieve the minimum element efficiently

 PriorityQueue<Integer> pq = new PriorityQueue<>();

 // Add all the elements

 // to the prioriry queue

 for (i = 0; i < n; i++)

 pq.add(arr[i]);

 // While there are more than 1 elements

 // left in the queue

 while (pq.size() > 1)

 {

 // Remove and get the minimum

 // element from the queue

 int min = pq.poll();

 // Remove and get the second minimum

 // element (currently minimum)

 int secondMin = pq.poll();

 // Update the sum

 sum += (min + secondMin);

 // Add the sum of the minimum

 // elements to the queue

 pq.add(min + secondMin);

 }

 // Return the minimized sum

 return sum;

 }

 // Driver code

 public static void main(String[] args)

 {

 int arr[] = { 1, 3, 7, 5, 6 };

 int n = arr.length;

 System.out.print(getMinSum(arr, n));

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

# Python3 implementation of the approach

# Function to return the minimized sum

def getMinSum(arr, n):

 sum = 0

 

 # Priority queue to store the elements of the array

 # and retrieve the minimum element efficiently

 pq = []

 

 # Add all the elements

 # to the priority queue

 for i in range( n ):

 pq.append(arr[i])

 

 # While there are more than 1 elements

 # left in the queue

 while (len(pq) > 1) :

 

 pq.sort(reverse=True)

 

 # Remove and get the minimum

 # element from the queue

 min = pq[-1];

 

 pq.pop();

 

 # Remove and get the second minimum

 # element (currently minimum)

 secondMin = pq[-1];

 

 pq.pop();

 

 # Update the sum

 sum += (min + secondMin);

 

 # Add the sum of the minimum

 # elements to the queue

 pq.append(min + secondMin)

 

 # Return the minimized sum

 return sum

 

# Driver code

if __name__ == "__main__":

 

 arr = [ 1, 3, 7, 5, 6 ]

 n = len(arr)

 print(getMinSum(arr, n))

# This code is contributed by chitranayal  
  
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

 // Function to return the minimized sum

 static int getMinSum(int[] arr, int n)

 {

 int i, sum = 0;

 // Priority queue to store the elements of the array

 // and retrieve the minimum element efficiently

 List<int> pq = new List<int>();

 // Add all the elements

 // to the priority queue

 for (i = 0; i < n; i++)

 {

 pq.Add(arr[i]);

 }

 // While there are more than 1 elements

 // left in the queue

 while(pq.Count > 1)

 {

 pq.Sort();

 // Remove and get the minimum

 // element from the queue

 int min = pq[0];

 pq.RemoveAt(0);

 // Remove and get the second minimum

 // element (currently minimum)

 int secondMin = pq[0];

 pq.RemoveAt(0);

 // Update the sum

 sum += (min + secondMin);

 // Add the sum of the minimum

 // elements to the queue

 pq.Add(min + secondMin);

 }

 // Return the minimized sum

 return sum;

 }

 // Driver code

 static public void Main ()

 {

 int[] arr = { 1, 3, 7, 5, 6 };

 int n = arr.Length;

 Console.WriteLine(getMinSum(arr, n));

 }

}

// This code is contributed by avanitrachhadiya2155  
  
---  
  
 __

 __

 **Output:**

    
    
    48

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

