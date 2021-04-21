Jump in rank of a student after updating marks



Given three arrays **names[]** , **marks[]** and **updates[]** where:

  1. **names[]** contains the names of students.
  2.  **marks[]** contains the marks of the same students.
  3.  **updates[]** contains the integers by which the marks of these students are to be updated.

The task is find the name of the student with maximum marks after updation and
the jump in the student’s rank i.e. **previous rank – current rank**.

**Note:** The details of the students are in descending order of their marks
and if more than two students scored equal marks (also the highest) then
choose the one who had a lower rank previously.

 **Examples:**

> **Input:** names[] = {“sam”, “ram”, “geek”, “sonu”},  
> marks[] = {99, 75, 70, 60},  
> updates[] = {-10, 5, 9, 39}  
> **Output:** Name: sonu, Jump: 3  
> Updated marks are {89, 80, 79, 99}, its clear that sonu has the highest
> marks with jump of 3
>
>  
>
>
>  
>
>
>  **Input:** names[] = {“sam”, “ram”, “geek”},  
> marks[] = {80, 79, 75},  
> updates[] = {0, 5, -9}  
> **Output:** Name: ram, Jump: 1

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** Create a structure **struct Student** to store the information
of each student, each of which will have 3 attributes **name** of the student,
**marks** of the student, **prev_rank** of the student.  
Now, updated the marks according to the content of the **updates[]** then with
a single traversal of the array, find the student who has the highest marks
after updation.

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

// Structure to store the information of

// students

struct Student {

 string name;

 int marks = 0;

 int prev_rank = 0;

};

// Function to print the name of student who

// stood first after updation in rank

void nameRank(string names[], int marks[],

 int updates[], int n)

{

 // Array of students

 Student x[n];

 for (int i = 0; i < n; i++) {

 // Store the name of the student

 x[i].name = names[i];

 // Update the marks of the student

 x[i].marks = marks[i] + updates[i];

 // Store the current rank of the student

 x[i].prev_rank = i + 1;

 }

 Student highest = x[0];

 for (int j = 1; j < n; j++) {

 if (x[j].marks >= highest.marks)

 highest = x[j];

 }

 // Print the name and jump in rank

 cout << "Name: " << highest.name

 << ", Jump: "

 << abs(highest.prev_rank - 1)

 << endl;

}

// Driver code

int main()

{

 // Names of the students

 string names[] = { "sam", "ram", "geek" };

 // Marks of the students

 int marks[] = { 80, 79, 75 };

 // Updates that are to be done

 int updates[] = { 0, 5, -9 };

 // Number of students

 int n = sizeof(marks) / sizeof(marks[0]);

 nameRank(names, marks, updates, n);

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

import java.util.*;

 

class GFG{

 

static class Student

{

 String name;

 int marks, prev_rank;

 

 Student()

 {

 this.marks = 0;

 this.prev_rank = 0;

 }

}

 

// Function to print the name of student who

// stood first after updation in rank

static void nameRank(String []names, int []marks,

 int []updates, int n)

{

 

 // Array of students

 Student []x = new Student[n];

 

 for(int i = 0; i < n; i++)

 {

 x[i] = new Student();

 

 // Store the name of the student

 x[i].name = names[i];

 

 // Update the marks of the student

 x[i].marks = marks[i] + updates[i];

 

 // Store the current rank of the student

 x[i].prev_rank = i + 1;

 }

 

 Student highest = x[0];

 

 for(int j = 1; j < n; j++)

 {

 if (x[j].marks >= highest.marks)

 highest = x[j];

 }

 

 // Print the name and jump in rank

 System.out.print("Name: " + highest.name +

 ", Jump: " +

 Math.abs(highest.prev_rank - 1));

}

 

// Driver code 

public static void main(String[] args)

{

 

 // Names of the students

 String []names = { "sam", "ram", "geek" };

 

 // Marks of the students

 int []marks = { 80, 79, 75 };

 

 // Updates that are to be done

 int []updates = { 0, 5, -9 };

 

 // Number of students

 int n = marks.length;

 

 nameRank(names, marks, updates, n);

}

}

// This code is contributed by pratham76  
  
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

# Function to prthe name of student who

# stood first after updation in rank

def nameRank(names, marks, updates, n):

 

 # Array of students

 x = [[0 for j in range(3)] for i in
range(n)]

 for i in range(n):

 

 # Store the name of the student

 x[i][0] = names[i]

 

 # Update the marks of the student

 x[i][1]= marks[i] + updates[i]

 

 # Store the current rank of the student

 x[i][2] = i + 1

 

 highest = x[0]

 for j in range(1, n):

 if (x[j][1] >= highest[1]):

 highest = x[j]

 

 # Print the name and jump in rank

 print("Name: ", highest[0], ", Jump: ",

 abs(highest[2] - 1), sep="")

# Driver code

# Names of the students

names= ["sam", "ram", "geek"]

# Marks of the students

marks = [80, 79, 75]

# Updates that are to be done

updates = [0, 5, -9]

# Number of students

n = len(marks)

nameRank(names, marks, updates, n)

# This code is contributed by SHUBHAMSINGH10  
  
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

 

class GFG{

public class Student

{

 public string name;

 public int marks, prev_rank;

 

 public Student()

 {

 this.marks = 0;

 this.prev_rank = 0;

 }

}

 

// Function to print the name of student who

// stood first after updation in rank

static void nameRank(string []names, int []marks,

 int []updates, int n)

{

 

 // Array of students

 Student []x = new Student[n];

 

 for(int i = 0; i < n; i++)

 {

 x[i] = new Student();

 

 // Store the name of the student

 x[i].name = names[i];

 

 // Update the marks of the student

 x[i].marks = marks[i] + updates[i];

 

 // Store the current rank of the student

 x[i].prev_rank = i + 1;

 }

 

 Student highest = x[0];

 

 for(int j = 1; j < n; j++)

 {

 if (x[j].marks >= highest.marks)

 highest = x[j];

 }

 

 // Print the name and jump in rank

 Console.Write("Name: " + highest.name +

 ", Jump: " +

 Math.Abs(highest.prev_rank - 1));

}

// Driver code 

public static void Main(string[] args)

{

 

 // Names of the students

 string []names = { "sam", "ram", "geek" };

 

 // Marks of the students

 int []marks = { 80, 79, 75 };

 

 // Updates that are to be done

 int []updates = { 0, 5, -9 };

 

 // Number of students

 int n = marks.Length;

 

 nameRank(names, marks, updates, n);

}

}

// This code is contributed by rutvik_56  
  
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

// Javascript implementation of the approach

 

// Function to print the name of student who

// stood first after updation in rank

function nameRank(names, marks, updates, n)

{

 

 // Array of students

 let x = new Array(n);

 for(let i = 0; i < n; i++)

 {

 x[i] = new Array(3);

 for(let j = 0; j < 3; j++)

 {

 x[i][j] = 0;

 }

 }

 

 for(let i = 0; i < n; i++)

 {

 

 // Store the name of the student

 x[i][0] = names[i]

 

 // Update the marks of the student

 x[i][1] = marks[i] + updates[i]

 

 // Store the current rank of the student

 x[i][2] = i + 1

 }

 

 let highest = x[0];

 

 for(let j = 1; j < n; j++)

 {

 if (x[j][1] >= highest[1])

 highest = x[j]

 }

 

 // Print the name and jump in rank

 document.write("Name: ", highest[0], ", Jump: ",

 Math.abs(highest[2] - 1), sep = "")

}

// Driver code

// Names of the students

let names = [ "sam", "ram", "geek" ];

// Marks of the students

let marks = [ 80, 79, 75 ];

// Updates that are to be done

let updates = [ 0, 5, -9 ];

// Number of students

let n = marks.length;

nameRank(names, marks, updates, n)

// This code is contributed by unknown2108

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    Name: ram, Jump: 1

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

