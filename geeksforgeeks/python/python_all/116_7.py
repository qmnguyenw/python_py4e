Python | Convert String list to ascii values



Sometimes, while working with Python, we can have a problem in which we need
to convert String List to ascii values. This kind of problem can occur many
times. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +ord()**  
This problem can be solved using above functionalities. In this, we iterate
the list and convert each character to it’s ascii number using ord().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String list to ascii values

# using loop + ord()

 

# initialize list 

test_list = ['gfg', 'is', 'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert String list to ascii values

# using loop + ord()

res = []

for ele in test_list:

 res.extend(ord(num) for num in ele)

 

# printing result

print("The ascii list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best']
    The ascii list is : [103, 102, 103, 105, 115, 98, 101, 115, 116]
    

**Method #2 : Using list comprehension + ord()**  
This is yet another way to perform this task. This is just shorthand to above
problem in which we compact the code using list comprehension using similar
logic.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String list to ascii values

# using list comprehension + ord()

 

# initialize list 

test_list = ['gfg', 'is', 'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert String list to ascii values

# using list comprehension + ord()

res = [ord(ele) for sub in test_list for ele in sub]

 

# printing result

print("The ascii list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best']
    The ascii list is : [103, 102, 103, 105, 115, 98, 101, 115, 116]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

