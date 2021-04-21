Python – String Integer Product



Sometimes, while working with data, we can have a problem in which we receive
a series of lists with data in string format, which we wish to find the
product of each string list integer. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Using loop +int()**  
This is the brute force method to perform this task. In this, we run a loop
for the entire list, convert each string to integer and perform product
listwise and store in a separate list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String Integer Product

# using loop + int()

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= int(ele)

 return res 

 

# initialize list 

test_list = [['1', '4'], ['5', '6'], ['7',
'10']]

 

# printing original list 

print("The original list : " + str(test_list))

 

# String Integer Product

# using loop + int()

res = []

for sub in test_list:

 par_prod = prod(sub)

 res.append(par_prod)

 

# printing result

print("List after product of nested string lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['1', '4'], ['5', '6'], ['7', '10']]
    List after product of nested string lists : [4, 30, 70]
    

**Method #2 : Using loop +int() \+ list comprehension**  
This is the shorthand with the help of which this task can be performed. In
this, we run a loop on lists using list comprehension and extract product
using explicit product function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String Integer Product

# using loop + int() + list comprehension

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= int(ele)

 return res 

 

# initialize list 

test_list = [['1', '4'], ['5', '6'], ['7',
'10']]

 

# printing original list 

print("The original list : " + str(test_list))

 

# String Integer Product

# using loop + int() + list comprehension

res = [prod(sub) for sub in test_list]

 

# printing result

print("List after product of nested string lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['1', '4'], ['5', '6'], ['7', '10']]
    List after product of nested string lists : [4, 30, 70]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

