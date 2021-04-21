Python | Selective Records Value Summation



Sometimes, while using list of tuples, we come across a problem in which we
have certain list of keys and we just need the summation of values of those
keys from list of tuples. This has a utility in rating or summation of
specific entities. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingdict() + sum() + get() \+ list comprehension**  
We can perform this particular task by first, converting the list into the
dictionary and then employing list comprehension to get the value of specific
keys using get function. The summation of values is performed using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Selective Records Value Summation

# using dict() + get() + list comprehension + sum()

 

# initializing list of tuples 

test_list = [('Nikhil', 1), ('Akash', 2), ('Akshat',
3), ('Manjeet', 4)]

 

# initializing selection list 

select_list = ['Nikhil', 'Akshat']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# printing selection list 

print ("The selection list is : " + str(select_list))

 

# using dict() + get() + list comprehension + sum()

# Selective Records Value Summation

temp = dict(test_list)

res = sum([temp.get(i, 0) for i in select_list])

 

# printing result

print ("The selective values summation of keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Nikhil', 1), ('Akash', 2), ('Akshat', 3), ('Manjeet', 4)]
    The selection list is : ['Nikhil', 'Akshat']
    The selective values summation of keys : 4
    

**Method #2 : Usingnext() + sum() \+ list comprehension**  
This particular problem can be solved using the next function which performs
the iteration using the iterators and hence more efficient way to achieve a
possible solution. The summation of values is performed using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Selective Records Value Summation

# using next() + list comprehension + sum()

 

# initializing list of tuples 

test_list = [('Nikhil', 1), ('Akash', 2), ('Akshat',
3), ('Manjeet', 4)]

 

# initializing selection list 

select_list = ['Nikhil', 'Akshat']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# printing selection list 

print ("The selection list is : " + str(select_list))

 

# using next() + list comprehension + sum()

# Selective Records Value Summation

res = sum([next((sub[1] for sub in test_list if
sub[0] == i), 0) for i in select_list])

 

# printing result

print ("The selective values summation of keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Nikhil', 1), ('Akash', 2), ('Akshat', 3), ('Manjeet', 4)]
    The selection list is : ['Nikhil', 'Akshat']
    The selective values summation of keys : 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

