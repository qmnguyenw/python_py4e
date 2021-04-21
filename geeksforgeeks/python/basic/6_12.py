Program to calculate Electricity Bill



Given an integer **U** denoting the amount of KWh units of electricity
consumed, the task is to calculate the electricity bill with the help of the
below charges:

>   * 1 to 100 units – ![Rs. 10/unit](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-a3f1a6b0ab57123db8794ae947a66ef6_l3.png)
>   * 100 to 200 units – ![Rs. 15/unit](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-4d00203554c4079bcddd1d14e9d9cba3_l3.png)
>   * 200 to 300 units – ![Rs. 20/unit](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-24a580a5bf9f76dd72f614fefe398ede_l3.png)
>   * above 300 units – ![Rs. 25/unit](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-ca19baca055791b0a8e75215e2242993_l3.png)
>

**Examples:**

>  **Input:** U = 250  
>  **Output:** 3500  
>  **Explanation:**  
>  Charge for the first 100 units – 10*100 = 1000  
> Charge for the 100 to 200 units – 15*100 = 1500  
> Charge for the 200 to 250 units – 20*50 = 1000  
> Total Electricity Bill = 1000 + 1500 + 1000 = 3500
>
>  **Input:** U = 95  
>  **Output:** 950  
>  **Explanation:**  
>  Charge for the first 100 units – 10*95 = 950  
> Total Electricity Bill = 950

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to identify the charge bar in which it falls and
then calculate the bill according to the charges mentioned above. Below is the
illustration of the steps:

  

  

  * Check units consumed is less than equal to the 100, If yes then the total electricity bill will be:  

> ![\\text{Total Electricity Bill} = \(\\text{units} *
> 10\)](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-f3037d34e8f078e7c368127be0114e9b_l3.png)

  * Else if, check that units consumed is less than equal to the 200, if yes then total electricity bill will be:  

> ![\\text{Total Electricity Bill} = \(100*10\) + \(\\text{units}-100\) *
> 15](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-33558ec224e23d702ec772dde83a1728_l3.png)

  * Else if, check that units consumed is less than equal to the 300, if yes then total electricity bill will be:  

> ![\\text{Total Electricity Bill} = \(100*10\) + \(100*15\) +
> \(\\text{units}-200\) * 20](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-d1fd49ec6bef8820eac8a786991b6d32_l3.png)

  * Else if, check that units consumed greater than 300, if yes then total electricity bill will be:  

> ![\\text{Total Electricity Bill} = \(100*10\) + \(100*15\) + \(100*20\) +
> \(\\text{units}-300\) * 25](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-8c1e043a47b56430c4cbaa2338e77c55_l3.png)

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to calculate the

// electricity bill 

#include<bits/stdc++.h>

using namespace std;

 

// Function to calculate the 

// electricity bill 

int calculateBill(int units) 

{ 

 

 // Condition to find the charges 

 // bar in which the units consumed 

 // is fall 

 if (units <= 100) 

 { 

 return units * 10; 

 } 

 else if (units <= 200)

 { 

 return (100 * 10) + 

 (units - 100) * 15; 

 } 

 else if (units <= 300)

 { 

 return (100 * 10) + 

 (100 * 15) + 

 (units - 200) * 20; 

 } 

 else if (units > 300)

 { 

 return (100 * 10) + 

 (100 * 15) + 

 (100 * 20) + 

 (units - 300) * 25; 

 } 

 return 0; 

} 

 

// Driver Code 

int main() 

{ 

 int units = 250; 

 cout << calculateBill(units); 

} 

 

// This code is contributed by spp____  
  
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

// Java implementation to calculate the

// electricity bill

 

import java.util.*;

 

class ComputeElectricityBill {

 

 // Function to calculate the

 // electricity bill

 public static int calculateBill(int units)

 {

 

 // Condition to find the charges

 // bar in which the units consumed

 // is fall

 if (units <= 100) {

 return units * 10;

 }

 else if (units <= 200) {

 return (100 * 10)

 + (units - 100)

 * 15;

 }

 else if (units <= 300) {

 return (100 * 10)

 + (100 * 15)

 + (units - 200)

 * 20;

 }

 else if (units > 300) {

 return (100 * 10)

 + (100 * 15)

 + (100 * 20)

 + (units - 300)

 * 25;

 }

 return 0;

 }

 

 // Driver Code

 public static void main(String args[])

 {

 int units = 250;

 

 System.out.println(

 calculateBill(units));

 }

}  
  
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

# Python3 implementation to calculate the

# electricity bill 

 

# Function to calculate the 

# electricity bill 

def calculateBill(units):

 

 # Condition to find the charges 

 # bar in which the units consumed 

 # is fall 

 if (units <= 100):

 

 return units * 10; 

 

 elif (units <= 200):

 

 return ((100 * 10) +

 (units - 100) * 15); 

 

 elif (units <= 300):

 

 return ((100 * 10) +

 (100 * 15) +

 (units - 200) * 20); 

 

 elif (units > 300):

 

 return ((100 * 10) +

 (100 * 15) +

 (100 * 20) +

 (units - 300) * 25); 

 

 return 0; 

 

# Driver Code 

units = 250; 

print(calculateBill(units)); 

 

# This code is contributed by Code_Mech  
  
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

// C# implementation to calculate the

// electricity bill 

using System;

 

class ComputeElectricityBill{ 

 

// Function to calculate the 

// electricity bill 

public static int calculateBill(int units) 

{ 

 

 // Condition to find the charges 

 // bar in which the units consumed 

 // is fall 

 if (units <= 100)

 { 

 return units * 10; 

 } 

 else if (units <= 200)

 { 

 return (100 * 10) + 

 (units - 100) * 15; 

 } 

 else if (units <= 300) 

 { 

 return (100 * 10) +

 (100 * 15) + 

 (units - 200) * 20; 

 } 

 else if (units > 300) 

 { 

 return (100 * 10) + 

 (100 * 15) + 

 (100 * 20) + 

 (units - 300) * 25; 

 } 

 return 0; 

} 

 

// Driver Code 

public static void Main(String []args) 

{ 

 int units = 250; 

 

 Console.WriteLine(calculateBill(units)); 

} 

} 

 

// This code is contributed by spp____  
  
---  
  
 __

 __

 **Output:**

    
    
    3500
    

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

