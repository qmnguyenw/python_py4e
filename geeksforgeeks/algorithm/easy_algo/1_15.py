Kth most frequent Character in a given String



Given a string **str** and an integer **K** , the task is to find the K-th
most frequent character in the string. If there are multiple characters that
can account as K-th most frequent character then, print any one of them.

 **Examples:**

>  **Input:** str = “GeeksforGeeks”, K = 3  
>  **Output:** f  
>  **Explanation:**  
>  K = 3, here ‘e’ appears 4 times  
> & ‘g’, ‘k’, ‘s’ appears 2 times  
> & ‘o’, ‘f’, ‘r’ appears 1 time.  
> Any output from ‘o’ (or) ‘f’ (or) ‘r’ will be correct.
>
>  **Input:** str = “trichotillomania”, K = 2  
>  **Output:** l

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach**

  

  

  * The idea is to Use the Characters as key in Hashmap and store their occurrences in the string.
  * Sort the Hashmap and find the K-th character.

Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find kth most frequent

// character in a string

#include <bits/stdc++.h>

using namespace std;

 

// Used for sorting by frequency.

bool sortByVal(const pair<char, int>& a,

 const pair<char, int>& b)

{

 return a.second > b.second;

}

 

// function to sort elements by frequency

char sortByFreq(string str, int k)

{

 // Store frequencies of characters

 unordered_map<char, int> m;

 for (int i = 0; i < str.length(); ++i)

 m[str[i]]++;

 

 // Copy map to vector

 vector<pair<char, int> > v;

 copy(m.begin(), m.end(), back_inserter(v));

 

 // Sort the element of array by frequency

 sort(v.begin(), v.end(), sortByVal);

 

 // Find k-th most frequent item. Please note

 // that we need to consider only distinct

 int count = 0;

 for (int i = 0; i < v.size(); i++) {

 

 // Increment count only if frequency is

 // not same as previous

 if (i == 0 || v[i].second != v[i - 1].second)

 count++;

 

 if (count == k)

 return v[i].first;

 }

 

 return -1;

}

 

// Driver program

int main()

{

 string str = "geeksforgeeks";

 int k = 3;

 cout << sortByFreq(str, k);

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    r
    

**Time Complexity:** _O(NlogN)_ Please note that this is an upper bound on
time complexity. If we consider alphabet size as constant (for example lower
case English alphabet size is 26), we can say time complexity as O(N). The
vector size would never be more that alphabet size.  
 **Auxiliary Space:** _O(N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

