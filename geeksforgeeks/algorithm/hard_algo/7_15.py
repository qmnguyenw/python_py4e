Minimum steps to reach target by a Knight | Set 2



Given a square chessboard of N x N size, the position of Knight and position
of a target is given, the task is to find out the minimum steps a Knight will
take to reach the target position.

![](https://media.geeksforgeeks.org/wp-content/uploads/KnightChess.jpg)

Examples :

    
    
    Input : (2, 4) - knight's position, (6, 4) - target cell
    Output : 2
    
    Input : (4, 5) (1, 1)
    Output : 3
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A BFS approach to solve the above problem has already been discussed in the
previous post. In this a post, a Dynamic Programming solution is discussed.

  

  

 **Explanation of the approach :**

  *  **Case 1 :** If target is not along one row or one column of knight’s position.  
Let a chess board of 8 x 8 cell. Now, let say knight is at (3, 3) and the
target is at (7, 8). There are possible 8 moves from the current position of
knight i.e. (2, 1), (1, 2), (4, 1), (1, 4), (5, 2), (2, 5), (5, 4), (4, 5).
But, among these only two moves (5, 4) and (4, 5) will be towards the target
and all other goes away from the target. So, for finding minimum steps go to
either (4, 5) or (5, 4). Now, calculate the minimum steps taken from (4, 5)
and (5, 4) to reach the target. This is calculated by dynamic programming.
Thus, this results in the minimum steps from (3, 3) to (7, 8).

  *  **Case 2 :** If the target is along one row or one column of knight’s position.  
Let a chess board of 8 x 8 cell. Now, let’s say knight is at (4, 3) and the
target is at (4, 7). There are possible 8 moves but towards the target, there
are only 4 moves i.e. (5, 5), (3, 5), (2, 4), (6, 4). As, (5, 5) is equivalent
to (3, 5) and (2, 4) is equivalent to (6, 4). So, from these 4 points, it can
be converted into 2 points. Taking (5, 5) and (6, 4) (here). Now, calculate
the minimum steps taken from these two points to reach the target. This is
calculated by dynamic programming. Thus, this results in the minimum steps
from (4, 3) to (4, 7).

 **Exception :** When the knight will be at corner and the target is such that
the difference of x and y coordinates with knight’s position is (1, 1) or
vice-versa. Then minimum steps will be 4.

 **Dynamic Programming Equation :**

> 1) **dp[diffOfX][diffOfY]** is the minimum steps taken from knight’s
> position to target’s position.
>
> 2) **dp[diffOfX][diffOfY] = dp[diffOfY][diffOfX]**.
>
> where, diffOfX = difference between knight’s x-coordinate and target’s
> x-coordinate  
> diffOfY = difference between knight’s y-coordinate and target’s y-coordinate

Below is the implementation of above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code for minimum steps for

// a knight to reach target position

#include <bits/stdc++.h>

 

using namespace std;

 

// initializing the matrix.

int dp[8][8] = { 0 };

 

int getsteps(int x, int y, 

 int tx, int ty)

{

 // if knight is on the target 

 // position return 0.

 if (x == tx && y == ty)

 return dp[0][0];

 else {

 

 // if already calculated then return

 // that value. Taking absolute difference.

 if (dp[abs(x - tx)][abs(y - ty)] != 0)

 return dp[abs(x - tx)][abs(y - ty)];

 

 else {

 

 // there will be two distinct positions

 // from the knight towards a target.

 // if the target is in same row or column

 // as of knight than there can be four

 // positions towards the target but in that

 // two would be the same and the other two

 // would be the same.

 int x1, y1, x2, y2;

 

 // (x1, y1) and (x2, y2) are two positions.

 // these can be different according to situation.

 // From position of knight, the chess board can be

 // divided into four blocks i.e.. N-E, E-S, S-W, W-N .

 if (x <= tx) {

 if (y <= ty) {

 x1 = x + 2;

 y1 = y + 1;

 x2 = x + 1;

 y2 = y + 2;

 } else {

 x1 = x + 2;

 y1 = y - 1;

 x2 = x + 1;

 y2 = y - 2;

 }

 } else {

 if (y <= ty) {

 x1 = x - 2;

 y1 = y + 1;

 x2 = x - 1;

 y2 = y + 2;

 } else {

 x1 = x - 2;

 y1 = y - 1;

 x2 = x - 1;

 y2 = y - 2;

 }

 }

 

 // ans will be, 1 + minimum of steps 

 // required from (x1, y1) and (x2, y2).

 dp[abs(x - tx)][abs(y - ty)] = 

 min(getsteps(x1, y1, tx, ty), 

 getsteps(x2, y2, tx, ty)) + 1;

 

 // exchanging the coordinates x with y of both

 // knight and target will result in same ans.

 dp[abs(y - ty)][abs(x - tx)] = 

 dp[abs(x - tx)][abs(y - ty)];

 return dp[abs(x - tx)][abs(y - ty)];

 }

 }

}

 

// Driver Code

int main()

{

 int i, n, x, y, tx, ty, ans;

 

 // size of chess board n*n

 n = 100;

 

 // (x, y) coordinate of the knight.

 // (tx, ty) coordinate of the target position.

 x = 4;

 y = 5;

 tx = 1;

 ty = 1;

 

 // (Exception) these are the four corner points 

 // for which the minimum steps is 4.

 if ((x == 1 && y == 1 && tx == 2 && ty == 2) || 

 (x == 2 && y == 2 && tx == 1 && ty == 1))

 ans = 4;

 else if ((x == 1 && y == n && tx == 2 && ty == n - 1) ||

 (x == 2 && y == n - 1 && tx == 1 && ty == n))

 ans = 4;

 else if ((x == n && y == 1 && tx == n - 1 && ty == 2) || 

 (x == n - 1 && y == 2 && tx == n && ty == 1))

 ans = 4;

 else if ((x == n && y == n && tx == n - 1 && ty == n - 1) || 

 (x == n - 1 && y == n - 1 && tx == n && ty == n))

 ans = 4;

 else {

 // dp[a][b], here a, b is the difference of

 // x & tx and y & ty respectively.

 dp[1][0] = 3;

 dp[0][1] = 3;

 dp[1][1] = 2;

 dp[2][0] = 2;

 dp[0][2] = 2;

 dp[2][1] = 1;

 dp[1][2] = 1;

 

 ans = getsteps(x, y, tx, ty);

 }

 

 cout << ans << endl;

 

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

//Java code for minimum steps for

// a knight to reach target position 

public class GFG {

 

// initializing the matrix. 

 static int dp[][] = new int[8][8];

 

 static int getsteps(int x, int y,

 int tx, int ty) {

 // if knight is on the target 

 // position return 0. 

 if (x == tx && y == ty) {

 return dp[0][0];

 } else // if already calculated then return 

 // that value. Taking absolute difference. 

 if (dp[ Math.abs(x - tx)][ Math.abs(y - ty)] != 0) {

 return dp[ Math.abs(x - tx)][ Math.abs(y - ty)];

 } else {

 

 // there will be two distinct positions 

 // from the knight towards a target. 

 // if the target is in same row or column 

 // as of knight than there can be four 

 // positions towards the target but in that 

 // two would be the same and the other two 

 // would be the same. 

 int x1, y1, x2, y2;

 

 // (x1, y1) and (x2, y2) are two positions. 

 // these can be different according to situation. 

 // From position of knight, the chess board can be 

 // divided into four blocks i.e.. N-E, E-S, S-W, W-N . 

 if (x <= tx) {

 if (y <= ty) {

 x1 = x + 2;

 y1 = y + 1;

 x2 = x + 1;

 y2 = y + 2;

 } else {

 x1 = x + 2;

 y1 = y - 1;

 x2 = x + 1;

 y2 = y - 2;

 }

 } else if (y <= ty) {

 x1 = x - 2;

 y1 = y + 1;

 x2 = x - 1;

 y2 = y + 2;

 } else {

 x1 = x - 2;

 y1 = y - 1;

 x2 = x - 1;

 y2 = y - 2;

 }

 

 // ans will be, 1 + minimum of steps 

 // required from (x1, y1) and (x2, y2). 

 dp[ Math.abs(x - tx)][ Math.abs(y - ty)]

 = Math.min(getsteps(x1, y1, tx, ty),

 getsteps(x2, y2, tx, ty)) + 1;

 

 // exchanging the coordinates x with y of both 

 // knight and target will result in same ans. 

 dp[ Math.abs(y - ty)][ Math.abs(x - tx)]

 = dp[ Math.abs(x - tx)][ Math.abs(y - ty)];

 return dp[ Math.abs(x - tx)][ Math.abs(y - ty)];

 }

 }

 

// Driver Code 

 static public void main(String[] args) {

 int i, n, x, y, tx, ty, ans;

 

 // size of chess board n*n 

 n = 100;

 

 // (x, y) coordinate of the knight. 

 // (tx, ty) coordinate of the target position. 

 x = 4;

 y = 5;

 tx = 1;

 ty = 1;

 

 // (Exception) these are the four corner points 

 // for which the minimum steps is 4. 

 if ((x == 1 && y == 1 && tx == 2 && ty == 2)

 || (x == 2 && y == 2 && tx == 1 && ty == 1)) {

 ans = 4;

 } else if ((x == 1 && y == n && tx == 2 && ty == n - 1)

 || (x == 2 && y == n - 1 && tx == 1 && ty == n)) {

 ans = 4;

 } else if ((x == n && y == 1 && tx == n - 1 && ty == 2)

 || (x == n - 1 && y == 2 && tx == n && ty == 1)) {

 ans = 4;

 } else if ((x == n && y == n && tx == n - 1 && ty == n - 1)

 || (x == n - 1 && y == n - 1 && tx == n && ty == n)) {

 ans = 4;

 } else {

 // dp[a][b], here a, b is the difference of 

 // x & tx and y & ty respectively. 

 dp[1][0] = 3;

 dp[0][1] = 3;

 dp[1][1] = 2;

 dp[2][0] = 2;

 dp[0][2] = 2;

 dp[2][1] = 1;

 dp[1][2] = 1;

 

 ans = getsteps(x, y, tx, ty);

 }

 

 System.out.println(ans);

 }

}

 

/*This code is contributed by PrinciRaj1992*/  
  
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

# Python3 code for minimum steps for

# a knight to reach target position

 

# initializing the matrix.

dp = [[0 for i in range(8)] for j in
range(8)];

 

 

def getsteps(x, y, tx, ty):

 

 # if knight is on the target

 # position return 0.

 if (x == tx and y == ty):

 return dp[0][0];

 

 # if already calculated then return

 # that value. Taking absolute difference.

 elif(dp[abs(x - tx)][abs(y - ty)] != 0):

 return dp[abs(x - tx)][abs(y - ty)];

 else:

 

 # there will be two distinct positions

 # from the knight towards a target.

 # if the target is in same row or column

 # as of knight than there can be four

 # positions towards the target but in that

 # two would be the same and the other two

 # would be the same.

 x1, y1, x2, y2 = 0, 0, 0, 0;

 

 # (x1, y1) and (x2, y2) are two positions.

 # these can be different according to situation.

 # From position of knight, the chess board can be

 # divided into four blocks i.e.. N-E, E-S, S-W, W-N .

 if (x <= tx):

 if (y <= ty):

 x1 = x + 2;

 y1 = y + 1;

 x2 = x + 1;

 y2 = y + 2;

 else:

 x1 = x + 2;

 y1 = y - 1;

 x2 = x + 1;

 y2 = y - 2;

 

 elif (y <= ty):

 x1 = x - 2;

 y1 = y + 1;

 x2 = x - 1;

 y2 = y + 2;

 else:

 x1 = x - 2;

 y1 = y - 1;

 x2 = x - 1;

 y2 = y - 2;

 

 # ans will be, 1 + minimum of steps

 # required from (x1, y1) and (x2, y2).

 dp[abs(x - tx)][abs(y - ty)] = \

 min(getsteps(x1, y1, tx, ty), 

 getsteps(x2, y2, tx, ty)) + 1;

 

 # exchanging the coordinates x with y of both

 # knight and target will result in same ans.

 dp[abs(y - ty)][abs(x - tx)] = \

 dp[abs(x - tx)][abs(y - ty)];

 return dp[abs(x - tx)][abs(y - ty)];

 

# Driver Code

if __name__ == '__main__':

 

 # size of chess board n*n

 n = 100;

 

 # (x, y) coordinate of the knight.

 # (tx, ty) coordinate of the target position.

 x = 4;

 y = 5;

 tx = 1;

 ty = 1;

 

 # (Exception) these are the four corner points

 # for which the minimum steps is 4.

 if ((x == 1 and y == 1 and tx == 2 and ty
== 2) or

 (x == 2 and y == 2 and tx == 1 and ty
== 1)):

 ans = 4;

 elif ((x == 1 and y == n and tx == 2 and
ty == n - 1) or

 (x == 2 and y == n - 1 and tx == 1 and
ty == n)):

 ans = 4;

 elif ((x == n and y == 1 and tx == n - 1
and ty == 2) or

 (x == n - 1 and y == 2 and tx == n and
ty == 1)):

 ans = 4;

 elif ((x == n and y == n and tx == n - 1
and ty == n - 1)

 or (x == n - 1 and y == n - 1 and tx ==
n and ty == n)):

 ans = 4;

 else:

 

 # dp[a][b], here a, b is the difference of

 # x & tx and y & ty respectively.

 dp[1][0] = 3;

 dp[0][1] = 3;

 dp[1][1] = 2;

 dp[2][0] = 2;

 dp[0][2] = 2;

 dp[2][1] = 1;

 dp[1][2] = 1;

 

 ans = getsteps(x, y, tx, ty);

 

 print(ans);

 

# This code is contributed by PrinciRaj1992  
  
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

// C# code for minimum steps for

// a knight to reach target position 

 

using System;

public class GFG{

 

 

// initializing the matrix. 

 static int [ , ]dp = new int[8 , 8]; 

 

 static int getsteps(int x, int y, 

 int tx, int ty) { 

 // if knight is on the target 

 // position return 0. 

 if (x == tx && y == ty) { 

 return dp[0 , 0]; 

 } else // if already calculated then return 

 // that value. Taking Absolute difference. 

 if (dp[ Math. Abs(x - tx) , Math. Abs(y - ty)] != 0) { 

 return dp[ Math. Abs(x - tx) , Math. Abs(y - ty)]; 

 } else { 

 

 // there will be two distinct positions 

 // from the knight towards a target. 

 // if the target is in same row or column 

 // as of knight than there can be four 

 // positions towards the target but in that 

 // two would be the same and the other two 

 // would be the same. 

 int x1, y1, x2, y2; 

 

 // (x1, y1) and (x2, y2) are two positions. 

 // these can be different according to situation. 

 // From position of knight, the chess board can be 

 // divided into four blocks i.e.. N-E, E-S, S-W, W-N . 

 if (x <= tx) { 

 if (y <= ty) { 

 x1 = x + 2; 

 y1 = y + 1; 

 x2 = x + 1; 

 y2 = y + 2; 

 } else { 

 x1 = x + 2; 

 y1 = y - 1; 

 x2 = x + 1; 

 y2 = y - 2; 

 } 

 } else if (y <= ty) { 

 x1 = x - 2; 

 y1 = y + 1; 

 x2 = x - 1; 

 y2 = y + 2; 

 } else { 

 x1 = x - 2; 

 y1 = y - 1; 

 x2 = x - 1; 

 y2 = y - 2; 

 } 

 

 // ans will be, 1 + minimum of steps 

 // required from (x1, y1) and (x2, y2). 

 dp[ Math. Abs(x - tx) , Math. Abs(y - ty)] 

 = Math.Min(getsteps(x1, y1, tx, ty), 

 getsteps(x2, y2, tx, ty)) + 1; 

 

 // exchanging the coordinates x with y of both 

 // knight and target will result in same ans. 

 dp[ Math. Abs(y - ty) , Math. Abs(x - tx)] 

 = dp[ Math. Abs(x - tx) , Math. Abs(y - ty)]; 

 return dp[ Math. Abs(x - tx) , Math. Abs(y - ty)]; 

 } 

 } 

 

// Driver Code 

 static public void Main() { 

 int i, n, x, y, tx, ty, ans; 

 

 // size of chess board n*n 

 n = 100; 

 

 // (x, y) coordinate of the knight. 

 // (tx, ty) coordinate of the target position. 

 x = 4; 

 y = 5; 

 tx = 1; 

 ty = 1; 

 

 // (Exception) these are the four corner points 

 // for which the minimum steps is 4. 

 if ((x == 1 && y == 1 && tx == 2 && ty == 2) 

 || (x == 2 && y == 2 && tx == 1 && ty == 1)) { 

 ans = 4; 

 } else if ((x == 1 && y == n && tx == 2 && ty == n - 1) 

 || (x == 2 && y == n - 1 && tx == 1 && ty == n)) { 

 ans = 4; 

 } else if ((x == n && y == 1 && tx == n - 1 && ty == 2) 

 || (x == n - 1 && y == 2 && tx == n && ty == 1)) { 

 ans = 4; 

 } else if ((x == n && y == n && tx == n - 1 && ty == n - 1) 

 || (x == n - 1 && y == n - 1 && tx == n && ty == n)) { 

 ans = 4; 

 } else { 

 // dp[a , b], here a, b is the difference of 

 // x & tx and y & ty respectively. 

 dp[1 , 0] = 3; 

 dp[0 , 1] = 3; 

 dp[1 , 1] = 2; 

 dp[2 , 0] = 2; 

 dp[0 , 2] = 2; 

 dp[2 , 1] = 1; 

 dp[1 , 2] = 1; 

 

 ans = getsteps(x, y, tx, ty); 

 } 

 

 Console.WriteLine(ans); 

 } 

} 

 

/*This code is contributed by PrinciRaj1992*/  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

