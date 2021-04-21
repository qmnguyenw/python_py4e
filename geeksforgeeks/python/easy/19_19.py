Generating all possible Subsequences using Recursion



Given an array. The task is to generate and print all of the possible
subsequences of the given array using recursion.  
 **Examples:**  

    
    
    Input : [1, 2, 3]
    Output : [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]
    
    Input : [1, 2]
    Output : [2], [1], [1, 2]
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** For every element in the array, there are two choices, either
to include it in the subsequence or not include it. Apply this for every
element in the array starting from index 0 until we reach the last index.
Print the subsequence once the last index is reached.  
Below diagram shows the recursion tree for array, **arr[] = {1, 2}**.  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201019164404/GFGGenerateAllSubsequences.png)

Below is the implementation of the above approach.  

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code to print all possible

// subsequences for given array using

// recursion

#include <bits/stdc++.h>

using namespace std;

 

void printArray(vector<int> arr, int n)

{

 for (int i = 0; i < n; i++)

 cout << arr[i] << " ";

 cout << endl;

}

 

// Recursive function to print all

// possible subsequences for given array

void printSubsequences(vector<int> arr, int index, 

 vector<int> subarr)

{

 // Print the subsequence when reach

 // the leaf of recursion tree

 if (index == arr.size())

 {

 int l = subarr.size();

 

 // Condition to avoid printing

 // empty subsequence

 if (l != 0)

 printArray(subarr, l);

 }

 else

 {

 // Subsequence without including

 // the element at current index

 printSubsequences(arr, index + 1, subarr);

 

 subarr.push_back(arr[index]);

 

 // Subsequence including the element

 // at current index

 printSubsequences(arr, index + 1, subarr);

 }

 return;

}

 

// Driver Code

int main()

{

 vector<int> arr{1, 2, 3};

 vector<int> b;

 

 printSubsequences(arr, 0, b);

 

 return 0;

}

 

// This code is contributed by

// sanjeev2552  
  
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

# Python3 code to print all possible

# subsequences for given array using 

# recursion 

 

# Recursive function to print all 

# possible subsequences for given array 

def printSubsequences(arr, index, subarr): 

 

 # Print the subsequence when reach 

 # the leaf of recursion tree 

 if index == len(arr): 

 

 # Condition to avoid printing 

 # empty subsequence 

 if len(subarr) != 0: 

 print(subarr) 

 

 else: 

 # Subsequence without including 

 # the element at current index 

 printSubsequences(arr, index + 1, subarr) 

 

 # Subsequence including the element 

 # at current index 

 printSubsequences(arr, index + 1, 

 subarr+[arr[index]]) 

 

 return

 

arr = [1, 2, 3] 

 

printSubsequences(arr, 0, []) 

 

#This code is contributed by Mayank Tyagi  
  
---  
  
 __

 __

 **Output:**

    
    
    [3]
    [2]
    [2, 3]
    [1]
    [1, 3]
    [1, 2]
    [1, 2, 3]
    
    

**Time Complexity:**

![O\(2^n\) ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5b85d092049c7251cfcc299c23812154_l3.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

