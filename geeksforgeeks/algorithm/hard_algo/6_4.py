Longest prefix in a string with highest frequency



Given a string, find a prefix with the highest frequency. If two prefixes have
the same frequency then consider the one with maximum length.

 **Examples:**

    
    
    **Input :** str = "abc" 
    **Output :** abc
    Each prefix has same frequency(one) and the 
    prefix with maximum length is "abc".
    
    **Input :** str = "abcab"
    **Output :** ab
    Both prefix "a" and "ab" occur two times and the 
    prefix with maximum length is "ab".
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The idea is to observe that every prefix of the given string will contain the
first character of the string in it and the first character alone is also a
prefix of the given string. So the prefix with the highest occurrence is the
first character. The task now remains to maximize the length of the highest
frequency prefix.

 **Approach :**

  1. Take a vector which will store the indices of the first element of the string.
  2. If the first element appeared only once, then the longest prefix will be the whole string.
  3. Otherwise, loop till the second appearance of the first element and check one letter after every stored index.
  4. If there is no mismatch we move forward otherwise we stop.

Below is the implementation of the above approach:  

## C++

  

  

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to find Longest prefix string with the 

// highest frequency

void prefix(string str)

{

 int k = 1, j;

 int n = str.length();

 

 vector<int> g;

 int flag = 0;

 

 // storing all indices where first element is found

 for (int i = 1; i < n; i++) {

 if (str[i] == str[0]) {

 g.push_back(i);

 flag = 1;

 }

 }

 

 // if the first letter in the string does not occur 

 // again then answer will be the whole string

 if (flag == 0) {

 cout << str << endl;

 }

 else {

 int len = g.size();

 

 // loop till second appearance of the first element

 while (k < g[0]) {

 

 int cnt = 0;

 for (j = 0; j < len; j++) {

 

 // check one letter after every stored index

 if (str[g[j] + k] == str[k]) {

 cnt++;

 }

 }

 

 // If there is no mismatch we move forward

 if (cnt == len) {

 k++;

 }

 // otherwise we stop

 else {

 break;

 }

 }

 

 for (int i = 0; i < k; i++) {

 cout << str[i];

 }

 

 cout << endl;

 }

}

 

// Driver Code

int main()

{

 string str = "abcab";

 prefix(str);

 

 return 0;

}  
  
---  
  
 __

 __

