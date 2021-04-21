Program for SSTF disk scheduling algorithm



Prerequisite – Disk scheduling algorithms  
Given an array of disk track numbers and initial head position, our task is to
find the total number of seek operations done to access all the requested
tracks if **Shortest Seek Time First (SSTF)** is a disk scheduling algorithm
is used.

 **Shortest Seek Time First (SSTF) –**  
Basic idea is the tracks which are closer to current disk head position should
be serviced first in order to _minimise the seek operations_.

 **Advantages of Shortest Seek Time First (SSTF) –**

  1. Better performance than FCFS scheduling algorithm.
  2. It provides better throughput.
  3. This algorithm is used in Batch Processing system where throughput is more important.
  4. It has less average response and waiting time.

 **Disadvantages of Shortest Seek Time First (SSTF) –**

  1. Starvation is possible for some requests as it favours easy to reach request and ignores the far away processes.
  2. Their is lack of predictability because of high variance of response time.
  3. Switching direction slows things down.

 **Algorithm –**

  

  

  1. Let Request array represents an array storing indexes of tracks that have been requested. ‘head’ is the position of disk head.
  2. Find the positive distance of all tracks in the request array from head.
  3. Find a track from requested array which has not been accessed/serviced yet and has minimum distance from head.
  4. Increment the total seek count with this distance.
  5. Currently serviced track position now becomes the new head position.
  6. Go to step 2 until all tracks in request array have not been serviced.

 **Example –**  
Request sequence = {176, 79, 34, 60, 92, 11, 41, 114}  
Initial head position = 50  
The following chart shows the sequence in which requested tracks are serviced
using SSTF.

![](https://media.geeksforgeeks.org/wp-content/uploads/3333-4.png)

Therefore, total seek count is calculates as:

    
    
    = (50-41)+(41-34)+(34-11)+(60-11)+(79-60)+(92-79)+(114-92)+(176-114)
    = 204 

**Implementation –**  
Implementation of SSTF is given below. Note that we have made a node class
having 2 members. ‘distance’ is used to store the distance between head and
the track position. ‘accessed’ is a boolean variable which tells whether the
track has been accessed/serviced before by disk head or not.  

## Java

 __

 __  
 __

 __

 __  
 __  
 __

class node {

 

 // represent difference between 

 // head position and track number

 int distance = 0; 

 

 // true if track has been accessed

 boolean accessed = false; 

}

 

public class SSTF {

 

 // Calculates difference of each 

 // track number with the head position

 public static void calculateDifference(int queue[], 

 int head, node diff[])

 

 {

 for (int i = 0; i < diff.length; i++)

 diff[i].distance = Math.abs(queue[i] - head);

 }

 

 // find unaccessed track 

 // which is at minimum distance from head

 public static int findMin(node diff[])

 {

 int index = -1, minimum = Integer.MAX_VALUE;

 

 for (int i = 0; i < diff.length; i++) {

 if (!diff[i].accessed && minimum > diff[i].distance) {

 

 minimum = diff[i].distance;

 index = i;

 }

 }

 return index;

 }

 

 public static void shortestSeekTimeFirst(int request[], 

 int head)

 

 {

 if (request.length == 0)

 return;

 

 // create array of objects of class node 

 node diff[] = new node[request.length]; 

 

 // initialize array

 for (int i = 0; i < diff.length; i++) 

 

 diff[i] = new node();

 

 // count total number of seek operation 

 int seek_count = 0; 

 

 // stores sequence in which disk access is done

 int[] seek_sequence = new int[request.length + 1]; 

 

 for (int i = 0; i < request.length; i++) {

 

 seek_sequence[i] = head;

 calculateDifference(request, head, diff);

 

 int index = findMin(diff);

 

 diff[index].accessed = true;

 

 // increase the total count

 seek_count += diff[index].distance; 

 

 // accessed track is now new head

 head = request[index]; 

 }

 

 // for last accessed track

 seek_sequence[seek_sequence.length - 1] = head; 

 

 System.out.println("Total number of seek operations = "

 + seek_count);

 

 System.out.println("Seek Sequence is");

 

 // print the sequence

 for (int i = 0; i < seek_sequence.length; i++) 

 System.out.println(seek_sequence[i]);

 }

 

 public static void main(String[] args)

 {

 // request array

 int arr[] = { 176, 79, 34, 60, 92, 11, 41,
114 }; 

 shortestSeekTimeFirst(arr, 50);

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

# Python3 program for implementation of

# SSTF disk scheduling 

 

# Calculates difference of each 

# track number with the head position

def calculateDifference(queue, head, diff):

 for i in range(len(diff)):

 diff[i][0] = abs(queue[i] - head) 

 

# find unaccessed track which is 

# at minimum distance from head 

def findMin(diff): 

 

 index = -1

 minimum = 999999999

 

 for i in range(len(diff)):

 if (not diff[i][1] and

 minimum > diff[i][0]):

 minimum = diff[i][0]

 index = i

 return index 

 

def shortestSeekTimeFirst(request, head): 

 if (len(request) == 0): 

 return

 

 l = len(request) 

 diff = [0] * l

 

 # initialize array 

 for i in range(l):

 diff[i] = [0, 0]

 

 # count total number of seek operation 

 seek_count = 0

 

 # stores sequence in which disk 

 # access is done 

 seek_sequence = [0] * (l + 1) 

 

 for i in range(l): 

 seek_sequence[i] = head 

 calculateDifference(request, head, diff) 

 index = findMin(diff) 

 

 diff[index][1] = True

 

 # increase the total count 

 seek_count += diff[index][0] 

 

 # accessed track is now new head 

 head = request[index] 

 

 # for last accessed track 

 seek_sequence[len(seek_sequence) - 1] = head 

 

 print("Total number of seek operations =", 

 seek_count) 

 

 print("Seek Sequence is") 

 

 # print the sequence 

 for i in range(l + 1):

 print(seek_sequence[i]) 

 

# Driver code 

if __name__ =="__main__":

 

 # request array 

 proc = [176, 79, 34, 60, 

 92, 11, 41, 114]

 shortestSeekTimeFirst(proc, 50)

 

# This code is contributed by

# Shubham Singh(SHUBHAMSINGH10)  
  
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

// C# program for implementation of FCFS

// scheduling 

using System;

 

public class node

{

 

 // represent difference between 

 // head position and track number

 public int distance = 0; 

 

 // true if track has been accessed

 public Boolean accessed = false; 

}

 

public class SSTF 

{

 

 // Calculates difference of each 

 // track number with the head position

 public static void calculateDifference(int []queue, 

 int head, node []diff)

 

 {

 for (int i = 0; i < diff.Length; i++)

 diff[i].distance = Math.Abs(queue[i] - head);

 }

 

 // find unaccessed track 

 // which is at minimum distance from head

 public static int findMin(node []diff)

 {

 int index = -1, minimum = int.MaxValue;

 

 for (int i = 0; i < diff.Length; i++)

 {

 if (!diff[i].accessed && minimum > diff[i].distance)

 {

 

 minimum = diff[i].distance;

 index = i;

 }

 }

 return index;

 }

 

 public static void shortestSeekTimeFirst(int []request, 

 int head)

 {

 if (request.Length == 0)

 return;

 

 // create array of objects of class node 

 node []diff = new node[request.Length]; 

 

 // initialize array

 for (int i = 0; i < diff.Length; i++) 

 

 diff[i] = new node();

 

 // count total number of seek operation 

 int seek_count = 0; 

 

 // stores sequence in which disk access is done

 int[] seek_sequence = new int[request.Length + 1]; 

 

 for (int i = 0; i < request.Length; i++)

 {

 

 seek_sequence[i] = head;

 calculateDifference(request, head, diff);

 

 int index = findMin(diff);

 

 diff[index].accessed = true;

 

 // increase the total count

 seek_count += diff[index].distance; 

 

 // accessed track is now new head

 head = request[index]; 

 }

 

 // for last accessed track

 seek_sequence[seek_sequence.Length - 1] = head; 

 

 Console.WriteLine("Total number of seek operations = "

 + seek_count);

 

 Console.WriteLine("Seek Sequence is");

 

 // print the sequence

 for (int i = 0; i < seek_sequence.Length; i++) 

 Console.WriteLine(seek_sequence[i]);

 }

 

 // Driver code

 public static void Main(String[] args)

 {

 // request array

 int []arr = { 176, 79, 34, 60, 92, 11, 41, 114 }; 

 shortestSeekTimeFirst(arr, 50);

 }

}

 

// This code contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    Total number of seek operations = 204
    Seek Sequence is
    50
    41
    34
    11
    60
    79
    92
    114
    176 

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

