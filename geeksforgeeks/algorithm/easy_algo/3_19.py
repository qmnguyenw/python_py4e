Find maximum meetings in one room



There is one meeting room in a firm. There are **N** meetings in the form of
**(S[i], F[i])** where **S[i]** is the start time of meeting **i** and
**F[i]** is finish time of meeting **i**. The task is to find the maximum
number of meetings that can be accommodated in the meeting room. Print all
meeting numbers

 **Examples:**

> **Input :** s[] = {1, 3, 0, 5, 8, 5}, f[] = {2, 4, 6, 7, 9, 9}  
> **Output :** 1 2 4 5  
> First meeting [1, 2]  
> Second meeting [3, 4]  
> Fourth meeting [5, 7]  
> Fifth meeting [8, 9]
>
>  **Input :** s[] = {75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924},  
> f[] = {112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252 }  
> **Output :** 6 7 1

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
Idea is to solve the problem using the greedy approach which is the same as
Activity Selection Problem.

  

  

  * Sort all pairs(Meetings) in increasing order of second number(Finish time) of each pair.
  * Select first meeting of sorted pair as the first Meeting in the room and push it into result vector and set a variable time_limet(say) with the second value(Finishing time) of the first selected meeting.
  * Iterate from the second pair to last pair of the array and if the value of the first element(Starting time of meeting) of the current pair is greater then previously selected pair finish time (time_limit) then select the current pair and update the result vector (push selected meeting number into vector) and variable time_limit.
  * Print the Order of meeting from vector.

Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find maxium number of meetings

#include <bits/stdc++.h>

using namespace std;

// Structure for storing starting time,

// finishing time and position of meeting.

struct meeting {

 int start;

 int end;

 int pos;

};

// Comparator function which can compare

// the second element of structure used to

// sort pairs in increasing order of second value.

bool comparator(struct meeting m1, meeting m2)

{

 return (m1.end < m2.end);

}

// Function for finding maximum meeting in one room

void maxMeeting(int s[], int f[], int n)

{

 struct meeting meet[n];

 for (int i = 0; i < n; i++)

 {

 // Starting time of meeting i.

 meet[i].start = s[i];

 

 // Finishing time of meeting i

 meet[i].end = f[i];

 

 // Original position/index of meeting

 meet[i].pos = i + 1;

 }

 // Sorting of meeting according to their finish time.

 sort(meet, meet + n, comparator);

 // Vector for storing selected meeting.

 vector<int> m;

 // Initially select first meeting.

 m.push_back(meet[0].pos);

 // time_limit to check whether new

 // meeting can be conducted or not.

 int time_limit = meet[0].end;

 // Check for all meeting whether it

 // can be selected or not.

 for (int i = 1; i < n; i++) {

 if (meet[i].start >= time_limit)

 {

 // Push selected meeting to vector

 m.push_back(meet[i].pos);

 

 // Update time limit.

 time_limit = meet[i].end;

 }

 }

 // Print final selected meetings.

 for (int i = 0; i < m.size(); i++) {

 cout << m[i] << " ";

 }

}

// Driver code

int main()

{

 // Starting time

 int s[] = { 1, 3, 0, 5, 8, 5 };

 

 // Finish time

 int f[] = { 2, 4, 6, 7, 9, 9 };

 

 // Number of meetings.

 int n = sizeof(s) / sizeof(s[0]);

 // Function call

 maxMeeting(s, f, n);

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

// Java program to find maxium number of meetings

import java.util.*;

// Comparator function which can compare

// the ending time of the meeting ans

// sort the list

class mycomparator implements Comparator<meeting>

{

 @Override

 public int compare(meeting o1, meeting o2)

 {

 if (o1.end < o2.end)

 {

 

 // Return -1 if second object is

 // bigger then first

 return -1;

 }

 else if (o1.end > o2.end)

 

 // Return 1 if second object is

 // smaller then first

 return 1;

 

 return 0;

 }

}

// Custom class for storing starting time, 

// finishing time and position of meeting.

class meeting

{

 int start;

 int end;

 int pos;

 

 meeting(int start, int end, int pos)

 {

 this.start = start;

 this.end = end;

 this.pos = pos;

 }

}

class GFG{

 

// Function for finding maximum meeting in one room

public static void maxMeeting(ArrayList<meeting> al, int s)

{

 

 // Initialising an arraylist for storing answer

 ArrayList<Integer> m = new ArrayList<>();

 

 int time_limit = 0;

 

 mycomparator mc = new mycomparator();

 

 // Sorting of meeting according to

 // their finish time.

 Collections.sort(al, mc);

 

 // Initially select first meeting.

 m.add(al.get(0).pos);

 

 // time_limit to check whether new 

 // meeting can be conducted or not.

 time_limit = al.get(0).end;

 

 // Check for all meeting whether it 

 // can be selected or not.

 for(int i = 1; i < al.size(); i++)

 {

 if (al.get(i).start > time_limit)

 {

 

 // Add selected meeting to arraylist

 m.add(al.get(i).pos);

 

 // Update time limit

 time_limit = al.get(i).end;

 }

 }

 

 // Print final selected meetings.

 for(int i = 0; i < m.size(); i++)

 System.out.print(m.get(i) + 1 + " ");

}

// Driver Code 

public static void main (String[] args)

{

 

 // Starting time

 int s[] = { 1, 3, 0, 5, 8, 5 };

 

 // Finish time

 int f[] = { 2, 4, 6, 7, 9, 9 }; 

 

 // Defining an arraylist of meet type

 ArrayList<meeting> meet = new ArrayList<>();

 for(int i = 0; i < s.length; i++)

 

 // Creating object of meeting

 // and adding in the list

 meet.add(new meeting(s[i], f[i], i));

 

 // Function call

 maxMeeting(meet, meet.size());

}

}

// This code is contributed by Sarthak Sethi  
  
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

# Python3 program to find maximum number

# of meetings

# Custom class for storing starting time,

# finishing time and position of meeting.

class meeting:

 

 def __init__(self, start, end, pos):

 

 self.start = start

 self.end = end

 self.pos = pos

# Function for finding maximum

# meeting in one room

def maxMeeting(l, n):

 # Initialising an arraylist

 # for storing answer

 ans = []

 

 # Sorting of meeting according to

 # their finish time.

 l.sort(key = lambda x: x.end)

 # Initially select first meeting

 ans.append(l[0].pos)

 # time_limit to check whether new

 # meeting can be conducted or not.

 time_limit = l[0].end

 

 # Check for all meeting whether it

 # can be selected or not.

 for i in range(1, n):

 if l[i].start > time_limit:

 ans.append(l[i].pos)

 time_limit = l[i].end

 

 # Print final selected meetings

 for i in ans:

 print(i + 1, end = " ")

 

 print()

# Driver code

if __name__ == '__main__':

 

 # Starting time

 s = [ 1, 3, 0, 5, 8, 5 ]

 # Finish time

 f = [ 2, 4, 6, 7, 9, 9 ]

 # Number of meetings.

 n = len(s)

 l = []

 for i in range(n):

 

 # Creating object of meeting

 # and adding in the list

 l.append(meeting(s[i], f[i], i))

 

 # Function call

 maxMeeting(l, n)

# This code is contributed by MuskanKalra1  
  
---  
  
 __

 __

 **Output:**

    
    
    1 2 4 5
    
    
    
    
    
    
    
    
    

**Time Complexity:** O(N log(N))  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

