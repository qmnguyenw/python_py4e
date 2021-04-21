Python – Product of Selective Tuple Keys



Sometimes, while using list of tuples, we come across a problem in which we
have certain list of keys and we just need the product of values of those keys
from list of tuples. This has a utility in rating or product of specific
entities. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingdict() + loop + get() \+ list comprehension**  
We can perform this particular task by first, converting the list into the
dictionary and then employing list comprehension to get the value of specific
keys using get function. The product of values is performed using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Product of Selective Tuple Keys

# using dict() + get() + list comprehension + loop

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list of tuples 

test_list = [('Nikhil', 1), ('Akash', 2), ('Akshat',
3), ('Manjeet', 4)]

 

# initializing selection list 

select_list = ['Nikhil', 'Akshat']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# printing selection list 

print ("The selection list is : " + str(select_list))

 

# using dict() + get() + list comprehension + loop

# Product of Selective Tuple Keys

temp = dict(test_list)

res = prod([temp.get(i, 0) for i in select_list])

 

# printing result

print ("The selective values product of keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Nikhil', 1), ('Akash', 2), ('Akshat', 3), ('Manjeet', 4)]
    The selection list is : ['Nikhil', 'Akshat']
    The selective values product of keys : 3
    

**Method #2 : Usingnext() + loop \+ list comprehension**  
This particular problem can be solved using the next function which performs
the iteration using the iterators and hence more efficient way to achieve a
possible solution. The product of values is performed using loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Product of Selective Tuple Keys

# using next() + list comprehension + loop

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list of tuples 

test_list = [('Nikhil', 1), ('Akash', 2), ('Akshat',
3), ('Manjeet', 4)]

 

# initializing selection list 

select_list = ['Nikhil', 'Akshat']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# printing selection list 

print ("The selection list is : " + str(select_list))

 

# using next() + list comprehension + loop

# Product of Selective Tuple Keys

res = prod([next((sub[1] for sub in test_list if
sub[0] == i), 0) for i in select_list])

 

# printing result

print ("The selective values product of keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Nikhil', 1), ('Akash', 2), ('Akshat', 3), ('Manjeet', 4)]
    The selection list is : ['Nikhil', 'Akshat']
    The selective values product of keys : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

