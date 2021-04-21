Python Program to print digit pattern



The program must accept an integer **N** as the input. The program must print
the desired pattern as shown in the example input/ output.

 **Examples:**

>  **Input :** 41325  
>  **Output :**  
>  |****  
> |*  
> |***  
> |**  
> |*****  
>  **Explanation:** for a given integer print the number of *’s that are
> equivalent to each digit in the integer. Here the first digit is 4 so print
> four *sin the first line. The second digit is 1 so print one *. So on and
> the last i.e., the fifth digit is 5 hence print five *s in the fifth line.
>
>  **Input :** 60710  
>  **Output :**  
>  |******  
> |  
> |*******  
> |*  
> |

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach**  
Read the input  
For each digit in the integer print the corresponding number of *s  
If the digit is 0 then print no *s and skip to the next line

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# function to print the pattern

def pattern(n):

 

 # traverse through the elements

 # in n assuming it as a string

 for i in n:

 

 # print | for every line

 print("|", end = "")

 

 # print i number of * s in 

 # each line

 print("*" * int(i))

 

# get the input as string 

n = "41325"

pattern(n)  
  
---  
  
 __

 __

 **Output:**

    
    
    |****
    |*
    |***
    |**
    |*****
    

**  
Alternate solution that takes integer as input :**

 __

 __  
 __

 __

 __  
 __  
 __

n= 41325

x = []

while n>0:

 x.append(n%10)

 n //= 10

for i in range(len(x)-1,-1,-1):

 print('|'+x[i]*'*')

 

# code contributed by Baivab Dash  
  
---  
  
 __

 __

 **Output:**

    
    
    |****
    |*
    |***
    |**
    |*****
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

