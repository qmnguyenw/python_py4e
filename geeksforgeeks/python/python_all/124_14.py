Python | Convert string tuples to list tuples



Sometimes, while working with Python we can have a problem in which we have a
list of records in form of tuples in stringified form and we desire to convert
them to list of tuples. This kind of problem can have it’s occurrence in data
science domain. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Usingeval() \+ list comprehension**  
This problem can be easily performed as one liner using the inbuilt function
of eval(), which performs this task of string to tuple conversion and list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Converting string tuples to list tuples 

# using list comprehension + eval()

 

# Initializing list 

test_list = ["('gfg', 1)", "('is', 2)", "('best', 3)"]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Converting string tuples to list tuples 

# using list comprehension + eval()

res = [eval(ele) for ele in test_list]

 

# printing result

print("The list tuple after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ["('gfg', 1)", "('is', 2)", "('best', 3)"]
    The list tuple after conversion : [('gfg', 1), ('is', 2), ('best', 3)]
    

**Method #2 : Usingeval() + map()**  
This task can also be performed using combination of above functions. The task
performed by list comprehension above can be performed using map() in this
method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Converting string tuples to list tuples 

# using map() + eval()

 

# Initializing list 

test_list = ["('gfg', 1)", "('is', 2)", "('best', 3)"]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Converting string tuples to list tuples 

# using map() + eval()

res = list(map(eval, test_list))

 

# printing result

print("The list tuple after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ["('gfg', 1)", "('is', 2)", "('best', 3)"]
    The list tuple after conversion : [('gfg', 1), ('is', 2), ('best', 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

