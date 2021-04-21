Python | Delimited String List to String Matrix



Sometimes, while working with Python strings, we can have problem in which we
need to convert String list which have strings that are joined by deliminitor
to String Matrix by separation by deliminitor. Lets discuss certain ways in
which this task can be performed.

 **Method #1 : Usingloop + split()**  
This is one of way in which this task can be performed. In this, we iterate
for each string and perform the split using split().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Delimited String List to String Matrix

# Using loop + split()

 

# initializing list

test_list = ['gfg:is:best', 'for:all', 'geeks:and:CS']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Delimited String List to String Matrix

# Using loop + split()

res = []

for sub in test_list:

 res.append(sub.split(':'))

 

# printing result 

print("The list after conversion : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg:is:best', 'for:all', 'geeks:and:CS']
    The list after conversion : [['gfg', 'is', 'best'], ['for', 'all'], ['geeks', 'and', 'CS']]
    

**Method #2 : Using list comprehension +split()**  
Yet another way to perform this task, is just modification of above method. In
this, we use list comprehension as shorthand and one-liner to perform this.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Delimited String List to String Matrix

# Using list comprehension + split()

 

# initializing list

test_list = ['gfg:is:best', 'for:all', 'geeks:and:CS']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Delimited String List to String Matrix

# Using list comprehension + split()

res = [sub.split(':') for sub in test_list]

 

# printing result 

print("The list after conversion : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg:is:best', 'for:all', 'geeks:and:CS']
    The list after conversion : [['gfg', 'is', 'best'], ['for', 'all'], ['geeks', 'and', 'CS']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

