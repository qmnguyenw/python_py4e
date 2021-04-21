Python | Join cycle in list



Sometimes, while dealing with graph problems in competitive programming, we
have a list of pairs and we need to find if there is a possible cycle in it,
and print all the elements in that cycle. Let’s discuss certain way in which
this problem can be tackled.

 **Method : Using yield + loop + generator**  
The brute method to perform is to use a generator and keep printing the value
if we know that the elements surely form a cycle and this is done by infinite
loop and stopping when no more matches are found.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Join cycle in list

# Using yield + loop + generator

 

# helper function to perform this task 

def cycle(test_list, val, stop = None):

 temp = dict(test_list)

 stop = stop if stop is not None else val

 while True:

 yield (val)

 val = temp.get(val, stop)

 if val == stop: break

 

# initializing list

test_list = [[6, 7], [9, 6], [7, 9]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Join cycle in list

# Using yield + loop + generator

# printing result

print("The cycle elements are : ")

for ele in cycle(test_list, 6):

 print(ele)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[6, 7], [9, 6], [7, 9]]
    The cycle elements are : 
    6
    7
    9
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

