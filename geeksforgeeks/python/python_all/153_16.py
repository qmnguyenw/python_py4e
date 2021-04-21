Python | Getting sublist element till N



Sometimes, we may come across a utility in which we require to get the first N
sublist elements that too only a particular index. This can have an
application in queuing to get only the initial N person’s name. Let’s discuss
certain ways in which this can be done.

 **Method #1 : Using list comprehension and list slicing**  
The above two powerful Python utilities can be useful here as well to get the
result as list comprehension can extract the element slicing can restrict the
size we need to extract.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# getting sublist element till N

# using list comprehension + list slicing 

 

# initializing list 

test_list = [['Geeks', 1, 15], ['for', 3, 5],
['Geeks', 3, 7]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing N

N = 2

 

# using list comprehension + list slicing

# getting sublist element till N

res = [i[0] for i in test_list[ : N]] 

 

# print result

print("The first element of sublist till N : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['Geeks', 1, 15], ['for', 3, 5], ['Geeks', 3, 7]]
    The first element of sublist till N : ['Geeks', 'for']
    

**Method #2 : Usingmap() + itemgetter() + islice()**  
The combination of above 3 functions can be used to perform this particular
task. The itemgetter function gets the element to extract, islice slices till
N and map function combines the result.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# getting sublist element till N

# using map() + itemgetter() + islice()

from operator import itemgetter

from itertools import islice

 

# initializing list 

test_list = [['Geeks', 1, 15], ['for', 3, 5],
['Geeks', 3, 7]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing N

N = 2

 

# using map() + itemgetter() + islice()

# getting sublist element till N

res = list(map(itemgetter(0), islice(test_list, 0, N)))

 

# print result

print("The first element of sublist till N : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['Geeks', 1, 15], ['for', 3, 5], ['Geeks', 3, 7]]
    The first element of sublist till N : ['Geeks', 'for']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

