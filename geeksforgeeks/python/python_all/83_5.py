Python – String Repetition and spacing in List



Sometimes while working with Python, we can have a problem in which we need to
perform the repetion of each string in list and also attach a deliminator to
each occurrence. This kind of problem can occur in day-day programming. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This task can be performed in brute force way using loop. In this, we iterate
the list and perform string addition and multiplication while iteration using
suitable operators.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String Repetition and spacing in List

# Using loop

 

# initializing list

test_list = ['gfg', 'is', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing delim

delim = '-'

 

# initializing K 

K = 3

 

# String Repetition and spacing in List

# Using loop

res = []

for sub in test_list:

 res.append((sub + delim) * K)

 

# printing result 

print("List after performing operations : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', 'is', 'best']
    List after performing operations : ['gfg-gfg-gfg-', 'is-is-is-', 'best-best-best-']
    

**Method #2 : Usingjoin() \+ list comprehension**  
The combination of above functionalities can also be used to perform this
task. In this, we perform the task of attaching delim using join() and list
comprehension performs the task of repetition. Avoids trailing delim.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String Repetition and spacing in List

# Using join() + list comprehension

 

# initializing list

test_list = ['gfg', 'is', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing delim

delim = '-'

 

# initializing K 

K = 3

 

# String Repetition and spacing in List

# Using join() + list comprehension

res = []

for sub in test_list:

 res.append(delim.join([sub for _ in range(K)]))

 

# printing result 

print("List after performing operations : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', 'is', 'best']
    List after performing operations : ['gfg-gfg-gfg', 'is-is-is', 'best-best-best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

