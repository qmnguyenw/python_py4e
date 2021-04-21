Python – Maximum of Sting Integer list



Sometimes, while working with data, we can have a problem in which we receive
a series of lists with data in string format, which we wish to find the max of
each string list integer. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop +int()**  
This is the brute force method to perform this task. In this, we run a loop
for the entire list, convert each string to integer and perform maximization
listwise and store in a separate list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum of Sting Integer

# using loop + int()

 

# initialize list 

test_list = [['1', '4'], ['5', '6'], ['7',
'10']]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Maximum of Sting Integer

# using loop + int()

res = []

for sub in test_list:

 par_max = 0

 for ele in sub:

 par_max = max(par_max, int(ele))

 res.append(par_max)

 

# printing result

print("List after maximization of nested string lists : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['1', '4'], ['5', '6'], ['7', '10']]
    List after maximization of nested string lists : [4, 6, 10]
    

**Method #2 : Usingmax() + int() \+ list comprehension**  
This is the shorthand with the help of which this task can be performed. In
this, we run a loop on lists using list comprehension and extract maximization
using max().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum of Sting Integer

# using max() + int() + list comprehension

 

# initialize list 

test_list = [['1', '4'], ['5', '6'], ['7',
'10']]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Maximum of Sting Integer

# using max() + int() + list comprehension

res = [max(int(ele) for ele in sub) for sub in
test_list]

 

# printing result

print("List after maximization of nested string lists : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['1', '4'], ['5', '6'], ['7', '10']]
    List after maximization of nested string lists : [4, 6, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

