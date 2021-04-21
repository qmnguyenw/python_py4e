Python | Append suffix/prefix to strings in list



Sometimes, while working with Python, we can a problem in which we need to pad
strings in lists at trailing or leading position. This kind of problem is
quite common and can occur in day-day programming or web development. Let’s
discuss a way in which this task can be performed.

 **Method : Using+ operator \+ list comprehension**

In this task, we just append the string at rear or front position using +
operator and list comprehension is used to iterate through all the elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append suffix / prefix to strings in list

# Using list comprehension + "+" operator

 

# initializing list

test_list = ['a', 'b', 'c', 'd']

 

# printing list

print("The original list : " + str(test_list))

 

# initializing append_str

append_str = 'gfg'

 

# Append suffix / prefix to strings in list

pre_res = [append_str + sub for sub in test_list]

suf_res = [sub + append_str for sub in test_list]

 

# Printing result

print("list after prefix addition : " + str(pre_res))

print("list after suffix addition : " + str(suf_res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : ['a', 'b', 'c', 'd']
    list after prefix addition : ['gfga', 'gfgb', 'gfgc', 'gfgd']
    list after suffix addition : ['agfg', 'bgfg', 'cgfg', 'dgfg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

