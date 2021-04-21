Python | Ways to initialize list with alphabets



While working with lists, sometimes we wish to initialize the list with the
English alphabets a-z. This is an essential utility in competitive programming
and also in certain applications. Let’s discuss various approaches to achieve
this.

 **Method #1 : Naive method**  
The most general method that comes in our mind is using the brute force method
of running a loop till 26 and incrementing it while appending the letters in
the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Filling alphabets

# using naive method 

 

# initializing empty list 

test_list = []

 

# printing initial list 

print ("Initial list : " + str(test_list))

 

# using naive method

# for filling alphabets

alpha = 'a'

for i in range(0, 26):

 test_list.append(alpha)

 alpha = chr(ord(alpha) + 1) 

 

# printing resultant list 

print ("List after insertion : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

> Initial list : []  
> List after insertion : [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’, ‘h’, ‘i’, ‘j’,
> ‘k’, ‘l’, ‘m’, ‘n’, ‘o’, ‘p’, ‘q’, ‘r’, ‘s’, ‘t’, ‘u’, ‘v’, ‘w’, ‘x’, ‘y’,
> ‘z’]

  

  

**Method #2 : Using list comprehension**  
This is method similar to the above method, but rather a shorthand to naive
method as it uses the list comprehension technique to achieve the task.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Filling alphabets

# using list comprehension

 

# initializing empty list 

test_list = []

 

# printing initial list 

print ("Initial list : " + str(test_list))

 

# using list comprehension

# for filling alphabets

test_list = [chr(x) for x in range(ord('a'),
ord('z') + 1)]

 

# printing resultant list 

print ("List after insertion : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

> Initial list : []  
> List after insertion : [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’, ‘h’, ‘i’, ‘j’,
> ‘k’, ‘l’, ‘m’, ‘n’, ‘o’, ‘p’, ‘q’, ‘r’, ‘s’, ‘t’, ‘u’, ‘v’, ‘w’, ‘x’, ‘y’,
> ‘z’]

**Method #3 : Usingmap()**  
Using map() is the elegant way to perform this particular task. It type
casts the numbers in a range to particular data type, char in this case and
assigns to the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Filling alphabets

# using map()

 

# initializing empty list 

test_list = []

 

# printing initial list 

print ("Initial list : " + str(test_list))

 

# using map()

# for filling alphabets

test_list = list(map(chr, range(97, 123)))

 

# printing resultant list 

print ("List after insertion : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

> Initial list : []  
> List after insertion : [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’, ‘h’, ‘i’, ‘j’,
> ‘k’, ‘l’, ‘m’, ‘n’, ‘o’, ‘p’, ‘q’, ‘r’, ‘s’, ‘t’, ‘u’, ‘v’, ‘w’, ‘x’, ‘y’,
> ‘z’]

**Method #4 : Usingstring.ascii_lowercase**  
The most pythonic and latest way to perform this particular task. Using this
new inbuilt function will internally handle the coding part providing the
useful shorthand for the user.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Filling alphabets

# using string

import string

 

# initializing empty list 

test_list = []

 

# printing initial list 

print ("Initial list : " + str(test_list))

 

# using string 

# for filling alphabets

test_list = list(string.ascii_lowercase)

 

# printing resultant list 

print ("List after insertion : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

> Initial list : []  
> List after insertion : [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’, ‘h’, ‘i’, ‘j’,
> ‘k’, ‘l’, ‘m’, ‘n’, ‘o’, ‘p’, ‘q’, ‘r’, ‘s’, ‘t’, ‘u’, ‘v’, ‘w’, ‘x’, ‘y’,
> ‘z’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

