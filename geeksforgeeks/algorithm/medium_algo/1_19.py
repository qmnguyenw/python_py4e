Change in Median of given array after deleting given elements



Given two arrays **arr1[]** and **arr2[]**. The array **arr1[]** is sorted.
The task is to print the change in the median after removing each element from
array **arr2[]** one by one.

 **Note:** The array **arr2[]** has only those elements that are present in
array **arr1[]**.

 **Examples:**

> **Input:** arr1[] = {2, 4, 6, 8, 10}, arr2[] = {4, 6}  
> **Output:** 1 1  
> **Explanation:**  
> Initially median is 6.  
> After removing 4, array becomes arr1[] = {2, 6, 8, 10}, median = 7,
> therefore the difference is 7 – 6 = 1.  
> After removing 6, array becomes arr1[] = {2, 8, 10}, median = 8, therefore
> the difference is 8 – 7 = 1.
>
>  **Input:** arr1[] = {1, 100, 250, 251}, arr2[] = {250, 1}  
> **Output:** -75 75.5  
> **Explanation:**  
> Initially median is 175.  
> After removing 250, array becomes arr1[] = {1, 100, 251}, median = 100,
> therefore the difference is 100 – 175 = -75.  
> After removing 1, array becomes arr1[] = {100, 251}, median = 175.5,
> therefore the difference is 175.5 – 100 = 75.5.
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to traverse each element of the array **arr2[]**
and remove each element from the array **arr1[]** and store the median of the
array **arr1[]** after each removal of element in an array(say **temp[]** ).
Print the consecutive difference of the elements of the array to get change in
median after removing elements from **arr2[]**.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

using namespace std;

// Function to find the median change

// after removing elements from arr2[]

void medianChange(vector<int>& arr1,

 vector<int>& arr2)

{

 int N = arr1.size();

 // To store the median

 vector<float> median;

 // Store the current median

 // If N is odd

 if (N & 1) {

 median

 .push_back(arr1[N / 2] * 1.0);

 }

 // If N is even

 else {

 median

 .push_back((arr1[N / 2]

 + arr1[(N - 1) / 2])

 / 2.0);

 }

 for (auto& x : arr2) {

 // Find the current element

 // in arr1

 auto it = find(arr1.begin(),

 arr1.end(),

 x);

 // Erase the element

 arr1.erase(it);

 // Decrement N

 N--;

 // Find the new median

 // and append

 // If N is odd

 if (N & 1) {

 median

 .push_back(arr1[N / 2] * 1.0);

 }

 // If N is even

 else {

 median

 .push_back((arr1[N / 2]

 + arr1[(N - 1) / 2])

 / 2.0);

 }

 }

 // Print the corresponding

 // difference of median

 for (int i = 0;

 i < median.size() - 1;

 i++) {

 cout << median[i + 1] - median[i]

 << ' ';

 }

}

// Driven Code

int main()

{

 // Given arrays

 vector<int> arr1 = { 2, 4, 6, 8, 10 };

 vector<int> arr2 = { 4, 6 };

 // Function Call

 medianChange(arr1, arr2);

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

// Java program for the

// above approach

import java.util.*;

class GFG{

 

// Function to find the median

// change after removing elements

// from arr2[]

public static void medianChange(List<Integer> arr1,

 List<Integer> arr2)

{

 int N = arr1.size();

 

 // To store the median

 List<Integer> median = new ArrayList<>();

 

 // Store the current median

 

 // If N is odd

 if ((N & 1) != 0)

 median.add(arr1.get(N / 2) * 1);

 

 // If N is even

 else

 median.add((arr1.get(N / 2) +

 arr1.get((N - 1) / 2)) / 2);

 

 for(int x = 0; x < arr2.size(); x++)

 {

 

 // Find the current element

 // in arr1

 int it = arr1.indexOf(arr2.get(x));

 

 // Erase the element

 arr1.remove(it);

 

 // Decrement N

 N--;

 

 // Find the new median

 // and append

 

 // If N is odd

 if ((N & 1) != 0)

 {

 median.add(arr1.get(N / 2) * 1);

 }

 

 // If N is even

 else

 {

 median.add((arr1.get(N / 2) +

 arr1.get((N - 1) / 2)) / 2);

 }

 }

 

 // Print the corresponding

 // difference of median

 for(int i = 0; i < median.size() - 1; i++)

 {

 System.out.print(median.get(i + 1) -

 median.get(i) + " ");

 }

}

// Driver Code 

public static void main(String[] args)

{

 

 // Given arrays

 List<Integer> arr1 = new ArrayList<Integer>(){

 { add(2); add(4); add(6); add(8); add(10); } };

 List<Integer> arr2 = new ArrayList<Integer>(){

 { add(4); add(6); } };

 

 // Function Call

 medianChange(arr1, arr2);

}

}

// This code is contributed by divyesh072019  
  
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

# Python3 program for the

# above approach

# Function to find the median

# change after removing elements

# from arr2[]

def medianChange(arr1, arr2):

 N = len(arr1)

 # To store the median

 median = []

 # Store the current median

 # If N is odd

 if (N & 1):

 median.append(arr1[N // 2] * 1)

 # If N is even

 else:

 median.append((arr1[N // 2] +

 arr1[(N - 1) // 2]) // 2)

 for x in arr2:

 # Find the current

 # element in arr1

 it = arr1.index(x)

 # Erase the element

 arr1.pop(it)

 # Decrement N

 N -= 1

 # Find the new median

 # and append

 # If N is odd

 if (N & 1):

 median.append(arr1[N // 2] * 1)

 # If N is even

 else:

 median.append((arr1[N // 2] +

 arr1[(N - 1) // 2]) // 2)

 # Print the corresponding

 # difference of median

 for i in range(len(median) - 1):

 print(median[i + 1] - median[i],

 end = ' ')

# Driver Code

if __name__ == "__main__":

 # Given arrays

 arr1 = [2, 4, 6,

 8, 10]

 arr2 = [4, 6]

 # Function Call

 medianChange(arr1, arr2)

# This code is contributed by Chitranayal  
  
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

// C# program for the above approach

using System;

using System.Collections.Generic;

class GFG{

 

// Function to find the median change

// after removing elements from arr2[]

static void medianChange(List<int> arr1,

 List<int> arr2)

{

 int N = arr1.Count;

 

 // To store the median

 List<double> median = new List<double>();

 

 // Store the current median

 

 // If N is odd

 if ((N & 1) != 0)

 {

 median.Add(arr1[N / 2] * 1.0);

 }

 

 // If N is even

 else

 {

 median.Add((arr1[N / 2] +

 arr1[(N - 1) / 2]) / 2.0);

 }

 

 foreach(int x in arr2)

 {

 

 // Find the current element

 // in arr1

 int it = arr1.IndexOf(x);

 

 // Erase the element

 arr1.RemoveAt(it);

 

 // Decrement N

 N--;

 

 // Find the new median

 // and append

 

 // If N is odd

 if ((N & 1) != 0)

 {

 median.Add(arr1[N / 2] * 1.0);

 }

 

 // If N is even

 else

 {

 median.Add((arr1[N / 2] +

 arr1[(N - 1) / 2]) / 2.0);

 }

 }

 

 // Print the corresponding

 // difference of median

 for(int i = 0; i < median.Count - 1; i++)

 {

 Console.Write(median[i + 1] -

 median[i] + " ");

 }

}

// Driver Code

static void Main()

{

 

 // Given arrays

 List<int> arr1 = new List<int>(

 new int[]{ 2, 4, 6, 8, 10 });

 List<int> arr2 = new List<int>(

 new int[]{ 4, 6 });

 

 // Function Call

 medianChange(arr1, arr2);

}

}

// This code is contributed by divyeshrabadiya07  
  
---  
  
 __

 __

 **Output:**

    
    
    1 1

_**Time Complexity:** O(M*N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

