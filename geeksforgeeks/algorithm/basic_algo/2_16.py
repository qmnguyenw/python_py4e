Number of wins for each player in a series of Rock-Paper-Scissor game



Two players are playing a series of games of Rock–paper–scissors. There are a
total of **K** games played. Player 1 has a sequence of moves denoted by
string **A** and similarly player 2 has string **B**. If any player reaches
the end of their string, they move back to the start of the string. The task
is to count the number of games won by each of the player when exactly **K**
games are being played.

 **Examples:**

> **Input:** k = 4, a = “SR”, b = “R”  
> **Output:** 0 2  
> Game 1: Player1 = S, Player2 = R, Winner = Player2  
> Game 2: Player1 = R, Player2 = R, Winner = Draw  
> Game 3: Player1 = S, Player2 = R, Winner = Player2  
> Game 4: Player1 = R, Player2 = R, Winner = Draw
>
>  **Input:** k = 3, a = “S”, b = “SSS”  
> **Output:** 0 0  
> All the games are draws.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Let length of string **a** be **n** and length of string **b**
be **m**. The observation here is that the games would repeat after **n * m**
moves. So, we can simulate the process for **n * m** games and then count the
number of times it gets repeated. For the remaining games, we can again
simulate the process since it would be now smaller than **n * m**. For
example, in the first example above, **n = 2** and **m = 1**. So, the games
will repeat after every **n * m = 2 * 1 = 2** moves i.e. **(Player2, Draw)** ,
**(Player2, Draw)** , ….., **(Player2, Draw)**.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

// Function that returns 1 if first player wins,

// 0 in case of a draw and -1 if second player wins

int compare(char first, char second)

{

 // If both players have the same move

 // then it's a draw

 if (first == second)

 return 0;

 if (first == 'R') {

 if (second == 'S')

 return 1;

 else

 return -1;

 }

 if (first == 'P') {

 if (second == 'R')

 return 1;

 else

 return -1;

 }

 if (first == 'S') {

 if (second == 'P')

 return 1;

 else

 return -1;

 }

}

// Function that returns the count of games

// won by both the players

pair<int, int> countWins(int k, string a, string b)

{

 int n = a.length();

 int m = b.length();

 int i = 0, j = 0;

 // Total distinct games that can be played

 int moves = n * m;

 pair<int, int> wins = { 0, 0 };

 while (moves--) {

 int res = compare(a[i], b[j]);

 // Player 1 wins the current game

 if (res == 1)

 wins.first++;

 // Player 2 wins the current game

 if (res == -1)

 wins.second++;

 i = (i + 1) % n;

 j = (j + 1) % m;

 }

 // Number of times the above n * m games repeat

 int repeat = k / (n * m);

 // Update the games won

 wins.first *= repeat;

 wins.second *= repeat;

 // Remaining number of games after

 // removing repeated games

 int rem = k % (n * m);

 while (rem--) {

 int res = compare(a[i], b[j]);

 // Player 1 wins the current game

 if (res == 1)

 wins.first++;

 // Player 2 wins the current game

 if (res == -1)

 wins.second++;

 i = (i + 1) % n;

 j = (j + 1) % m;

 }

 return wins;

}

// Driver code

int main()

{

 int k = 4;

 string a = "SR", b = "R";

 auto wins = countWins(k, a, b);

 cout << wins.first << " " << wins.second;

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

// Java implementation of the above approach

import java.util.*;

import java.awt.Point;

class GFG{

 

// Function that returns 1 if first player wins,

// 0 in case of a draw and -1 if second player wins

public static int compare(char first, char second)

{

 

 // If both players have the same move

 // then it's a draw

 if (first == second)

 return 0;

 

 if (first == 'R')

 {

 if (second == 'S')

 return 1;

 else

 return -1;

 }

 if (first == 'P')

 {

 if (second == 'R')

 return 1;

 else

 return -1;

 }

 if (first == 'S')

 {

 if (second == 'P')

 return 1;

 else

 return -1;

 }

 

 return 0;

}

 

// Function that returns the count of games

// won by both the players

public static Point countWins(int k, String a,

 String b)

{

 int n = a.length();

 int m = b.length();

 int i = 0, j = 0;

 

 // Total distinct games that

 // can be played

 int moves = n * m;

 Point wins = new Point (0, 0);

 

 while (moves-- > 0)

 {

 int res = compare(a.charAt(i),

 b.charAt(j));

 

 // Player 1 wins the current game

 if (res == 1)

 wins = new Point(wins.x + 1,

 wins.y);

 

 // Player 2 wins the current game

 if (res == -1)

 wins = new Point(wins.x,

 wins.y + 1);

 

 i = (i + 1) % n;

 j = (j + 1) % m;

 }

 

 // Number of times the above

 // n * m games repeat

 int repeat = k / (n * m);

 

 // Update the games won

 wins = new Point(wins.x * repeat,

 wins.y * repeat);

 

 // Remaining number of games after

 // removing repeated games

 int rem = k % (n * m);

 

 while (rem-- > 0)

 {

 int res = compare(a.charAt(i),

 b.charAt(j));

 

 // Player 1 wins the current game

 if (res == 1)

 wins = new Point(wins.x + 1,

 wins.y);

 

 // Player 2 wins the current game

 if (res == -1)

 wins = new Point(wins.x,

 wins.y + 1);

 

 i = (i + 1) % n;

 j = (j + 1) % m;

 }

 return wins;

} 

// Driver code

public static void main(String[] args)

{

 int k = 4;

 String a = "SR", b = "R";

 Point wins = countWins(k, a, b);

 System.out.println(wins.x + " " + wins.y);

}

}

// This code is contributed by divyeshrabadiya07  
  
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

# Python3 implementation of the above approach

# Function that returns 1 if first

# player wins, 0 in case of a draw

# and -1 if second player wins

def compare(first, second):

 # If both players have the same

 # move then it's a draw

 if (first == second):

 return 0

 if (first == 'R'):

 if (second == 'S'):

 return 1

 else:

 return -1

 

 if (first == 'P'):

 if (second == 'R'):

 return 1

 else:

 return -1

 

 if (first == 'S'):

 if (second == 'P'):

 return 1

 else:

 return -1

# Function that returns the count

# of games won by both the players

def countWins(k, a, b):

 n = len(a)

 m = len(b)

 i = 0

 j = 0

 # Total distinct games that

 # can be played

 moves = n * m

 wins = [ 0, 0 ]

 

 while (moves > 0):

 res = compare(a[i], b[j])

 # Player 1 wins the current game

 if (res == 1):

 wins[0] += 1

 # Player 2 wins the current game

 if (res == -1):

 wins[1] += 1

 

 i = (i + 1) % n

 j = (j + 1) % m

 moves -= 1

 # Number of times the above

 # n * m games repeat

 repeat = k // (n * m)

 # Update the games won

 wins[0] *= repeat

 wins[1] *= repeat

 # Remaining number of games after

 # removing repeated games

 rem = k % (n * m)

 while (rem > 0):

 res = compare(a[i], b[j])

 # Player 1 wins the current game

 if (res == 1):

 wins[0] += 1

 # Player 2 wins the current game

 if (res == -1):

 wins[1] += 1

 

 i = (i + 1) % n

 j = (j + 1) % m

 

 return wins

# Driver code

if __name__ == "__main__":

 

 k = 4

 a = "SR"

 b = "R"

 

 wins = countWins(k, a, b);

 

 print(wins[0], wins[1])

# This code is contributed by chitranayal  
  
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

// C# implementation of the above approach

using System;

using System.Collections.Generic; 

class GFG{

 

// Function that returns 1 if first player

// wins, 0 in case of a draw and -1 if

// second player wins

static int compare(char first, char second)

{

 

 // If both players have the same

 // move then it's a draw

 if (first == second)

 return 0;

 

 if (first == 'R')

 {

 if (second == 'S')

 return 1;

 else

 return -1;

 }

 if (first == 'P')

 {

 if (second == 'R')

 return 1;

 else

 return -1;

 }

 if (first == 'S')

 {

 if (second == 'P')

 return 1;

 else

 return -1;

 }

 return 0;

}

 

// Function that returns the count of games

// won by both the players

static Tuple<int, int> countWins(int k, string a,

 string b)

{

 int n = a.Length;

 int m = b.Length;

 int i = 0, j = 0;

 

 // Total distinct games that

 // can be played

 int moves = n * m;

 Tuple<int, int> wins = Tuple.Create(0, 0);

 

 while (moves-- > 0)

 {

 int res = compare(a[i], b[j]);

 

 // Player 1 wins the current game

 if (res == 1)

 wins = Tuple.Create(wins.Item1 + 1,

 wins.Item2);

 

 // Player 2 wins the current game

 if (res == -1)

 wins = Tuple.Create(wins.Item1,

 wins.Item2 + 1);

 

 i = (i + 1) % n;

 j = (j + 1) % m;

 }

 

 // Number of times the above

 // n * m games repeat

 int repeat = k / (n * m);

 

 // Update the games won

 wins = Tuple.Create(wins.Item1 * repeat,

 wins.Item2 * repeat);

 

 // Remaining number of games after

 // removing repeated games

 int rem = k % (n * m);

 

 while (rem-- > 0)

 {

 int res = compare(a[i], b[j]);

 

 // Player 1 wins the current game

 if (res == 1)

 wins = Tuple.Create(wins.Item1 + 1,

 wins.Item2);

 

 // Player 2 wins the current game

 if (res == -1)

 wins = Tuple.Create(wins.Item1,

 wins.Item2 + 1);

 

 i = (i + 1) % n;

 j = (j + 1) % m;

 }

 return wins;

}

// Driver Code

static void Main()

{

 int k = 4;

 string a = "SR", b = "R";

 Tuple<int, int> wins = countWins(k, a, b);

 

 Console.WriteLine(wins.Item1 + " " +

 wins.Item2);

}

}

// This code is contributed by divyesh072019  
  
---  
  
 __

 __

 **Output:**

    
    
    0 2

**Time Complexity:** O(N * M)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

