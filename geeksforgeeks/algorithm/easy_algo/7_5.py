Meta Binary Search | One-Sided Binary Search



Meta binary search (also called one-sided binary search by Steven Skiena in
The Algorithm Design Manual on page 134) is a modified form of binary search
that incrementally constructs the index of the target value in the array. Like
normal binary search, meta binary search takes O(log n) time.

 **Examples:**

    
    
    Input: [-10, -5, 4, 6, 8, 10, 11], key_to_search = 10
    Output: 5
    
    Input: [-2, 10, 100, 250, 32315], key_to_search = -2
    Output: 0
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The exact implementation varies, but the basic algorithm has two parts:

  1. Figure out how many bits are necessary to store the largest array index.
  2. Incrementally construct the index of the target value in the array by determining whether each bit in the index should be set to 1 or 0.

 **Approach:**

  1. Store number of bits to represent the largest array index in variable lg
  2. Use lg to start off the search in a for loop
  3. If element is found return pos
  4. Otherwise incrementally construct index to reach the target value in the for loop
  5. If element found return pos otherwise -1

Below is the implementation of the above approach:  

## C++

  

  

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of above approach

 

#include <iostream>

#include <cmath>

#include <vector>

using namespace std;

 

// Function to show the working of Meta binary search

int bsearch(vector<int> A, int key_to_search)

{

 int n = (int)A.size();

 // Set number of bits to represent largest array index

 int lg = log2(n-1)+1; 

 

 //while ((1 << lg) < n - 1)

 //lg += 1;

 

 int pos = 0;

 for (int i = lg ; i >= 0; i--) {

 if (A[pos] == key_to_search)

 return pos;

 

 // Incrementally construct the

 // index of the target value

 int new_pos = pos | (1 << i);

 

 // find the element in one

 // direction and update position

 if ((new_pos < n) && (A[new_pos] <= key_to_search))

 pos = new_pos;

 }

 

 // if element found return pos otherwise -1

 return ((A[pos] == key_to_search) ? pos : -1);

}

 

// Driver code

int main(void)

{

 

 vector<int> A = { -2, 10, 100, 250, 32315 };

 cout << bsearch(A, 10) << endl;

 

 return 0;

}

 

// This implementation was improved by Tanin  
  
---  
  
 __

 __

