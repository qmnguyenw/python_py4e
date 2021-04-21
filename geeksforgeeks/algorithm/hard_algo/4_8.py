Find four elements that sum to a given value | Two-Pointer approach



Given an array **arr** of integers of size **N** and a **target** number, the
task is to find all unique quadruplets in it, whose sum is equal to the target
number.

 **Examples:**

>  **Input:** arr[] = {4, 1, 2, -1, 1, -3], target = 1  
>  **Output:** [[-3, -1, 1, 4], [-3, 1, 1, 2]]  
>  **Explanation:**  
>  Both the quadruplets sum equals to target.
>
>  **Input:** arr[] = {2, 0, -1, 1, -2, 2}, target = 2  
>  **Output:** [[-2, 0, 2, 2], [-1, 0, 1, 2]]

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Two-Pointers approach:**  
This problem follows the Two Pointers pattern and shares similarities with
Triplet Sum to Zero.

  

  

We can follow a similar approach to iterate through the array, taking one
number at a time. At every step during the iteration, we will search for the
quadruplets similar to Triplet Sum to Zero whose sum is equal to the given
target.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find four

// elements that sum to a given value

 

#include <bits/stdc++.h>

using namespace std;

 

class QuadrupleSumToTarget {

 

public:

 // Function to find quadruplets

 static vector<vector<int> >

 searchQuadruplets(

 vector<int>& arr,

 int target)

 {

 sort(arr.begin(), arr.end());

 vector<vector<int> > quadruplets;

 

 for (int i = 0; i < arr.size() - 3; i++) {

 if (i > 0 && arr[i] == arr[i - 1]) {

 

 // Skip same element

 // to avoid duplicate

 continue;

 }

 

 for (int j = i + 1; j < arr.size() - 2; j++) {

 if (j > i + 1 && arr[j] == arr[j - 1]) {

 

 // Skip same element

 // to avoid duplicate quad

 continue;

 }

 searchPairs(

 arr, target,

 i, j, quadruplets);

 }

 }

 return quadruplets;

 }

 

private:

 // Function to search Quadruplets

 static void

 searchPairs(

 const vector<int>& arr,

 int targetSum, int first,

 int second,

 vector<vector<int> >& quadruplets)

 {

 int left = second + 1;

 int right = arr.size() - 1;

 

 while (left < right) {

 int sum

 = arr[first]

 + arr[second]

 + arr[left]

 + arr[right];

 

 if (sum == targetSum) {

 

 // Found the quadruplet

 quadruplets

 .push_back(

 { arr[first], arr[second],

 arr[left],

 arr[right] });

 left++;

 right--;

 

 // Skip same element to avoid

 // duplicate quadruplets

 while (left < right

 && arr[left]

 == arr[left - 1]) {

 left++;

 }

 

 // Skip same element to avoid

 // duplicate quadruplets

 while (left < right

 && arr[right]

 == arr[right + 1]) {

 right--;

 }

 }

 

 // We need a pair

 // with a bigger sum

 else if (sum < targetSum) {

 left++;

 }

 

 // We need a pair

 // with a smaller sum

 else {

 right--;

 }

 }

 }

};

 

void printQuad(

 vector<int>& vec, int target)

{

 

 // Function call

 auto result

 = QuadrupleSumToTarget::

 searchQuadruplets(

 vec, target);

 

 // Print Quadruples

 for (int j = 0; j < result.size(); j++) {

 vector<int> vec = result[j];

 if (j == 0)

 cout << "[";

 

 for (int i = 0; i < vec.size(); i++) {

 

 if (i == 0)

 cout << "[";

 cout << vec[i];

 if (i != vec.size() - 1)

 cout << ", ";

 else

 cout << "]";

 }

 

 if (j != result.size() - 1)

 cout << ", ";

 else

 cout << "]";

 }

}

 

// Driver code

int main(int argc, char* argv[])

{

 vector<int> vec

 = { 4, 1, 2,

 -1, 1, -3 };

 int target = 1;

 

 printQuad(vec, target);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    [[-3, -1, 1, 4], [-3, 1, 1, 2]]
    

**Time complexity:** Sorting the array will take **O(N*logN)**. Overall
**searchQuadruplets()** will take **O(N * logN + N^3)** , which is
asymptotically equivalent to **O(N^3)**.

 **Auxiliary Space complexity:** The auxiliary space complexity of the above
algorithm will be **O(N)** which is required for sorting.

 **Similar Articles:**

  1. Find four elements that sum to a given value | Set 1 (n^3 solution)
  2. Find four elements that sum to a given value | Set 2 ( O(n^2Logn) Solution)
  3. Find four elements that sum to a given value | Set 3 (Hashmap)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

