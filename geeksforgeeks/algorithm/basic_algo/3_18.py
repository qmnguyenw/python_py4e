Minimum number of items to be delivered



Given N buckets, each containing A[i] items. Given K tours within which all of
the items are needed to be delivered. It is allowed to take items from only
one bucket in 1 tour. The task is to tell the minimum number of items needed
to be delivered per tour so that all of the items can be delivered within K
tours.  
 **Conditions : K >= N**  
 **Examples** :

    
    
    **Input** : 
    N = 5
    A[] = { 1, 3, 5, 7, 9 }
    K = 10
    **Output** : 3
    By delivering 3 items at a time, 
    Number of tours required for bucket 1 = 1
    Number of tours required for bucket 2 = 1
    Number of tours required for bucket 3 = 2
    Number of tours required for bucket 4 = 3
    Number of tours required for bucket 5 = 3
    Total number of tours = 10
    
    **Input** :
    N = 10
    A = 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
    k = 50
    **Output** : 9
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach** : It is needed to find the minimum number of items per delivery.
So, the idea is to iterate from 1 to the maximum value of items in a bucket
and calculate the number of tours required for each bucket and find the total
number of tours for complete delivery. The first such value with tours less
than or equals K gives the required number.  
Below is the implementation of the above idea:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

//C++ program to find the minimum numbers of tours required

#include <bits/stdc++.h>

 

using namespace std;

int getMin(int N,int A[],int k)

{

 //Iterating through each possible 

 // value of minimum Items

 int maximum=0,tours=0;

 

 for(int i=0;i<N;i++)

 maximum=max(maximum,A[i]);

 

 for(int i=1;i<maximum+1;i++)

 {

 tours=0;

 for(int j=0;j<N;j++)

 {

 if(A[j]%i==0)//perfecctly Divisible 

 {

 tours+=A[j]/i;

 }else{

 // Not Perfectly Divisible means required

 // tours are Floor Division + 1

 tours += floor(A[j]/i) + 1;

 }

 }

 if(tours<=k)

 {

 // Return First Feasible Value found,

 // since it is also the minimum

 return i;

 }

 }

 

 return -1;

}

//Driver code

int main() 

{

 int a[]={1, 4, 9, 16, 25, 36, 49, 64, 81, 100};

 

 int n=sizeof(a)/sizeof(a[0]);

 

 int k=50;

 

 if(getMin(n,a,k)==-1)

 cout<<"Not Possible";

 else

 cout<<getMin(n,a,k);

 

}

//This code is contributed by Mohit kumar 29  
  
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

// Java program to find the minimum numbers of tours required

import java.util.*;

class solution

{

 

static int getMin(int N,int A[],int k)

{

 //Iterating through each possible 

// value of minimum Items

int maximum=0,tours=0;

 

for(int i=0;i<N;i++)

 maximum=Math.max(maximum,A[i]);

 

for(int i=1;i<maximum+1;i++)

{

 tours=0;

 for(int j=0;j<N;j++)

 {

 if(A[j]%i==0)//perfecctly Divisible 

 {

 tours+=A[j]/i;

 }else{

 // Not Perfectly Divisible means required

 // tours are Floor Division + 1

 tours += Math.floor(A[j]/i) + 1;

 }

 }

 if(tours<=k)

 {

 // Return First Feasible Value found,

 // since it is also the minimum

 return i;

 }

}

 

return -1;

}

//Driver code

public static void main(String args[]) 

{

int a[]={1, 4, 9, 16, 25, 36, 49, 64,
81, 100};

 

int n=a.length;

 

int k=50;

 

if(getMin(n,a,k)==-1)

System.out.println("Not Possible");

else

System.out.println(getMin(n,a,k));

 

}

}

//This code is contributed by 

// Surendra_Gangwar  
  
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

# Python3 program to find minimum numbers of

# tours required

 

def getMin(N, A, k):

 

 # Iterating through each possible 

 # value of minimum Items

 for i in range(1, max(A)+1):

 tours = 0

 for j in range(0, len(A)):

 if(A[j]% i == 0):# Perfectly Divisible

 tours += A[j]/i

 

 else:

 # Not Perfectly Divisible means required

 # tours are Floor Division + 1

 tours += A[j]//i + 1

 

 if(tours <= k):

 # Return First Feasible Value found,

 # since it is also the minimum

 return i 

 return "Not Possible"

 

# Driver Code

N = 10

A = [1, 4, 9, 16, 25, 36, 49, 64, 81,
100]

k = 50

print(getMin(N, A, k))  
  
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

// C# program to find the minimum

// numbers of tours required

using System;

 

class GFG

{

 

static int getMin(int N, int [] A, int k)

{

 // Iterating through each possible 

 // value of minimum Items

 int maximum = 0,tours = 0;

 

 for(int i = 0; i < N; i++)

 maximum = Math.Max(maximum, A[i]);

 

 for(int i = 1; i < maximum + 1; i++)

 {

 tours = 0;

 for(int j = 0; j < N; j++)

 {

 if(A[j] % i == 0)// perfecctly Divisible 

 {

 tours += A[j] /i;

 }

 else

 {

 // Not Perfectly Divisible means required

 // tours are Floor Division + 1

 tours += (int)Math.Floor(A[j] / (i * 1.0)) + 1;

 }

 }

 if(tours <= k)

 {

 // Return First Feasible Value found,

 // since it is also the minimum

 return i;

 }

 }

 

 return -1;

}

 

// Driver code

public static void Main() 

{

 int []a = {1, 4, 9, 16, 25, 36, 49, 64, 81, 100};

 

 int n = 10;

 

 int k = 50;

 

 if(getMin(n, a, k) == -1)

 Console.WriteLine("Not Possible");

 else

 Console.WriteLine(getMin(n, a, k));

}

}

 

// This code is contributed by 

// Mohit kumar  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP program to find the minimum number

// of tours required

 

function getMin($N, $A, $k)

{

 

 // Iterating through each possible 

 // value of minimum Items

 $maximum = 0;

 $tours = 0;

 

 for($i = 0; $i < $N; $i++)

 $maximum = max($maximum, $A[$i]);

 

 for($i = 1; $i < $maximum + 1; $i++)

 {

 $tours = 0;

 for($j = 0; $j < $N; $j++)

 {

 if($A[$j] % $i == 0) // perfectly Divisible 

 {

 $tours += $A[$j] / $i;

 }

 else

 {

 // Not Perfectly Divisible means required

 // tours are Floor Division + 1

 $tours += floor($A[$j] / $i) + 1;

 }

 }

 

 if($tours <= $k)

 {

 // Return First Feasible Value found,

 // since it is also the minimum

 return $i;

 }

 }

 

 return -1;

}

 

// Driver code

$a = array(1, 4, 9, 16, 25, 36,

 49, 64, 81, 100);

 

$n = sizeof($a);

 

$k = 50;

 

if(getMin($n, $a, $k) == -1)

 echo "Not Possible";

else

 echo getMin($n, $a, $k);

 

// This code is contributed by ihritik

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    9
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

