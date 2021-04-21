Real time optimized KMP Algorithm for Pattern Searching



In the article, we have already discussed the KMP algorithm for pattern
searching. In this article, a real-time optimized KMP algorithm is discussed.

From the previous article, it is known that KMP(a.k.a. Knuth-Morris-Pratt)
algorithm preprocesses the pattern P and constructs a failure function F(also
called as lps[]) to store the length of the longest suffix of the sub-pattern
P[1..l], which is also a prefix of P, for l = 0 to m-1. Note that the sub-
pattern starts at index 1 because a suffix can be the string itself. After a
mismatched occurred at index P[j], we update j to F[j-1].

The original KMP Algorithm has the runtime complexity of O(M + N) and
auxiliary space O(M), where N is the size of the input text and M is the size
of the pattern. Preprocessing step costs O(M) time. It is hard to achieve
runtime complexity better than that but we are still able to eliminate some
inefficient shifts.

 **Inefficiencies of the original KMP algorithm:** Consider the following case
by using the original KMP algorithm:

>  **Input:** T = “cabababcababaca”, P = “ababaca”  
>  **Output:** Found at index 8
>
>  
>
>
>  
>

The longest proper prefix or lps[] for the above test case is {0, 0, 1, 2, 3,
0, 1}. Lets assume that the red color represents a mismatch occurs, green
color represents the checking we skipped. Therefore, the searching process
according to the original KMP algorithm occurs as follows:  
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200520123449/KMP-
Algorithm-Page-1.png)

One thing which can be noticed is that in the third, fourth, and fifth
matching, the mismatch occurs at the same location, T[7]. If we can skip the
fourth and fifth matching, then the original KMP algorithm can further be
optimised to answer the real-time queries.

 **Real-time Optimization:** The term **real-time** in this case can be
interpreted as checking each character in the text T at most once. Our goal in
this case is to shift the pattern properly (just like KMP algorithm does), but
no need to check the mismatched character again. That is, for the same above
example, the optimized KMP algorithm should work in the following way:  
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200520123730/KMP-
Algorithm-Page-2.png)

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** One way to achieve the goal is to modify the preprocessing
process.

  * Let **K** be the size of the letters of the pattern **P**. We will construct a failure table to contain **K** failure functions(i.e. lps[]).
  * Each failure function in the failure table is mapped to a character(key in the failure table) in the alphabet of the pattern P.
  * Recall that the original failure function **F[l]** (or lps[]) stores the length of the longest suffix of P[1..l], which is also a prefix of **P** , for l = 0 to m-1, where m is the size of the pattern.
  * If a mismatched occurs at **T[i]** and **P[j]** , the new value of j would be updated to **F[j-1]** and the counter ‘i’ would be unchanged.
  * In our new failure table **FT[][]** , if a failure function F’ is mapped with a character c, **F'[l]** should store the length of the longest suffix of P[1..l] + c (‘+’ represents appending), which is also a prefix of P, for l = 0 to m-1.
  * The intuition is to make proper shifts but also depending on the mismatched character. Here the character c, which is also a key in the failure table, is our “guess” about the mismatched character in the text T.
  * That is, if the mismatched character is c, how should we shift the pattern properly? Since we are constructing the failure table in the preprocessing step, we have to make enough guesses about the mismatched character.
  * Hence, the number of lps[]’s in the failure table equals to the size of the alphabet of the pattern, and each value, the failure function, should be different with respect to the key, a character in **P**.
  * Assume we have already constructed the desired failure table. Let **FT[][]** be the failure table, **T** be the text, **P** be the pattern.
  * Then, in the matching process, if a mismatch occurs at **T[i]** and **P[j]** (i.e. T[i] != P[j]):
    1. If **T[i]** is a character in **P** , **j** will be updated to **FT[T[i]][j-1]** , ‘ **i** ‘ will be updated to ‘ **i + 1** ‘. We are doing this since we are guaranteed that **T[i]** is matched or skipped.
    2. If T[i] is not a character, ‘j’ will be updated to 0, ‘i’ will be updated to ‘i + 1’.
  * Note that if a mismatching does not occur, the behaviour is exactly the same as the original KMP algorithm.

 **Constructing Failure Table:**

  * To construct the failure table FT[][], we will need the failure function F(or lps[]) from the original KMP algorithm.
  * Since F[l] tells us the length of the longest suffix of the sub-pattern P[1..l], which is also a prefix of P, the values stored in the failure table is one step beyond it.
  * That is, for any key t in the failure table FT[][], the values stored in FT[t] is a failure function that satisfies for the character ‘t’ and FT[t][l] stores the length of the longest suffix of a sub-pattern P[1..l] + t(‘+’ means append), which is also a prefix of P, for l from 0 to m-1.
  * F[l] has already guaranteed that P[0..F[l]-1] is the longest suffix of the sub-pattern P[1..l], so we will need to check if P[F[l]] is t.
  * If true, then we can assign FT[t][l] to be F[l] + 1, as we are guaranteed that P[0..F[l]] is the longest suffix of the sub-pattern P[1..l] + t.
  * If false, that indicates P[F[l]] is not t. That is, we fail the matching at character P[F[l]] with the character t, but P[0..F[l]-1] matches a suffix of P[1..l].
  * By borrowing the idea from KMP algorithm, just like how we compute the failure function in original KMP algorithm, if the mismatch occurs at P[F[l]] with mismatched character t, we would like to update the next matching starting at FT[t][F[l]-1].
  * That is, we use the idea of the KMP algorithm to compute the failure table. Notice that F[l] – 1 is always less than l, so when we are computing FT[t][l], FT[t][F[l] – 1] is ready for us already.
  * One special case is that if F[l] is 0 and P[F[l]] is not t, F[l] – 1 has a value of -1, in this case, we will update FT[t][l] to 0. (i.e. there is no suffix of P[1..l] + t exists such that it is a prefix of P.)
  * As a conclusion of failure table construction, when we are computing FT[t][l], for any key t and l from 0 to m-1, we will check:
    
    
    If P[F[l]] is t,
      if yes:
        FT[t][l] <- F[l] + 1;
      if no: 
        check if F[l] is 0,
          if yes:
            FT[t][l] <- 0;
          if no:
            FT[t][l] <- FT[t][F[t] - 1];
    

Here are the desired outputs of the above example, outputs include the failure
table for better illustration.

 **Examples:**

>  **Input:** T = “cabababcababaca”, P = “ababaca”  
>  **Output:** Failure Table:  
> Key Value  
> ‘a’ [1 1 1 3 1 1 1]  
> ‘b’ [0 0 2 0 4 0 2]  
> ‘c’ [0 0 0 0 0 0 0]  
> Found pattern at index 8

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to implement a

// real time optimized KMP

// algorithm for pattern searching

 

#include <iostream>

#include <set>

#include <string>

#include <unordered_map>

 

using std::string;

using std::unordered_map;

using std::set;

using std::cout;

 

// Function to print

// an array of length len

void printArr(int* F, int len,

 char name)

{

 cout << '(' << name << ')'

 << "contain: [";

 

 // Loop to iterate through

 // and print the array

 for (int i = 0; i < len; i++) {

 cout << F[i] << " ";

 }

 cout << "]\n";

}

 

// Function to print a table.

// len is the length of each array

// in the map.

void printTable(

 unordered_map<char, int*>& FT,

 int len)

{

 cout << "Failure Table: {\n";

 

 // Iterating through the table

 // and printing it

 for (auto& pair : FT) {

 

 printArr(pair.second,

 len, pair.first);

 }

 cout << "}\n";

}

 

// Function to construct

// the failure function

// corresponding to the pattern

void constructFailureFunction(

 string& P, int* F)

{

 

 // P is the pattern,

 // F is the FailureFunction

 // assume F has length m,

 // where m is the size of P

 

 int len = P.size();

 

 // F[0] must have the value 0

 F[0] = 0;

 

 // The index, we are parsing P[1..j]

 int j = 1;

 int l = 0;

 

 // Loop to iterate through the

 // pattern

 while (j < len) {

 

 // Computing the failure function or

 // lps[] similar to KMP Algorithm

 if (P[j] == P[l]) {

 l++;

 F[j] = l;

 j++;

 }

 else if (l > 0) {

 l = F[l - 1];

 }

 else {

 F[j] = 0;

 j++;

 }

 }

}

 

// Function to construct the failure table.

// P is the pattern, F is the original

// failure function. The table is stored in

// FT[][]

void constructFailureTable(

 string& P,

 set<char>& pattern_alphabet,

 int* F,

 unordered_map<char, int*>& FT)

{

 int len = P.size();

 

 // T is the char where we mismatched

 for (char t : pattern_alphabet) {

 

 // Allocate an array

 FT[t] = new int[len];

 int l = 0;

 while (l < len) {

 if (P[F[l]] == t)

 

 // Old failure function gives

 // a good shifting

 FT[t][l] = F[l] + 1;

 else {

 

 // Move to the next char if

 // the entry in the failure

 // function is 0

 if (F[l] == 0)

 FT[t][l] = 0;

 

 // Fill the table if F[l] > 0

 else

 FT[t][l] = FT[t][F[l] - 1];

 }

 l++;

 }

 }

}

 

// Function to implement the realtime

// optimized KMP algorithm for

// pattern searching. T is the text

// we are searching on and

// P is the pattern we are searching for

void KMP(string& T, string& P,

 set<char>& pattern_alphabet)

{

 

 // Size of the pattern

 int m = P.size();

 

 // Size of the text

 int n = T.size();

 

 // Initialize the Failure Function

 int F[m];

 

 // Constructing the failure function

 // using KMP algorithm

 constructFailureFunction(P, F);

 printArr(F, m, 'F');

 

 unordered_map<char, int*> FT;

 

 // Construct the failure table and

 // store it in FT[][]

 constructFailureTable(

 P,

 pattern_alphabet,

 F, FT);

 printTable(FT, m);

 

 // The starting index will be when

 // the first match occurs

 int found_index = -1;

 

 // Variable to iterate over the

 // indices in Text T

 int i = 0;

 

 // Variable to iterate over the

 // indices in Pattern P

 int j = 0;

 

 // Loop to iterate over the text

 while (i < n) {

 if (P[j] == T[i]) {

 

 // Matched the last character in P

 if (j == m - 1) {

 found_index = i - m + 1;

 break;

 }

 else {

 i++;

 j++;

 }

 }

 else {

 if (j > 0) {

 

 // T[i] is not in P's alphabet

 if (FT.find(T[i]) == FT.end())

 

 // Begin a new

 // matching process

 j = 0;

 

 else

 j = FT[T[i]][j - 1];

 

 // Update 'j' to be the length of

 // the longest suffix of P[1..j]

 // which is also a prefix of P

 

 i++;

 }

 else

 i++;

 }

 }

 

 // Printing the index at which

 // the pattern is found

 if (found_index != -1)

 cout << "Found at index "

 << found_index << '\n';

 else

 cout << "Not Found \n";

 

 for (char t : pattern_alphabet)

 

 // Deallocate the arrays in FT

 delete[] FT[t];

 

 return;

}

 

// Driver code

int main()

{

 string T = "cabababcababaca";

 string P = "ababaca";

 set<char> pattern_alphabet

 = { 'a', 'b', 'c' };

 KMP(T, P, pattern_alphabet);

}  
  
---  
  
 __

 __

 **Output:**

    
    
    (F)contain: [0 0 1 2 3 0 1 ]
    Failure Table: {
    (c)contain: [0 0 0 0 0 0 0 ]
    (a)contain: [1 1 1 3 1 1 1 ]
    (b)contain: [0 0 2 0 4 0 2 ]
    }
    Found at index 8
    

**Note:** The above source code will find the **first** occurrence of the
pattern. With slight modification, it can be used to find all the occurrences.

 **Time Complexity:**

    * The new preprocessing step has a running time complexity of O(![|\\Sigma_P| \\cdot M\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-0cbc225d19f88e1619c2ea2bef8bf27f_l3.png), where ![ \\Sigma_P](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-eb805d96ef379742b04d1764da9489ef_l3.png) is the alphabet set of pattern P, M is the size of P.
    * The whole modified KMP algorithm has a running time complexity of O(![|\\Sigma_P| \\cdot M + N](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-fc28748c959d0d612dd90a3eb66489d1_l3.png)). The auxiliary space usage of O(![|\\Sigma_P| \\cdot M](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-23c52da1e2bfcdaa1b24976de5818b6b_l3.png)).
    * The running time and space usage look like “worse” than the original KMP algorithm. However, if we are searching for the same pattern in multiple texts or the alphabet set of the pattern is small, as the preprocessing step only needs to be done once and each character in the text will be compared at most once (real-time). So, it is more efficient than the original KMP algorithm and good in practice.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

