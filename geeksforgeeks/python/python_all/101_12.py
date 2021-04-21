Python | Mutually different Records



Sometimes, while working with data, we may have a problem in which we require
to find the unmatching records between two lists that we receive. This is a
very common problem and records usually occurs as a tuple. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension**  
List comprehension can be opted as method to perform this task in one line
rather than running a loop to find the common element. In this, we just
iterate for single list and check if any element occurs in other one.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mutually different Records

# Using list comprehension

 

# Initializing lists

test_list1 = [('gfg', 1), ('is', 2), ('best',
3)]

test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Mutually different Records

# Using list comprehension

res1 = [ele1 for ele1 in test_list1 for ele2 in
test_list2 if ele1 == ele2]

res = [ele for ele in test_list1 if ele not in res1]

res2 = [ele for ele in test_list2 if ele not in res1]

rest = res2 + res

 

# printing result

print("The unmatched data records are : " + str(rest))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [('gfg', 1), ('is', 2), ('best', 3)]
    The original list 2 is : [('i', 3), ('love', 4), ('gfg', 1)]
    The unmatched data records are : [('i', 3), ('love', 4), ('is', 2), ('best', 3)]
    

**Method #2 : Usingset.symmetric_difference()**  
This task can also be performed in smaller way using the generic set symmetric
difference. In this, we first convert the list of records to a set and then
perform its unmatching using symmetric_difference().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mutually different Records

# Using set.symmetric_difference()

 

# Initializing lists

test_list1 = [('gfg', 1), ('is', 2), ('best',
3)]

test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Mutually different Records

# set.symmetric_difference()

res =
list(set(test_list1).symmetric_difference(set(test_list2)))

 

# printing result

print("The unmatched data records are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [('gfg', 1), ('is', 2), ('best', 3)]
    The original list 2 is : [('i', 3), ('love', 4), ('gfg', 1)]
    The unmatched data records are : [('i', 3), ('love', 4), ('is', 2), ('best', 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

