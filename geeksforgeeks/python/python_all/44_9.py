Python – Convert Delimiter separated list to Number



Given a String with delimiter separated numbers, concatenate to form integer
after removing delimiter.

>  **Input** : test_str = “1@6@7@8”, delim = ‘@’  
>  **Output** : 1678  
>  **Explanation** : Joined elements after removing delim “@”
>
>  **Input** : test_str = “1!6!7!8”, delim = ‘!’  
>  **Output** : 1678  
>  **Explanation** : Joined elements after removing delim “!”

 **Method #1 : Using loop + split() + int()**

This is one of the ways in which this task can be performed. In this, we split
the string on delimiter and then run a loop to concat, at end result is
converted to int().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Delimiter separated list to Number

# Using loop + split() + join()

 

# initializing string

test_str = "1@6@7@8@5@8@9"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing Delimiter

delim = "@"

 

# spliting to get list of string numbers

temp = test_str.split(delim)

res = ''

for ele in temp:

 res = res + ele

 

# converting result into integer

res = int(res)

 

# printing result 

print("Constructed integer : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 1@6@7@8@5@8@9
    Constructed integer : 1678589
    

**Method #2 : Using join() + split() + int()**

This is one another way in which this task can be performed. In this, we
perform final concatenation using join() and int() to get final result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Delimiter seperated list to Number

# Using join() + split() + int()

 

# initializing string

test_str = "1@6@7@8@5@8@9"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing Delimiter

delim = "@"

 

# join used over splitted result 

# final result casted using int()

res = int("".join(test_str.split(delim)))

 

# printing result 

print("Constructed integer : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 1@6@7@8@5@8@9
    Constructed integer : 1678589
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

