Predict the winner in Coin Game



There are two players **P1** and **P2** and two piles of coins consisting of
**M** and **N** coins respectively. At each turn, a player can choose only one
of the piles out of these and discard the other one. This discarded pile
cannot be used further in the game. The pile player chooses is further divided
into two piles of non zero parts. The player who cannot divide the pile i.e.
the number of coins in the pile is < 2, loses the game. The task is to
determine which player wins if **P1** starts the game and both the players
play optimally.

 **Examples:**

>  **Input:** M = 4, N = 4  
>  **Output:** Player 1  
> Player 1 can choose any one of the piles as both contain the same number of
> coins  
> and then splits the chosen one (the one which is not chosen is discarded)
> into two piles with 1 coin each.  
> Now, player 2 is left with no move (as both the remaining piles contain a
> single coin each  
> which cannot be split into two groups of non-zero coins).
>
>  **Input:** M = 1, N = 1  
>  **Output:** Player 2  
> There’s no move to make.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Simply check if any of the pile consists of even number of
coins. If yes then Player 1 wins else Player 2 wins.

  

  

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

 

// Function to print the winner of the game

void findWinner(int M, int N)

{

 if (M % 2 == 0 || N % 2 == 0)

 cout << "Player 1";

 else

 cout << "Player 2";

}

 

// Driver code

int main()

{

 int M = 1, N = 2;

 findWinner(M, N);

 

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

// Java implementation of the approach

import java.io.*;

 

class GFG {

 

 // Function to print the winner of the game

 static void findWinner(int M, int N)

 {

 if (M % 2 == 0 || N % 2 == 0)

 System.out.println("Player 1");

 else

 System.out.println("Player 2");

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int M = 1, N = 2;

 findWinner(M, N);

 }

}

 

// This code is contributed by ajit.  
  
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

# Python implementation of the approach

# Function to print the winner of the game

 

def findWinner(M, N):

 if (M % 2 == 0 or N % 2 == 0):

 print("Player 1");

 else:

 print("Player 2");

 

# Driver code

M = 1;

N = 2;

findWinner(M, N);

 

 

# This code contributed by PrinciRaj1992   
  
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

 

class GFG {

 

 // Function to print the winner of the game

 static void findWinner(int M, int N)

 {

 if (M % 2 == 0 || N % 2 == 0)

 Console.WriteLine("Player 1");

 else

 Console.WriteLine("Player 2");

 }

 

 // Driver code

 static public void Main()

 {

 int M = 1, N = 2;

 findWinner(M, N);

 }

}

 

// This code is contributed by Tushil..  
  
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

//PHP implementation of the approach

// Function to print the winner of the game

 

function findWinner($M, $N)

{

 if ($M % 2 == 0 || $N % 2 == 0)

 echo "Player 1";

 else

 echo "Player 2";

}

 

 // Driver code

 $M = 1;

 $N = 2;

 findWinner($M, $N);

 

// This code is contributed by Tushil.

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    Player 1
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

