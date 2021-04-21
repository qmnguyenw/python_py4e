Python | Test list element similarity



Given a list, your task is to determine the list is K percent same i.e has
element that is populated more than K % times.  
  
Given below are few methods to solve the task.  
 **Method #1 Using collections.Counter**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to check whether the list

# K percent same or not

from collections import Counter

 

# initializing list

ini_list1 = [1, 2, 3, 1, 1, 1, 1, 1,
3, 2]

 

# printing initial list

print ("Initial list", ini_list1)

 

# initializing K

K = 60

 

# code to check whether list is K % same or not

i, freq = Counter(ini_list1).most_common(1)[0]

 

if len(ini_list1)*(K / 100) <= freq:

 print("True")

else:

 print("False")  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial list [1, 2, 3, 1, 1, 1, 1, 1, 3, 2] 
    True
    

**Method #2: Using dictionary and its values**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to check whether the list

# K percent same or not

from collections import Counter, defaultdict

 

# initializing list

ini_list1 = [1, 2, 3, 1, 1, 1, 1, 1,
3, 2]

 

# printing initial list

print ("Initial list", ini_list1)

 

# initializing K

K = 60

 

# code to check whether list is K % same or not

freq = defaultdict(int)

for x in ini_list1:

 freq[x] += 1

freq = freq.values()

if max(freq) >= (K / 100) * sum(freq):

 print ("True")

else:

 print ("False")  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list [1, 2, 3, 1, 1, 1, 1, 1, 1, 1]
    True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

