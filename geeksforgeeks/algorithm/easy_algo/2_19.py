First Come, First Serve – CPU Scheduling | (Non-preemptive)



 **Prerequisite:** CPU Scheduling in Operating Systems  
Given **N** processes with their Arrival Time as **at[]** and Burst Time as
**bt[]**. The task is to find the Waiting Time for each processes and Average
Waiting Time using First Come First Serve(FCFS) algorithm.

 **Examples**

>  **Input:** N = 5, at[] = {0, 1, 2, 3, 4}, bt[] = {4, 3, 1, 2, 5}Processes|
> Arrival Time| Burst Time| P1| 0| 4| P2| 1| 3| P3| 2| 1| P4| 3| 2| P5| 4| 5  
> ---|---|---  
>  
>  **Output:** Waiting Time for each process are:Processes| Waiting Time| P1|
> 0| P2| 3| P3| 5| P4| 5| P5| 6  
> ---|---  
>  
> Average Waiting Time = 3.8
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  1. The waiting time for first process is 0 as it is executed first.
  2. The waiting time for upcoming process can be calculated by:
    
    
    wt[i] =  ( at[i - 1] + bt[i - 1] + wt[i - 1] ) - at[i]
    

where **wt[i]** = waiting time of current process  
 **at[i-1]** = arrival time of previous process  
 **bt[i-1]** = burst time of previous process  
 **wt[i-1]** = waiting time of previous process  
 **at[i]** = arrival time of current process

  3. The Average waiting time can be calculated by:
    
    
    Average Waiting Time = (sum of all waiting time)/(Number of processes)
    

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to Calculate Waiting

// Time for given Processes

#include <iostream>

using namespace std;

 

// Function to Calculate waiting time

// and average waiting time

void CalculateWaitingTime(int at[],

 int bt[], int N)

{

 

 // Declare the array for waiting

 // time

 int wt[N];

 

 // Waiting time for first process

 // is 0

 wt[0] = 0;

 

 // Print waiting time process 1

 cout << "P.No.\tArrival Time\t"

 << "Burst Time\tWaiting Time\n";

 cout << "1"

 << "\t\t" << at[0] << "\t\t"

 << bt[0] << "\t\t" << wt[0] << endl;

 

 // Calculating waiting time for

 // each process from the given

 // formula

 for (int i = 1; i < 5; i++) {

 wt[i] = (at[i - 1] + bt[i - 1] + wt[i - 1]) - at[i];

 

 // Print the waiting time for

 // each process

 cout << i + 1 << "\t\t" << at[i]

 << "\t\t" << bt[i] << "\t\t"

 << wt[i] << endl;

 }

 

 // Declare variable to calculate

 // average

 float average;

 float sum = 0;

 

 // Loop to calculate sum of all

 // waiting time

 for (int i = 0; i < 5; i++) {

 sum = sum + wt[i];

 }

 

 // Find average waiting time

 // by dividing it by no. of process

 average = sum / 5;

 

 // Print Average Waiting Time

 cout << "Average waiting time = "

 << average;

}

 

// Driver code

int main()

{

 // Number of process

 int N = 5;

 

 // Array for Arrival time

 int at[] = { 0, 1, 2, 3, 4 };

 

 // Array for Burst Time

 int bt[] = { 4, 3, 1, 2, 5 };

 

 // Function call to find

 // waiting time

 CalculateWaitingTime(at, bt, N);

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

// Java program to Calculate Waiting

// Time for given Processes

class GFG

{

 

// Function to Calculate waiting time

// and average waiting time

static void CalculateWaitingTime(int at[],

 int bt[], int N)

{

 

 // Declare the array for waiting

 // time

 int []wt = new int[N];

 

 // Waiting time for first process

 // is 0

 wt[0] = 0;

 

 // Print waiting time process 1

 System.out.print("P.No.\tArrival Time\t"

 + "Burst Time\tWaiting Time\n");

 System.out.print("1"

 + "\t\t" + at[0]+ "\t\t"

 + bt[0]+ "\t\t" + wt[0] +"\n");

 

 // Calculating waiting time for

 // each process from the given

 // formula

 for (int i = 1; i < 5; i++) {

 wt[i] = (at[i - 1] + bt[i - 1] + wt[i - 1]) - at[i];

 

 // Print the waiting time for

 // each process

 System.out.print(i + 1+ "\t\t" + at[i]

 + "\t\t" + bt[i]+ "\t\t"

 + wt[i] +"\n");

 }

 

 // Declare variable to calculate

 // average

 float average;

 float sum = 0;

 

 // Loop to calculate sum of all

 // waiting time

 for (int i = 0; i < 5; i++) {

 sum = sum + wt[i];

 }

 

 // Find average waiting time

 // by dividing it by no. of process

 average = sum / 5;

 

 // Print Average Waiting Time

 System.out.print("Average waiting time = "

 + average);

}

 

// Driver code

public static void main(String[] args)

{

 // Number of process

 int N = 5;

 

 // Array for Arrival time

 int at[] = { 0, 1, 2, 3, 4 };

 

 // Array for Burst Time

 int bt[] = { 4, 3, 1, 2, 5 };

 

 // Function call to find

 // waiting time

 CalculateWaitingTime(at, bt, N);

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

# Python3 program to Calculate Waiting

# Time for given Processes

 

# Function to Calculate waiting time

# and average waiting time

def CalculateWaitingTime(at, bt, N):

 

 # Declare the array for waiting

 # time

 wt = [0]*N;

 

 # Waiting time for first process

 # is 0

 wt[0] = 0;

 

 # Prwaiting time process 1

 print("P.No.\tArrival Time\t" , "Burst Time\tWaiting Time");

 print("1" , "\t\t" , at[0] , "\t\t" , bt[0] ,
"\t\t" , wt[0]);

 

 # Calculating waiting time for

 # each process from the given

 # formula

 for i in range(1,5):

 wt[i] = (at[i - 1] + bt[i - 1] + wt[i - 1])
- at[i];

 

 # Print the waiting time for

 # each process

 print(i + 1 , "\t\t" , at[i] , "\t\t" , bt[i] , "\t\t"
, wt[i]);

 

 

 # Declare variable to calculate

 # average

 average = 0.0;

 sum = 0;

 

 # Loop to calculate sum of all

 # waiting time

 for i in range(5):

 sum = sum + wt[i];

 

 # Find average waiting time

 # by dividing it by no. of process

 average = sum / 5;

 

 # PrAverage Waiting Time

 print("Average waiting time = " , average);

 

 

# Driver code

if __name__ == '__main__':

 # Number of process

 N = 5;

 

 # Array for Arrival time

 at = [ 0, 1, 2, 3, 4 ];

 

 # Array for Burst Time

 bt = [ 4, 3, 1, 2, 5 ];

 

 # Function call to find

 # waiting time

 CalculateWaitingTime(at, bt, N);

 

# This code is contributed by 29AjayKumar  
  
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

// C# program to Calculate Waiting

// Time for given Processes

using System;

 

class GFG

{

 

// Function to Calculate waiting time

// and average waiting time

static void CalculateWaitingTime(int []at,

 int []bt, int N)

{

 

 // Declare the array for waiting

 // time

 int []wt = new int[N];

 

 // Waiting time for first process

 // is 0

 wt[0] = 0;

 

 // Print waiting time process 1

 Console.Write("P.No.\tArrival Time\t"

 + "Burst Time\tWaiting Time\n");

 Console.Write("1"

 + "\t\t" + at[0]+ "\t\t"

 + bt[0]+ "\t\t" + wt[0] +"\n");

 

 // Calculating waiting time for

 // each process from the given

 // formula

 for (int i = 1; i < 5; i++) {

 wt[i] = (at[i - 1] + bt[i - 1] + wt[i - 1]) - at[i];

 

 // Print the waiting time for

 // each process

 Console.Write(i + 1+ "\t\t" + at[i]

 + "\t\t" + bt[i]+ "\t\t"

 + wt[i] +"\n");

 }

 

 // Declare variable to calculate

 // average

 float average;

 float sum = 0;

 

 // Loop to calculate sum of all

 // waiting time

 for (int i = 0; i < 5; i++) {

 sum = sum + wt[i];

 }

 

 // Find average waiting time

 // by dividing it by no. of process

 average = sum / 5;

 

 // Print Average Waiting Time

 Console.Write("Average waiting time = "

 + average);

}

 

// Driver code

public static void Main(String[] args)

{

 // Number of process

 int N = 5;

 

 // Array for Arrival time

 int []at = { 0, 1, 2, 3, 4 };

 

 // Array for Burst Time

 int []bt = { 4, 3, 1, 2, 5 };

 

 // Function call to find

 // waiting time

 CalculateWaitingTime(at, bt, N);

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    P.No.    Arrival Time    Burst Time    Waiting Time
    1        0        4        0
    2        1        3        3
    3        2        1        5
    4        3        2        5
    5        4        5        6
    Average waiting time = 3.8
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

