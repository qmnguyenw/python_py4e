Python – Replace all words except the given word



Given a String. The task is to replace all the words with ‘?’ except the given
word K.

 **Examples:**

> **Input** : test_str = ‘gfg is best for geeks’, K = “gfg”, repl_char = “?”  
> **Output** : gfg ? ? ? ?  
> **Explanation** : All words except gfg is replaced by ?.
>
>  **Input** : test_str = ‘gfg is best for gfg’, K = “gfg”, repl_char = “?”  
> **Output** : gfg ? ? ? gfg  
> **Explanation** : All words except gfg is replaced by ?.

**Method #1 : Using split() + join() + loop**

  

  

This is a brute way in which this task can be performed. In this, we perform
the task of changing the string to word list using split() and then check for
K word, if not found, replace it by the appropriate value. And at last,
convert back to the string using join().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace all words not K

# Using join() + split() + loop

 

# initializing string

test_str = 'gfg is best for geeks gfg is for cs I love gfg'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = "gfg"

 

# initializing repl_char

repl_char = "?"

 

# extracting words

temp = test_str.split(" ")

for idx in range(len(temp)):

 ele = temp[idx]

 

 # replace non K with repl_char

 if not ele == K:

 temp[idx] = repl_char

 

# joining result

res = " ".join(temp)

 

# printing result

print("The resultant string : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : gfg is best for geeks gfg is for cs I love gfg  
> The resultant string : gfg ? ? ? ? gfg ? ? ? ? ? gfg

 **Method #2: Using** **list comprehension** ****

This is yet another way in which this task can be performed. In this, we
iterate for elements and perform the task using one-liner using similar
functionality as the above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace all words not K

# Using list comprehension

 

# initializing string

test_str = 'gfg is best for geeks gfg is for cs I love gfg'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = "gfg"

 

# initializing repl_char

repl_char = "?"

 

# using one-liner to solve this problem

res = " ".join(

 [repl_char if not ele == K else ele for ele in
test_str.split()])

 

# printing result

print("The resultant string : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : gfg is best for geeks gfg is for cs I love gfg  
> The resultant string : gfg ? ? ? ? gfg ? ? ? ? ? gfg

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

