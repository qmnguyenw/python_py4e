SCAN (Elevator) Disk Scheduling Algorithms



Prerequisite-Disk scheduling algorithms.  
Given an array of disk track numbers and initial head position, our task is to
find the total number of seek operations done to access all the requested
tracks if SCAN disk scheduling algorithm is used.

 **SCAN (Elevator) algorithm**  
In SCAN disk scheduling algorithm, head starts from one end of the disk and
moves towards the other end, servicing requests in between one by one and
reach the other end. Then the direction of the head is reversed and the
process continues as head continuously scan back and forth to access the disk.
So, this algorithm works as an elevator and hence also known as the **elevator
algorithm**. As a result, the requests at the midrange are serviced more and
those arriving behind the disk arm will have to wait.

 **Advantages of SCAN (Elevator) algorithm**

  1. This algorithm is simple and easy to understand.
  2. SCAN algorithm have no starvation.
  3. This algorithm is better than FCFS Scheduling algorithm .

 **Disadvantages of SCAN (Elevator) algorithm**

  1. More complex algorithm to implement.
  2. This algorithm is not fair because it cause long waiting time for the cylinders just visited by the head.
  3. It causes the head to move till the end of the disk in this way the requests arriving ahead of the arm position would get immediate service but some other requests that arrive behind the arm position will have to wait for the request to complete.

 **Algorithm-**

  

  

  1. Let Request array represents an array storing indexes of tracks that have been requested in ascending order of their time of arrival. ‘head’ is the position of disk head.
  2. Let direction represents whether the head is moving towards left or right.
  3. In the direction in which head is moving service all tracks one by one.
  4. Calculate the absolute distance of the track from the head.
  5. Increment the total seek count with this distance.
  6. Currently serviced track position now becomes the new head position.
  7. Go to step 3 until we reach at one of the ends of the disk.
  8. If we reach at the end of the disk reverse the direction and go to step 2 until all tracks in request array have not been serviced.

 **Example:**

    
    
    **Input:** 
    Request sequence = {176, 79, 34, 60, 92, 11, 41, 114}
    Initial head position = 50
    Direction = left (We are moving from right to left)
    
    **Output:**
    Total number of seek operations = 226
    Seek Sequence is
    41
    34
    11
    0
    60
    79
    92
    114
    176

The following chart shows the sequence in which requested tracks are serviced
using SCAN.  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190727175932/fcfs-2.jpg)

Therefore, the total seek count is calculated as:

    
    
    = (50-41)+(41-34)+(34-11)
     +(11-0)+(60-0)+(79-60)
     +(92-79)+(114-92)+(176-114)
    = 226

 **Implementation:**  
Implementation of SCAN is given below. Note that distance is used to store the
absolute distance between the head and current track position. disk_size is
the size of the disk. Vectors left and right stores all the request tracks on
the left-hand side and the right-hand side of the initial head position
respectively.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to demonstrate

// SCAN Disk Scheduling algorithm

#include <bits/stdc++.h>

using namespace std;

int size = 8;

int disk_size = 200;

void SCAN(int arr[], int head, string direction)

{

 int seek_count = 0;

 int distance, cur_track;

 vector<int> left, right;

 vector<int> seek_sequence;

 // appending end values

 // which has to be visited

 // before reversing the direction

 if (direction == "left")

 left.push_back(0);

 else if (direction == "right")

 right.push_back(disk_size - 1);

 for (int i = 0; i < size; i++) {

 if (arr[i] < head)

 left.push_back(arr[i]);

 if (arr[i] > head)

 right.push_back(arr[i]);

 }

 // sorting left and right vectors

 std::sort(left.begin(), left.end());

 std::sort(right.begin(), right.end());

 // run the while loop two times.

 // one by one scanning right

 // and left of the head

 int run = 2;

 while (run--) {

 if (direction == "left") {

 for (int i = left.size() - 1; i >= 0; i--) {

 cur_track = left[i];

 // appending current track to seek sequence

 seek_sequence.push_back(cur_track);

 // calculate absolute distance

 distance = abs(cur_track - head);

 // increase the total count

 seek_count += distance;

 // accessed track is now the new head

 head = cur_track;

 }

 direction = "right";

 }

 else if (direction == "right") {

 for (int i = 0; i < right.size(); i++) {

 cur_track = right[i];

 // appending current track to seek sequence

 seek_sequence.push_back(cur_track);

 // calculate absolute distance

 distance = abs(cur_track - head);

 // increase the total count

 seek_count += distance;

 // accessed track is now new head

 head = cur_track;

 }

 direction = "left";

 }

 }

 cout << "Total number of seek operations = "

 << seek_count << endl;

 cout << "Seek Sequence is" << endl;

 for (int i = 0; i < seek_sequence.size(); i++) {

 cout << seek_sequence[i] << endl;

 }

}

// Driver code

int main()

{

 // request array

 int arr[size] = { 176, 79, 34, 60,

 92, 11, 41, 114 };

 int head = 50;

 string direction = "left";

 SCAN(arr, head, direction);

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

// Java program to demonstrate

// SCAN Disk Scheduling algorithm

import java.util.*;

class GFG

{

static int size = 8;

static int disk_size = 200;

static void SCAN(int arr[], int head, String direction)

{

 int seek_count = 0;

 int distance, cur_track;

 Vector<Integer> left = new Vector<Integer>(),

 right = new Vector<Integer>();

 Vector<Integer> seek_sequence = new Vector<Integer>();

 // appending end values

 // which has to be visited

 // before reversing the direction

 if (direction == "left")

 left.add(0);

 else if (direction == "right")

 right.add(disk_size - 1);

 for (int i = 0; i < size; i++)

 {

 if (arr[i] < head)

 left.add(arr[i]);

 if (arr[i] > head)

 right.add(arr[i]);

 }

 // sorting left and right vectors

 Collections.sort(left);

 Collections.sort(right);

 // run the while loop two times.

 // one by one scanning right

 // and left of the head

 int run = 2;

 while (run-- >0)

 {

 if (direction == "left")

 {

 for (int i = left.size() - 1; i >= 0; i--)

 {

 cur_track = left.get(i);

 // appending current track to seek sequence

 seek_sequence.add(cur_track);

 // calculate absolute distance

 distance = Math.abs(cur_track - head);

 // increase the total count

 seek_count += distance;

 // accessed track is now the new head

 head = cur_track;

 }

 direction = "right";

 }

 else if (direction == "right")

 {

 for (int i = 0; i < right.size(); i++)

 {

 cur_track = right.get(i);

 

 // appending current track to seek sequence

 seek_sequence.add(cur_track);

 // calculate absolute distance

 distance = Math.abs(cur_track - head);

 // increase the total count

 seek_count += distance;

 // accessed track is now new head

 head = cur_track;

 }

 direction = "left";

 }

 }

 System.out.print("Total number of seek operations = "

 + seek_count + "\n");

 System.out.print("Seek Sequence is" + "\n");

 for (int i = 0; i < seek_sequence.size(); i++)

 {

 System.out.print(seek_sequence.get(i) + "\n");

 }

}

// Driver code

public static void main(String[] args)

{

 // request array

 int arr[] = { 176, 79, 34, 60,

 92, 11, 41, 114 };

 int head = 50;

 String direction = "left";

 SCAN(arr, head, direction);

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

# Python3 program to demonstrate

# SCAN Disk Scheduling algorithm

size = 8

disk_size = 200

def SCAN(arr, head, direction):

 seek_count = 0

 distance, cur_track = 0, 0

 left = []

 right = []

 seek_sequence = []

 # Appending end values

 # which has to be visited

 # before reversing the direction

 if (direction == "left"):

 left.append(0)

 elif (direction == "right"):

 right.append(disk_size - 1)

 for i in range(size):

 if (arr[i] < head):

 left.append(arr[i])

 if (arr[i] > head):

 right.append(arr[i])

 # Sorting left and right vectors

 left.sort()

 right.sort()

 # Run the while loop two times.

 # one by one scanning right

 # and left of the head

 run = 2

 while (run != 0):

 if (direction == "left"):

 for i in range(len(left) - 1, -1, -1):

 cur_track = left[i]

 # Appending current track to

 # seek sequence

 seek_sequence.append(cur_track)

 # Calculate absolute distance

 distance = abs(cur_track - head)

 # Increase the total count

 seek_count += distance

 # Accessed track is now the new head

 head = cur_track

 

 direction = "right"

 

 elif (direction == "right"):

 for i in range(len(right)):

 cur_track = right[i]

 

 # Appending current track to seek

 # sequence

 seek_sequence.append(cur_track)

 # Calculate absolute distance

 distance = abs(cur_track - head)

 # Increase the total count

 seek_count += distance

 # Accessed track is now new head

 head = cur_track

 

 direction = "left"

 

 run -= 1

 print("Total number of seek operations =",

 seek_count)

 print("Seek Sequence is")

 for i in range(len(seek_sequence)):

 print(seek_sequence[i])

# Driver code

# request array

arr = [ 176, 79, 34, 60,

 92, 11, 41, 114 ]

head = 50

direction = "left"

SCAN(arr, head, direction)

# This code is contributed by divyesh072019  
  
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

// C# program to demonstrate

// SCAN Disk Scheduling algorithm

using System;

using System.Collections.Generic;

class GFG

{

static int size = 8;

static int disk_size = 200;

static void SCAN(int []arr, int head, String direction)

{

 int seek_count = 0;

 int distance, cur_track;

 List<int> left = new List<int>(),

 right = new List<int>();

 List<int> seek_sequence = new List<int>();

 // appending end values

 // which has to be visited

 // before reversing the direction

 if (direction == "left")

 left.Add(0);

 else if (direction == "right")

 right.Add(disk_size - 1);

 for (int i = 0; i < size; i++)

 {

 if (arr[i] < head)

 left.Add(arr[i]);

 if (arr[i] > head)

 right.Add(arr[i]);

 }

 // sorting left and right vectors

 left.Sort();

 right.Sort();

 // run the while loop two times.

 // one by one scanning right

 // and left of the head

 int run = 2;

 while (run-- >0)

 {

 if (direction == "left")

 {

 for (int i = left.Count - 1; i >= 0; i--)

 {

 cur_track = left[i];

 // appending current track to seek sequence

 seek_sequence.Add(cur_track);

 // calculate absolute distance

 distance = Math.Abs(cur_track - head);

 // increase the total count

 seek_count += distance;

 // accessed track is now the new head

 head = cur_track;

 }

 direction = "right";

 }

 else if (direction == "right")

 {

 for (int i = 0; i < right.Count; i++)

 {

 cur_track = right[i];

 

 // appending current track to seek sequence

 seek_sequence.Add(cur_track);

 // calculate absolute distance

 distance = Math.Abs(cur_track - head);

 // increase the total count

 seek_count += distance;

 // accessed track is now new head

 head = cur_track;

 }

 direction = "left";

 }

 }

 Console.Write("Total number of seek operations = "

 + seek_count + "\n");

 Console.Write("Seek Sequence is" + "\n");

 for (int i = 0; i < seek_sequence.Count; i++)

 {

 Console.Write(seek_sequence[i] + "\n");

 }

}

// Driver code

public static void Main(String[] args)

{

 // request array

 int []arr = { 176, 79, 34, 60,

 92, 11, 41, 114 };

 int head = 50;

 String direction = "left";

 SCAN(arr, head, direction);

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

 // Javascript program to demonstrate

 // SCAN Disk Scheduling algorithm

 

 let size = 8;

 let disk_size = 200;

 function SCAN(arr, head, direction)

 {

 let seek_count = 0;

 let distance, cur_track;

 let left = [], right = [];

 let seek_sequence = [];

 // appending end values

 // which has to be visited

 // before reversing the direction

 if (direction == "left")

 left.push(0);

 else if (direction == "right")

 right.push(disk_size - 1);

 for (let i = 0; i < size; i++)

 {

 if (arr[i] < head)

 left.push(arr[i]);

 if (arr[i] > head)

 right.push(arr[i]);

 }

 // sorting left and right vectors

 left.sort(function(a, b){return a - b});

 right.sort(function(a, b){return a - b});

 // run the while loop two times.

 // one by one scanning right

 // and left of the head

 let run = 2;

 while (run-- >0)

 {

 if (direction == "left")

 {

 for (let i = left.length - 1; i >= 0; i--)

 {

 cur_track = left[i];

 // appending current track to seek sequence

 seek_sequence.push(cur_track);

 // calculate absolute distance

 distance = Math.abs(cur_track - head);

 // increase the total count

 seek_count += distance;

 // accessed track is now the new head

 head = cur_track;

 }

 direction = "right";

 }

 else if (direction == "right")

 {

 for (let i = 0; i < right.length; i++)

 {

 cur_track = right[i];

 // appending current track to seek sequence

 seek_sequence.push(cur_track);

 // calculate absolute distance

 distance = Math.abs(cur_track - head);

 // increase the total count

 seek_count += distance;

 // accessed track is now new head

 head = cur_track;

 }

 direction = "left";

 }

 }

 document.write("Total number of seek operations = "

 + seek_count + "</br>");

 document.write("Seek Sequence is" + "</br>");

 for (let i = 0; i < seek_sequence.length; i++)

 {

 document.write(seek_sequence[i] + "</br>");

 }

 }

 

 // request array

 

 let arr = [ 176, 79, 34, 60, 92, 11, 41, 114 ];

 let head = 50;

 let direction = "left";

 

 SCAN(arr, head, direction);

 

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    Total number of seek operations = 226
    Seek Sequence is
    41
    34
    11
    0
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

