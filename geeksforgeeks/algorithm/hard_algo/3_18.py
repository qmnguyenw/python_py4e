Maximum CPU Load from the given list of jobs



Given an array of jobs with different time requirements, where each job
consists of **start time** , **end time** and **CPU load**. The task is to
find the maximum CPU load at any time if all jobs are running on the same
machine.

 **Examples:**

> **Input:** jobs[] = {{1, 4, 3}, {2, 5, 4}, {7, 9, 6}}  
> **Output:** 7  
> **Explanation:**  
> In the above-given jobs, there are two jobs which overlaps.  
> That is, Job [1, 4, 3] and [2, 5, 4] overlaps for the time period in [2, 4]  
> Hence, the maximum CPU Load at this instant will be maximum (3 + 4 = 7).
>
>  **Input:** jobs[] = {{6, 7, 10}, {2, 4, 11}, {8, 12, 15}}  
> **Output:** 15  
> **Explanation:**  
> Since, There are no jobs that overlaps.  
> Maximum CPU Load will be – max(10, 11, 15) = 15

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

This problem is generally the application of the Merge Intervals.  
**Approach:** The idea is to maintain min-heap for the jobs on the basis of
their end times. Then, for each instance find the jobs which are complete and
remove them from the Min-heap. That is, Check that the end-time of the jobs in
the min-heap had ended before the start time of the current job. Also at each
instance, find the maximum CPU Load on the machine by taking the sum of all
the jobs that are present in the min-heap.

  

  

 **For Example:**

    
    
    Given Jobs be {{1, 4, 3}, {2, 5, 4}, {7, 9, 6}}
    Min-Heap - {}
    
    **Instance 1:**
    The job {1, 4, 3} is inserted into the min-heap
    Min-Heap - {{1, 4, 3}},
    Total CPU Load  = 3
    
    **Instance 2:**
    The job {2, 5, 4} is inserted into the min-heap.
    While the job {1, 4, 3} is still in the CPU, 
    because end-time of Job 1 is greater than 
    the start time of the new job {2, 5, 4}.
    Min-Heap - {{1, 4, 3}, {2, 5, 4}}
    Total CPU Load = 4 + 3 = 7
    
    **Instance 3:**
    The job {7, 9, 6} is inserted into the min-heap.
    After popping up all the other jobs because their
    end time is less than the start time of the new job
    Min Heap - {7, 9, 6}
    Total CPU Load =  6
    
    Maximum CPU Load = max(3, 7, 6) = 7

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// maximum CPU Load from the given

// lists of the jobs

#include <algorithm>

#include <iostream>

#include <queue>

#include <vector>

using namespace std;

// Blueprint of the job

class Job {

 public:

 int start = 0;

 int end = 0;

 int cpuLoad = 0;

 

 // Constructor function for

 // the CPU Job

 Job(int start, int end,

 int cpuLoad)

 {

 this->start = start;

 this->end = end;

 this->cpuLoad = cpuLoad;

 }

};

class MaximumCPULoad {

 

 // Structure to compare two

 // CPU Jobs by their end time

 public:

 struct endCompare {

 bool operator()(const Job& x,

 const Job& y) {

 return x.end > y.end;

 }

 };

 

 // Function to find the maximum

 // CPU Load at any instance of

 // the time for given jobs

 static int findMaxCPULoad(

 vector<Job>& jobs)

 {

 // Condition when there are

 // no jobs then CPU Load is 0

 if (jobs.empty()) {

 return 0;

 }

 

 // Sorting all the jobs

 // by their start time

 sort(jobs.begin(), jobs.end(),

 [](const Job& a, const Job& b) {

 return a.start < b.start;

 });

 int maxCPULoad = 0;

 int currentCPULoad = 0;

 

 // Min-heap implemented using the

 // help of the priority queue

 priority_queue<Job, vector<Job>,

 endCompare> minHeap;

 

 // Loop to iterate over all the

 // jobs from the given list

 for (auto job : jobs) {

 

 // Loop to remove all jobs from

 // the heap which is ended

 while (!minHeap.empty() &&

 job.start > minHeap.top().end) {

 currentCPULoad -=

 minHeap.top().cpuLoad;

 minHeap.pop();

 }

 

 // Add the current Job to CPU

 minHeap.push(job);

 currentCPULoad += job.cpuLoad;

 maxCPULoad = max(maxCPULoad,

 currentCPULoad);

 }

 return maxCPULoad;

 }

};

// Driver Code

int main(int argc, char* argv[])

{

 vector<Job> input = { { 1, 4, 3 },

 { 7, 9, 6 }, { 2, 5, 4 } };

 cout << "Maximum CPU load at any time: "

 << MaximumCPULoad::findMaxCPULoad(input)

 << endl;

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

# Python implementation to find the

# maximum CPU Load from the given

# lists of the jobs

from heapq import *

# Blueprint of the job

class job:

 

 # Constructor of the Job

 def __init__(self, start,\

 end, cpu_load):

 self.start = start

 self.end = end

 self.cpu_load = cpu_load

 

 # Operator overloading for the

 # Object that is Job

 def __lt__(self, other):

 # min heap based on job.end

 return self.end < other.end

# Function to find the maximum

# CPU Load for the given list of jobs

def find_max_cpu_load(jobs):

 

 # Sort the jobs by start time

 jobs.sort(key = lambda x: x.start)

 max_cpu_load, current_cpu_load = 0, 0

 

 # Min-Heap

 min_heap = []

 

 # Loop to iterate over the list

 # of the jobs given for the CPU

 for j in jobs:

 

 # Remove all the jobs from

 # the min-heap which ended

 while(len(min_heap) > 0 and\

 j.start >= min_heap[0].end):

 current_cpu_load -= min_heap[0].cpu_load

 heappop(min_heap)

 

 # Add the current job

 # into min_heap

 heappush(min_heap, j)

 current_cpu_load += j.cpu_load

 max_cpu_load = max(max_cpu_load,

 current_cpu_load)

 return max_cpu_load

# Driver Code

if __name__ == "__main__":

 jobs = [job(1, 4, 3), job(2, 5, 4),\

 job(7, 9, 6)]

 

 print("Maximum CPU load at any time: " +\

 str(find_max_cpu_load(jobs)))  
  
---  
  
 __

 __

 **Output**

    
    
    Maximum CPU load at any time: 7

 **Performance Analysis:**

  * **Time complexity:** O(N*logN)
  *  **Auxiliary Space:** O(N)

 **Approach 2 – Without using heap, Merge the overlapping intervals.**

This can also be solved by using idea of Merge Intervals.  
The idea is fairly straight forward – > Merge the overlapping intervals and
add their load.  
Below is the Java code for the same.

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// JAVA Implementation of the above

// approach

import java.util.Arrays;

import java.util.*;

public class MaximumCpuLoad {

 

private static int maxCpuLoad(int[][] process) {

 Arrays.sort(process,(a,b)->'

 {

 return a[0]-b[0];

 });

 

 

 // list of intervals

 List<int[]> li = new LinkedList<int[]>();

 

 

 // variable to store the result

 int ans=0;

 

 // Merge intervals

 for(int[] p : process)

 {

 if(!li.isEmpty() && p[0]<li.get(li.size()-1)[1])

 {

 li.get(li.size()-1)[1]=

 Math.max(p[1], li.get(li.size()-1)[1]);

 li.get(li.size()-1)[2]=

 p[2]+li.get(li.size()-1)[2];

 

 }

 else

 {

 li.add(p);

 }

 

 ans= Math.max(ans, li.get(li.size()-1)[2]);

 }

 

 return ans;

 

}

 

 

 

 // Driver Code

 public static void main(String[] args)

 {

 // Given Process

 int[][] process = new int[][] {{1,4,3},
{7,9,6}, {2,5,4}};

 

 // Function call

 int ans = maxCpuLoad(process);

 System.out.print(ans);

 }

}  
  
---  
  
 __

 __

 **Output**

    
    
    7

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

