How to check if an instance of 15 puzzle is solvable?



Given a 4×4 board with 15 tiles (every tile has one number from 1 to 15) and
one empty space. The objective is to place the numbers on tiles in order using
the empty space. We can slide four adjacent (left, right, above and below)
tiles into the empty space. For example,  

![15puzzle](https://media.geeksforgeeks.org/wp-content/uploads/15-puzzle.png)

Here X marks the spot to where the elements can be shifted and the final
configuration always remains the same the puzzle is solvable.  
In general, for a given grid of width N, we can find out check if a N*N – 1
puzzle is solvable or not by following below simple rules :  

  1. If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
  2. If N is even, puzzle instance is solvable if 
    * the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is odd.
    * the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is even.
  3. For all other cases, the puzzle instance is not solvable.

 **What is an inversion here?**  
If we assume the tiles written out in a single row (1D Array) instead of being
spread in N-rows (2D Array), a pair of tiles (a, b) form an inversion if a
appears before b but a > b.  
For above example, consider the tiles written out in a row, like this:  
2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 X  
The above grid forms only 1 inversion i.e. (2, 1).  
 **Illustration:**  

![15puz1](https://media.geeksforgeeks.org/wp-content/cdn-uploads/15puz1.png)

  

  

![15puz2](https://media.geeksforgeeks.org/wp-content/cdn-uploads/15puz2.png)

![15Puzz3](https://media.geeksforgeeks.org/wp-content/cdn-uploads/15Puzz3.png)

![15Puzz4](https://media.geeksforgeeks.org/wp-content/cdn-uploads/15Puzz4.png)

Below is a simple C++ program to check whether a given instance of 15 puzzle
is solvable or not. The program is generic and can be extended to any grid
width.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to check if a given instance of N*N-1

// puzzle is solvable or not

#include <iostream>

#define N 4

using namespace std;

// A utility function to count inversions in given

// array 'arr[]'. Note that this function can be

// optimized to work in O(n Log n) time. The idea

// here is to keep code small and simple.

int getInvCount(int arr[])

{

 int inv_count = 0;

 for (int i = 0; i < N * N - 1; i++)

 {

 for (int j = i + 1; j < N * N; j++)

 {

 // count pairs(i, j) such that i appears

 // before j, but i > j.

 if (arr[j] && arr[i] && arr[i] > arr[j])

 inv_count++;

 }

 }

 return inv_count;

}

// find Position of blank from bottom

int findXPosition(int puzzle[N][N])

{

 // start from bottom-right corner of matrix

 for (int i = N - 1; i >= 0; i--)

 for (int j = N - 1; j >= 0; j--)

 if (puzzle[i][j] == 0)

 return N - i;

}

// This function returns true if given

// instance of N*N - 1 puzzle is solvable

bool isSolvable(int puzzle[N][N])

{

 // Count inversions in given puzzle

 int invCount = getInvCount((int*)puzzle);

 // If grid is odd, return true if inversion

 // count is even.

 if (N & 1)

 return !(invCount & 1);

 else // grid is even

 {

 int pos = findXPosition(puzzle);

 if (pos & 1)

 return !(invCount & 1);

 else

 return invCount & 1;

 }

}

/* Driver program to test above functions */

int main()

{

 int puzzle[N][N] =

 {

 {12, 1, 10, 2},

 {7, 11, 4, 14},

 {5, 0, 9, 15}, // Value 0 is used for empty space

 {8, 13, 6, 3},

 };

 /*

 int puzzle[N][N] = {{1, 8, 2},

 {0, 4, 3},

 {7, 6, 5}};

 int puzzle[N][N] = {

 {13, 2, 10, 3},

 {1, 12, 8, 4},

 {5, 0, 9, 6},

 {15, 14, 11, 7},

 };

 int puzzle[N][N] = {

 {6, 13, 7, 10},

 {8, 9, 11, 0},

 {15, 2, 12, 5},

 {14, 3, 1, 4},

 };

 int puzzle[N][N] = {

 {3, 9, 1, 15},

 {14, 11, 4, 6},

 {13, 0, 10, 12},

 {2, 7, 8, 5},

 };

 */

 isSolvable(puzzle)? cout << "Solvable":

 cout << "Not Solvable";

 return 0;

}  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

//PHP program to check if a given instance of N*N-1

// puzzle is solvable or not

$N= 4;

// A utility function to count inversions in given

// array 'arr[]'. Note that this function can be

// optimized to work in O(n Log n) time. The idea

// here is to keep code small and simple.

function getInvCount( $arr)

{

 global $N;

 $inv_count = 0;

 for ($i = 0; $i < $N * $N - 1; $i++)

 {

 for ($j = $i + 1; $j < $N * $N; $j++)

 {

 // count pairs(i, j) such that i appears

 // before j, but i > j.

 $inv_count++;

 }

 }

 return $inv_count;

}

// find Position of blank from bottom

function findXPosition($puzzle)

{

 global $N;

 // start from bottom-right corner of matrix

 for ($i = $N - 1; $i >= 0; $i--)

 for ($j = $N - 1; $j >= 0; $j--)

 if ($puzzle[$i][$j] == 0)

 return $N - $i;

}

// This function returns true if given

// instance of N*N - 1 puzzle is solvable

function isSolvable( $puzzle)

{

 global $N;

 // Count inversions in given puzzle

 $invCount = getInvCount($puzzle);

 // If grid is odd, return true if inversion

 // count is even.

 if ($N & 1)

 return !($invCount & 1);

 else // grid is even

 {

 $pos = findXPosition($puzzle);

 if ($pos & 1)

 return !($invCount & 1);

 else

 return $invCount & 1;

 }

}

/* Driver program to test above functions */

 $puzzle =

 array(

 array(12, 1, 10, 2),

 array(7, 11, 4, 14),

 array(5, 0, 9, 15), // Value 0 is used for empty space

 array(8, 13, 6, 3),

 );

 

 if(isSolvable($puzzle)==0)

 

 echo "Solvable";

 else

 echo "Not Solvable";

#This code is contributed by aj_36

?>  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    Solvable
    

