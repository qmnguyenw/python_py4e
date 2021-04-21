Python – Elements Lengths in List



Sometimes, while working with Python lists, can have problem in which we need
to count the sizes of elements that are part of lists. This is because list
can allow different element types to be its members. This kind of problem can
have application in many domains such has day-day programming and web
development. Lets discuss certain ways in which we can perform this task.

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this, we iterate for
each loop element and find its size using elements counter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements Lengths in List

# Using loop

 

# initializing list

test_list = ['GFG', (4, 5, 6), 17, [5, 6,
7, 8], 'Best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Elements Lengths in List

# Using loop

res = []

for ele in test_list:

 count = 0

 if type(ele) == int:

 res.append(1)

 else :

 for sub in ele:

 count = count + 1

 res.append(count)

 

# printing result 

print("The element sizes in order are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['GFG', (4, 5, 6), 17, [5, 6, 7, 8], 'Best']
    The element sizes in order are : [3, 3, 1, 4, 4]
    

**Method #2 : Using list comprehension +len()**  
This task can also be performed using list comprehension. In this, we compute
length using len() and iteration is performed using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements Lengths in List

# Using list comprehension + len()

 

# initializing list

test_list = ['GFG', (4, 5, 6), 17, [5, 6,
7, 8], 'Best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Elements Lengths in List

# Using list comprehension + len()

res = [len(sub) if type(sub) != int else 1 for sub
in test_list]

 

# printing result 

print("The element sizes in order are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['GFG', (4, 5, 6), 17, [5, 6, 7, 8], 'Best']
    The element sizes in order are : [3, 3, 1, 4, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

