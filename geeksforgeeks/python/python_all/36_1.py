Python – Horizontal Concatenation of Multiline Strings



Given pair of strings, which is multiline, perform concatenation horizontally.

 **Examples:**

>  **Input** :  
> test_str1 = ”’  
> geeks for  
> geeks”’,  
> test_str2 = ”’  
> is  
> best”’  
> **Output** :  
> geeks foris  
> geeksbest  
> **Explanation** : 1st line joined with 1st line of 2nd string, “geeks for”
> -> “is”.
>
>  **Input** :  
> test_str1 = ”’  
> geeks for ”’  
> test_str2 = ”’  
> geeks ”’  
> **Output** :  
> geeks for geeks  
> **Explanation** : 1st line joined with 1st line of 2nd string, “geeks for ”
> -> “geeks”.  
>

**Method #1 : Using zip() + split() + join() + list comprehension**

  

  

In this, we perform the task of splitting by “\n” using split(), and they are
paired together using zip(). The next step is joining both the zipped strings
for horizontal orientation using “\n” and join().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Horizontal Concatenation of Multiline Strings

# Using zip() + split() + join() + list comprehension

 

# initializing strings

test_str1 = '''

geeks 4

geeks'''

 

test_str2 = '''

is

best'''

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# split lines

splt_lines = zip(test_str1.split('\n'), test_str2.split('\n'))

 

# horizontal join

res = '\n'.join([x + y for x, y in splt_lines])

 

# printing result

print("After String Horizontal Concatenation : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string 1 is : 
    geeks 4
    geeks
    The original string 2 is : 
    is
    best
    After String Horizontal Concatenation : 
    geeks 4is
    geeksbest
    

**Method #2 : Using map() + operator.add + join()**

In this, we use map() to with help of add() to perform concatenation, split()
is used to perform initial split by “\n”.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Horizontal Concatenation of Multiline Strings

# Using map() + operator.add + join()

from operator import add

 

# initializing strings

test_str1 = '''

geeks 4

geeks'''

test_str2 = '''

is

best'''

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# using add to concat, map() to concat each lines zipped

res = '\n'.join(map(add, test_str1.split('\n'),
test_str2.split('\n')))

 

# printing result

print("After String Horizontal Concatenation : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string 1 is : 
    geeks 4
    geeks
    The original string 2 is : 
    is
    best
    After String Horizontal Concatenation : 
    geeks 4is
    geeksbest
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

