Python | Sort alternate numeric and alphabet list



Sometimes, while performing sorting in list, we have a problem in which we
need to perform particular type of sorting in which we need to sort in
alternate ways in which we have numerics and alphabets sorted in order. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Usingisalpha() + isnumeric() + zip_longest()**  
The combination of above methods can be used to perform this task. In this, we
separate the numeric and alphabets and then perform a sort on them separately
and join using zip_longest().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sort alternate numeric and alphabet list

# using isalpha() + isnumeric() + zip_longest()

from itertools import zip_longest

 

# Initializing list

test_list = ['3', 'B', '2', 'A', 'C', '1']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Sort alternate numeric and alphabet list

# using isalpha() + isnumeric() + zip_longest()

num_list = sorted(filter(str.isnumeric, test_list), 

 key = lambda sub: int(sub))

 

chr_list = sorted(filter(str.isalpha, test_list))

res = [ele for sub in zip_longest(num_list, chr_list)

 for ele in sub if ele]

 

# printing result 

print ("List after performing sorting : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['3', 'B', '2', 'A', 'C', '1']
    List after performing sorting : ['1', 'A', '2', 'B', '3', 'C']
    

**Method #2 : Usingsorted() + key + lambda + isnumeric()**  
The combination of above methods can be used to perform this task. In this, we
perform the sorting in alternate manner using ord() and lambda function,
testing using isnumeric().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sort alternate numeric and alphabet list

# using sorted() + key + lambda + isnumeric()

from itertools import zip_longest

 

# Initializing list

test_list = ['3', 'B', '2', 'A', 'C', '1']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Sort alternate numeric and alphabet list

# using sorted() + key + lambda + isnumeric()

res = sorted(test_list, key = lambda ele : (int(ele), 0)

 if ele.isnumeric()

 else ((ord(ele) - 64) % 26, 1))

 

# printing result 

print ("List after performing sorting : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['3', 'B', '2', 'A', 'C', '1']
    List after performing sorting : ['1', 'A', '2', 'B', '3', 'C']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

