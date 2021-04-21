Python – Interconvert Horizontal and Vertical String



Given a String, convert to vertical if horizontal and vice-versa.

>  **Input** : test_str = ‘geeksforgeeks’  
>  **Output** : g  
> e  
> e  
> k  
> s  
>  **Explanation** : Horizontal String converted to Vertical.
>
>  **Input** : test_str = g  
> e  
> e  
> k  
> s  
>  **Output** : ‘geeks’  
>  **Explanation** : Vertical String converted to Horizontal.

 **Method #1 : [Horizontal to Vertical] using loop + “\n”**

In this, we add newline character to after each character so that each element
gets rendered at next line.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Interconvert Horizontal and Vertical String

# using [Horizontal to Vertical] using loop + "\n"

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original String

print("The original string is : " + str(test_str))

 

# using loop to add "\n" after each character 

res = ''

for ele in test_str:

 res += ele + "\n"

 

# printing result 

print("The converted string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    The converted string : g
    e
    e
    k
    s
    f
    o
    r
    g
    e
    e
    k
    s
    
    

**Method #2 : [Vertical to Horizontal] using replace() + “\n”**

In this, we perform the task of conversion by removing “\n” by replacement by
empty string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Interconvert Horizontal and Vertical String

# using [Vertical to Horizontal] using replace() + "\n"

 

# initializing string

test_str = 'g\ne\ne\nk\ns\nf\no\nr\ng\ne\ne\nk\ns\n'

 

# printing original String

print("The original string is : " + str(test_str))

 

# using replace() + "\n" to solve this problem

res = test_str.replace("\n", "")

 

# printing result 

print("The converted string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : g
    e
    e
    k
    s
    f
    o
    r
    g
    e
    e
    k
    s
    
    The converted string : geeksforgeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

