Python – Element Frequency starting with K in dictionary value List



Sometimes while working with a lots of data, we can have a problem in which we
have data in form of strings list which are values of dictionary keys and we
wish to count occurrences of elements starting with character K. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop +startswith()**  
This is one way in which this task can be performed. In this, we check for
each element in dictionary lists using nested loops in brute force and
increase the counter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Element Frequency starting with K in dictionary value List

# using loop + startswith()

 

# initializing dictionary 

test_dict = {1 : ['Gfg', 'is', 'for', 'Geeks'], 2
: ['Gfg', 'is', 'CS', 'God'], 3: ['Gfg',
'best']}

 

# printing original dictionary 

print("The original dictionary is : " + str(test_dict)) 

 

# initializing K 

K = 'G'

 

# Element Frequency starting with K in dictionary value List

# using loop + startswith()

res = 0

for sub in test_dict.values():

 for ele in sub:

 if ele.startswith(K):

 res += 1

 

# printing result 

print("The element frequency starting with K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {1: ['Gfg', 'is', 'for', 'Geeks'], 2: ['Gfg', 'is', 'CS', 'God'], 3: ['Gfg', 'best']}
    The element frequency starting with K : 5
    

**Method #2 : Usingsum() + startswith()**  
This is yet another way in which this task can be performed. In this, we
perform task of getting  
frequency using sum() and generator is used to perform flattening the logic in
one line.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Element Frequency starting with K in dictionary value List

# using sum() + startswith()

 

# initializing dictionary 

test_dict = {1 : ['Gfg', 'is', 'for', 'Geeks'], 2
: ['Gfg', 'is', 'CS', 'God'], 3: ['Gfg',
'best']}

 

# printing original dictionary 

print("The original dictionary is : " + str(test_dict)) 

 

# initializing K 

K = 'G'

 

# Element Frequency starting with K in dictionary value List

# using sum() + startswith()

res = sum(ele.startswith(K) for ele in [sub for j in
test_dict.values() for sub in j])

 

# printing result 

print("The element frequency starting with K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {1: ['Gfg', 'is', 'for', 'Geeks'], 2: ['Gfg', 'is', 'CS', 'God'], 3: ['Gfg', 'best']}
    The element frequency starting with K : 5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

