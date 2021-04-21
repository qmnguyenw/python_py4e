Sort an array of strings based on the frequency of good words in them



Given a set of **product reviews** ( **R** ) by different customers and a
string **S** containing good words separated by a **_** , the task is to sort
the reviews in **decreasing** order of their goodness value.  
 **Goodness Value** is defined by the number of good words present in that
review.

 **Examples:**

>  **Input:** S = “geeks_for_geeks_is_great”,  
> R = {“geeks_are_geeks”, “geeks_dont_lose”, “geeks_for_geeks_is_love”}  
>  **Output:**  
>  geeks for geeks is love  
> geeks are geeks  
> geeks dont lose
>
>  **Input:** S = “cool_wifi_ice”,  
> R = {“water_is_cool”, “cold_ice_drink”, “cool_wifi_speed”}  
>  **Output:**  
>  cool wifi speed  
> water is cool  
> cold ice drink

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Insert all the good words in an unordered_set and then
iterate through each word of each sentence of the reviews array and keep a
count of the good words by checking if this word is present in that set of
good words. We then use a stable sorting algorithm and sort the array R
according to the count of good words in each review present in R. It’s clear
that the time complexity of this method is **greater than O(N * NlogN)**.

  

  

 **Efficient approach:** Make a Trie of all the good words and check the
goodness of each word in a review using the trie.

  1. Insert all the good words in a trie.
  2. For each review, calculate the number of good words in it by checking whether a given word exists in the trie or not.

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

#define F first

#define S second

#define MAX 26

 

// Comparator function for sorting

bool cmp(const pair<int, int>& a, const pair<int,
int>& b)

{

 

 // Compare the number of good words

 if (a.F == b.F)

 return a.S < b.S;

 return a.F > b.F;

}

 

// Structure of s Trie node

struct node {

 bool exist;

 node* arr[MAX];

 node(bool bul = false)

 {

 exist = bul;

 for (int i = 0; i < MAX; i++)

 arr[i] = NULL;

 }

};

 

// Function to add a string to the trie

void add(string s, node* trie)

{

 // Add a node to the trie

 int n = s.size();

 for (int i = 0; i < n; i++) {

 

 // If trie doesn't already contain

 // the current node then create one

 if (trie->arr[s[i] - 'a'] == NULL)

 trie->arr[s[i] - 'a'] = new node();

 

 trie = trie->arr[s[i] - 'a'];

 }

 trie->exist = true;

 return;

}

 

// Function that returns true if

// the trie contains the string s

bool search(string s, node* trie)

{

 // Search for a node in the trie

 for (int i = 0; i < s.size(); i++) {

 if (trie->arr[s[i] - 'a'] == NULL)

 return false;

 

 trie = trie->arr[s[i] - 'a'];

 }

 return trie->exist;

}

 

// Function to replace every '_' with a

// white space in the given string

void convert(string& str)

{

 // Convert '_' to spaces

 for (int i = 0; i < str.size(); i++)

 if (str[i] == '_')

 str[i] = ' ';

 return;

}

 

// Function to sort the array based on good words

void sortArr(string good, vector<string>& review)

{

 

 // Extract all the good words which

 // are '_' separated

 convert(good);

 node* trie = new node();

 string word;

 stringstream ss;

 ss << good;

 

 // Building the entire trie by stringstreaming

 // the 'good words' string

 while (ss >> word)

 add(word, trie);

 int k, n = review.size();

 

 // To store the number of good words

 // and the string index pairs

 vector<pair<int, int> > rating(n);

 for (int i = 0; i < n; i++) {

 convert(review[i]);

 ss.clear();

 ss << review[i];

 k = 0;

 while (ss >> word) {

 

 // If this word is present in the trie

 // then increment its count

 if (search(word, trie))

 k++;

 }

 

 // Store the number of good words in the

 // current string paired with its

 // index in the original array

 rating[i].F = k;

 rating[i].S = i;

 }

 

 // Using comparator function to

 // sort the array as required

 sort(rating.begin(), rating.end(), cmp);

 

 // Print the sorted array

 for (int i = 0; i < n; i++)

 cout << review[rating[i].S] << "\n";

}

 

// Driver code

int main()

{

 

 // String containing good words

 string S = "geeks_for_geeks_is_great";

 

 // Vector of strings to be sorted

 vector<string> R = { "geeks_are_geeks", "geeks_dont_lose",

 "geeks_for_geeks_is_love" };

 

 // Sort the array based on the given conditions

 sortArr(S, R);

}  
  
---  
  
 __

 __

 **Output:**

    
    
    geeks for geeks is love
    geeks are geeks
    geeks dont lose
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

