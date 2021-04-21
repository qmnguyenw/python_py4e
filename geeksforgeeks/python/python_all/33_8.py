Python – Convert Snake Case String to Camel Case



Given a snake case string, convert to camel case.

>  **Input** : test_str = ‘geeksforgeeks_is_best_for_geeks’  
> **Output** : geeksforgeeksIsBestForGeeks  
> **Explanation** : String converted to Camel Case.
>
>  **Input** : test_str = ‘geeksforgeeks_best_for_geeks’  
> **Output** : geeksforgeeksBestForGeeks  
> **Explanation** : String converted to Camel Case.

**Method #1 : Using split() + join() + title() + generator expression**

The combination of above functions can be used to solve this problem. In this,
we first split all underscores, and then join the string appending initial
word, followed by title cased words using generator expression and title().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Snake Case String to Camel Case

# Using split() + join() + title() + generator expression

 

# initializing string

test_str = 'geeksforgeeks_is_best'

 

# printing original string

print("The original string is : " + str(test_str))

 

# split underscore using split

temp = test_str.split('_')

 

# joining result 

res = temp[0] + ''.join(ele.title() for ele in
temp[1:])

 

# printing result 

print("The camel case string is : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks_is_best
    The camel case string is : geeksforgeeksIsBest
    

**Method #2 : Using split() + join() + title() + map()**

The combination of above functions can be used to solve this problem. In this,
we perform the task of extending logic to entire strings using map().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Snake Case String to Camel Case

# Using split() + join() + title() + map()

 

# initializing string

test_str = 'geeksforgeeks_is_best'

 

# printing original string

print("The original string is : " + str(test_str))

 

# saving first and rest using split()

init, *temp = test_str.split('_')

 

# using map() to get all words other than 1st

# and titlecasing them

res = ''.join([init.lower(), *map(str.title, temp)])

 

# printing result 

print("The camel case string is : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks_is_best
    The camel case string is : geeksforgeeksIsBest
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

