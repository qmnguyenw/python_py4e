Python | Extend tuples by count of elements in tuple



Sometime, while working with data, we can have a application in which we need
to duplicate tuple elements by the amount of element count. This is very
unique application but can occur in certain cases. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using nested loops**  
This is the brute force method by which this task can be performed. In this,
the outer loop is for iteration to each element in list and inner loop is to
add the similar element equating to length of respective tuple by outer loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extend tuples by count in list

# using nested loop

 

# initialize list of tuple

test_list = [('1', '4', '6'), ('5', '8'), ('2',
'9'), ('1', )]

 

# printing original tuples list

print("The original list : " + str(test_list))

 

# Extend tuples by count in list

# using nested loop

res = []

for sub in range(len(test_list)):

 for ele in range(len(test_list[sub])):

 res.append(test_list[sub])

 

# printing result

print("The modified and extended list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [(‘1’, ‘4’, ‘6’), (‘5’, ‘8’), (‘2’, ‘9’), (‘1’, )]  
> The modified and extended list is : [(‘1’, ‘4’, ‘6’), (‘1’, ‘4’, ‘6’), (‘1’,
> ‘4’, ‘6’), (‘5’, ‘8’), (‘5’, ‘8’), (‘2’, ‘9’), (‘2’, ‘9’), (‘1’, )]

  

  

**Method #2 : Using loop +chain()**  
This is yet another way in which this task can be performed. In this, we
reduce one loop, inner loop and multiply the tuples into one and flatten using
chain(). It may have certain overheads depending upon different cases.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extend tuples by count in list

# using loop + chain()

from itertools import chain

 

# initialize list of tuple

test_list = [('1', '4', '6'), ('5', '8'), ('2',
'9'), ('1', )]

 

# printing original tuples list

print("The original list : " + str(test_list))

 

# Extend tuples by count in list

# using loop + chain()

res = []

for sub in range(len(test_list)):

 res.append([test_list[sub]]*len(test_list[sub]))

res1 = chain(*res)

res = list(res1)

 

# printing result

print("The modified and extended list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [(‘1’, ‘4’, ‘6’), (‘5’, ‘8’), (‘2’, ‘9’), (‘1’, )]  
> The modified and extended list is : [(‘1’, ‘4’, ‘6’), (‘1’, ‘4’, ‘6’), (‘1’,
> ‘4’, ‘6’), (‘5’, ‘8’), (‘5’, ‘8’), (‘2’, ‘9’), (‘2’, ‘9’), (‘1’, )]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

