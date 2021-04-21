Priority CPU Scheduling with different arrival time – Set 2



 **Prerequisite –** Program for Priority Scheduling – Set 1

Priority scheduling is a non-preemptive algorithm and one of the most common
scheduling algorithms in batch systems. Each process is assigned first arrival
time (less arrival time process first) if two processes have same arrival
time, then compare to priorities (highest process first). Also, if two
processes have same priority then compare to process number (less process
number first). This process is repeated while all process get executed.

 **Implementation –**

  1. First input the processes with their arrival time, burst time and priority.
  2. Sort the processes, according to arrival time if two process arrival time is same then sort according process priority if two process priority are same then sort according to process number.
  3. Now simply apply FCFS algorithm.

![](https://media.geeksforgeeks.org/wp-content/uploads/opSystemScheduling.png)  
 **Gantt Chart –**  
![](https://media.geeksforgeeks.org/wp-content/uploads/gantchart2.jpg)

 **Examples –**

  

  

    
    
    **Input :**
    process no-> 1 2 3 4 5 
    arrival time-> 0 1 3 2 4
    burst time-> 3 6 1 2 4
    priority-> 3 4 9 7 8
    **Output :**
    Process_no Start_time Complete_time Trun_Around_Time Wating_Time
    1          0           3            3           0
    2          3           9            8           2
    4          9           11           9           7
    3          11          12           9           8
    5          12          16           12          8
    Average Wating Time is : 5.0
    Average Trun Around time is : 8.2
    
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation for Priority Scheduling with

//Different Arrival Time priority scheduling

/*1. sort the processes according to arrival time 

2. if arrival time is same the acc to priority

3. apply fcfs

*/

 

#include <bits/stdc++.h>

 

using namespace std;

 

#define totalprocess 5

 

// Making a struct to hold the given input 

 

struct process

{

int at,bt,pr,pno;

};

 

process proc[50];

 

/*

Writing comparator function to sort according to priority if 

arrival time is same 

*/

 

bool comp(process a,process b)

{

if(a.at == b.at)

{

return a.pr<b.pr;

}

else

{

 return a.at<b.at;

}

}

 

// Using FCFS Algorithm to find Waiting time

void get_wt_time(int wt[])

{

// declaring service array that stores cumulative burst time 

int service[50];

 

// Initilising initial elements of the arrays

service[0] = proc[0].at;

wt[0]=0;

 

 

for(int i=1;i<totalprocess;i++)

{

service[i]=proc[i-1].bt+service[i-1];

 

wt[i]=service[i]-proc[i].at;

 

// If waiting time is negative, change it into zero

 

 if(wt[i]<0)

 {

 wt[i]=0;

 }

}

 

}

 

void get_tat_time(int tat[],int wt[])

{

// Filling turnaroundtime array

 

for(int i=0;i<totalprocess;i++)

{

 tat[i]=proc[i].bt+wt[i];

}

 

}

 

void findgc()

{

//Declare waiting time and turnaround time array

int wt[50],tat[50];

 

double wavg=0,tavg=0;

 

// Function call to find waiting time array

get_wt_time(wt);

//Function call to find turnaround time

get_tat_time(tat,wt);

 

int stime[50],ctime[50];

 

stime[0] = proc[0].at;

ctime[0]=stime[0]+tat[0];

 

// calculating starting and ending time

for(int i=1;i<totalprocess;i++)

 {

 stime[i]=ctime[i-1];

 ctime[i]=stime[i]+tat[i]-wt[i];

 }

 

cout<<"Process_no\tStart_time\tComplete_time\tTurn_Around_Time\tWaiting_Time"<<endl;

 

 // display the process details

 

for(int i=0;i<totalprocess;i++)

 {

 wavg += wt[i];

 tavg += tat[i];

 

 cout<<proc[i].pno<<"\t\t"<<

 stime[i]<<"\t\t"<<ctime[i]<<"\t\t"<<

 tat[i]<<"\t\t\t"<<wt[i]<<endl;

 }

 

 // display the average waiting time

 //and average turn around time

 

 cout<<"Average waiting time is : ";

 cout<<wavg/(float)totalprocess<<endl;

 cout<<"average turnaround time : ";

 cout<<tavg/(float)totalprocess<<endl;

 

}

 

int main()

{

int arrivaltime[] = { 1, 2, 3, 4, 5 };

int bursttime[] = { 3, 5, 1, 7, 4 };

int priority[] = { 3, 4, 1, 7, 8 };

 

for(int i=0;i<totalprocess;i++)

{

 proc[i].at=arrivaltime[i];

 proc[i].bt=bursttime[i];

 proc[i].pr=priority[i];

 proc[i].pno=i+1;

 } 

 

 //Using inbuilt sort function

 

 sort(proc,proc+totalprocess,comp);

 

 //Calling function findgc for finding Gantt Chart

 

 findgc(); 

 

 return 0;

}

 

// This code is contributed by Anukul Chand.  
  
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

// Java implementation for Priority Scheduling with

//Different Arrival Time priority scheduling

import java.util.*;

 

/// Data Structure

class Process {

 int at, bt, pri, pno;

 Process(int pno, int at, int bt, int pri)

 {

 this.pno = pno;

 this.pri = pri;

 this.at = at;

 this.bt = bt;

 }

}

 

/// Gantt chart structure

class GChart {

 // process number, start time, complete time,

 // turn around time, waiting time

 int pno, stime, ctime, wtime, ttime;

}

 

// user define comparative method (first arrival first serve,

// if arrival time same then heigh priority first)

class MyComparator implements Comparator {

 

 public int compare(Object o1, Object o2)

 {

 

 Process p1 = (Process)o1;

 Process p2 = (Process)o2;

 if (p1.at < p2.at)

 return (-1);

 

 else if (p1.at == p2.at && p1.pri > p2.pri)

 return (-1);

 

 else

 return (1);

 }

}

 

 

// class to find Gantt chart

class FindGantChart {

 void findGc(LinkedList queue)

 {

 

 // initial time = 0

 int time = 0;

 

 // priority Queue sort data according

 // to arrival time or priority (ready queue)

 TreeSet prique = new TreeSet(new MyComparator());

 

 // link list for store processes data

 LinkedList result = new LinkedList();

 

 // process in ready queue from new state queue

 while (queue.size() > 0)

 prique.add((Process)queue.removeFirst());

 

 Iterator it = prique.iterator();

 

 // time set to according to first process

 time = ((Process)prique.first()).at;

 

 // scheduling process

 while (it.hasNext()) {

 

 // dispatcher dispatch the

 // process ready to running state

 Process obj = (Process)it.next();

 

 GChart gc1 = new GChart();

 gc1.pno = obj.pno;

 gc1.stime = time;

 time += obj.bt;

 gc1.ctime = time;

 gc1.ttime = gc1.ctime - obj.at;

 gc1.wtime = gc1.ttime - obj.bt;

 

 /// store the exxtreted process

 result.add(gc1);

 }

 

 // create object of output class and call method

 new ResultOutput(result);

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

# Python3 implementation for Priority Scheduling with

# Different Arrival Time priority scheduling 

"""1. sort the processes according to arrival time 

 2. if arrival time is same the acc to priority 

 3. apply fcfs """

 

totalprocess = 5

proc = []

for i in range(5):

 l = []

 for j in range(4):

 l.append(0)

 proc.append(l)

 

# Using FCFS Algorithm to find Waiting time 

def get_wt_time( wt): 

 

 # declaring service array that stores

 # cumulative burst time 

 service = [0] * 5

 

 # Initilising initial elements 

 # of the arrays 

 service[0] = 0

 wt[0] = 0

 

 for i in range(1, totalprocess): 

 service[i] = proc[i - 1][1] + service[i - 1] 

 wt[i] = service[i] - proc[i][0] + 1

 

 # If waiting time is negative,

 # change it o zero 

 if(wt[i] < 0) : 

 wt[i] = 0

 

def get_tat_time(tat, wt): 

 

 # Filling turnaroundtime array 

 for i in range(totalprocess):

 tat[i] = proc[i][1] + wt[i] 

 

def findgc():

 

 # Declare waiting time and

 # turnaround time array 

 wt = [0] * 5

 tat = [0] * 5

 

 wavg = 0

 tavg = 0

 

 # Function call to find waiting time array 

 get_wt_time(wt) 

 

 # Function call to find turnaround time 

 get_tat_time(tat, wt) 

 

 stime = [0] * 5

 ctime = [0] * 5

 stime[0] = 1

 ctime[0] = stime[0] + tat[0]

 

 # calculating starting and ending time 

 for i in range(1, totalprocess): 

 stime[i] = ctime[i - 1] 

 ctime[i] = stime[i] + tat[i] - wt[i] 

 

 print("Process_no\tStart_time\tComplete_time",

 "\tTurn_Around_Time\tWaiting_Time")

 

 # display the process details 

 for i in range(totalprocess):

 wavg += wt[i] 

 tavg += tat[i] 

 

 print(proc[i][3], "\t\t", stime[i], 

 "\t\t", end = " ")

 print(ctime[i], "\t\t", tat[i], "\t\t\t", wt[i]) 

 

 

 # display the average waiting time 

 # and average turn around time 

 print("Average waiting time is : ", end = " ")

 print(wavg / totalprocess)

 print("average turnaround time : " , end = " ")

 print(tavg / totalprocess)

 

# Driver code 

if __name__ =="__main__":

 arrivaltime = [1, 2, 3, 4, 5]

 bursttime = [3, 5, 1, 7, 4]

 priority = [3, 4, 1, 7, 8] 

 

 for i in range(totalprocess): 

 

 proc[i][0] = arrivaltime[i] 

 proc[i][1] = bursttime[i] 

 proc[i][2] = priority[i] 

 proc[i][3] = i + 1

 

 # Using inbuilt sort function 

 proc = sorted (proc, key = lambda x:x[2])

 proc = sorted (proc)

 

 # Calling function findgc for

 # finding Gantt Chart 

 findgc() 

 

# This code is contributed by

# Shubham Singh(SHUBHAMSINGH10)  
  
---  
  
 __

 __

  
 **Output:**

    
    
    Process_no Start_time Complete_time Trun_Around_Time Wating_Time
    1           1           4              3            0
    2           4           9              7            2
    3           9           10             7            6
    4          10           17             13           6
    5          17           21             16           12
    Average Wating Time is : 5.2
    Average Trun Around time is : 9.2
    

This article is contributed by **Amit Verma**. If you like GeeksforGeeks and
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

