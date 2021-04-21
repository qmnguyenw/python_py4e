Max count of unique ratio/fraction pairs in given arrays



Given two arrays **num[]** and **den[]** which denotes the numerator and
denominator respectively, the task is to find the count of the unique
fractions.  
 **Examples:**  

> **Input:** num[] = {1, 2, 3, 4, 5}, den[] = {2, 4, 6, 1, 11}  
> **Output:** 3  
> **Explanation:**  
> Simplest forms of the fractions  
> Frac[0] => ![\\frac{1}{2} ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-fd6173506651c8ed05047c80d3e98494_l3.png)
>
> Frac[1] =>![\\frac{2}{4} = \\frac{1}{2} ](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-00d27d1b1006bdbf818ec1ce66962c78_l3.png)
>
> Frac[2] =>![\\frac{3}{6} = \\frac{1}{2} ](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-97599159a6f5d5a9f144ba75a216f38b_l3.png)
>
> Frac[3] =>![\\frac{4}{1} ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-97c3ea14045e1348a7009a19180d87fb_l3.png)
>
>  
>
>
>  
>
>
> Frac[4] =>![\\frac{5}{11} ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-7c061b3f198f7a213342ac5df334f5a5_l3.png)
>
> Count of Unique Fractions => 3  
>  **Input:** num[] = {10, 20, 30, 50}, den[] = {10, 10, 10, 10}  
> **Output:** 4  
> **Explanation:**  
> Simplest forms of the fractions  
> Frac[0] =>![\\frac{10}{10} ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-b9988c66f4688d043797ff175a53627c_l3.png)
>
> Frac[1] =>![\\frac{20}{10} ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-b05c1c3380724013da6e85570dc9b294_l3.png)
>
> Frac[2] =>![\\frac{30}{10} ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-f13689b5e96f32fe026ae55a169f3870_l3.png)
>
> Frac[3] =>![\\frac{50}{10} ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-754fbf14f7f47615e182ed44bf555487_l3.png)
>
> Count of Unique Fractions => 4

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to use hash-map to find the unique fractions. To
store the fractions such that the duplicates are not there, we convert each
fraction to its lowest form.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find

// fractions in its lowest form 

 

#include <bits/stdc++.h> 

 

using namespace std; 

 

// Recursive function to 

// find gcd of a and b 

int gcd(int a, int b) 

{ 

 if (b == 0) 

 return a; 

 return gcd(b, a % b); 

} 

 

// Function to count the unique 

// fractios in the given array 

int countUniqueFractions(int num[], 

 int den[], int N){ 

 

 // Hash-map to store the fractions 

 // in its lowest form 

 map<pair<int, int>, int> mp; 

 

 // Loop to iterate over the 

 // fractions and store is lowest 

 // form in the hash-map 

 for (int i = 0; i < N; i++) { 

 int numer, denom; 

 

 // To find the Lowest form 

 numer = num[i] / gcd(num[i], den[i]); 

 denom = den[i] / gcd(num[i], den[i]); 

 mp[make_pair(numer, denom)] += 1; 

 } 

 

 return mp.size(); 

} 

 

// Driver code 

int main() 

{ 

 int N = 6; 

 

 // Numerator Array 

 int num[] = { 1, 40, 20, 5, 6, 7 }; 

 

 // Denominator Array 

 int den[] = { 10, 40, 2, 5, 12, 14 }; 

 

 cout << countUniqueFractions(num, den, N); 

 

 return 0; 

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

// Java implementation to find

// fractions in its lowest form 

import java.lang.*;

import java.util.*;

 

class GFG{

 

static class pair

{

 int x, y;

 pair(int x,int y)

 {

 this.x = x;

 this.y = y;

 }

 

 @Override

 public int hashCode() 

 { 

 return this.x; 

 } 

 

 @Override

 public boolean equals(Object obj) 

 { 

 

 // If both the object references are 

 // referring to the same object. 

 if(this == obj) 

 return true; 

 

 // It checks if the argument is of the 

 // type pair by comparing the classes 

 // of the passed argument and this object. 

 // if(!(obj instanceof pair)) return 

 // false; ---> avoid. 

 if(obj == null || 

 obj.getClass() != 

 this.getClass()) 

 return false; 

 

 // Type casting of the argument. 

 pair geek = (pair) obj; 

 

 // comparing the state of argument with 

 // the state of 'this' Object. 

 return (geek.x == this.x && 

 geek.y == this.y); 

 } 

}

 

// Recursive function to 

// find gcd of a and b

static int gcd(int a, int b)

{

 if (b == 0)

 return a;

 

 return gcd(b, a % b);

}

 

// Function to count the unique

// fractios in the given array

static int countUniqueFractions(int num[], 

 int den[], int N)

{

 

 // Hash-map to store the fractions

 // in its lowest form

 Map<pair, Integer> mp = new HashMap<>();

 

 // Loop to iterate over the 

 // fractions and store is lowest

 // form in the hash-map

 for(int i = 0; i < N; i++)

 {

 

 // To find the Lowest form

 int numer = num[i] / gcd(num[i], den[i]);

 int denom = den[i] / gcd(num[i], den[i]);

 pair tmp = new pair(numer, denom);

 mp.put(tmp, 1);

 }

 return mp.size();

}

 

// Driver Code

public static void main (String[] args)

{

 int N = 6;

 

 // Numerator Array

 int num[] = { 1, 40, 20, 5, 6, 7 };

 

 // Denominator Array

 int den[] = { 10, 40, 2, 5, 12, 14 };

 

 System.out.print(countUniqueFractions(num, den, N));

}

}

 

// This code is contributed by offbeat  
  
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

# Python3 implementation to find

# fractions in its lowest form 

from collections import defaultdict 

 

# Recursive function to 

# find gcd of a and b 

def gcd(a, b): 

 

 if (b == 0): 

 return a 

 return gcd(b, a % b) 

 

# Function to count the unique 

# fractios in the given array 

def countUniqueFractions(num, den, N): 

 

 # Hash-map to store the fractions 

 # in its lowest form 

 mp = defaultdict(int) 

 

 # Loop to iterate over the 

 # fractions and store is lowest 

 # form in the hash-map 

 for i in range(N): 

 

 # To find the Lowest form 

 numer = num[i] // gcd(num[i], den[i]) 

 denom = den[i] // gcd(num[i], den[i]) 

 mp[(numer, denom)] += 1

 

 return len(mp) 

 

# Driver code 

if __name__ == "__main__": 

 

 N = 6

 

 # Numerator Array 

 num = [ 1, 40, 20, 5, 6, 7 ] 

 

 # Denominator Array 

 den = [ 10, 40, 2, 5, 12, 14 ] 

 

 print(countUniqueFractions(num, den, N)) 

 

# This code is contributed by chitranayal   
  
---  
  
__

__

**Output:**

    
    
    4
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

