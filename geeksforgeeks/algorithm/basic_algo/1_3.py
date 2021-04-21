Selection Sort VS Bubble Sort



In this, we will cover the comparison between Selection Sort VS Bubble Sort.
The resources required by Selection Sort & Bubble Sort algorithms on the basis
of Time and Space Complexity are as follows.

    
    
    Time Complexity - ![O\(n^2\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-d3c2f213cefe3af64dbf1dacd22ec5ce_l3.png)
    Same Complexity - ![O\(1\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-64fde0c2eba99ef139c22c744a16e0e3_l3.png)

Let’s dive deep into the working of these algorithms.  
**Selection Sort** **:**  
The selection sort algorithm generally is the first sorting algorithm that is
taught to us. Here in every iteration of the inner loop, the smallest element
is replaced with the starting element in each loop. After the end of each
loop, we increment the starting position by 1 and run it till the second last
element in the array. Hence, by doing so at the end of the outer loop we will
be having a sorted array.  
The image below explains the iteration of Selection Sort Algorithm.  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201128163500/SelectionSorthttpscoursescswashingtoneducoursescse37319aulectures05reading-300x286.jpg)

Here we can simplify the selection sort algorithm by saying that the sorting
here is done on the basis of the smallest to the largest element. The smallest
element is first sorted and then the second smallest element and so on.  
**Implementation of Selection Sort :**  
Below is the implementation of the above-explained algorithm.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<iostream>

using namespace std;

void Selection_Sort(int arr[], int n) 

{

 for(int i = 0; i < n - 1; ++i) 

 {

 int min_index = i; 

 for(int j = i + 1; j < n; ++j) 

 {

 if(arr[j] < arr[min_index]) 

 min_index = j;

 }

 swap(arr[i], arr[min_index]); 

 }

}

int main()

{

 int n = 5;

 int arr[5] = {2, 0, 1, 4, 3};

 Selection_Sort(arr, n);

 cout<<"The Sorted Array by using Selection Sort is : ";

 for(int i = 0; i < n; ++i)

 cout<<arr[i]<<" ";

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

class GFG{

 static void Selection_Sort(int arr[], int n) 

 {

 for(int i = 0; i < n - 1; ++i) 

 {

 int min_index = i; 

 for(int j = i + 1; j < n; ++j) 

 {

 if(arr[j] < arr[min_index]) 

 min_index = j;

 }

 int temp = arr[i];

 arr[i] = arr[min_index];

 arr[min_index] = temp;

 }

 }

 // Driver code

 public static void main(String[] args)

 {

 int n = 5;

 int arr[] = {2, 0, 1, 4, 3};

 Selection_Sort(arr, n);

 System.out.print("The Sorted Array by using Selection Sort is : ");

 for(int i = 0; i < n; ++i)

 System.out.print(arr[i] + " ");

 }

}

// This code is contributed by aashish1995  
  
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

using System;

public class GFG{

 static void Selection_Sort(int []arr, int n) 

 {

 for(int i = 0; i < n - 1; ++i) 

 {

 int min_index = i; 

 for(int j = i + 1; j < n; ++j) 

 {

 if(arr[j] < arr[min_index]) 

 min_index = j;

 }

 int temp = arr[i];

 arr[i] = arr[min_index];

 arr[min_index] = temp;

 }

 }

 // Driver code

 public static void Main(String[] args)

 {

 int n = 5;

 int []arr = {2, 0, 1, 4, 3};

 Selection_Sort(arr, n);

 Console.Write("The Sorted Array by using Selection Sort is : ");

 for(int i = 0; i < n; ++i)

 Console.Write(arr[i] + " ");

 }

}

// This code is contributed by aashish1995  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    The Sorted Array by using Selection Sort is : 0 1 2 3 4 

