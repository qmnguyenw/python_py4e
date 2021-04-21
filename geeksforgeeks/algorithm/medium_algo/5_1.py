Counting Inversions using Ordered Set and GNU C++ PBDS



Given an array **arr[]** of N integers. The task is to find the number of
inversion. Two elements **arr[i]** and **arr[j]** form an inversion if
**arr[i] > arr[j] and i < j**.

 **Examples**

>  **Input:** arr[] = {8, 4, 2, 1}  
>  **Output:** 6  
>  **Explanation:**  
>  Given array has six inversions:
>
>   * (8, 4): arr[0] > arr[1] and 0 < 1
>   * (8, 2): arr[0] > arr[2] and 0 < 2
>   * (8, 1): arr[0] > arr[3] and 0 < 3
>   * (4, 2): arr[1] > arr[2] and 1 < 2
>   * (4, 1): arr[1] > arr[3] and 1 < 3
>   * (2, 1): arr[2] > arr[3] and 2 < 3
>

>
>  **Input:** arr[] = {2, 3}  
>  **Output:** 0  
>  **Explanation:**  
>  There is no such pair exists such that arr[i] > arr[j] and i < j.

We have already discussed below approaches:

  

  

  * Count Inversions in an array | Set 1 (Using Merge Sort)
  * Count inversions in an array | Set 2 (Using Self-Balancing BST)
  * Counting Inversions using Set in C++ STL
  * Count inversions in an array | Set 3 (Using BIT)

In this post, we will be discussing an approach using Ordered Set and GNU C++
PBDS.

 **Approach:**  
We will be using the function **order_of_key(K)** which returns number of
elements strictly smaller than K in **log N** time.

  1. Insert the first element of the array in the Ordered_Set.
  2. For all the remaining element in **arr[]** do the following:
    * Insert the current element in the Ordered_Set.
    * Find the number of element strictly less than **current element + 1** in Ordered_Set using function **order_of_key(arr[i]+1)**.
    * The difference between size of **Ordered_Set** and order_of_key(current_element + 1) will given the inversion count for the current element.

 **For Example:**

    
    
    arr[] = {8, 4, 2, 1}
    Ordered_Set S = {8}
    For remaining element in arr[]:
    At index 1, the element is  4
    S = {4, 8}
    key = order_of_key(5) = 1
    The difference between size of S and key gives the total 
    number of inversion count for that current element.
    inversion_count = S.size() - key =  2 - 1 = 1
    Inversion Pairs are: (8, 4)
    
    At index 2, the element is  2
    S = {2, 4, 8}
    key = order_of_key(3) = 1
    inversion_count = S.size() - key =  3 - 1 = 2
    Inversion Pairs are: (8, 2) and (4, 2)
    
    At index 3, the element is 1
    S = {1, 2, 4, 8}
    key = order_of_key(2) = 1
    inversion_count = S.size() - key =  4 - 1 = 3
    Inversion Pairs are: (8, 1), (4, 1) and (2, 1)
    
    Total inversion count = 1 + 2 + 3 = 6
    

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

// Ordered set in GNU C++ based

// approach for inversion count

#include <bits/stdc++.h>

#include <ext/pb_ds/assoc_container.hpp>

#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;

using namespace std;

 

// Ordered Set Tree

typedef tree<int, null_type, less_equal<int>,

 rb_tree_tag,

 tree_order_statistics_node_update>

 ordered_set;

 

// Returns inversion count in

// arr[0..n-1]

int getInvCount(int arr[], int n)

{

 int key;

 // Intialise the ordered_set

 ordered_set set1;

 

 // Insert the first

 // element in set

 set1.insert(arr[0]);

 

 // Intialise inversion

 // count to zero

 int invcount = 0;

 

 // Finding the inversion

 // count for current element

 for (int i = 1; i < n; i++) {

 set1.insert(arr[i]);

 

 // Number of elements strictly

 // less than arr[i]+1

 key = set1.order_of_key(arr[i] + 1);

 

 // Difference between set size

 // and key will give the

 // inversion count

 invcount += set1.size() - key;

 }

 return invcount;

}

 

// Driver's Code

int main()

{

 int arr[] = { 8, 4, 2, 1 };

 int n = sizeof(arr) / sizeof(int);

 

 // Function call to count

 // inversion

 cout << getInvCount(arr, n);

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

**Time Complexity:** O(Nlog N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

