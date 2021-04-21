Print a given matrix in spiral form using direction tracking method



Given a 2-D matrix **mat[][]** , the task is to print it in the spiral form.

 **Examples:**

>  **Input:** mat[][] = {  
> {1, 2, 3, 4},  
> {5, 6, 7, 8},  
> {9, 10, 11, 12},  
> {13, 14, 15, 16}}  
>  **Output:** 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
>
>  **Input:** mat[][] = {  
> {1, 2, 3, 4, 5, 6},  
> {7, 8, 9, 10, 11, 12},  
> {13, 14, 15, 16, 17, 18}}  
>  **Output:** 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be easily solved using direction method. Since
we are starting with East direction then always turning right whenever next
index is either invalid (out of matrix) or visited earlier. The directions
followed will be **East - > South -> West -> North -> …** starting from
**mat[0][0]** and ending finally when all the elements of the matrix have been
traversed.

  

  

Below is the implementation of the above approach:

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

#define R 5

#define C 5

 

enum direction { east,

 west,

 north,

 south };

 

// Function to set the new direction on turning

// right from the current direction

void turnright(enum direction& c_direction)

{

 switch (c_direction) {

 case east:

 c_direction = south;

 break;

 case west:

 c_direction = north;

 break;

 case north:

 c_direction = east;

 break;

 case south:

 c_direction = west;

 break;

 }

}

 

// Function to return the next possible cell

// indexes with current direction

pair<int, int> next(int i, int j,

 const enum direction& c_direction)

{

 switch (c_direction) {

 case east:

 j++;

 break;

 case west:

 j--;

 break;

 case north:

 i--;

 break;

 case south:

 i++;

 break;

 }

 return pair<int, int>(i, j);

}

 

// Function that returns true

// if arr[i][j] is a valid index

bool isvalid(const int& i, const int& j)

{

 if (i < R && i >= 0 && j >= 0 && j < C)

 return true;

 return false;

}

 

// Function that returns true if arr[i][j]

// has already been visited

bool alreadyVisited(int& i, int& j, int& mini, int& minj,

 int& maxi, int& maxj)

{

 

 // If inside the current bounds then

 // it has not been visited earlier

 if (i >= mini && i <= maxi && j >= minj && j <= maxj)

 return false;

 return true;

}

 

// Function to update the constraints of the matrix

void ConstraintWalls(int& mini, int& minj, int& maxi,

 int& maxj, direction c_direction)

{

 

 // Update the constraints according

 // to the direction

 switch (c_direction) {

 case east:

 mini++;

 break;

 case west:

 maxi--;

 break;

 case north:

 minj++;

 break;

 case south:

 maxj--;

 break;

 }

}

 

// Function to print the given matrix in the spiral form

void printspiral(int arr[R][C])

{

 

 // To store the count of all the indexes

 int count = 0;

 

 // Starting direction is East

 enum direction current_direction = east;

 

 // Boundary constraints in the matrix

 int mini = 0, minj = 0, maxi = R - 1, maxj = C - 1;

 int i = 0, j = 0;

 

 // While there are elements remaining

 while (count < (R * C)) {

 

 // Print the current element

 // and increment the count

 cout << arr[i][j] << " ";

 count++;

 

 // Next possible cell if direction remains the same

 pair<int, int> p = next(i, j, current_direction);

 

 // If current cell is already visited or is invalid

 if (!isvalid(p.first, p.second)

 || alreadyVisited(p.first, p.second, mini, minj, maxi, maxj)) {

 

 // If not visited earlier then only change the constraint

 if (!alreadyVisited(i, j, mini, minj, maxi, maxj))

 ConstraintWalls(mini, minj, maxi, maxj, current_direction);

 

 // Change the direction

 turnright(current_direction);

 

 // Next indexes with new direction

 p = next(i, j, current_direction);

 }

 

 // Next row and next column

 i = p.first;

 j = p.second;

 }

}

 

// Driver code

int main()

{

 int arr[R][C];

 

 // Fill the matrix

 int counter = 1;

 for (int i = 0; i < R; i++)

 for (int j = 0; j < C; j++)

 arr[i][j] = counter++;

 

 // Print the spiral form

 printspiral(arr);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    1 2 3 4 5 10 15 20 25 24 23 22 21 16 11 6 7 8 9 14 19 18 17 12 13
    

**Time Complexity:** O(R*C)  
 **Space Complexity:** O(1)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

