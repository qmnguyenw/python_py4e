Python – Reverse sort Matrix Row by Kth Column



Sometimes, while working with data, we can have a problem in which we need to
perform sorting of each row of records by some of decisive factor like score.
This kind of problem is common in competitive programming and web development.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingsorted() \+ lambda + reverse**  
The combination of above methods can be used to perform this task. In this, we
sort the list in descending order using reverse by particular column using
lambda function and list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Reverse sort Matrix Row by Kth Column

# using sorted() + lambda + reverse()

 

# Initializing list

test_list = [['Manjeet', 65], ['Akshat', 42],
['Akash', 38], ['Nikhil', 192]]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 1

 

# Reverse sort Matrix Row by Kth Column

# using sorted() + lambda + reverse()

res = sorted(test_list, key = lambda ele: ele[K], reverse =
True)

 

# printing result 

print ("List after performing sorting of matrix records : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [[‘Manjeet’, 65], [‘Akshat’, 42], [‘Akash’, 38],
> [‘Nikhil’, 192]]  
> List after performing sorting of matrix records : [[‘Nikhil’, 192],
> [‘Manjeet’, 65], [‘Akshat’, 42], [‘Akash’, 38]]

  

  

**Method #2 : Usingsort() + itemgetter()**  
The combination of above methods can also be used to solve this problem. In
this, we perform the task of lambda function using itemgetter and sort()
performs sorting.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Reverse sort Matrix Row by Kth Column

# using sort() + itemgetter()

from operator import itemgetter

 

# Initializing list

test_list = [['Manjeet', 65], ['Akshat', 42],
['Akash', 38], ['Nikhil', 192]]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 1

 

# Reverse sort Matrix Row by Kth Column

# using sort() + itemgetter()

test_list.sort(key = itemgetter(K), reverse = True)

 

# printing result 

print ("List after performing sorting of matrix records : " +
str(test_list))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [[‘Manjeet’, 65], [‘Akshat’, 42], [‘Akash’, 38],
> [‘Nikhil’, 192]]  
> List after performing sorting of matrix records : [[‘Nikhil’, 192],
> [‘Manjeet’, 65], [‘Akshat’, 42], [‘Akash’, 38]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

