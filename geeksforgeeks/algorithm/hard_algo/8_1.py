Maximum area of triangle having different vertex colors



Given a matrix of **N** rows and **M** columns, consists of three value {r, g,
b}. The task is to find the area of the largest triangle that has one side
parallel to y-axis i.e vertical and the color of all three vertices are
different.

 **Examples:**

    
    
    **Input :** N = 4, M =5
      mat[][] =
      {
      r, r, r, r, r,
      r, r, r, r, g,
      r, r, r, r, r,
      b, b, b, b, b,
      }
    **Output :** 10
    The maximum area of triangle is 10.
    Triangle coordinates are (0,0) containing r, (1,4) containing g, (3,0) containing b.
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/maximum-area-of-triangle-having-different-vertex-colors.png)
    
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We know area of a triangle = 1/2 * base *height, so we need to maximize the
base and height of the triangle. Since one side is parallel to the y-axis, we
can consider that side as the base of the triangle.

To maximize base, we can find the first and last occurrence of {r, g, b} for
each column. So we have two sets of 3 values for each column. For base in any
column, one vertex is from the first set and the second vertex from the second
set such that they have different values.

  

  

To maximize height, for any column as a base, the third vertex must be chosen
such that the vertex should be farthest from the column, on the left or right
side of the column having a value different from the other two vertices.  
Now for each column find the maximum area of the triangle.

Below is the implementation of this approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find maximum area of triangle

// having different vertex color in a matrix.

#include<bits/stdc++.h>

using namespace std;

#define R 4

#define C 5

 

// return the color value so that their corresponding

// index can be access.

int mapcolor(char c)

{

 if (c == 'r')

 return 0;

 else if (c == 'g')

 return 1;

 else if (c == 'b')

 return 2;

}

 

// Returns the maximum area of triangle from all

// the possible triangles

double findarea(char mat[R][C], int r, int c,

 int top[3][C], int bottom[3][C],

 int left[3], int right[3])

{

 double ans = (double)1;

 

 // for each column

 for (int i = 0; i < c; i++)

 

 // for each top vertex

 for (int x = 0; x < 3; x++)

 

 // for each bottom vertex

 for (int y = 0; y < 3; y++)

 {

 // finding the third color of

 // vertex either on right or left.

 int z = 3 - x - y;

 

 // finding area of triangle on left side of column.

 if (x != y && top[x][i] != INT_MAX &&

 bottom[y][i] != INT_MIN && left[z] != INT_MAX)

 {

 ans = max(ans, ((double)1/(double)2) *

 (bottom[y][i] - top[x][i]) *

 (i - left[z]));

 }

 

 // finding area of triangle on right side of column.

 if (x != y && top[x][i] != INT_MAX &&

 bottom[y][i] != INT_MIN &&

 right[z] != INT_MIN)

 {

 ans = max(ans, ((double)1/(double)2) *

 (bottom[y][i] - top[x][i]) *

 (right[z] - i));

 }

 }

 

 return ans;

}

 

// Precompute the vertices of top, bottom, left

// and right and then computing the maximum area.

double maxarea(char mat[R][C], int r, int c)

{

 int left[3], right[3];

 int top[3][C], bottom[3][C];

 memset(left, INT_MAX, sizeof left);

 memset(right, INT_MIN, sizeof right);

 memset(top, INT_MAX, sizeof top);

 memset(bottom, INT_MIN, sizeof bottom);

 

 // finding the r, b, g cells for the left

 // and right vertices.

 for (int i = 0; i < r; i++)

 {

 for (int j = 0; j < c; j++)

 {

 left[mapcolor(mat[i][j])] =

 min(left[mapcolor(mat[i][j])], j);

 right[mapcolor(mat[i][j])] =

 max(left[mapcolor(mat[i][j])], j);

 }

 }

 

 // finsing set of {r, g, b} of top and

 // bottom for each column.

 for (int j = 0; j < c; j++)

 {

 for( int i = 0; i < r; i++)

 {

 top[mapcolor(mat[i][j])][j] =

 min(top[mapcolor(mat[i][j])][j], i);

 bottom[mapcolor(mat[i][j])][j] =

 max(bottom[mapcolor(mat[i][j])][j], i);

 }

 }

 

 return findarea(mat, R, C, top, bottom, left, right);

}

 

// Driven Program

int main()

{

 char mat[R][C] =

 {

 'r', 'r', 'r', 'r', 'r',

 'r', 'r', 'r', 'r', 'g',

 'r', 'r', 'r', 'r', 'r',

 'b', 'b', 'b', 'b', 'b',

 };

 

 cout << maxarea(mat, R, C) << endl;

 return 0;

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

# Python3 program to find the maximum

# area of triangle having different 

# vertex color in a matrix. 

 

# Return the color value so that their 

# corresponding index can be access. 

def mapcolor(c): 

 

 if c == 'r': 

 return 0

 elif c == 'g':

 return 1

 elif c == 'b':

 return 2

 

# Returns the maximum area of triangle 

# from all the possible triangles 

def findarea(mat, r, c, top, 

 bottom, left, right): 

 

 ans = 1

 

 # for each column 

 for i in range(0, c): 

 

 # for each top vertex 

 for x in range(0, 3): 

 

 # for each bottom vertex 

 for y in range(0, 3): 

 

 # finding the third color of 

 # vertex either on right or left. 

 z = 3 - x - y 

 

 # finding area of triangle on 

 # left side of column. 

 if (x != y and top[x][i] != INT_MAX and

 bottom[y][i] != INT_MIN and

 left[z] != INT_MAX): 

 

 ans = max(ans, 0.5 * (bottom[y][i] -

 top[x][i]) * (i - left[z]))

 

 # finding area of triangle on right side of column. 

 if (x != y and top[x][i] != INT_MAX and

 bottom[y][i] != INT_MIN and

 right[z] != INT_MIN):

 

 ans = max(ans, 0.5 * (bottom[y][i] -

 top[x][i]) * (right[z] - i))

 

 return ans 

 

# Precompute the vertices of top, bottom, left 

# and right and then computing the maximum area. 

def maxarea(mat, r, c): 

 

 left = [-1] * 3

 right = [0] * 3

 top = [[-1 for i in range(C)] 

 for j in range(3)]

 bottom = [[0 for i in range(C)] 

 for j in range(3)]

 

 # finding the r, b, g cells for 

 # the left and right vertices. 

 for i in range(0, r): 

 

 for j in range(0, c): 

 

 left[mapcolor(mat[i][j])] = \

 min(left[mapcolor(mat[i][j])], j)

 

 right[mapcolor(mat[i][j])] = \

 max(left[mapcolor(mat[i][j])], j) 

 

 # finsing set of r, g, b of top 

 # and bottom for each column. 

 for j in range(0, c): 

 

 for i in range(0, r): 

 

 top[mapcolor(mat[i][j])][j] = \

 min(top[mapcolor(mat[i][j])][j], i)

 

 bottom[mapcolor(mat[i][j])][j] = \

 max(bottom[mapcolor(mat[i][j])][j], i)

 

 return int(findarea(mat, R, C, top, 

 bottom, left, right)) 

 

# Driver Code

if __name__ == "__main__":

 

 R, C = 4, 5

 mat = [['r', 'r', 'r', 'r', 'r'], 

 ['r', 'r', 'r', 'r', 'g'], 

 ['r', 'r', 'r', 'r', 'r'], 

 ['b', 'b', 'b', 'b', 'b']] 

 

 INT_MAX, INT_MIN = float('inf'), float('-inf')

 print(maxarea(mat, R, C))

 

# This code is contributed by Rituraj Jain  
  
---  
  
 __

 __

 **Output:**

    
    
    10
    

**Time Complexity :** O(M * N).

 **Source:** http://stackoverflow.com/questions/40078660/maximum-area-of-
triangle-having-all-vertices-of-different-color

This article is contributed by **Anuj Chauhan(anuj0503)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

