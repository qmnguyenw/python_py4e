Minimum number of prefix reversals to sort permutation of first N numbers



Given N numbers which have a permutation of first N numbers. In a single
operation, any prefix can be reversed. The task is to find the minimum number
of such operations such that the numbers in the array are in increasing order.

 **Examples:**

    
    
    **Input** : a[] = {3, 1, 2} 
    **Output** : 2 
    Step1: Reverse the complete array a, a[] = {2, 1, 3} 
    Step2: Reverse the prefix(0-1) in s, a[] = {1, 2, 3} 
    
    **Input** : a[] = {1, 2, 4, 3} 
    **Output** : 3 
    Step1: Reverse the complete array a, a[] = {3, 4, 2, 1} 
    Step2: Reverse the prefix(0-1) in s, a[] = {4, 3, 2, 1} 
    Step3: Reverse the complete array a, a[] = {1, 2, 3, 4} 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The approach to solve this problem is to use BFS.

  * Encode the given numbers in a string. Sort the array and encode it into a string _destination_.
  * Then do a BFS from the initial permutation. Each time, check all permutations induced by reversing a prefix of current permutation.
  * If it is not visited, put it into the queue with the count of reversals done.
  * When the permutation of the encoded string is same as the destination string, return the numbers of reversals required to reach here.
  * That is, all permutations of strings are done and the minimal of those is returned as the answer.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find

// minimum number of prefix reversals

// to sort permutation of first N numbers

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the minimum prefix reversals

int minimumPrefixReversals(int a[], int n)

{

 string start = "";

 string destination = "", t, r;

 for (int i = 0; i < n; i++) {

 // converts the number to a character

 // and add to string

 start += to_string(a[i]);

 }

 sort(a, a + n);

 for (int i = 0; i < n; i++) {

 destination += to_string(a[i]);

 }

 

 // Queue to store the pairs

 // of string and number of reversals

 queue<pair<string, int> > qu;

 pair<string, int> p;

 

 // Initially push the original string

 qu.push(make_pair(start, 0));

 

 // if original string is the destination string

 if (start == destination) {

 return 0;

 }

 

 // iterate till queue is empty

 while (!qu.empty()) {

 

 // pair at the top

 p = qu.front();

 

 // string

 t = p.first;

 

 // pop the top-most element

 qu.pop();

 

 // peform prefix reversals for all index and push

 // in the queue and check for the minimal

 for (int j = 2; j <= n; j++) {

 r = t;

 

 // reverse the string till prefix j

 reverse(r.begin(), r.begin() + j);

 

 // if after reversing the string from first i index

 // it is the destination

 if (r == destination) {

 return p.second + 1;

 }

 

 // push the number of reversals for string r

 qu.push(make_pair(r, p.second + 1));

 }

 }

}

 

// Driver Code

int main()

{

 

 int a[] = { 1, 2, 4, 3 };

 int n = sizeof(a) / sizeof(a[0]);

 

 // Calling function

 cout << minimumPrefixReversals(a, n);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    3
    

