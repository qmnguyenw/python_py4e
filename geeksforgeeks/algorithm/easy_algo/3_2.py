Count of lexicographically smaller characters on right



Given a string consisting of only lowercase English alphabets. The task is to
count the total number of alphabetically smaller characters on the right side
of characters at each index.

 **Examples:**

>  **Input:** str = “edcba”  
>  **Output:** 4 3 2 1 0  
>  **Explanation:**  
>  Number of characters on the right side of index 0 which is smaller than  
>  **e** are **dcba** = 4  
> Number of characters on the right side of index 1 which is smaller than  
>  **d** are **cba** = 3  
> Number of characters on the right side of index 2 which is smaller than  
>  **c** are **ba** = 2  
> Number of characters on the right side of index 3 which is smaller than  
>  **b** are **a** = 1  
> Number of characters on the right side of index 4 which is smaller than  
>  **a** are **‘\0’** = 0  
>  **Input:** str = “eaaa”  
>  **Output:** 3 0 0 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:**  
The idea is to traverse all the characters on the right side of each index of
string one by one and print the count of characters which are alphabetically
smaller.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

 

// function to count the smaller

// characters at the right of index i

void countSmaller(string str)

{

 

 // store the length of string

 int n = str.length();

 for (int i = 0; i < n; i++) {

 

 // for each index initialize

 // count as zero

 int cnt = 0;

 for (int j = i + 1; j < n; j++) {

 

 // increment the count if

 // characters are smaller

 // than at ith index

 if (str[j] < str[i]) {

 cnt += 1;

 }

 }

 

 // print the count of characters

 // smaller than the index i

 cout << cnt << " ";

 }

}

 

// Driver code

int main()

{

 // input string

 string str = "edcba";

 countSmaller(str);

}  
  
---  
  
 __

 __

## Java

 __

 __  
 __

 __

 __  
 __  
 __

class GFG

{

 

// function to count the smaller

// characters at the right of index i

static void countSmaller(String str)

{

 

 // store the length of String

 int n = str.length();

 for (int i = 0; i < n; i++) 

 {

 

 // for each index initialize

 // count as zero

 int cnt = 0;

 for (int j = i + 1; j < n; j++)

 {

 

 // increment the count if

 // characters are smaller

 // than at ith index

 if (str.charAt(j) < str.charAt(i))

 {

 cnt += 1;

 }

 }

 

 // print the count of characters

 // smaller than the index i

 System.out.print(cnt+ " ");

 }

}

 

// Driver code

public static void main(String[] args)

{

 // input String

 String str = "edcba";

 countSmaller(str);

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function to count the smaller

# characters at the right of index i

def countSmaller(str):

 

 # store the length of String

 n = len(str);

 for i in range(n):

 

 # for each index initialize

 # count as zero

 cnt = 0;

 for j in range(i + 1, n):

 

 # increment the count if

 # characters are smaller

 # than at ith index

 if (str[j] < str[i]):

 cnt += 1;

 

 # print the count of characters

 # smaller than the index i

 print(cnt, end =" ");

 

# Driver code

if __name__ == '__main__':

 

 # input String

 str = "edcba";

 countSmaller(str);

 

# This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

## C#

 __

 __  
 __

 __

 __  
 __  
 __

using System;

 

class GFG

{

 

// function to count the smaller

// characters at the right of index i

static void countSmaller(String str)

{

 

 // store the length of String

 int n = str.Length;

 for (int i = 0; i < n; i++) 

 {

 

 // for each index initialize

 // count as zero

 int cnt = 0;

 for (int j = i + 1; j < n; j++)

 {

 

 // increment the count if

 // characters are smaller

 // than at ith index

 if (str[j] < str[i])

 {

 cnt += 1;

 }

 }

 

 // print the count of characters

 // smaller than the index i

 Console.Write(cnt+ " ");

 }

}

 

// Driver code

public static void Main(String[] args)

{

 // input String

 String str = "edcba";

 countSmaller(str);

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    4 3 2 1 0
    

