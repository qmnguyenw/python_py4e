Python | Selective Merge in String list



Sometimes, while working with Python lists, we can have a problem in which we
need to perform the merge operation. There can be various modifications to
merge. One such can be replacing every character except a particular
character. Let’s see different ways in which this task can be performed.

 **Method #1 : Using list comprehension +join() + zip()**  
The combination of above methods can be used to perform this task. In this, we
combine the like elements using zip() and merge operation is performed using
join(). List comprehension is used to provide logic and iterations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Selective Merge in String list

# using list comprehension + join() + zip()

 

# initialize lists

test_list1 = ["abc", "de", "efgh"]

test_list2 = ["gfg", "is", "good"]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# initialize exempt char 

exm_chr = 'g'

 

# Selective Merge in String list

# using list comprehension + join() + zip()

res = [''.join(l if l == exm_chr else k for k, l in
zip(i, j))

 for i, j in zip(test_list1, test_list2)]

 

# printing result

print("The resultant list after Selective Merge : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : ['abc', 'de', 'efgh']
    The original list 2 : ['gfg', 'is', 'good']
    The resultant list after Selective Merge : ['gbg', 'de', 'gfgh']
    

**Method #2 : Usingmap() + lambda() + join() + zip()**  
The combination of above functions can also be used to perform this task. In
this, we use map() and join() to perform task performed by list comprehension.
Rest all task is performed similar to above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Selective Merge in String list

# using map() + lambda() + join() + zip()

 

# initialize lists

test_list1 = ["abc", "de", "efgh"]

test_list2 = ["gfg", "is", "good"]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# initialize exempt char 

exm_chr = 'g'

 

# Selective Merge in String list

# using map() + lambda() + join() + zip()

temp = lambda ele: ''.join([i if j != exm_chr else j for
i, j in ele])

res = list(map(temp, (map(lambda k: zip(*k),
zip(test_list1, test_list2)))))

 

# printing result

print("The resultant list after Selective Merge : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : ['abc', 'de', 'efgh']
    The original list 2 : ['gfg', 'is', 'good']
    The resultant list after Selective Merge : ['gbg', 'de', 'gfgh']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

