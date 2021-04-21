Generating subarrays using recursion



Given an array, generate all the possible subarrays of the given array using
recursion.

 **Examples:**

    
    
    Input : [1, 2, 3]
    Output : [1], [1, 2], [2], [1, 2, 3], [2, 3], [3]
    
    Input : [1, 2]
    Output : [1], [1, 2], [2]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have discussed iterative program to generate all subarrays. In this post,
recursive is discussed.

 **Approach:** We use two pointers **start** and **end** to maintain the
starting and ending point of the array and follow the steps given below:

  * Stop if we have reached the end of the array
  * Increment the **end** index if **start** has become greater than **end**
  * Print the subarray from index **start** to **end** and increment the starting index

Below is the implementation of the above approach.  

## C++

  

  

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code to print all possible subarrays

// for given array using recursion 

 

#include <iostream>

# include <vector>

using namespace std;

 

// Recursive function to print all possible subarrays 

// for given array 

void printSubArrays(vector<int> arr, int start, int end)

{ 

 // Stop if we have reached the end of the array 

 if (end == arr.size()) 

 return;

 

 // Increment the end point and start from 0 

 else if (start > end) 

 printSubArrays(arr, 0, end + 1);

 

 // Print the subarray and increment the starting point 

 else

 {

 cout << "[";

 for (int i = start; i < end; i++){

 cout << arr[i] << ", ";

 }

 

 cout << arr[end] << "]" << endl;

 printSubArrays(arr, start + 1, end);

 }

 

 return;

}

 

int main()

{

 vector<int> arr = {1, 2, 3};

 printSubArrays(arr, 0, 0);

 return 0;

}  
  
---  
  
 __

 __

