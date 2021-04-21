Python – Pairs with multiple similar values in dictionary



Sometimes, whilw working with dictionaries, we can have a problem in which we
need to keep the dictionaries which are having similar key’s value in other
dictionary. This is a very specific problem. This can have applications in web
development domain. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using list comprehension**  
This task can be performed using list comprehension. In this we iterate each
element in list and nesting loop is run to match key’s value with every other
value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Pairs with multiple similar values in dictionary

# using list comprehension

 

# Initializing list

test_list = [{'Gfg' : 1, 'is' : 2}, {'Gfg' : 2,
'is' : 2}, {'Gfg' : 1, 'is' : 2}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Pairs with multiple similar values in dictionary

# using list comprehension

res = [sub for sub in test_list if len([ele for ele
in test_list if ele['Gfg'] == sub['Gfg']]) > 1]

 

# printing result 

print ("List after keeping dictionary with same key's value : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [{'is': 2, 'Gfg': 1}, {'is': 2, 'Gfg': 2}, {'is': 2, 'Gfg': 1}]
    List after keeping dictionary with same key's value : [{'is': 2, 'Gfg': 1}, {'is': 2, 'Gfg': 1}]
    

**Method #2 : UsingCounter() \+ list comprehension**  
In this method, the task of finding the frequency is performed using Counter()
and then task of finding the elements having multiple keys value is done using
list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Pairs with multiple similar values in dictionary

# using list comprehension + Counter()

from collections import Counter

 

# Initializing list

test_list = [{'Gfg' : 1, 'is' : 2}, {'Gfg' : 2,
'is' : 2}, {'Gfg' : 1, 'is' : 2}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Pairs with multiple similar values in dictionary

# using list comprehension + Counter()

temp = Counter(sub['Gfg'] for sub in test_list)

res = [ele for ele in test_list if temp[ele['Gfg']] >
1]

 

# printing result 

print ("List after keeping dictionary with same key's value : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [{'is': 2, 'Gfg': 1}, {'is': 2, 'Gfg': 2}, {'is': 2, 'Gfg': 1}]
    List after keeping dictionary with same key's value : [{'is': 2, 'Gfg': 1}, {'is': 2, 'Gfg': 1}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

