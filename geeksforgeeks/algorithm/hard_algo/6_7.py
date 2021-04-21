Range Queries to Find number of sub-arrays with a given xor



Given an array **arr[]** of size **n** and **q** queries and an integer **k**.
Each query consists of an index range **[l, r]** and the task is to count the
number of pairs of indices **i** and **j** such that **l ≤ i ≤ j ≤ r**
(1-based indexing) and the xor of the elements **a[i], a[i + 1], …, a[j]** is
equal to **k**.

 **Examples:**

>  **Input:** arr[] = {1, 1, 1, 0, 2, 3}, q[] = {{2, 6}}, k = 3  
>  **Output:** 2  
> {1, 0, 2} and {3} are the required sub-arrays  
> within the index range [2, 6] (1-based indexing)
>
>  **Input:** arr[] = {1, 1, 1}, q[] = {{1, 3}, {1, 1}, {1, 2}}, k = 1  
>  **Output:**  
>  4  
> 1  
> 2

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** **This post** discusses to find sub-arrays with a given xor in
O(n) per query, so if q is large, our total run time complexity would be O(n *
q).  
Since we are given queries offline, The idea is to use’s Mo’s algorithm. We
divide the array into sqrt(n) blocks and sort the queries according to block
index, ties are broken with less r value first.  
We will keep an array xorr[], where xorr[i] stores the xor of the prefix of
array elements from 0 to i (index 0 based).  
We will also keep another array cnt[], where cnt[y] stores the number of
prefixes with xorr[i] = k.  
Suppose, we add an element at index x, let xorr[x] ^ k = y, now if cnt[y] is
greater than 0 then there exists prefixes with same xor, so we get y sub-
arrays with a given xor k that end at index x.

  

  

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <bits/stdc++.h>

using namespace std;

const long long bsz = 316;

long long res = 0;

 

// Query structure

struct Query {

 long long l, r, q_idx, block_idx;

 

 Query() {}

 Query(long long _l, long long _r, long long _q_idx)

 {

 l = _l, r = _r, q_idx = _q_idx, block_idx = _l / bsz;

 }

 

 // We use operator overloading

 // to sort the queries

 bool operator<(const Query& y) const

 {

 if (block_idx != y.block_idx)

 return block_idx < y.block_idx;

 return r < y.r;

 }

};

 

Query queries[1000005];

unordered_map<long long, long long> cnt;

long long n, q, k;

long long xorr[1000005];

 

// Function to add elements while traversing

void add(long long u)

{

 long long y = xorr[u] ^ k;

 

 // We find the number of prefixes with value y

 // that are contributing to the answer,

 // add them to the answer

 res = res + cnt[y];

 

 // If we are performing add operation, and suppose

 // we are at index u then count of xorr[u]

 // will increase by 1 as we are adding

 // the answer to the list

 cnt[xorr[u]]++;

}

 

// Function to delete elements while traversing

void del(long long u)

{

 // If we are performing delete operation and suppose

 // we are at index u then count of xorr[u]

 // will decrease by 1 as we are removing

 // the answer from the list

 cnt[xorr[u]]--;

 long long y = xorr[u] ^ k;

 

 // We find the number of prefixes with value y

 // that was initially contributing to the answer

 // now we do not need them, hence subtract it from answer

 res = res - cnt[y];

}

 

// Here we are performing Mo's algorithm

// if you have no idea of it then go through here:

// https:// www.geeksforgeeks.org/mos-algorithm-query-square-root-
decomposition-set-1-introduction/

void Mo()

{

 // first we sort the queries with block index, and ties are broken by less
r value .

 sort(queries + 1, queries + q + 1);

 vector<long long> ans(q + 1);

 long long l = 1, r = 0;

 res = 0;

 cnt[0] = 1;

 

 // Iterate each query and check whether

 // we have to move the left and right pointer

 // to left or right

 for (long long i = 1; i <= q; ++i) {

 

 // If current right pointer r is less than

 // the rightmost index of the present query,

 // increment r

 while (r < queries[i].r) {

 ++r;

 

 // While incrementing we are adding new numbers

 // to our list. Hence, we modify our answer

 // for each r using add() function

 add(r);

 }

 

 // If current left pointer is greater than the

 // left most index of the present query, decrement l

 while (l > queries[i].l) {

 l--;

 

 // While decrementing l, we are again adding

 // new numbers to our list, hence we modify

 // our answer using add() function

 add(l - 1);

 }

 

 // Similarly, if current left pointer is less than

 // the left most index of the present query, increment l

 while (l < queries[i].l) {

 

 // While incrementing we are deleting elements

 // as we are moving right, hence we modify our answer

 // using del() function

 del(l - 1);

 ++l;

 }

 

 // If current right pointer is greater than the rightmost

 // index of the present query, decrement it

 while (r > queries[i].r) {

 

 // While decrementing, modify the answer

 del(r);

 --r;

 }

 ans[queries[i].q_idx] = res;

 }

 for (long long i = 1; i <= q; ++i) {

 cout << ans[i] << endl;

 }

}

 

// Driver code

int main()

{

 q = 3, k = 3;

 vector<long long> v;

 v.push_back(0);

 v.push_back(1);

 v.push_back(1);

 v.push_back(1);

 v.push_back(0);

 v.push_back(2);

 v.push_back(3);

 

 // 1-based indexing

 n = v.size() + 1;

 

 xorr[1] = v[1];

 for (long long i = 2; i <= n; ++i)

 xorr[i] = xorr[i - 1] ^ v[i];

 

 // Queries

 queries[1] = Query(1, 6, 1);

 queries[2] = Query(2, 4, 2);

 queries[3] = Query(2, 6, 3);

 

 Mo();

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    0
    2
    

**Time Complexity:** O((n + q) * sqrt(n))

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

