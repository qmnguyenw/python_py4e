Python | Move given element to List Start



The conventional problem involving the element shifts has been discussed many
times earlier, but sometimes we have strict constraints performing them and
knowledge of any possible variation helps. This article talks about one such
problem of shifting K’s at start of list, catch here is it checks for just K’s
excluding the conventional ‘None’ (False) values. Let’s discuss certain ways
in which this can be performed.

 **Method #1 : Using list comprehension +isinstance()**  
In this method, we perform the operation of shifting in 2 steps. In 1st step
we get all the values that we need to get at front and at end we just push the
K’s to front. The isinstance method is used to filter out the Boolean False
entity.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Move all K element to List Start

# using list comprehension + isinstance() 

 

# initializing list 

test_list = [1, 4, None, "Manjeet", False, 4,
False, 4, "Nikhil"] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# initializing K 

K = 4

 

# using list comprehension + isinstance() 

# Move all K element to List Start

temp = [ele for ele in test_list if ele != K and ele
or ele is None or isinstance(ele, bool) ] 

res = [K] * (len(test_list) - len(temp)) + temp

 

# print result 

print("The list after shifting K's to start : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [1, 4, None, 'Manjeet', False, 4, False, 4, 'Nikhil']
    The list after shifting K's to start : [4, 4, 4, 1, None, 'Manjeet', False, False, 'Nikhil']
    

**Method #2 : Using list comprehension + isinstance() \+ list slicing**  
This method is similar to the above method, the only modification is that to
reduce number of steps, list slicing is used to attach the K’s to perform
whole task in just 1 step.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Move all K element to List Start

# using list comprehension + isinstance() + list slicing 

 

# initializing list 

test_list = [1, 4, None, "Manjeet", False, 4,
False, 4, "Nikhil"] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# initializing K 

K = 4

 

# using list comprehension + isinstance() + list slicing 

# Move all K element to List Start

res = ([K] * len(test_list) + [ele for ele in test_list
if ele != K and ele or not isinstance(ele, int) 

 or isinstance(ele, bool)])[len([ele for ele in
test_list if ele != K and ele or not isinstance(ele,
int) 

 or isinstance(ele, bool)]):] 

 

# print result 

print("The list after shifting K's to end : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [1, 4, None, 'Manjeet', False, 4, False, 4, 'Nikhil']
    The list after shifting K's to start : [4, 4, 4, 1, None, 'Manjeet', False, False, 'Nikhil']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

