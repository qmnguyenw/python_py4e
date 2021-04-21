Python Program to Converts Characters To Uppercase Around Numbers



Given a String, the following program converts the alphabetic character around
any digit to its uppercase.

>  **Input** : test_str = ‘geeks4geeks is best1 f6or ge8eks’  
> **Output** : geekS4Geeks is besT1 F6Or gE8Ek  
> **Explanation** : S and G are uppercased as surrounded by 4.  
>  **Input** : test_str = ‘geeks4geeks best1 f6or ge8eks’  
> **Output** : geekS4Geeks besT1 F6Or gE8Ek  
> **Explanation** : S and G are uppercased as surrounded by 4.

**Method 1 :** _Using_ _upper()_ _,_ _loop_ _and_ _isdigit()_

In this, we iterate for each character, check whether it’s a digit and if it
is then, transform the surrounding alphabets(next and previous) to uppercase
using upper().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geeks4geeks is best1 for ge8eks'

 

# printing original string

print("The original string is : " + str(test_str))

 

res = ''

for idx in range(len(test_str) - 1):

 if test_str[idx + 1].isdigit() or test_str[idx -
1].isdigit():

 res += test_str[idx].upper()

 else:

 res += test_str[idx]

 

# printing result 

print("Transformed String : " + str(res))   
  
---  
  
__

__

**Output:**

  

  

> The original string is : geeks4geeks is best1 for ge8eks
>
> Transformed String : geekS4Geeks is besT1 for gE8Ek

 **Method 2 :** _Using_ _list comprehension_

This is similar to above method, only difference being that the following
tackles the same problem in a single line.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geeks4geeks is best1 for ge8eks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# list comprehension offering 1 liner solution

res = ''.join([test_str[idx].upper() if test_str[idx +
1].isdigit() or test_str[idx - 1].isdigit() else
test_str[idx] for idx in range(len(test_str) - 1)])

 

# printing result 

print("Transformed String : " + str(res))   
  
---  
  
__

__

**Output:**

> The original string is : geeks4geeks is best1 for ge8eks
>
> Transformed String : geekS4Geeks is besT1 for gE8Ek

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

