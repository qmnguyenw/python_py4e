Python | Maximum frequency character in String



This article gives us the methods to find the frequency of maximum occurring
character in a python string. This is quite important utility nowdays and
knowledge of it is always useful. Let’s discuss certain ways in which this
task can be performed.

 **Method 1 : Naive method + max()**  
In this method, we simply iterate through the string and form a key in a
dictionary of newly occurred element or if element is already occurred, we
increase its value by 1. We find maximum occurring character by using max() on
values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Maximum frequency character in String

# naive method 

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string

print ("The original string is : " + test_str)

 

# using naive method to get

# Maximum frequency character in String

all_freq = {}

for i in test_str:

 if i in all_freq:

 all_freq[i] += 1

 else:

 all_freq[i] = 1

res = max(all_freq, key = all_freq.get) 

 

# printing result 

print ("The maximum of all characters in GeeksforGeeks is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The maximum of all characters in GeeksforGeeks is : e
    

**Method 2 : Usingcollections.Counter() + max()**  
The most suggested method that could be used to find all occurrences is this
method, this actually gets all element frequency and could also be used to
print single element frequency if required. We find maximum occurring
character by using max() on values.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Maximum frequency character in String

# collections.Counter() + max()

from collections import Counter

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string

print ("The original string is : " + test_str)

 

# using collections.Counter() + max() to get 

# Maximum frequency character in String

res = Counter(test_str)

res = max(res, key = res.get) 

 

# printing result 

print ("The maximum of all characters in GeeksforGeeks is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The maximum of all characters in GeeksforGeeks is : e
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

