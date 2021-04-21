Program to check if a date is valid or not



Given a date, check if it is valid or not. It may be assumed that the given
date is in range from 01/01/1800 to 31/12/9999.

 **Examples :**

    
    
    Input : d = 10, m = 12, y = 2000
    Output : Yes
    The given date 10/12/2000 is valid
    
    Input  : d = 30, m = 2, y = 2000
    Output : No
    The given date 30/2/2000 is invalid. The
    February month cannot have 30 as day.

Recommended: Please solve it on “ _ ** _PRACTICE_**_ ” first, before moving on
to the solution.

The idea is simple. We need to handle following things.  
1) y, m and d are in allowed range.  
2) Days in February are in allowed range and leap year is handled.  
3) Days in 30 day months are handled.

Below is the implementation to check if a given year is valid or not.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to check if

// given date is valid or not.

#include<iostream>

using namespace std;

const int MAX_VALID_YR = 9999;

const int MIN_VALID_YR = 1800;

// Returns true if

// given year is valid.

bool isLeap(int year)

{

// Return true if year

// is a multiple pf 4 and

// not multiple of 100.

// OR year is multiple of 400.

return (((year % 4 == 0) &&

 (year % 100 != 0)) ||

 (year % 400 == 0));

}

// Returns true if given

// year is valid or not.

bool isValidDate(int d, int m, int y)

{

 // If year, month and day

 // are not in given range

 if (y > MAX_VALID_YR ||

 y < MIN_VALID_YR)

 return false;

 if (m < 1 || m > 12)

 return false;

 if (d < 1 || d > 31)

 return false;

 // Handle February month

 // with leap year

 if (m == 2)

 {

 if (isLeap(y))

 return (d <= 29);

 else

 return (d <= 28);

 }

 // Months of April, June,

 // Sept and Nov must have

 // number of days less than

 // or equal to 30.

 if (m == 4 || m == 6 ||

 m == 9 || m == 11)

 return (d <= 30);

 return true;

}

// Driver code

int main(void)

{

isValidDate(10, 12, 2000)? cout << "Yes\n" :

 cout << "No\n";

isValidDate(31, 11, 2000)? cout << "Yes\n" :

 cout << "No\n";

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

// Java program to check if

// given date is valid or not.

import java.io.*;

class GFG

{

 static int MAX_VALID_YR = 9999;

 static int MIN_VALID_YR = 1800;

 // Returns true if

 // given year is valid.

 static boolean isLeap(int year)

 {

 // Return true if year is

 // a multiple of 4 and not

 // multiple of 100.

 // OR year is multiple of 400.

 return (((year % 4 == 0) &&

 (year % 100 != 0)) ||

 (year % 400 == 0));

 }

 // Returns true if given

 // year is valid or not.

 static boolean isValidDate(int d,

 int m,

 int y)

 {

 // If year, month and day

 // are not in given range

 if (y > MAX_VALID_YR ||

 y < MIN_VALID_YR)

 return false;

 if (m < 1 || m > 12)

 return false;

 if (d < 1 || d > 31)

 return false;

 // Handle February month

 // with leap year

 if (m == 2)

 {

 if (isLeap(y))

 return (d <= 29);

 else

 return (d <= 28);

 }

 // Months of April, June,

 // Sept and Nov must have

 // number of days less than

 // or equal to 30.

 if (m == 4 || m == 6 ||

 m == 9 || m == 11)

 return (d <= 30);

 return true;

 }

 // Driver code

 public static void main(String args[])

 {

 if (isValidDate(10, 12, 2000))

 System.out.println("Yes");

 else

 System.out.println("No");

 if (isValidDate(31, 11, 2000))

 System.out.println("Yes");

 else

 System.out.println("No");

 }

}

// This code is contributed

// by Nikita Tiwari.  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to check

# if a date is valid or not

import datetime

def date_validation(day, month, year):

 

 isValidDate = True

 

 try :

 datetime.datetime(int(year),

 int(month), int(day))

 

 except ValueError :

 isValidDate = False

 

 if(isValidDate) :

 print ("Yes")

 else :

 print ("No")

date_validation(10,12,2000)

date_validation(31,11,2000)

# This code is contributed by ajay0007  
  
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

// C# program to check if

// given date is valid or not.

using System;

class GFG

{

 const int MAX_VALID_YR = 9999;

 const int MIN_VALID_YR = 1800;

 // Returns true if

 // given year is valid.

 static bool isLeap(int year)

 {

 

 // Return true if year is a

 // multiple of 4 and not

 // multiple of 100. OR year

 // is multiple of 400.

 return (((year % 4 == 0) &&

 (year % 100 != 0)) ||

 (year % 400 == 0));

 }

 // Returns true if given

 // year is valid or not.

 static bool isValidDate(int d,

 int m,

 int y)

 {

 

 // If year, month and day

 // are not in given range

 if (y > MAX_VALID_YR ||

 y < MIN_VALID_YR)

 return false;

 if (m < 1 || m > 12)

 return false;

 if (d < 1 || d > 31)

 return false;

 // Handle February month

 // with leap year

 if (m == 2)

 {

 if (isLeap(y))

 return (d <= 29);

 else

 return (d <= 28);

 }

 // Months of April, June,

 // Sept and Nov must have

 // number of days less than

 // or equal to 30.

 if (m == 4 || m == 6 ||

 m == 9 || m == 11)

 return (d <= 30);

 return true;

 }

 // Driver code

 public static void Main()

 {

 

 if (isValidDate(10, 12, 2000))

 Console.WriteLine("Yes");

 else

 Console.WriteLine("No");

 if (isValidDate(31, 11, 2000))

 Console.WriteLine("Yes");

 else

 Console.WriteLine("No");

 }

}

// This code is contributed

// by Anant Agarwal.  
  
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

// PHP program to check if

// given date is valid or not.

// Returns true if

// given year is valid.

function isLeap($year)

{

// Return true if year is

// a multiple of 4 and

// not multiple of 100.

// OR year is multiple of 400.

return ((($year % 4 == 0) &&

 ($year % 100 != 0)) ||

 ($year % 400 == 0));

}

// Returns true if given

// year is valid or not.

function isValidDate($d, $m, $y)

{

 $MAX_VALID_YR = 9999;

 $MIN_VALID_YR = 1800;

 // If year, month and day

 // are not in given range

 if ($y > $MAX_VALID_YR ||

 $y < $MIN_VALID_YR)

 return false;

 if ($m < 1 || $m > 12)

 return false;

 if ($d < 1 || $d > 31)

 return false;

 // Handle February month

 // with leap year

 if ($m == 2)

 {

 if (isLeap($y))

 return ($d <= 29);

 else

 return ($d <= 28);

 }

 // Months of April, June,

 // Sept and Nov must have

 // number of days less than

 // or equal to 30.

 if ($m == 4 || $m == 6 ||

 $m == 9 || $m == 11)

 return ($d <= 30);

 return true;

}

// Driver code

{

if(isValidDate(10, 12, 2000))

echo "Yes\n" ;

else

echo "No\n";

if(isValidDate(31, 11, 2000))

 echo "Yes\n" ;

else

echo "No\n";

 

}

// This code is contributed

// by nitin mittal.

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

// Javascript program to check if

// given date is valid or not.

const MAX_VALID_YR = 9999;

const MIN_VALID_YR = 1800;

// Returns true if

// given year is valid.

function isLeap(year)

{

 

 // Return true if year

 // is a multiple pf 4 and

 // not multiple of 100.

 // OR year is multiple of 400.

 return (((year % 4 == 0) &&

 (year % 100 != 0)) ||

 (year % 400 == 0));

}

// Returns true if given

// year is valid or not.

function isValidDate(d, m, y)

{

 

 // If year, month and day

 // are not in given range

 if (y > MAX_VALID_YR ||

 y < MIN_VALID_YR)

 return false;

 

 if (m < 1 || m > 12)

 return false;

 if (d < 1 || d > 31)

 return false;

 // Handle February month

 // with leap year

 if (m == 2)

 {

 if (isLeap(y))

 return (d <= 29);

 else

 return (d <= 28);

 }

 // Months of April, June,

 // Sept and Nov must have

 // number of days less than

 // or equal to 30.

 if (m == 4 || m == 6 ||

 m == 9 || m == 11)

 return (d <= 30);

 return true;

}

// Driver code

isValidDate(10, 12, 2000) ? document.write("Yes<br>") :

 document.write("No<br>");

isValidDate(31, 11, 2000) ? document.write("Yes<br>") :

 document.write("No<br>");

 

// This code is contributed by souravmahato348

</script>  
  
---  
  
 __

 __

 **Output :**

    
    
    Yes
    No

This article is contributed by **RAHUL NITKKR**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
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

