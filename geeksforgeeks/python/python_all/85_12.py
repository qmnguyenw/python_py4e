Python – Elements with K lists similar index value



Sometimes, while working with data, we can have a problem in which we need to
get elements which are similar in K lists in particular index. This can have
application in many domains such as day-day and other domains. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Usingzip() \+ loop**  
This is brute way in which this task can be performed. In this, we iterate the
loop in zipped list and compare with elements in particular index for
similarity.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Elements with K lists similar index value

# using zip() + loop

 

# Initializing lists

test_list1 = [1, 3, 5, 7]

test_list2 = [1, 4, 8, 9]

test_list3 = [3, 7, 5, 10]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

print("The original list 3 is : " + str(test_list3))

 

# Initializing K 

K = 2

 

# Elements with K lists similar index value

# using zip() + loop

res = []

for a, b, c in zip(test_list1, test_list2, test_list3):

 if a == b or b == c or c == a:

 if a == b:

 res.append(a)

 elif b == c:

 res.append(b)

 elif c == a:

 res.append(c)

 

# printing result 

print ("The list after checking on 2 lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 5, 7]
    The original list 2 is : [1, 4, 8, 9]
    The original list 3 is : [3, 7, 5, 10]
    The list after checking on 2 lists : [1, 5]
    

**Method #2 : Using list comprehension +set() + count()**  
The combination of above methods can also be used to perform this task. In
this, we check for count using count() and rest of functionalities are
performed using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Elements with K lists similar index value

# using list comprehension + count() + set()

 

# Initializing lists

test_list1 = [1, 3, 5, 7]

test_list2 = [1, 4, 8, 9]

test_list3 = [3, 7, 5, 10]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

print("The original list 3 is : " + str(test_list3))

 

# Initializing K 

K = 2

 

# Elements with K lists similar index value

# using list comprehension + count() + set()

res = [ele for sub in zip(test_list1, test_list2, test_list3)
for ele in set(sub) if sub.count(ele) > 1]

 

# printing result 

print ("The list after checking on 2 lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 5, 7]
    The original list 2 is : [1, 4, 8, 9]
    The original list 3 is : [3, 7, 5, 10]
    The list after checking on 2 lists : [1, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

