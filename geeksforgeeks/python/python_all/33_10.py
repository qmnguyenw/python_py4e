Python program to reverse alternate characters in a string



Given a String, reverse its alternate characters string.

>  **Input** : test_str = ‘geeks4rgeeks’  
> **Output** : keekr4sgeegs  
> **Explanation** : only g, e, s, r, e, k are reversed, rest all have same
> position.
>
>  **Input** : test_str = ‘geeks’  
> **Output** : seekg  
> **Explanation** : only g, e, s are reversed, rest all have same position.

**Method #1 : Using loop + slicing + reversed()**

This is one of the ways in which this task can be performed. In this, we
extract alternates using slicing and then reverse the string using reversed.
The reconstruction of the string is done using a loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate characters reverse in String 

# Using loop + slicing + reversed()

 

# initializing string

test_str = 'geeks4rgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# extracting alternate string 

alt = test_str[::2]

not_alt = test_str[1::2]

 

# performing reverse 

alt = "".join(reversed(alt))

 

res = ''

# remaking string 

for idx in range(len(alt)):

 res += alt[idx]

 res += not_alt[idx]

 

# printing result 

print("Is alternate reversed string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks4rgeeks
    Is alternate reversed string : keekr4sgeegs
    
    

**Method #2 : Using list comprehension**

This is one more way in which this task can be performed. In this, we perform
a similar function as above by using one-liner functionality using list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate characters reverse in String 

# Using list comprehension

 

# initializing string

test_str = 'geeks4rgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# using one-liner to solve the problem 

res = "".join(["".join(reversed(test_str[::2]))[idx] +
test_str[1::2][idx]

 for idx in
range(len("".join(reversed(test_str[::2]))))])

 

# printing result 

print("Is alternate reversed string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks4rgeeks
    Is alternate reversed string : keekr4sgeegs
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

