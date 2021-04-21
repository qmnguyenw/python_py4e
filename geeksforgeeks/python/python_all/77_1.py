Python – Iterative Pair Pattern



Sometimes, while working with Python, we can have problem in which we need to
perform the pattern construction or iterative pair string in which second
element keeps increasing. This kind of problem can have application in day-day
programming and school programming. Lets discuss certain ways in which this
task can be performed.  
 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
manually check for the second element and perform an increment on each
iteration and store.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Iterative Pair Pattern

# Using loop

# initializing 1st element

frst_ele = 'G'

# initializing 2nd element

secnd_ele = '*'

# initializing N

N = 4

# Iterative Pair Pattern

# Using loop

res = frst_ele + secnd_ele

for idx in range(1, N):

 res += frst_ele + secnd_ele * (idx + 1)

# printing result

print("The constructed pattern is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The constructed pattern is : G*G**G***G****
    
    

  
**Method #2 : Using join() + generator expression**  
The combination of above methods can be used to perform this task. In this, we
perform the task of increment and pattern construction in one liner logic in
generator expression.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Iterative Pair Pattern

# Using join() + generator expression

# initializing 1st element

frst_ele = 'G'

# initializing 2nd element

secnd_ele = '*'

# initializing N

N = 4

# Iterative Pair Pattern

# Using join() + generator expression

res = frst_ele.join(secnd_ele * idx for idx in range(N +
1))

# printing result

print("The constructed pattern is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The constructed pattern is : G*G**G***G****
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

