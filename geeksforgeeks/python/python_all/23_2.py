Python – Test for Word construction from character list



Given a List and a String, test if the string can be made from list
characters.

 **Examples:**

>  **Input** : test_list = [‘g’, ‘g’, ‘e’, ‘k’, ‘s’, ‘4’, ‘g’, ‘g’, ‘e’, ‘s’,
> ‘e’, ‘e’, ‘4’, ‘k’], test_str = ‘geeks4geeks’  
> **Output** : True  
> **Explanation** : String can be made according to character frequencies.  
>
>
> **Input** : test_list = [‘s’, ‘4’, ‘g’, ‘g’, ‘e’, ‘s’, ‘e’, ‘e’, ‘4’, ‘k’],
> test_str = ‘geeks4geeks’  
> **Output** : False  
> **Explanation** : String cannot be made according to character frequencies.

**Method #1: Using** **all()** **+** **count()**

  

  

In this, we test for all characters count from string to be less than the
frequency of each character in the list. The frequencies are extracted using
count().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Word construction from character list

# Using all() + count()

 

# initializing list

test_list = ['g', 'g', 'e', 'k', 's', '4',
'g', 

 'g', 'e', 's', 'e', 'e', '4', 'k']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing string 

test_str = 'geeks4geeks'

 

# cheking for frequency of chars less than in list

res = all(test_str.count(chr) <= test_list.count(chr)
for chr in test_str)

 

# printing result 

print("Is word construction possible ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘g’, ‘g’, ‘e’, ‘k’, ‘s’, ‘4’, ‘g’, ‘g’, ‘e’, ‘s’,
> ‘e’, ‘e’, ‘4’, ‘k’]  
> Is word construction possible ? : True

 **Method #2 : Using Counter()**

In this, we compute frequencies using Counter(), and then perform subtraction
of word from list characters. In case of an empty list, means not possible to
form a word.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Word construction from character list

# Using Counter()

from collections import Counter

 

# initializing list

test_list = ['g', 'g', 'e', 'k', 's', '4',
'g', 

 'g', 'e', 's', 'e', 'e', '4', 'k']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing string 

test_str = 'geeks4geeks'

 

# cheking for frequency of chars less than in list

res = not bool(dict(Counter(test_str) - Counter(test_list)))

 

# printing result 

print("Is word construction possible ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘g’, ‘g’, ‘e’, ‘k’, ‘s’, ‘4’, ‘g’, ‘g’, ‘e’, ‘s’,
> ‘e’, ‘e’, ‘4’, ‘k’]  
> Is word construction possible ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

