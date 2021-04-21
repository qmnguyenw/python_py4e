Minimum number of page turns to get to a desired page



Given a book of **N** pages, the task is to calculate the minimum number of
page turns to get to a give desired page **K**. We can either start turning
pages from the front side of the book (i.e from page 1) or from the back side
of the book (i.e page number N). Each page has two sides, front and back,
except the first page, which has only back side and the last page which may
only have back side depending on the number of pages of the book.  
**Examples :**  

    
    
    **Input :** N = 6 and K = 2.
    **Output :** 1.
    From front, (1) -> (2, 3), page turned = 1.
    From back, (6) -> (4, 5) -> (2,3), page turned = 2.
    So, Minimum number of page turned = 1.
    
    **Input :** N = 5 and K = 4.
    **Output :** 1.
    From front, (1) -> (2, 3) -> (4,5), page turned = 2.
    From back, (4, 5) page turned = 1. From back, it is 2nd page, since 4 is on other side of page 5 and page 5 is the first one from back
    So, Minimum number of page turned = 1.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

The idea is to calculate distance of the desired page from the front and from
the back of the book, minimum of this is the required answer.  
Now, Consider there is page 0, which is front of the first page. And if N is
even, consider there is page N+1, which is back of the last page, so total
number of pages are N+1.  
To calculate the distance,  
1\. If K is even, front distance = (K – 0)/2 and back distance = (N – 1 –
K)/2.  
2\. If K is odd, front distance = (K – 1)/2 and back distance = (N – K)/2.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find minimum number of page

// turns to reach a page

#include<bits/stdc++.h>

using namespace std;

int minTurn(int n, int k)

{

 // Considering back of last page.

 if (n%2 == 0)

 n++;

 // Calculating Distance from front and

 // back of the book and return the min

 return min((k + 1)/2, (n - k + 1)/2);

}

// Driven Program

int main()

{

 int n = 6, k = 2;

 cout << minTurn(n,k) << endl;

 return 0;

}

// This code is modified by naveenkonda  
  
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

// Java program to find minimum

// number of page turns to

// reach a page

import java.io.*;

public class GFG

{

// Function to calculate

// minimum number of page

// turns required

static int minTurn(int n, int k)

{

 

 // Considering back of last page.

 if (n % 2 == 0)

 n++;

 // Calculating Distance from front and

 // back of the book and return the min

 Math.min((k + 1) / 2, (n - k + 1) / 2);

}

 // Driver Code

 static public void main (String[] args)

 {

 int n = 6, k = 2;

 System.out.println(minTurn(n, k));

 }

}

// This code is contributed by vt_m.  
  
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

# Python3 program to find minimum number

# of page turns to reach a page

def minTurn(n, k):

 

 # Considering back of last page.

 if (n % 2 == 0):

 n += 1

 // Calculating Distance from front and

 // back of the book and return the min

 return min((k + 1) / 2, (n - k + 1) / 2)

# Driver Code

if __name__ == '__main__':

 n = 6

 k = 2

 print(int(minTurn(n, k)))

 

# This code is contributed by

# Surendra_Gangwar  
  
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

// C# program to find minimum

// number of page turns to

// reach a page

using System;

public class GFG

{

// Function to calculate

// minimum number of page

// turns required

static int minTurn(int n, int k)

{

 

 // Considering back of last page.

 if (n % 2 == 0)

 n++; 

 // Calculating Distance from front and

 // back of the book and return the min

 return Math.Min((k + 1) / 2,

 (n - k + 1) / 2);

}

 // Driver Code

 static public void Main (String[] args)

 {

 int n = 6, k = 2;

 Console.WriteLine(minTurn(n, k));

 }

}

// This code is contributed by vt_m.  
  
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

// PHP program to find minimum number

// of page turns to reach a page

function minTurn($n, $k)

{

 // Considering back of last page.

 if ($n % 2 == 0)

 $n++;

 // Calculating Distance from front and

 // back of the book and return the min

 return min(($k + 1) / 2,

 ($n - $k + 1) / 2);

}

// Driver Code

$n = 6; $k = 2;

echo minTurn($n, $k) ;

// This code is contributed by nitin mittal.

?>  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// Javascript program to find minimum

// number of page turns to

// reach a page

// Function to calculate

// minimum number of page

// turns required

function minTurn(n, k)

{

 

 // Considering back of last page.

 if (n % 2 == 0)

 n++;

 

 // Calculating Distance from front and

 // back of the book and return the min

 let x = Math.min((k + 1) / 2, (n - k + 1) / 2);

 return Math.floor(x);

}

 

// Driver code 

 let n = 6, k = 2;

 document.write(minTurn(n, k));

 

</script>  
  
---  
  
 __

 __

 **Output :**  

    
    
    1

 **Time Complexity :** O(1)  
This article is contributed by **Anuj Chauhan(anuj0503)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

