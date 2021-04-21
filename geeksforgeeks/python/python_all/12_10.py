Python Program to move numbers to the end of the string



Given a string, the task is to write a Python program to move all the numbers
in it to its end.

 **Examples:**

>  **Input** : test_str = ‘geek2eeks4g1eek5sbest6forall9’  
> **Output** : geekeeksgeeksbestforall241569  
> **Explanation** : All numbers are moved to end.
>
>  **Input** : test_str = ‘geekeeksg1eek5sbest6forall9’  
> **Output** : geekeeksgeeksbestforall1569  
> **Explanation** : All numbers are moved to end.  
>

**Method 1 :** _Using_ _isdigit()_ _and_ _loop_

  

  

In this, we check elements and digits using isdigit(), keeping track of all
the numbers and append at end of string post iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geek2eeks4g1eek5sbest6forall9'

 

# printing original string

print("The original string is : " + str(test_str))

 

# getting all numbers and removing digits

res = ''

dig = ''

for ele in test_str:

 if ele.isdigit():

 dig += ele

 else:

 res += ele

 

# adding digits at end

res += dig

 

# printing result

print("Strings after digits at end : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : geek2eeks4g1eek5sbest6forall9
>
> Strings after digits at end : geekeeksgeeksbestforall241569

 **Method 2 :** _Using_ _join()_ __

In this, we perform the task of extracting digits and ignoring them using
separate comprehensions and then joining both. At the end, digit string is
joined at end of actual string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geek2eeks4g1eek5sbest6forall9'

 

# printing original string

print("The original string is : " + str(test_str))

 

# getting all numbers

dig = ''.join(ele for ele in test_str if ele.isdigit())

 

# getting all elements not digit

res = ''.join(ele for ele in test_str if not
ele.isdigit())

 

# adding digits at end

res += dig

 

# printing result

print("Strings after digits at end : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : geek2eeks4g1eek5sbest6forall9
>
> Strings after digits at end : geekeeksgeeksbestforall241569

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

