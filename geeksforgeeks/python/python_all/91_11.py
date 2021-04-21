Python | Records List Concatenation



Sometimes, while working with Python records, we can have a problem in which
we need to perform cross concatenation of list of tuples. This kind of
application is popular in web development domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using list comprehension +zip()**  
The combination of above functionalities can be used to perform this
particular task. In this, we iterate through the list using list comprehension
and the concatenation across lists is performed with help of zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Records List Concatenation

# using list comprehension + zip()

 

# initialize lists

test_list1 = [("g", "f"), ("g", "is"), ("be",
"st")]

test_list2 = [("fg", "g"), ("gf", "best"), ("st", "
gfg")]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Records List Concatenation

# using list comprehension + zip()

res = [(x[0] + y[0], x[1] + y[1]) for x, y
in zip(test_list1, test_list2)]

 

# printing result

print("The Concatenation across lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [('g', 'f'), ('g', 'is'), ('be', 'st')]
    The original list 2 : [('fg', 'g'), ('gf', 'best'), ('st', ' gfg')]
    The Concatenation across lists is : [('gfg', 'fg'), ('ggf', 'isbest'), ('best', 'st gfg')]
    

**Method #2 : Usingjoin() + zip() + map()**  
This is yet another way to perform this task. This is similar to above method,
the difference is that summation is performed by inbuilt function and
extending logic to each element is done by map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Records List Concatenation

# using join() + zip() + map()

 

# initialize lists

test_list1 = [("g", "f"), ("g", "is"), ("be",
"st")]

test_list2 = [("fg", "g"), ("gf", "best"), ("st", "
gfg")]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Records List Concatenation

# using join() + zip() + map()

res = [tuple(map("".join, zip(a, b))) for a, b in
zip(test_list1, test_list2)]

 

# printing result

print("The Concatenation across lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [('g', 'f'), ('g', 'is'), ('be', 'st')]
    The original list 2 : [('fg', 'g'), ('gf', 'best'), ('st', ' gfg')]
    The Concatenation across lists is : [('gfg', 'fg'), ('ggf', 'isbest'), ('best', 'st gfg')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

