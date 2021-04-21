Inversion Count using Policy Based Data Structure



 **Pre-requisite:Policy based data structure**

Given an array **arr[]** , the task is to find the number of inversions for
each element of the array.

>  **Inversion Count:** for an array indicates – how far (or close) the array
> is from being sorted. If the array is already sorted then the inversion
> count is 0. If the array is sorted in the reverse order then the inversion
> count is the maximum.
>
> Formally, Number of indices ![i](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-aeba42a2346918ec8531199b1d5c206d_l3.png) and
> ![j](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-993d084f16613ab590616a3b93e4a1ed_l3.png) such that
> ![arr\[i\] > arr\[j\]](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-8772e852f4947238f9726ffbbba9a363_l3.png) and ![i <
> j](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-d068d6704cf3d26651275bd185b8a603_l3.png).

 **Examples:**

  

  

>  **Input:** {5, 2, 3, 2, 3, 8, 1}  
>  **Output:** {0, 1, 1, 2, 1, 0, 6}  
>  **Explanation:**  
>  Inversion count for each elements –  
> Element at index 0: There are no elements with less index than 0, which is
> greater than arr[0].  
> Element at index 1: There is one element with less index than 1, which is
> greater than 2. That is 5.  
> Element at index 2: There is one element with less index than 2, which is
> greater than 3. That is 5.  
> Element at index 3: There are two elements with less index than 3, which is
> greater than 2. That is 5, 3.  
> Element at index 4: There is one element with less index than 4, which is
> greater than 3. That is 5.  
> Element at index 5: There are no elements with less index than 5, which is
> greater than 8.  
> Element at index 6: There are six elements with less index than 6, which is
> greater than 1. That is 5, 2, 3, 2, 3
>
>  **Input:** arr[] = {3, 2, 1}  
>  **Output:** {0, 1, 2}

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * Create a policy based data structure of type pair.
  * Iterate the given array and perform the following steps –
    * Apply order_of_key({X, N+1}) for each element X where N is the size of array.  
 **Note:** order_of_key is nothing but lower_bound. Also, we used N+1 because
it is greater than all the indices in the array.

    * Let order_of_key comes out to be l, then the inversion count for current element will be equal to ![St.size\(\) - l](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-20548d9d04f719c358292eec993c32a9_l3.png) which is ultimately the count of elements smaller than X and came before X in the array.
    * Insert the current element X along with its index in the policy-based data structure St. The index is inserted along with each element for its unique identification in the set and to deal with duplicates.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// Inversion Count using Policy

// Based Data Structure

 

#include <bits/stdc++.h>

 

// Header files for policy based

// data structure which are

// to be included

#include <ext/pb_ds/assoc_container.hpp>

#include <ext/pb_ds/tree_policy.hpp>

 

using namespace __gnu_pbds;

using namespace std;

 

typedef tree<pair<int, int>, null_type,

 less<pair<int, int> >, rb_tree_tag,

 tree_order_statistics_node_update>

 new_data_set;

 

// Function to find the inversion count

// of the elements of the array

void inversionCount(int arr[], int n)

{

 int ans[n];

 

 // Making a new policy based data

 // structure which will

 // store pair<int, int>

 new_data_set St;

 

 // Loop to iterate over the elements

 // of the array

 for (int i = 0; i < n; i++) {

 

 // Now to find lower_bound of

 // the element X, we will use pair

 // as {x, n+1} to cover all the

 // elements and even the duplicates

 int cur = St.order_of_key({ arr[i],

 n + 1 });

 

 ans[i] = St.size() - cur;

 

 // Store element along with index

 St.insert({ arr[i], i });

 }

 

 for (int i = 0; i < n; i++) {

 cout << ans[i] << " ";

 }

 cout << "\n";

}

 

// Driver Code

int main()

{

 int arr[] = { 5, 2, 3, 2, 3, 8, 1 };

 int n = sizeof(arr) / sizeof(int);

 

 // Function Call

 inversionCount(arr, n);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    0 1 1 2 1 0 6
    

**Time Complexity:** ![O\(N*LogN\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-784d82c3904891c429822f99c0edc1fc_l3.png)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

