Python | Element Occurrence in dictionary of list values



Sometimes we can have a task in which we are required to count the occurrences
of test elements in list or winning numbers, against the numbers with the
associated keys with list as values. This can have applications in gaming or
other utilities. Let’s discuss certain ways in which this can be done.

 **Method #1 : Using dictionary comprehension +sum()**  
This task can be performed using the combination of above two utilities in
which we use dictionary comprehension to bind the logic and sum function can
be used to perform the summation of the matches found from test list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Element Occurrence in dictionary value list

# using list comprehension + sum()

 

# initializing dictionary

test_dict = { "Akshat" : [1, 4, 5, 3],

 "Nikhil" : [4, 6],

 "Akash" : [5, 2, 1] }

 

# initializing test list 

test_list = [2, 1]

 

# printing original dict

print("The original dictionary : " + str(test_dict))

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + sum()

# Element Occurrence in dictionary value list

res = {idx : sum(1 for i in j if i in test_list)

 for idx, j in test_dict.items()}

 

# print result

print("The summation of element occurrence : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'Nikhil': [4, 6], 'Akshat': [1, 4, 5, 3], 'Akash': [5, 2, 1]}
    The original list : [2, 1]
    The summation of element occurrence : {'Nikhil': 0, 'Akshat': 1, 'Akash': 2}
    

**Method #2 : Usingcollections.Counter()**  
Python offers an inbuilt function that performs the task of extracting the
frequency and using this and conditioning to presence in test list, we can
solve the above problem using this function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Element Occurrence in dictionary value list

# using collections.Counter()

from collections import Counter

 

# initializing dictionary

test_dict = { "Akshat" : [1, 4, 5, 3],

 "Nikhil" : [4, 6],

 "Akash" : [5, 2, 1] }

 

# initializing test list 

test_list = [2, 1]

 

# printing original dict

print("The original dictionary : " + str(test_dict))

 

# printing original list 

print("The original list : " + str(test_list))

 

# using collections.Counter()

# Element Occurrence in dictionary value list

# omits the 0 occurrence word key

res = dict(Counter(j for j in test_dict

 for i in test_list if i in test_dict[j]))

 

# print result

print("The summation of element occurrence : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'Nikhil': [4, 6], 'Akshat': [1, 4, 5, 3], 'Akash': [5, 2, 1]}
    The original list : [2, 1]
    The summation of element occurrence : {'Akshat': 1, 'Akash': 2}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

