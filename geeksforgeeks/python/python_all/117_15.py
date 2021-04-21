Python – Get summation of numbers in string list



Sometimes, while working with data, we can have a problem in which we receive
series of lists with data in string format, which we wish to accumulate as
list. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +int()**  
This is the brute force method to perform this task. In this, we run a loop
for entire list, convert each string to integer and perform summation listwise
and store in a separate list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of String Integer lists

# using loop + int()

 

# initialize list 

test_list = [['1', '4'], ['5', '6'], ['7',
'10']]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Summation of String Integer lists

# using loop + int()

res = []

for sub in test_list:

 par_sum = 0

 for ele in sub:

 par_sum = par_sum + int(ele)

 res.append(par_sum)

 

# printing result

print("List after summation of nested string lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['1', '4'], ['5', '6'], ['7', '10']]
    List after summation of nested string lists : [5, 11, 17]
    

**Method #2 : Using sum() + int() \+ list comprehension**  
This is the shorthand with the help of which this task can be performed. In
this, we run a loop on lists using list comprehension and extract summation
using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of String Integer lists

# using sum() + int() + list comprehension

 

# initialize list 

test_list = [['1', '4'], ['5', '6'], ['7',
'10']]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Summation of String Integer lists

# using sum() + int() + list comprehension

res = [sum(int(ele) for ele in sub) for sub in
test_list]

 

# printing result

print("List after summation of nested string lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['1', '4'], ['5', '6'], ['7', '10']]
    List after summation of nested string lists : [5, 11, 17]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

