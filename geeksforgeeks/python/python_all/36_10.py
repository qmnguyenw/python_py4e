Python – Restrict Elements Frequency in List



Given a List, and elements frequency list, restrict frequency of elements in
list from frequency list.

>  **Input** : test_list = [1, 4, 5, 4, 1, 4, 4, 5, 5, 6], restrct_dict = {4 :
> 3, 1 : 1, 6 : 1, 5 : 1}  
>  **Output** : [1, 4, 5, 4, 4, 6]  
>  **Explanation** : Limit of 1 is 1, any occurrance more than that is
> removed. Similar with all elements.
>
>  **Input** : test_list = [1, 4, 5, 4, 1, 4, 4, 5, 5, 6], restrct_dict = {4 :
> 2, 1 : 1, 6 : 1, 5 : 1}  
>  **Output** : [1, 4, 5, 4, 6]  
>  **Explanation** : Limit of 4 is 3, any occurrance more than that is
> removed. Similar with all elements.

 **Method : Using loop + defaultdict()**

In this, we iterate for elements and and maintain lookup counter for each
element using defauldict(), if any element exceeds restrict dict, that element
is not added then onwards.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Restrict Elements Frequency in List

# Using loop + defaultdict()

from collections import defaultdict

 

# initializing list

test_list = [1, 4, 5, 4, 1, 4, 4, 5,
5, 6]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing restrct_dict

restrct_dict = {4 : 3, 1 : 1, 6 : 1, 5 :
2}

 

res = []

lookp = defaultdict(int)

for ele in test_list:

 lookp[ele] += 1

 

 # move to next ele if greater than restrct_dict count

 if lookp[ele] > restrct_dict[ele]:

 continue

 else:

 res.append(ele)

 

# printing results

print("Filtered List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [1, 4, 5, 4, 1, 4, 4, 5, 5, 6]
    Filtered List : [1, 4, 5, 4, 4, 5, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

