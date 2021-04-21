Sort an Array of dates in ascending order using Custom Comparator



Given an array **arr[]** of **N** dates in the form of “DD-MM-YYYY”, the task
is to sort these dates in ascending order.

 **Examples:**

> **Input:** arr[] = { “25-08-1996”, “03-08-1970”, “09-04-1994” }  
> **Output:**  
> 03-08-1970  
> 09-04-1994  
> 25-08-1996
>
>  **Input:** arr[] = { “03-08-1970”, “09-04-2020”, “19-04-2019″”}  
> **Output:**  
> 03-08-1970  
> 19-04-2019  
> 09-04-2020

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  

  

  * Create a Custom comparator function that compares two dates as below: 
    * First compare the year of the two elements. The element with greater year will come after the other element.
    * If the year of both the dates is same then compare the months. The element with a greater month will come after the other element.
    * If the month of both the dates is same then compare the dates. The element with greater date will come after the other element.
  * Then sort the array using the defined custom comparator. In C++, it is done as: 

> sort(initial position, ending position, comparator)  
>

  * Print the modified array.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to sort the

// array of dates in the form of

// "DD-MM-YYYY" using custom comparator

#include <bits/stdc++.h>

using namespace std;

// Comparator to sort the array of dates

int myCompare(string date1,

 string date2)

{

 string day1 = date1.substr(0, 2);

 string month1 = date1.substr(3, 2);

 string year1 = date1.substr(6, 4);

 string day2 = date2.substr(0, 2);

 string month2 = date2.substr(3, 2);

 string year2 = date2.substr(6, 4);

 // Condition to check the year

 if (year1 < year2)

 return 1;

 if (year1 > year2)

 return 0;

 // Condition to check the month

 if (month1 < month2)

 return 1;

 if (month1 > month2)

 return 0;

 // Condition to check the day

 if (day1 < day2)

 return 1;

 if (day1 > day2)

 return 0;

}

// Function that prints the

// dates in ascensding order

void printDatesAscending(

 vector<string> arr)

{

 // Sort the dates using library

 // sort function with custom Comparator

 sort(arr.begin(), arr.end(), myCompare);

 // Loop to print the dates

 for (int i = 0; i < arr.size(); i++)

 cout << arr[i] << "\n";

}

// Driver Code

int main()

{

 vector<string> arr;

 arr.push_back("25-08-1996");

 arr.push_back("03-08-1970");

 arr.push_back("09-04-1994");

 arr.push_back("29-08-1996");

 arr.push_back("14-02-1972");

 printDatesAscending(arr);

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

// Java implementation to sort the

// array of dates in the form of

// "DD-MM-YYYY" using custom comparator

import java.util.*;

import java.lang.*;

class GFG{

 

// Function that prints the

// dates in ascensding order

static void printDatesAscending(ArrayList<String> arr)

{

 

 // Sort the dates using library

 // sort function with custom Comparator

 Collections.sort(arr,new Comparator<>()

 {

 public int compare(String date1, String date2)

 {

 String day1 = date1.substring(0, 2);

 String month1 = date1.substring(3, 5);

 String year1 = date1.substring(6);

 

 String day2 = date2.substring(0, 2);

 String month2 = date2.substring(3, 5);

 String year2 = date2.substring(6);

 

 // Condition to check the year

 if (year2.compareTo(year1) > 0)

 return -1;

 else if (year2.compareTo(year1) < 0)

 return 1;

 

 // Condition to check the month 

 else if (month2.compareTo(month1) > 0)

 return -1;

 else if (month2.compareTo(month1) < 0)

 return 1;

 

 // Condition to check the day

 else if (day2.compareTo(day1) > 0)

 return -1;

 else

 return 1;

 }

 });

 

 // Loop to print the dates

 for(int i = 0; i < arr.size(); i++)

 System.out.println(arr.get(i));

} 

// Driver code

public static void main(String[] args)

{

 ArrayList<String> arr = new ArrayList<>();

 arr.add("25-08-1996");

 arr.add("03-08-1970");

 arr.add("09-04-1994");

 arr.add("29-08-1996");

 arr.add("14-02-1972");

 

 printDatesAscending(arr);

}

}

// This code is contributed by offbeat  
  
---  
  
 __

 __

 **Output:**

    
    
    03-08-1970
    14-02-1972
    09-04-1994
    25-08-1996
    29-08-1996

**Time Complexity:** _O(N*log N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

