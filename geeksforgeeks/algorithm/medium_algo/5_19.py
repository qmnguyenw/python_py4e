Minimum possible travel cost among N cities



There are **N** cities situated on a straight road and each is separated by a
distance of **1** unit. You have to reach the **(N + 1) th** city by boarding
a bus. The **i th** city would cost of **C[i]** dollars to travel **1** unit
of distance. In other words, cost to travel from the **i th** city to the **j
th** city is **abs(i – j ) * C[i]** dollars. The task is to find the minimum
cost to travel from city **1** to city **(N + 1)** i.e. beyond the last city.  
 **Examples:**  

> **Input:** C[] = {3, 5, 4}  
> **Output:** 9  
> The bus boarded from the first city has the minimum  
> cost of all so it will be used to travel (N + 1) unit.  
>  **Input:** C[] = {4, 7, 8, 3, 4}  
> **Output:** 18  
> Board the bus at the first city then change  
> the bus at the fourth city.  
> (3 * 4) + (2 * 3) = 12 + 6 = 18  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The approach is very simple, just travel by the bus which has
the lowest cost so far. Whenever a bus with an even lower cost is found,
change the bus from that city. Following are the steps to solve:  

  1. Start with the first city with a cost of **C[1]**.
  2. Travel to the next city until a city **j** having cost less than the previous city (by which we are travelling, let’s say city **i** ) is found.
  3. Calculate cost as **abs(j – i) * C[i]** and add it to the total cost so far.
  4. Repeat the previous steps until all the cities have been traversed.

Below is the implementation of the above approach:  

## C++

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

// Function to return the minimum cost to

// travel from the first city to the last

int minCost(vector<int>& cost, int n)

{

 // To store the total cost

 int totalCost = 0;

 // Start from the first city

 int boardingBus = 0;

 for (int i = 1; i < n; i++) {

 // If found any city with cost less than

 // that of the previous boarded

 // bus then change the bus

 if (cost[boardingBus] > cost[i]) {

 // Calculate the cost to travel from

 // the currently boarded bus

 // till the current city

 totalCost += ((i - boardingBus) * cost[boardingBus]);

 // Update the currently boarded bus

 boardingBus = i;

 }

 }

 // Finally calculate the cost for the

 // last boarding bus till the (N + 1)th city

 totalCost += ((n - boardingBus) * cost[boardingBus]);

 return totalCost;

}

// Driver code

int main()

{

 vector<int> cost{ 4, 7, 8, 3, 4 };

 int n = cost.size();

 cout << minCost(cost, n);

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

// Java implementation of the approach

class GFG

{

// Function to return the minimum cost to

// travel from the first city to the last

static int minCost(int []cost, int n)

{

 // To store the total cost

 int totalCost = 0;

 // Start from the first city

 int boardingBus = 0;

 for (int i = 1; i < n; i++)

 {

 // If found any city with cost less than

 // that of the previous boarded

 // bus then change the bus

 if (cost[boardingBus] > cost[i])

 {

 // Calculate the cost to travel from

 // the currently boarded bus

 // till the current city

 totalCost += ((i - boardingBus) * cost[boardingBus]);

 // Update the currently boarded bus

 boardingBus = i;

 }

 }

 // Finally calculate the cost for the

 // last boarding bus till the (N + 1)th city

 totalCost += ((n - boardingBus) * cost[boardingBus]);

 return totalCost;

}

// Driver code

public static void main(String[] args)

{

 int []cost = { 4, 7, 8, 3, 4 };

 int n = cost.length;

 System.out.print(minCost(cost, n));

}

}

// This code is contributed by PrinciRaj1992  
  
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

# Python3 implementation of the approach

# Function to return the minimum cost to

# travel from the first city to the last

def minCost(cost, n):

 # To store the total cost

 totalCost = 0

 # Start from the first city

 boardingBus = 0

 for i in range(1, n):

 # If found any city with cost less than

 # that of the previous boarded

 # bus then change the bus

 if (cost[boardingBus] > cost[i]):

 # Calculate the cost to travel from

 # the currently boarded bus

 # till the current city

 totalCost += ((i - boardingBus) *

 cost[boardingBus])

 # Update the currently boarded bus

 boardingBus = i

 # Finally calculate the cost for the

 # last boarding bus till the (N + 1)th city

 totalCost += ((n - boardingBus) *

 cost[boardingBus])

 return totalCost

# Driver code

cost = [ 4, 7, 8, 3, 4]

n = len(cost)

print(minCost(cost, n))

# This code is contributed by Mohit Kumar  
  
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

// C# implementation of the approach

using System;

class GFG

{

// Function to return the minimum cost to

// travel from the first city to the last

static int minCost(int []cost, int n)

{

 // To store the total cost

 int totalCost = 0;

 // Start from the first city

 int boardingBus = 0;

 for (int i = 1; i < n; i++)

 {

 // If found any city with cost less than

 // that of the previous boarded

 // bus then change the bus

 if (cost[boardingBus] > cost[i])

 {

 // Calculate the cost to travel from

 // the currently boarded bus

 // till the current city

 totalCost += ((i - boardingBus) *

 cost[boardingBus]);

 // Update the currently boarded bus

 boardingBus = i;

 }

 }

 // Finally calculate the cost for the

 // last boarding bus till the (N + 1)th city

 totalCost += ((n - boardingBus) *

 cost[boardingBus]);

 return totalCost;

}

// Driver code

public static void Main(String[] args)

{

 int []cost = { 4, 7, 8, 3, 4 };

 int n = cost.Length;

 Console.Write(minCost(cost, n));

}

}

// This code is contributed by 29AjayKumar  
  
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

// javascript implementation of the approach 

// Function to return the minimum cost to

 // travel from the first city to the last

 function minCost(cost , n) {

 // To store the total cost

 var totalCost = 0;

 // Start from the first city

 var boardingBus = 0;

 for (i = 1; i < n; i++) {

 // If found any city with cost less than

 // that of the previous boarded

 // bus then change the bus

 if (cost[boardingBus] > cost[i]) {

 // Calculate the cost to travel from

 // the currently boarded bus

 // till the current city

 totalCost += ((i - boardingBus) * cost[boardingBus]);

 // Update the currently boarded bus

 boardingBus = i;

 }

 }

 // Finally calculate the cost for the

 // last boarding bus till the (N + 1)th city

 totalCost += ((n - boardingBus) * cost[boardingBus]);

 return totalCost;

 }

 // Driver code

 

 var cost = [ 4, 7, 8, 3, 4 ];

 var n = cost.length;

 document.write(minCost(cost, n));

// This code contributed by umadevi9616

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    18

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

