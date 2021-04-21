Count of ways to traverse a Matrix according to given conditions



Given an integer **N** which represents an **N x N** Square Matrix, the task
is to print the number of ways to move from top left to the bottom right of
the Square Matrix by following the conditions:

  * If the current position of the pointer is at the edges of the Square Matrix, then the next move can either be a vertical or a horizontal movement, any number of steps (Like a **rook** on the chessboard).
  * If the current position of the pointer is at the diagonals of the Square Matrix, then the next move should also lie on the diagonal. (Like a **bishop** on the chessboard).
  * If the current position of the pointer is at any other place than the above two, then the next possible step can be in any way like a **knight** moves on a chessboard but the row and column of the new position > row and column of the old position.

 **Examples:**

> **Input:** N = 2  
> **Output:** 3  
> **Explanation:**  
> The three possible ways are:  
> {0-0} – {0-1} – {1-1}  
> {0-0} – {1-0} – {1-1}  
> {0-0} – {1-1}  
> **Input:** 3  
> **Output:** 18  
> **Explanation:**  
> The possible ways are:  
> {0-0} – {2-1} – {2-2}  
> {0-0} – {1-2} – {2-2}  
> {0-0} – {0-1} – {2-2}  
> {0-0} – {0-1} – {0-2} – {1-2} – {2-2}  
> {0-0} – {0-1} – {0-2} – {2-2}  
> {0-0} – {0-1} – {1-1} – {2-2}  
> {0-0} – {0-1} – {2-1} – {2-2}  
> {0-0} – {0-2} – {1-2} – {2-2}  
> {0-0} – {0-2} – {2-2}  
> {0-0} – {1-0} – {2-2}  
> {0-0} – {1-0} – {1-1} – {2-2}  
> {0-0} – {1-0} – {1-2} – {2-2}  
> {0-0} – {1-0} – {2-0} – {2-1} – {2-2}  
> {0-0} – {1-0} – {2-0} – {2-2}  
> {0-0} – {2-0} – {2-1} – {2-2}  
> {0-0} – {2-0} – {2-2}  
> {0-0} – {1-1} – {2-2}  
> {0-0} – {2-2}

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to recursively check for every possible case
whether it reaches the end of the Square Matrix or not. To do this, a
recursive function is defined which takes the current position and the last
position as the input parameters. The following are the conditions of the
recursive function:

  * **Base Case:** The base case of the function is to check if the current pointer has reached the bottom right position in the Square Matrix. If reached, then the counter **count** which keeps the note of the total number of ways is incremented. If the last position cannot be reached, then the function should be stopped and shouldn’t be called for the next iteration. This is implemented as: 

    
    
    if (cr == er && cc == ec) {
        count++;
        return;
    }
    
    if (cr > er || cc > ec) {
       return;
    }
    

  * **Recursive Case:** Given that three types of traversals are possible. Therefore, the recursive case is to recursively call the function by checking if the current position. If the current position is at the edges of the Square Matrix, then the pointer can be moved only horizontally or vertically. And for every subsequent vertical traversal, two more choices of horizontal and vertical traversals are possible. Therefore, in order to keep a track of the total number of ways, both of these are called recursively in a loop. 

    
    
    for (int i = 1; i <= er; i++) {
        if (cc == 0 || cr == 0 
           || cr == er || cc == ec) {
            chessboard1(cr, cc + i, er, ec);
        }
    }
    
    for (int i = 1; i <= er; i++) {
        if (cc == 0 || cr == 0 
           || cr == er || cc == ec) {
            chessboard1(cr + i, cc, er, ec);
        }
    }
    

  * Apart from this, if the current pointer is at the diagonals, then the pointer can move diagonally. However, for every subsequent diagonal traversal, another set of subsequent diagonals are possible. Therefore, in order to keep a track of the total number of ways, a for loop is used to recursively call the function.   

    
    
    for (int i = 1; i <= er; i++) {
        if (cr == cc || cr + cc == er) {
            chessboard1(cr + i, cc + i,
                        er, ec);
        }
    }
    

  * If none of the above cases is satisfied, then the next position can be moved in such a way that:
    * new row is > old row.
    * new column > old column.
  * After executing the above function, the value stored in the **count** variable is the total number of ways to traverse the Square Matrix.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count the number

// of ways to traverse the given

// N x N Square Matrix recursively

#include<bits/stdc++.h>

using namespace std;

 

// Variable to store the

// total number of ways to

// traverse the Square Matrix

 

// Function to recursively

// count the total number

// of ways to traverse the

// given N x N Square Matrix

void chessboard1(int cr, int cc,

 int er, int ec,

 int& count)

{

 // If the last index has been

 // reached, then the count is

 // incremented and returned

 if (cr == er && cc == ec)

 {

 count++;

 return;

 }

 // If the last index cannot

 // be reached

 if (cr > er || cc > ec)

 {

 return;

 }

 // If the current position is

 // neither on the edges nor

 // on the diagonal, then the

 // pointer moves like a knight

 chessboard1(cr + 2, cc + 1,

 er, ec,count);

 chessboard1(cr + 1, cc + 2,

 er, ec,count);

 // If the pointer is on the

 // edges of the Square Matrix

 // next move can be horizontal

 // or vertical

 // This for loop is used to include

 // all the horizontal traversal cases

 // recursively

 for (int i = 1; i <= er; i++)

 {

 if (cc == 0 || cr == 0||

 cr == er || cc == ec)

 {

 chessboard1(cr, cc + i,

 er, ec,count);

 }

 }

 // This for loop is used to include

 // all the vertical traversal cases

 // recursively

 for (int i = 1; i <= er; i++)

 {

 if (cc == 0 || cr == 0||

 cr == er || cc == ec)

 {

 chessboard1(cr + i, cc,

 er, ec,count);

 }

 }

 // If the pointer is on the

 // diagonal of the Square Matrix

 // next move is also diagonal.

 // For loop is used to include

 // all the diagonal traversal cases.

 for (int i = 1; i <= er; i++)

 {

 if (cr == cc || cr + cc == er)

 {

 chessboard1(cr + i, cc + i, 

 er, ec, count);

 }

 }

}

 

// Driver code

int main()

{

 int N = 3;

 int count=0;

 chessboard1(0, 0, N - 1, N - 1,count);

 cout<<count;

}

// This code is contributed by chahattekwani71  
  
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

// Java program to count the number

// of ways to traverse the given

// N x N Square Matrix recursively

public class GFG {

 // Variable to store the total number

 // of ways to traverse the Square Matrix

 static int count = 0;

 // Function to recursively

 // count the total number

 // of ways to traverse the

 // given N x N Square Matrix

 public static void chessboard1(

 int cr, int cc,

 int er, int ec)

 {

 // If the last index has been reached, then

 // the count is incremented and returned

 if (cr == er && cc == ec) {

 count++;

 return;

 }

 // If the last index cannot be reached

 if (cr > er || cc > ec) {

 return;

 }

 // If the current position is neither

 // on the edges nor on the diagonal,

 // then the pointer moves

 // like a knight

 chessboard1(cr + 2, cc + 1, er, ec);

 chessboard1(cr + 1, cc + 2, er, ec);

 // If the pointer is on the

 // edges of the Square Matrix

 // next move can be horizontal or vertical

 // This for loop is used to include all the

 // horizontal traversal cases recursively

 for (int i = 1; i <= er; i++) {

 if (cc == 0 || cr == 0

 || cr == er || cc == ec) {

 chessboard1(cr, cc + i, er, ec);

 }

 }

 // This for loop is used to include all the

 // vertical traversal cases recursively

 for (int i = 1; i <= er; i++) {

 if (cc == 0 || cr == 0

 || cr == er || cc == ec) {

 chessboard1(cr + i, cc, er, ec);

 }

 }

 // If the pointer is on the

 // diagonal of the Square Matrix

 // next move is also diagonal.

 // For loop is used to include

 // all the diagonal traversal cases.

 for (int i = 1; i <= er; i++) {

 if (cr == cc

 || cr + cc == er) {

 chessboard1(cr + i,

 cc + i,

 er, ec);

 }

 }

 }

 // Driver code

 public static void main(String[] args)

 {

 int N = 3;

 chessboard1(0, 0, N - 1, N - 1);

 System.out.println(count);

 }

}  
  
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

// C# program to count the number

// of ways to traverse the given

// N x N Square Matrix recursively

using System;

class GFG{

// Variable to store the total number

// of ways to traverse the Square Matrix

static int count = 0;

// Function to recursively

// count the total number

// of ways to traverse the

// given N x N Square Matrix

public static void chessboard1(int cr, int cc,

 int er, int ec)

{

 

 // If the last index has been reached, then

 // the count is incremented and returned

 if (cr == er && cc == ec)

 {

 count++;

 return;

 }

 // If the last index cannot be reached

 if (cr > er || cc > ec)

 {

 return;

 }

 // If the current position is neither

 // on the edges nor on the diagonal,

 // then the pointer moves

 // like a knight

 chessboard1(cr + 2, cc + 1, er, ec);

 chessboard1(cr + 1, cc + 2, er, ec);

 // If the pointer is on the edges

 // of the Square Matrix next move

 // can be horizontal or vertical

 // This for loop is used to include all the

 // horizontal traversal cases recursively

 for(int i = 1; i <= er; i++)

 {

 if (cc == 0 || cr == 0 ||

 cr == er || cc == ec)

 {

 chessboard1(cr, cc + i, er, ec);

 }

 }

 

 // This for loop is used to include all the

 // vertical traversal cases recursively

 for(int i = 1; i <= er; i++)

 {

 if (cc == 0 || cr == 0 ||

 cr == er || cc == ec)

 {

 chessboard1(cr + i, cc, er, ec);

 }

 }

 

 // If the pointer is on the

 // diagonal of the Square Matrix

 // next move is also diagonal.

 // For loop is used to include

 // all the diagonal traversal cases.

 for(int i = 1; i <= er; i++)

 {

 if (cr == cc || cr + cc == er)

 {

 chessboard1(cr + i, cc + i,

 er, ec);

 }

 }

}

// Driver code

public static void Main(string[] args)

{

 int N = 3;

 

 chessboard1(0, 0, N - 1, N - 1);

 

 Console.Write(count);

}

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output :**

    
    
    18
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

