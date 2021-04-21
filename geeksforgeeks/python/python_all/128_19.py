Python | Arrange Tuples consecutively in list



Sometimes, while working with tuple list, we may require a case in which we
require that a tuple starts from the end of previous tuple, i.e the element 0
of every tuple should be equal to ending element of tuple in list of tuple.
This type of problem and sorting is useful in competitive programming. Let’s
discuss way in which this problem can be solved.

 **Method : Using loop +dict()**  
This task can easily be solved by converting a tuple container list to
dictionary and then it’s easy to access a value of a key and arrange them
accordingly to sort in a way in which one tuple element begins with the ending
of other element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Arranging Tuples consecutively in list

# using loop + dict()

 

# initialize list

test_list = [(5, 6), (11, 8), (6, 11), (8,
9) ]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Arranging Tuples consecutively in list

# using loop + dict()

temp = dict(test_list) 

ele = test_list[0][0] 

res = [] 

for _ in range(len(test_list)):

 res.append((ele, temp[ele]))

 ele = temp[ele]

 

# printing result

print("The arranged list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(5, 6), (11, 8), (6, 11), (8, 9)]
    The arranged list is : [(5, 6), (6, 11), (11, 8), (8, 9)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

