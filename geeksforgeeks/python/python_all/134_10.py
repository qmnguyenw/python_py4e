Python | Count keys with particular value in dictionary



Sometimes, while working with Python dictionaries, we can come across a
problem in which we have a particular value, and we need to find frequency if
it’s occurrence. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Using loop**  
This problem can be solved using naive method of loop. In this we just iterate
through each key in dictionary and when a match is found, the counter is
increased.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count keys with particular value in dictionary

# Using loop

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 2, 'CS' : 2}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize value 

K = 2

 

# Using loop

# Selective key values in dictionary

res = 0

for key in test_dict:

 if test_dict[key] == K:

 res = res + 1

 

# printing result 

print("Frequency of K is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘gfg’: 1, ‘CS’: 2, ‘best’: 3, ‘for’: 2, ‘is’: 2}  
> Frequency of K is : 3

  

  

**Method #2 : Usingsum() + values()**  
This can also be solved using the combination of sum() and value(). In this,
sum is used to perform the summation of values filtered and values of
dictionary are extracted using values()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count keys with particular value in dictionary

# Using sum() + values()

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 2, 'CS' : 2}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize value 

K = 2

 

# Using sum() + values()

# Selective key values in dictionary

res = sum(x == K for x in test_dict.values())

 

# printing result 

print("Frequency of K is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘gfg’: 1, ‘CS’: 2, ‘best’: 3, ‘for’: 2, ‘is’: 2}  
> Frequency of K is : 3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

