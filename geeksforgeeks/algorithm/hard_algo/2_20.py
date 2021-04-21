Number of steps to sort the array by changing order of three elements in each
step



Given an array **arr[]** of size **N** consisting of unique elements in the
range **[0, N-1]** , the task is to find **K** which is the number of steps
required to sort the given array by selecting three distinct elements and
rearranging them. And also, print the indices selected in those K steps in K
lines.

> For example, in the array {5, 4, 3, 2, 1, 0}, one possible way to sort the
> given array by selecting three distinct elements is to select the numbers
> {2, 1, 0} and sort them as {0, 1, 2} thereby making the array {5, 4, 3, 0,
> 1, 2}. Similarly, the remaining operations are performed and the indices
> selected ({3, 4, 5} in the above case) are printed in separate lines.

 **Examples:**

>  **Input:** arr[] = {0, 5, 4, 3, 2, 1}  
>  **Output:**  
>  2  
> 1 2 5  
> 2 5 4  
>  **Explanation:**  
>  The above array can be sorted in 2 steps:  
> Step I: We change the order of elements at indices 1, 2, 5 then the array
> becomes {0, 1, 5, 3, 2, 4}.  
> Step II: We again change the order of elements at the indices 2, 5, 4 then
> the array becomes {0, 1, 2, 3, 4, 5} which is sorted.
>
>  **Input:** arr[] = {0, 3, 1, 6, 5, 2, 4}  
>  **Output:** -1  
>  **Explanation:**  
>  The above array cannot be sorted in any number of steps.  
> Suppose we choose indices 1, 3, 2 then the array becomes {0, 1, 6, 3, 5, 2,
> 4}  
> After that, we choose indices 2, 6, 4 then the array becomes {0, 1, 5, 3, 4,
> 2, 6}.  
> Now only two elements are left unsorted so we cannot choose 3 elements so
> the above array cannot be sorted. We can try with any order of indices and
> we will always be left with 2 elements unsorted.
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to first count the elements which are not sorted
and insert them in an unordered set. If count is 0 then we don’t need any
number of steps for sorting the array so we print 0 and exit. Else, we first
erase all the elements from the set for which i = A[A[i]] then we perform the
following operation till the set becomes empty:

  * We select all the possible combination of indices(if available) such that minimum two elements will get sorted.
  * Now, change the order of the elements and erase them from the set if i = A[i].
  * Then, we are left with only those elements such that i = A[A[i]] and the count of those must be a multiple of 4 otherwise it is not possible to sort the elements.
  * Then, we choose any two pair and perform changing the order of elements two times. Then all the four chosen elements will get sorted.
  * We store all the indices which are involved in the changing of orders of elements in a vector and print it as the answer.

Let’s understand the above approach with an example. Let the array arr[] = {0,
8, 9, 10, 1, 7, 12, 4, 3, 2, 6, 5, 11}. Then:

  * Initially, the set will contain all the 12 elements and there are no elements such that i = A[A[i]].
  * Now, {11, 5, 7} are chosen and the order of the elements are changed. Then, arr[] = {0, 8, 9, 10, 1, 5, 12, 7, 3, 2, 6, 4, 11}.
  * Now, {11, 4, 1} are chosen and the order of the elements are changed. Then, arr[] = {0, 1, 9, 10, 4, 5, 12, 7, 3, 2, 6, 8, 11}.
  * Now, {11, 8, 3} are chosen and the order of the elements are changed. Then, arr[] = {0, 1, 9, 3, 4, 5, 12, 7, 8, 2, 6, 10, 11}.
  * Now, {11, 10, 6} are chosen and the order of the elements are changed. Then, arr[] = {0, 1, 9, 3, 4, 5, 6, 7, 8, 2, 10, 12, 11}.
  * After the above step, we are left with two pairs of unsorted elements such that i = A[A[i]].
  * Finally, {2, 11, 9} and {11, 9, 5} are chosen and reordered. Then, arr[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} which is sorted.

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to sort the array

// by changing the order of

// three elements

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to change the order of

// the elements having a temporary

// vector and the required indices

// as the arguments

void cngorder(vector<int>& v, int i,

 int j, int k)

{

 int temp = v[k];

 v[k] = v[j];

 v[j] = v[i];

 v[i] = temp;

}

 

// Function to sort the elements having

// the given array and its size.

void sortbyorder3(vector<int>& A, int n)

{

 

 // Flag to check whether the sorting

 // is possible or not

 bool flag = 0;

 

 int count = 0;

 

 // Set that will contains unsorted

 // elements

 unordered_set<int> s;

 

 // Iterating through the elements

 for (int i = 0; i < n; i++) {

 

 // Inserting the required elements

 // in the set

 if (i != A[i])

 count++, s.insert(i);

 }

 

 // When the given array is

 // already sorted

 if (count == 0)

 cout << "0" << endl;

 

 else {

 

 // Vector that will contain

 // the answer

 vector<vector<int> > ans;

 

 // Temporary vector to store

 // the indices

 vector<int> vv;

 

 int x, y, z;

 

 count = 0;

 

 // Loop that will execute till the

 // set becomes empty

 while (!s.empty()) {

 auto it = s.begin();

 int i = *it;

 

 // Check for the condition

 if (i == A[A[i]]) {

 s.erase(i);

 s.erase(A[i]);

 continue;

 }

 

 // Case when the minimum two

 // elements will get sorted

 else {

 x = A[i], y = A[A[i]], z = A[A[A[i]]];

 vv.push_back(x), vv.push_back(y),

 vv.push_back(z);

 

 // Changing the order of elements

 cngorder(A, x, y, z);

 

 // Pushing the indices to the

 // answer vector

 ans.push_back(vv);

 

 // If the third element also

 // gets sorted

 if (vv[0] == A[vv[0]])

 s.erase(vv[0]);

 

 // Erasing the two sorted elements

 // from the set

 s.erase(vv[1]), s.erase(vv[2]);

 vv.clear();

 }

 }

 

 count = 0;

 

 // The count of the remaining

 // unsorted elements

 for (int i = 0; i < n; i++) {

 if (i != A[i])

 count++;

 }

 

 // If the count of the left

 // unsorted elements is not

 // a multiple of 4, then

 // sorting is not possible

 if (count % 4 != 0)

 flag = 1;

 

 // Only the elements such that

 // i = A[A[i]] are left

 // for sorting

 else {

 

 // Indices of any one element

 // from the two pairs that

 // will be sorted in 2 steps

 int i1 = -1, i2 = -1;

 for (int i = 0; i < n; i++) {

 

 // Index of any element of

 // the pair

 if (A[i] != i && i1 == -1) {

 i1 = i;

 }

 

 // When we find the second

 // pair and the index of

 // any one element is stored

 else if (A[i] != i && i1 != -1

 && i2 == -1) {

 if (i1 == A[i])

 continue;

 else

 i2 = i;

 }

 

 // When we got both the pair

 // of elements

 if (i1 != -1 && i2 != -1) {

 

 // Remaining two indices

 // of the elements

 int i3 = A[i1], i4 = A[i2];

 

 // The first order of indices

 vv.push_back(i1),

 vv.push_back(i2),

 vv.push_back(A[i1]);

 

 // Pushing the indices to the

 // answer vector

 ans.push_back(vv);

 vv.clear();

 

 // The second order of indices

 vv.push_back(i2),

 vv.push_back(A[i1]),

 vv.push_back(A[i2]);

 

 // Pushing the indices to the

 // answer vector

 ans.push_back(vv);

 vv.clear();

 

 // Changing the order of the

 // first combination of

 // the indices

 cngorder(A, i1, i2, i3);

 

 // Changing the order of the

 // second combination of

 // the indices after which all

 // the 4 elements will be sorted

 cngorder(A, i2, i3, i4);

 

 i1 = -1, i2 = -1;

 }

 }

 }

 

 // If the flag value is 1

 // the sorting is not possible

 if (flag == 1)

 cout << "-1" << endl;

 

 else {

 

 // Printing the required number

 // of steps

 cout << ans.size() << endl;

 

 // Printing the indices involved

 // in the shifting

 for (int i = 0; i < ans.size(); i++) {

 cout << ans[i][0]

 << " " << ans[i][1]

 << " " << ans[i][2]

 << endl;

 }

 }

 }

}

 

// Driver code

int main()

{

 

 int n;

 vector<int> A{ 0, 8, 9, 10, 1, 7, 12,

 4, 3, 2, 6, 5, 11 };

 n = A.size();

 

 // Calling the sorting function

 sortbyorder3(A, n);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    11 5 7
    11 4 1
    11 8 3
    11 10 6
    2 11 9
    11 9 12
    

**Time Complexity:** _O(N)_ , where N is the size of the array.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

