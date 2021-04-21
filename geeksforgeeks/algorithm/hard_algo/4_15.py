Vertical and Horizontal retrieval (MRT) on Tapes



 **Prerequisite:** Optimal Storage on Tapes  
You are given **tapes[]** of different sizes and **records[]** of different
volumes. The task is to fill the volumes in tapes horizontally or vertically
such that Retrieval Time is minimised.  
 **Examples:**

>  **Input:** tape[] = { 25, 80, 160}, records[] = { 15, 2, 8, 23, 45, 50, 60,
> 120 }  
>  **Output:**  
>  **Horizontal Filling:**  
>  1st tape : [ 2 8 15 ] MRT : 12.3333  
> 2nd tape : [ 23 45 ] MRT : 45.5  
> 3rd tape : [ 50 60 ] MRT : 80  
>  **Vertical Filling:**  
>  1st tape : [ 2 23 ] MRT : 13.5  
> 2nd tape : [ 8 45 ] MRT : 30.5  
> 3rd tape : [ 15 50 60 ] MRT : 68.3333

For Minimum Retrieval Time we will insert volumes of records in increasing
order of their size.  
The formula for Minimum Retrieval Time is:

    
    
    MRT = **(1/N)*Σ(A(i)*(N-i))**
    where 0 &leq; i < N
    

There are two ways of adding volumes on tapes for reducing retrieval time:

  1. Horizontal Retrieval
  2. Vertical Retrieval

 _ **Horizontal Retrieval**_

  

  

We have,  
tapes[] = { 25, 80, 160}  
records[] = { 2, 8, 15, 23, 45, 50, 60, 120 } _(in increasing order)_  
 **Horizontal Filling on tape:**

  1. Inserting 2
    
    
    1st tape : [ 2 ]
    2nd tape : [ ]
    3rd tape : [ ]
    

  2. Inserting 8
    
    
    1st tape : [ 2 8 ]
    2nd tape : [ ]
    3rd tape : [ ]
    

  3. Inserting 15
    
    
    1st tape : [ 2 8 15 ]
    2nd tape : [ ]
    3rd tape : [ ]
    

  4. Inserting 23
    
    
    1st tape : [ 2 8 15 ]
    2nd tape : [ 23 ]
    3rd tape : [ ]
    

  5. Inserting 45
    
    
    1st tape : [ 2 8 15 ]
    2nd tape : [ 23 45 ]
    3rd tape : [ ]
    

  6. Inserting 50
    
    
    1st tape : [ 2 8 15 ]
    2nd tape : [ 23 45 ]
    3rd tape : [ 50 ]
    

  7. Inserting 60
    
    
    1st tape : [ 2 8 15 ]
    2nd tape : [ 23 45 ]
    3rd tape : [ 50 60 ]
    

Below is the program for Horizontal Filling  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print Horizontal

// filling

#include <bits/stdc++.h>

using namespace std;

 

void horizontalFill(int records[],

 int tape[], int nt)

{

 // It is used for checking whether

 // tape is full or not

 int sum = 0;

 

 // It is used for calculating

 // total retrieval time

 int Retrieval_Time = 0;

 

 // It is used for calculating

 // mean retrieval time

 double Mrt;

 int current = 0;

 

 // vector is used because n number of

 // records can insert in one tape with

 // size constraint

 vector<int> v;

 

 for (int i = 0; i < nt; i++) {

 

 // Null vector obtained to use fresh

 // vector 'v'

 v.clear();

 Retrieval_Time = 0;

 

 // initialize variables to

 // 0 for each iteration

 sum = 0;

 cout << "tape " << i + 1 << " : [ ";

 

 // sum is used for checking whether

 // i'th tape is full or not

 sum += records[current];

 

 // check sum less than size of tape

 while (sum <= tape[i]) {

 cout << records[current] << " ";

 v.push_back(records[current]);

 

 // increment in j for next record

 current++;

 sum += records[current];

 }

 cout << "]";

 

 // calculating total retrieval

 // time

 for (int i = 0; i < v.size(); i++) {

 

 // MRT formula

 Retrieval_Time += v[i] * (v.size() - i);

 }

 

 // calculating mean retrieval time

 // using formula

 Mrt = (double)Retrieval_Time / v.size();

 

 // v.size() is function of vector is used

 // to get size of vector

 cout << "\tMRT : " << Mrt << endl;

 }

}

 

// Driver Code

int main()

{

 int records[] = { 15, 2, 8, 23, 45, 50, 60, 120 };

 int tape[] = { 25, 80, 160 };

 

 // store the size of records[]

 int n = sizeof(records) / sizeof(records[0]);

 

 // store the size of tapes[]

 int m = sizeof(tape) / sizeof(tape[0]);

 

 // sorting of an array is required to

 // attain greedy approach of

 // algorithm

 sort(records, records + n);

 horizontalFill(records, tape, m);

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

// Java program to print Horizontal

// filling

import java.util.*;

 

class GFG

{

 

static void horizontalFill(int records[],

 int tape[], int nt)

{

 // It is used for checking whether

 // tape is full or not

 int sum = 0;

 

 // It is used for calculating

 // total retrieval time

 int Retrieval_Time = 0;

 

 // It is used for calculating

 // mean retrieval time

 double Mrt;

 int current = 0;

 

 // vector is used because n number of

 // records can insert in one tape with

 // size constraint

 Vector<Integer> v = new Vector<Integer>();

 

 for (int i = 0; i < nt; i++)

 {

 

 // Null vector obtained to use fresh

 // vector 'v'

 v.clear();

 Retrieval_Time = 0;

 

 // initialize variables to

 // 0 for each iteration

 sum = 0;

 System.out.print("tape " + (i + 1) + " : [ ");

 

 // sum is used for checking whether

 // i'th tape is full or not

 sum += records[current];

 

 // check sum less than size of tape

 while (sum <= tape[i])

 {

 System.out.print(records[current] + " ");

 v.add(records[current]);

 

 // increment in j for next record

 current++;

 sum += records[current];

 }

 System.out.print("]");

 

 // calculating total retrieval

 // time

 for (int j = 0; j < v.size(); j++) 

 {

 

 // MRT formula

 Retrieval_Time += v.get(j) * (v.size() - j);

 }

 

 // calculating mean retrieval time

 // using formula

 Mrt = (double)Retrieval_Time / v.size();

 

 // v.size() is function of vector is used

 // to get size of vector

 System.out.print("\tMRT : " + Mrt +"\n");

 }

}

 

// Driver Code

public static void main(String[] args)

{

 int records[] = { 15, 2, 8, 23, 45, 50, 60,
120 };

 int tape[] = { 25, 80, 160 };

 

 // store the size of records[]

 int n = records.length;

 

 // store the size of tapes[]

 int m = tape.length;

 

 // sorting of an array is required to

 // attain greedy approach of

 // algorithm

 Arrays.sort(records);

 horizontalFill(records, tape, m);

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

# Python3 program to print Horizontal

# filling 

 

def horizontalFill(records, tape, nt) : 

 

 # It is used for checking whether 

 # tape is full or not 

 sum = 0; 

 

 # It is used for calculating 

 # total retrieval time 

 Retrieval_Time = 0; 

 

 # It is used for calculating 

 # mean retrieval time 

 current = 0; 

 

 # vector is used because n number of 

 # records can insert in one tape with 

 # size constraint 

 v = []; 

 

 for i in range(nt) :

 

 # Null vector obtained to use fresh 

 # vector 'v' 

 v.clear(); 

 Retrieval_Time = 0; 

 

 # initialize variables to 

 # 0 for each iteration 

 sum = 0; 

 print("tape" , i + 1 ,": [ ",end =""); 

 

 # sum is used for checking whether 

 # i'th tape is full or not 

 sum += records[current]; 

 

 # check sum less than size of tape 

 while (sum <= tape[i]) :

 print(records[current],end= " "); 

 v.append(records[current]); 

 

 # increment in j for next record 

 current += 1; 

 sum += records[current]; 

 

 print("]",end=""); 

 

 # calculating total retrieval 

 # time 

 for i in range(len(v)) :

 

 # MRT formula 

 Retrieval_Time += v[i] * (len(v) - i); 

 

 

 # calculating mean retrieval time 

 # using formula 

 Mrt = Retrieval_Time / len(v); 

 

 # v.size() is function of vector is used 

 # to get size of vector 

 print("tMRT :", Mrt); 

 

# Driver Code 

if __name__ == "__main__" : 

 

 records = [ 15, 2, 8, 23, 45, 50, 60,
120 ];

 tape = [ 25, 80, 160 ];

 

 # store the size of records[]

 n = len(records);

 

 # store the size of tapes[]

 m = len(tape);

 # sorting of an array is required to 

 # attain greedy approach of

 # algorithm

 records.sort();

 horizontalFill(records, tape, m); 

 

# This code is contributed by AnkitRai01  
  
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

// C# program to print Horizontal

// filling

using System;

using System.Collections.Generic;

 

class GFG

{

 

static void horizontalFill(int []records,

 int []tape, int nt)

{

 // It is used for checking whether

 // tape is full or not

 int sum = 0;

 

 // It is used for calculating

 // total retrieval time

 int Retrieval_Time = 0;

 

 // It is used for calculating

 // mean retrieval time

 double Mrt;

 int current = 0;

 

 // vector is used because n number of

 // records can insert in one tape with

 // size constraint

 List<int> v = new List<int>();

 

 for (int i = 0; i < nt; i++)

 {

 

 // Null vector obtained to use fresh

 // vector 'v'

 v.Clear();

 Retrieval_Time = 0;

 

 // initialize variables to

 // 0 for each iteration

 sum = 0;

 Console.Write("tape " + (i + 1) + " : [ ");

 

 // sum is used for checking whether

 // i'th tape is full or not

 sum += records[current];

 

 // check sum less than size of tape

 while (sum <= tape[i])

 {

 Console.Write(records[current] + " ");

 v.Add(records[current]);

 

 // increment in j for next record

 current++;

 sum += records[current];

 }

 Console.Write("]");

 

 // calculating total retrieval

 // time

 for (int j = 0; j < v.Count; j++) 

 {

 

 // MRT formula

 Retrieval_Time += v[j] * (v.Count - j);

 }

 

 // calculating mean retrieval time

 // using formula

 Mrt = (double)Retrieval_Time / v.Count;

 

 // v.Count is function of vector is used

 // to get size of vector

 Console.Write("\tMRT : " + Mrt +"\n");

 }

}

 

// Driver Code

public static void Main(String[] args)

{

 int []records = { 15, 2, 8, 23, 45, 50, 60, 120 };

 int []tape = { 25, 80, 160 };

 

 // store the size of records[]

 int n = records.Length;

 

 // store the size of tapes[]

 int m = tape.Length;

 

 // sorting of an array is required to

 // attain greedy approach of

 // algorithm

 Array.Sort(records);

 horizontalFill(records, tape, m);

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    tape 1 : [ 2 8 15 ]    MRT : 12.3333
    tape 2 : [ 23 45 ]    MRT : 45.5
    tape 3 : [ 50 60 ]    MRT : 80
    

_**Vertical Retrieval**_

 **Vertical Filling on tape:**

  1. Inserting 2
    
    
    1st tape : [ 2 ]
    2nd tape : [ ]
    3rd tape : [ ]
    

  2. Inserting 8
    
    
    1st tape : [ 2 ]
    2nd tape : [ 8 ]
    3rd tape : [ ]
    

  3. Inserting 15
    
    
    1st tape : [ 2 ]
    2nd tape : [ 8 ]
    3rd tape : [ 15 ]
    

  4. Inserting 23
    
    
    1st tape : [ 2 23 ]
    2nd tape : [ 8 ]
    3rd tape : [ 15 ]
    

  5. Inserting 45
    
    
    1st tape : [ 2 23 ]
    2nd tape : [ 8 45 ]
    3rd tape : [ 15 ]
    

  6. Inserting 50
    
    
    1st tape : [ 2 23 ]
    2nd tape : [ 8 45 ]
    3rd tape : [ 15 50 ]
    

  7. Inserting 60
    
    
    1st tape : [ 2 23 60 ]
    2nd tape : [ 8 45 ]
    3rd tape : [ 15 50 ]
    

Below is the program for Vertical Filling  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print Vertical filling

#include <bits/stdc++.h>

using namespace std;

 

void vertical_Fill(int records[], int tape[],

 int m, int n)

{

 // 2D matrix for vertical insertion on

 // tapes

 int v[m][n] = { 0 };

 

 // It is used for checking whether tape

 // is full or not

 int sum = 0;

 

 // It is used for calculating total

 // retrieval time

 int Retrieval_Time = 0;

 

 // It is used for calculating mean

 // retrieval time

 double Mrt;

 

 // It is used for calculating mean

 // retrieval time

 int z = 0, j = 0;

 

 // vertical insertion on tape

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < m; j++) {

 

 // initialize variables to

 // 0 for each iteration

 sum = 0;

 

 // Used for getting 'sum' sizes

 // of records in tape to determine

 // whether tape is full or not

 for (int k = 0; k < i; k++) {

 sum += v[j][k];

 }

 

 // if tape is not full

 if (sum + records[z] <= tape[j]) {

 v[j][i] = records[z];

 z++;

 }

 }

 

 // check for ability of tapes to hold

 // value

 if (v[2][i] == 0) {

 break;

 }

 }

 

 for (int i = 0; i < m; i++) {

 

 // initialize variables to 0 for each

 // iteration

 Retrieval_Time = 0;

 

 // display elements of tape

 cout << "tape " << i + 1 << " : [ ";

 for (j = 0; j < n; j++) {

 

 if (v[i][j] != 0) {

 cout << v[i][j] << " ";

 }

 else {

 break;

 }

 }

 cout << "]";

 

 // calculating total retrieval time

 for (int k = 0; v[i][k] != 0; k++) {

 // MRT formula

 Retrieval_Time += v[i][k] * (j - k);

 }

 

 // calculating mean retrieval time

 // using formula

 Mrt = (double)Retrieval_Time / j;

 

 // v.size() is function of vector is used

 // to get size of vector

 cout << "\tMRT : " << Mrt << endl;

 }

}

 

// Driver Code

int main()

{

 int records[] = { 15, 2, 8, 23, 45, 50, 60, 120 };

 int tape[] = { 25, 80, 160 };

 

 // store the size of records[]

 int n = sizeof(records) / sizeof(records[0]);

 

 // store the size of tapes[]

 int m = sizeof(tape) / sizeof(tape[0]);

 

 // sorting of an array is required to

 // attain greedy approach of

 // algorithm

 sort(records, records + n);

 vertical_Fill(records, tape, m, n);

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

// Java program to print Vertical filling

import java.util.*;

 

class GFG

{

 

static void vertical_Fill(int records[], int tape[],

 int m, int n)

{

 // 2D matrix for vertical insertion on

 // tapes

 int [][]v = new int[m][n];

 

 // It is used for checking whether tape

 // is full or not

 int sum = 0;

 

 // It is used for calculating total

 // retrieval time

 int Retrieval_Time = 0;

 

 // It is used for calculating mean

 // retrieval time

 double Mrt;

 

 // It is used for calculating mean

 // retrieval time

 int z = 0, j = 0;

 

 // vertical insertion on tape

 for (int i = 0; i < n; i++)

 {

 for (j = 0; j < m; j++)

 {

 

 // initialize variables to

 // 0 for each iteration

 sum = 0;

 

 // Used for getting 'sum' sizes

 // of records in tape to determine

 // whether tape is full or not

 for (int k = 0; k < i; k++) 

 {

 sum += v[j][k];

 }

 

 // if tape is not full

 if (sum + records[z] <= tape[j])

 {

 v[j][i] = records[z];

 z++;

 }

 }

 

 // check for ability of tapes to hold

 // value

 if (v[2][i] == 0) 

 {

 break;

 }

 }

 

 for (int i = 0; i < m; i++) 

 {

 

 // initialize variables to 0 for each

 // iteration

 Retrieval_Time = 0;

 

 // display elements of tape

 System.out.print("tape " + (i + 1)+ " : [ ");

 for (j = 0; j < n; j++)

 {

 

 if (v[i][j] != 0)

 {

 System.out.print(v[i][j]+ " ");

 }

 else

 {

 break;

 }

 }

 System.out.print("]");

 

 // calculating total retrieval time

 for (int k = 0; v[i][k] != 0; k++)

 {

 

 // MRT formula

 Retrieval_Time += v[i][k] * (j - k);

 }

 

 // calculating mean retrieval time

 // using formula

 Mrt = (double)Retrieval_Time / j;

 

 // v.size() is function of vector is used

 // to get size of vector

 System.out.print("\tMRT : " + Mrt +"\n");

 }

}

 

// Driver Code

public static void main(String[] args)

{

 int records[] = { 15, 2, 8, 23, 45, 50, 60,
120 };

 int tape[] = { 25, 80, 160 };

 

 // store the size of records[]

 int n = records.length;

 

 // store the size of tapes[]

 int m = tape.length;

 

 // sorting of an array is required to

 // attain greedy approach of

 // algorithm

 Arrays.sort(records);

 vertical_Fill(records, tape, m, n);

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

# Python3 program to print Vertical filling

import numpy as np

 

def vertical_Fill(records, tape, m, n) : 

 

 # 2D matrix for vertical insertion on 

 # tapes 

 v = np.zeros((m, n)) ;

 

 # It is used for checking whether tape 

 # is full or not 

 sum = 0; 

 

 # It is used for calculating total 

 # retrieval time 

 Retrieval_Time = 0; 

 

 # It is used for calculating mean 

 # retrieval time 

 Mrt = None; 

 

 # It is used for calculating mean 

 # retrieval time 

 z = 0; j = 0; 

 

 # vertical insertion on tape 

 for i in range(n) :

 for j in range(m) :

 

 # initialize variables to 

 # 0 for each iteration 

 sum = 0; 

 

 # Used for getting 'sum' sizes 

 # of records in tape to determine 

 # whether tape is full or not 

 for k in range(i) :

 sum += v[j][k]; 

 

 # if tape is not full 

 if (sum + records[z] <= tape[j]) :

 v[j][i] = records[z]; 

 z += 1; 

 

 # check for ability of tapes to hold 

 # value 

 if (v[2][i] == 0) :

 break; 

 

 for i in range(m) :

 

 # initialize variables to 0 for each 

 # iteration 

 Retrieval_Time = 0; 

 

 # display elements of tape 

 print("tape" , i + 1 ,": [", end = ""); 

 for j in range(n) :

 

 if (v[i][j] != 0) :

 print(v[i][j], end= " "); 

 

 else :

 break; 

 

 print("]", end="");

 

 k = 0;

 

 # calculating total retrieval time 

 while v[i][k] != 0 :

 

 # MRT formula 

 Retrieval_Time += v[i][k] * (j - k);

 k += 1;

 

 # calculating mean retrieval time

 # using formula

 Mrt = Retrieval_Time / j; 

 

 # v.size() is function of vector is used 

 # to get size of vector 

 print("MRT :", Mrt);

 

# Driver Code 

if __name__ == "__main__" : 

 

 records = [ 15, 2, 8, 23, 45, 50, 60,
120 ]; 

 tape = [ 25, 80, 160 ]; 

 

 # store the size of records[] 

 n = len(records); 

 

 # store the size of tape[] 

 m = len(tape); 

 

 # sorting of an array is required to 

 # attain greedy approach of 

 # algorithm 

 records.sort(); 

 vertical_Fill(records, tape, m, n);

 

# This code is contributed by AnkitRai01  
  
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

// C# program to print Vertical filling

using System;

 

class GFG

{

 

static void vertical_Fill(int []records, int []tape,

 int m, int n)

{

 // 2D matrix for vertical insertion on

 // tapes

 int [,]v = new int[m, n];

 

 // It is used for checking whether tape

 // is full or not

 int sum = 0;

 

 // It is used for calculating total

 // retrieval time

 int Retrieval_Time = 0;

 

 // It is used for calculating mean

 // retrieval time

 double Mrt;

 

 // It is used for calculating mean

 // retrieval time

 int z = 0, j = 0;

 

 // vertical insertion on tape

 for (int i = 0; i < n; i++)

 {

 for (j = 0; j < m; j++)

 {

 

 // initialize variables to

 // 0 for each iteration

 sum = 0;

 

 // Used for getting 'sum' sizes

 // of records in tape to determine

 // whether tape is full or not

 for (int k = 0; k < i; k++) 

 {

 sum += v[j, k];

 }

 

 // if tape is not full

 if (sum + records[z] <= tape[j])

 {

 v[j, i] = records[z];

 z++;

 }

 }

 

 // check for ability of tapes to hold

 // value

 if (v[2, i] == 0) 

 {

 break;

 }

 }

 

 for (int i = 0; i < m; i++) 

 {

 

 // initialize variables to 0 for each

 // iteration

 Retrieval_Time = 0;

 

 // display elements of tape

 Console.Write("tape " + (i + 1) + " : [ ");

 for (j = 0; j < n; j++)

 {

 

 if (v[i, j] != 0)

 {

 Console.Write(v[i, j]+ " ");

 }

 else

 {

 break;

 }

 }

 Console.Write("]");

 

 // calculating total retrieval time

 for (int k = 0; v[i, k] != 0; k++)

 {

 

 // MRT formula

 Retrieval_Time += v[i, k] * (j - k);

 }

 

 // calculating mean retrieval time

 // using formula

 Mrt = (double)Retrieval_Time / j;

 

 // v.Count is function of vector is used

 // to get size of vector

 Console.Write("\tMRT : " + Mrt +"\n");

 }

}

 

// Driver Code

public static void Main(String[] args)

{

 int []records = { 15, 2, 8, 23, 45, 50, 60, 120 };

 int []tape = { 25, 80, 160 };

 

 // store the size of records[]

 int n = records.Length;

 

 // store the size of tapes[]

 int m = tape.Length;

 

 // sorting of an array is required to

 // attain greedy approach of

 // algorithm

 Array.Sort(records);

 vertical_Fill(records, tape, m, n);

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    tape 1 : [ 2 23 ]    MRT : 13.5
    tape 2 : [ 8 45 ]    MRT : 30.5
    tape 3 : [ 15 50 60 ]    MRT : 68.3333
    

Comparing both the results we can use a particular tape filling technique
which provides the best results(minimum MRT).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

