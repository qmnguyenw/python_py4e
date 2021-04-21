Sort mixed list in Python



Sometimes, while working with Python, we can have a problem in which we need
to sort a particular list which has mixed data types. That it contains
integers and strings and we need to sort each of them accordingly. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Usingsort() \+ comparator**

This problem can be solved using sort functionality provided by Python. We can
construct our own custom comparator to complete the task of mixed sort.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Mixed List

# using sort() + comparator

 

# comparator function for sort

def mixs(num):

 try:

 ele = int(num)

 return (0, ele, '')

 except ValueError:

 return (1, num, '')

 

 

# initialize list 

test_list = [4, 'gfg', 2, 'best', 'is', 3]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Sort Mixed List

# using sort() + comparator

test_list.sort(key = mixs)

 

# printing result

print("List after mixed sorting : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 'gfg', 2, 'best', 'is', 3]
    List after mixed sorting : [2, 3, 4, 'best', 'gfg', 'is']
    

  

  

**Method #2 : Usingsorted() + key + lambda + isdigit()**

The combination of above functionalities can also be used to achieve solution
to this problem. In this, we just sort the list using sorted() using key
functionality using lambda function to segregate digits using isdigit().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Mixed List

# using sorted() + key + lambda + isdigit()

 

# initialize list 

test_list = ['4', 'gfg', '2', 'best', 'is', '3']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Sort Mixed List

# using sorted() + key + lambda + isdigit()

res = sorted(test_list, key = lambda ele: (0, int(ele))

 if ele.isdigit() else (1, ele))

 

# printing result

print("List after mixed sorting : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['4', 'gfg', '2', 'best', 'is', '3']
    List after mixed sorting : ['2', '3', '4', 'best', 'gfg', 'is']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

