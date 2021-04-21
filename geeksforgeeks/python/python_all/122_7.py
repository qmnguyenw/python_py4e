Python | Merge Tuple String List values to String



Sometimes, while working with records, we can have a problem in which any
element of record can be of type string but mistakenly processed as list of
characters. This can be a problem while working with a lot of data. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension +join()**  
The combination of above functionalities can be used to achieve to solution of
above task. In this, we get the character list using list comprehension and
conversion task is performed by join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Merge Tuple String List values to String

# using list comprehension + join()

 

# initialize list

test_list = [(['g', 'f', 'g'], 1), (['i', 's'],
2), (['b', 'e', 's', 't'], 3)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Merge Tuple String List values to String

# using list comprehension + join()

res = [''.join(i) for i, j in test_list]

 

# printing result

print("The joined character list tuple element to string is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [([‘g’, ‘f’, ‘g’], 1), ([‘i’, ‘s’], 2), ([‘b’, ‘e’, ‘s’,
> ‘t’], 3)]  
> The joined character list tuple element to string is : [‘gfg’, ‘is’, ‘best’]

  

  

**Method #2 : Usingmap() + join() \+ lambda**  
The task performed by list comprehension in the above method can be performed
by map() and lambda function can be used to construct the logic to achieve the
solution to this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Merge Tuple String List values to String

# using map() + join() + lambda

 

# initialize list

test_list = [(['g', 'f', 'g'], 1), (['i', 's'],
2), (['b', 'e', 's', 't'], 3)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Merge Tuple String List values to String

# using map() + join() + lambda

res = list(map(lambda sub : "".join(sub[0]), test_list))

 

# printing result

print("The joined character list tuple element to string is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [([‘g’, ‘f’, ‘g’], 1), ([‘i’, ‘s’], 2), ([‘b’, ‘e’, ‘s’,
> ‘t’], 3)]  
> The joined character list tuple element to string is : [‘gfg’, ‘is’, ‘best’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

