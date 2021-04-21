Python – Like Index Common characters



Sometimes we come across this type of problem in which we require to intersect
each element of one list with the other. This type of problems usually occurs
in developments in which we have the combined information, like names and
surnames in different lists. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Using list comprehension +zip() + intersection()**  
List comprehension does the task of intersecting the similar index elements.
The task of zip function is concatenating the resultant string into a single
list and return list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Like Index Common characters

# using list comprehension + zip() + intersection()

 

# initializing lists 

test_list1 = ["Geeksfor", "is", "be"]

test_list2 = ['Geeks', 'sb', 'ste']

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using list comprehension + zip()

# Like Index Common characters + intersection()

res = ["".join(list(set(i).intersection(set(j)))) for i,
j in zip(test_list1, test_list2)]

 

# printing result 

print ("The list after element intersection is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['Geeksfor', 'is', 'be']
    The original list 2 is : ['Geeks', 'sb', 'ste']
    The list after element intersection is : ['sGek', 's', 'e']
    

**Method #2 : Usingmap() + lambda + zip() + intersection()**  
The task of mapping each index element with each other is performed by map
function in this method and the functionality of intersection is performed by
lambda and intersection() function. This method works only in Python 2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Like Index Common characters

# using map() + lambda + zip() + intersection()

 

# initializing lists 

test_list1 = ["Geeksfor", "is", "be"]

test_list2 = ['Geeks', 'sb', 'ste']

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using map() + lambda + zip() + intersection()

# Like Index Common characters

res = list(map(lambda(i, j):
"".join(list(set(i).intersection(set(j)))), zip(test_list1,
test_list2)))

 

# printing result 

print ("The list after element intersection is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['Geeksfor', 'is', 'be']
    The original list 2 is : ['Geeks', 'sb', 'ste']
    The list after element intersection is : ['sGek', 's', 'e']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

