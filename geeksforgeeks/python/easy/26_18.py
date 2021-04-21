Python Dictionary Comprehension



Like List Comprehension, Python allows dictionary comprehensions. We can
create dictionaries using simple expressions.  
A dictionary comprehension takes the form **_{key: value for (key, value) in
iterable}_**

Let’s see a example,lets assume we have two lists named keys and value now,

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate dictionary

# comprehension

 

# Lists to represent keys and values

keys = ['a','b','c','d','e']

values = [1,2,3,4,5] 

 

# but this line shows dict comprehension here 

myDict = { k:v for (k,v) in zip(keys, values)} 

 

# We can use below too

# myDict = dict(zip(keys, values)) 

 

print (myDict)  
  
---  
  
 __

 __

Output :

    
    
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

We can also make dictionary from a list using comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate dictionary

# creation using list comprehension

myDict = {x: x**2 for x in
[1,2,3,4,5]}

print (myDict)  
  
---  
  
 __

 __

Output :

  

  

    
    
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

and like,

 __

 __  
 __

 __

 __  
 __  
 __

sDict= {x.upper(): x*3 for x in 'coding '}

print (sDict)  
  
---  
  
 __

 __

Output :

    
    
    {'O': 'ooo', 'N': 'nnn', 'I': 'iii', 'C': 'ccc', 'D': 'ddd', 'G': 'ggg'}

We can use Dictionary comprehensions with if and else statements and with
other expressions too. This example below maps the numbers to their cubes that
are not divisible by 4:

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate dictionary

# comprehension using if.

newdict = {x: x**3 for x in range(10) if
x**3 % 4 == 0}

print(newdict)  
  
---  
  
 __

 __

Output :

    
    
    {0: 0, 8: 512, 2: 8, 4: 64, 6: 216}

This article is contributed by **Shantanu Sharma.**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

