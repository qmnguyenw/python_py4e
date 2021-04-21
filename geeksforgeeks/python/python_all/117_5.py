Python | Extract least frequency element



Sometimes, while working with data, we can have a problem in which we need to
extract element which is occurring least number of times in the list. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Usingdefaultdict() \+ loop**  
The combination of above functions can be used to perform this task. In this,
we extract each element’s frequency using defaultdict() and extract the
minimum frequency element after traversing the defaultdict.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract least frequency element

# using defaultdict() + loop

from collections import defaultdict

 

# initialize list 

test_list = [1, 3, 4, 5, 1, 3, 5]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Extract least frequency element

# using defaultdict() + loop

res = defaultdict(int)

for ele in test_list:

 res[ele] += 1

min_occ = 9999

for ele in res:

 if min_occ > res[ele]:

 min_occ = res[ele]

 tar_ele = ele

 

# printing result

print("The minimum occurring element is : " + str(tar_ele))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 3, 4, 5, 1, 3, 5]
    The minimum occurring element is : 4
    

**Method #2 : UsingCounter()**  
This method is similar to above, the difference is that the frequency is
stored using Counter() and then we extract element with least frequency.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract least frequency element

# using Counter()

from collections import Counter

 

# initialize list 

test_list = [1, 3, 4, 5, 1, 3, 5]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Extract least frequency element

# using Counter

res = Counter(test_list)

tar_ele = res.most_common()[-1][0]

 

# printing result

print("The minimum occurring element is : " + str(tar_ele))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 3, 4, 5, 1, 3, 5]
    The minimum occurring element is : 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

