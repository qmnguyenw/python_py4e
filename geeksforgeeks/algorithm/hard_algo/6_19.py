Merge K sorted arrays of different sizes | ( Divide and Conquer Approach )



Given **k** sorted arrays of different length, merge them into a single array
such that the merged array is also sorted.

 **Examples:**

    
    
    **Input :** {{3, 13}, 
            {8, 10, 11}
            {9, 15}}
    **Output :** {3, 8, 9, 10, 11, 13, 15}
    
    **Input :** {{1, 5}, 
             {2, 3, 4}}
    **Output :** {1, 2, 3, 4, 5}
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Let S be the total number of elements in all the arrays.

 **Simple Approach** : A simple approach is to append the arrays one after
another and sort them. Time complexity in this case will be **O( S *
log(S))**.

 **Efficient Approach** : An efficient solution will be to take pairs of
arrays at each step. Then merge the pairs using the two pointer technique of
merging two sorted arrays. Thus, after merging all the pairs, the number of
arrays will reduce by half.

  

  

We, will continue this till the number of remaining arrays doesn’t become 1.
Thus, the number of steps required will be of the order log(k) and since at
each step, we are taking O(S) time to perform the merge operations, the total
time complexity of this approach becomes **O(S * log(k))**.

We already have discussed this approach for merging K sorted arrays of same
sizes.

Since in this problem the arrays are of different sizes, we will use dynamic
arrays ( eg: vector in case of C++ or arraylist in case of Java ) because they
reduce the number of lines and work load significantly.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to merge K sorted arrays of

// different arrays

 

#include <iostream>

#include <vector>

using namespace std;

 

// Function to merge two arrays

vector<int> mergeTwoArrays(vector<int> l, vector<int> r)

{ 

 // array to store the result

 // after merging l and r

 vector<int> ret;

 

 // variables to store the current

 // pointers for l and r

 int l_in = 0, r_in = 0;

 

 // loop to merge l and r using two pointer

 while (l_in + r_in < l.size() + r.size()) {

 if (l_in != l.size() && (r_in == r.size() || l[l_in] < r[r_in])) {

 ret.push_back(l[l_in]);

 l_in++;

 }

 else {

 ret.push_back(r[r_in]);

 r_in++;

 }

 }

 

 return ret;

}

 

// Function to merge all the arrays

vector<int> mergeArrays(vector<vector<int> > arr)

{

 // 2D-array to store the results of

 // a step temporarily

 vector<vector<int> > arr_s;

 

 // Loop to make pairs of arrays and merge them

 while (arr.size() != 1) {

 

 // To clear the data of previous steps

 arr_s.clear();

 

 for (int i = 0; i < arr.size(); i += 2) {

 if (i == arr.size() - 1)

 arr_s.push_back(arr[i]);

 

 else

 arr_s.push_back(mergeTwoArrays(arr[i],

 arr[i + 1]));

 }

 

 arr = arr_s;

 }

 

 // Returning the required output array

 return arr[0];

}

 

// Driver Code

int main()

{

 // Input arrays

 vector<vector<int> > arr{ { 3, 13 },

 { 8, 10, 11 },

 { 9, 15 } };

 // Merged sorted array

 vector<int> output = mergeArrays(arr);

 

 for (int i = 0; i < output.size(); i++)

 cout << output[i] << " ";

 

 return 0;

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

# Python3 program to merge K sorted

# arrays of different arrays 

 

# Function to merge two arrays 

def mergeTwoArrays(l, r): 

 

 # array to store the result 

 # after merging l and r 

 ret = [] 

 

 # variables to store the current 

 # pointers for l and r 

 l_in, r_in = 0, 0

 

 # loop to merge l and r using two pointer 

 while l_in + r_in < len(l) + len(r): 

 if (l_in != len(l) and

 (r_in == len(r) or

 l[l_in] < r[r_in])):

 

 ret.append(l[l_in]) 

 l_in += 1

 

 else:

 ret.append(r[r_in]) 

 r_in += 1

 

 return ret 

 

# Function to merge all the arrays 

def mergeArrays(arr): 

 

 # 2D-array to store the results 

 # of a step temporarily 

 arr_s = [] 

 

 # Loop to make pairs of arrays

 # and merge them 

 while len(arr) != 1: 

 

 # To clear the data of previous steps 

 arr_s[:] = []

 

 for i in range(0, len(arr), 2): 

 if i == len(arr) - 1:

 arr_s.append(arr[i]) 

 

 else:

 arr_s.append(mergeTwoArrays(arr[i], 

 arr[i + 1])) 

 

 arr = arr_s[:] 

 

 # Returning the required output array 

 return arr[0] 

 

# Driver Code 

if __name__ == "__main__":

 

 # Input arrays 

 arr = [[3, 13], 

 [8, 10, 11], 

 [9, 15]]

 

 # Merged sorted array 

 output = mergeArrays(arr) 

 

 for i in range(0, len(output)): 

 print(output[i], end = " ") 

 

# This code is contributed by Rituraj Jain  
  
---  
  
 __

 __

 **Output:**

    
    
    3 8 9 10 11 13 15
    

Note that there exist a better solution using heap (or priority queue). The
time complexity of the heap based solution is O(N Log k) where N is the total
number of elements in all K arrays.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

