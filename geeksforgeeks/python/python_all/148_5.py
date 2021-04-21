Python | Triple list difference



The difference between 2 lists have been dealt previously, but sometimes, we
can have more than two lists and we need to find the mutual differences of one
list with every other list. This kind of problem has applications in many
domains. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Usingmap() + set() \+ list comprehension**

The combination of above 3 functions can be used to perform this particular
task. The map function can be used to convert the list to set by the set
function and list comprehension can be used to get the new mutual difference
list for each list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# triple list difference 

# using map() + set() + list comprehension

 

# initializing lists 

test_list1 = [1, 5, 6, 4, 7]

test_list2 = [8, 4, 3]

test_list3 = [9, 10, 3, 5]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

print("The original list 3 : " + str(test_list3))

 

# using map() + set() + list comprehension

# triple list difference 

temp1, temp2, temp3 = map(set, (test_list1, test_list2,
test_list3))

res1 = [ele for ele in test_list1 if ele not in temp2
and ele not in temp3]

res2 = [ele for ele in test_list2 if ele not in temp1
and ele not in temp3]

res3 = [ele for ele in test_list3 if ele not in temp2
and ele not in temp1]

 

# print result

print("The mutual difference list are : "

 + str(res1) + " " + str(res2) + " " + str(res3))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [1, 5, 6, 4, 7]
    The original list 2 : [8, 4, 3]
    The original list 3 : [9, 10, 3, 5]
    The mutual difference list are : [1, 6, 7] [8] [9, 10]
    

  

  

**Method #2 : Using map() + set() + "-" operator**

This problem can also be solved the minus operator, if one wishes not to use
the list comprehension. The minus operator can perform the boolean match
difference to compute the valid set difference.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# triple list difference 

# using map() + set() + "-" operator

 

# initializing lists 

test_list1 = [1, 5, 6, 4, 7]

test_list2 = [8, 4, 3]

test_list3 = [9, 10, 3, 5]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

print("The original list 3 : " + str(test_list3))

 

# using map() + set() + "-" operator

# triple list difference 

temp1, temp2, temp3 = map(set, (test_list1, test_list2,
test_list3))

res1 = temp1 - temp2 - temp3

res2 = temp2 - temp3 - temp1

res3 = temp3 - temp1 - temp2

res1, res2, res3 = map(list, (res1, res2, res3))

 

# print result

print("The mutual difference list are : "

 + str(res1) + " " + str(res2) + " " + str(res3))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [1, 5, 6, 4, 7]
    The original list 2 : [8, 4, 3]
    The original list 3 : [9, 10, 3, 5]
    The mutual difference list are : [1, 6, 7] [8] [9, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

