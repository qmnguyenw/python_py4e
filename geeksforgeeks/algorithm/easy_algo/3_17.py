Maximum Sequence Length | Collatz Conjecture



Given an integer **N**. The task is to find the number in the range from **1**
to **N-1** which is having the maximum number of terms in its Collatz Sequence
and the number of terms in the sequence.

The collatz sequence of a number **N** is defined as:

  * If **N** is **Odd** then change **N** to **3*N + 1**.
  * If **N** is **Even** then change **N** to **N / 2**.

For example let us have a look at the sequence when **N = 13** :  
13 -> 40 -> 20 -> 10 -> 5 > 16 -> 8 -> 4 -> 2 -> 1

 **Examples:**

>  **Input:** 10  
>  **Output:** (9, 20)
>
>  
>
>
>  
>
>
> 9 has 20 terms in its Collatz sequence
>
>  **Input:** 50  
>  **Output:** (27, 112)  
> 27 has 112 terms

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

As in the above example discussed for **N = 13** , collatz sequence for **N =
13** and **N = 40** have similar terms except one, that ensures there may be
an involvement of dynamic programming to store the answer for subproblems and
reuse it.

But here normal memoization will not work because at one step we are either
making a number large from itself ( in above example N = 13 is depending upon
the solution of N = 40 ) or dividing by **2** ( N = 40 solution depends upon
the solution of N = 20 ).

So instead of using a dp array we will use a Map/ dictionary data structure to
store the solution of subproblems and will perform the normal operation as
discussed in the collatz sequence.

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

def collatzLenUtil(n, collLenMap):

 

 # If value already 

 # computed, return it

 if n in collLenMap:

 return collLenMap[n]

 

 # Base case

 if(n == 1):

 collLenMap[n] = 1

 

 # Even case

 elif(n % 2 == 0):

 collLenMap[n] \

 = 1 \

 + collatzLenUtil(n//2, collLenMap)

 

 # Odd case

 else:

 collLenMap[n] \

 = 1 \

 + collatzLenUtil(3 * n + 1, collLenMap)

 

 return collLenMap[n]

 

def collatzLen(n):

 

 # Declare empty Map / Dict

 # to store collatz lengths

 collLenMap = {}

 

 collatzLenUtil(n, collLenMap)

 

 # Initalise ans and 

 # its collatz length

 num, l =-1, 0

 

 for i in range(1, n):

 

 # If value not already computed,

 # pass Dict to Helper function

 # and calculate and store value

 if i not in collLenMap:

 collatzLenUtil(i, collLenMap)

 

 cLen = collLenMap[i]

 if l < cLen:

 l = cLen

 num = i

 

 # Return ans and 

 # its collatz length

 return (num, l)

 

print(collatzLen(10))  
  
---  
  
 __

 __

 **Output:**

    
    
    (9, 20)
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

