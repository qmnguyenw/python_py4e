Loop Unrolling



Loop unrolling is a loop transformation technique that helps to optimize the
execution time of a program. We basically remove or reduce iterations. Loop
unrolling increases the program’s speed by eliminating loop control
instruction and loop test instructions.

 **Program 1:**

 __

 __  
 __

 __

 __  
 __  
 __

// This program does not uses loop unrolling.

#include<stdio.h>

 

int main(void)

{

 for (int i=0; i<5; i++)

 printf("Hello\n"); //print hello 5 times

 

 return 0;

}   
  
---  
  
__

__

**Program 2:**

 __

 __  
 __

 __

 __  
 __  
 __

// This program uses loop unrolling.

#include<stdio.h>

 

int main(void)

{

 // unrolled the for loop in program 1

 printf("Hello\n");

 printf("Hello\n");

 printf("Hello\n");

 printf("Hello\n");

 printf("Hello\n");

 

 return 0;

}   
  
---  
  
__

__

Output:

    
    
    Hello
    Hello
    Hello
    Hello
    Hello
    

**Illustration:**  
Program 2 is more efficient than program 1 because in program 1 there is a
need to check the value of i and increment the value of i every time round the
loop. So small loops like this or loops where there is fixed number of
iterations are involved can be unrolled completely to reduce the loop
overhead.

  

  

 **Advantages:**

  * Increases program efficiency.
  * Reduces loop overhead.
  * If statements in loop are not dependent on each other, they can be executed in parallel.

 **Disadvantages:**

  * Increased program code size, which can be undesirable.
  * Possible increased usage of register in a single iteration to store temporary variables which may reduce performance.
  * Apart from very small and simple codes, unrolled loops that contain branches are even slower than recursions.

 **Reference:**  
https://en.wikipedia.org/wiki/Loop_unrolling

This article is contributed by **Harsh Agarwal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
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

