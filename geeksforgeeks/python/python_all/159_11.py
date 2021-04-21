Python | Finding frequency in list of tuples



In python we need to handle various forms of data and one among them is list
of tuples in which we may have to perform any kind of operation. This
particular article discusses the ways of finding the frequency of the 1st
element in list of tuple which can be extended to any index. Let’s discuss
certain ways in which this can be performed.

 **Method #1 : Usingmap() + count()**  
The map function can be used to accumulate the indices of all the tuples in a
list and the task of counting the frequency can be done using the generic
count function of python library.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# finding frequency in list of tuples

# using map() + count()

 

# initializing list of tuples

test_list = [('Geeks', 1), ('for', 2), ('Geeks',
3)]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using map() + count()

# finding frequency in list of tuples 

res = list(map(lambda i : i[0],
test_list)).count('Geeks')

 

# printing result

print ("The frequency of element is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [('Geeks', 1), ('for', 2), ('Geeks', 3)]
    The frequency of element is : 2
    

  
**Method #2 : UsingCounter() \+ list comprehension**  
List comprehension performs the task of getting the first element of the
tuples and the counting part is handled by Counter function of collection
library.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# finding frequency in list of tuples

# using Counter() + list comprehension

from collections import Counter

 

# initializing list of tuples

test_list = [('Geeks', 1), ('for', 2), ('Geeks',
3)]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using Counter() + list comprehension

# finding frequency in list of tuples 

res = Counter(i[0] for i in test_list)

 

# printing result

print ("The frequency of element is : " + str(res['Geeks']))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [('Geeks', 1), ('for', 2), ('Geeks', 3)]
    The frequency of element is : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

