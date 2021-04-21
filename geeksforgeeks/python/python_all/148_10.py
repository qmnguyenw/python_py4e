Python | Shift zeroes at end of list



The conventional problem involving the element shifts has been discussed many
times earlier, but sometimes we have strict constraints performing them and
knowledge of any possible variation helps. This article talks about one such
problem of shifting 0’s at end of list, catch here is it checks for just 0’s
excluding the conventional ‘None’ (False) values. Let’s discuss certain ways
in which this can be performed.

 **Method #1 : Using list comprehension + isinstance()**

In this method, we perform the operation of shifting in 2 steps. In 1st step
we get all the values that we need to get at front and at end we just push the
zeroes to end. The isinstance method is used to filter out the Boolean False
entity.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Shift zeroes at end of list

# using list comprehension + isinstance()

 

# initializing list

test_list = [1, 4, None, "Manjeet", False, 0,
False, 0, "Nikhil"]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + isinstance()

# Shift zeroes at end of list

temp = [ele for ele in test_list if ele or

 ele is None or isinstance(ele, bool)]

res = temp + [0] * (len(test_list) - len(temp))

 

# print result

print("The list after shifting 0's to end : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [1, 4, None, ‘Manjeet’, False, 0, False, 0, ‘Nikhil’]  
> The list after shifting 0’s to end : [1, 4, None, ‘Manjeet’, False, False,
> ‘Nikhil’, 0, 0]
>
>  
>
>
>  
>

Method #2 : Using list comprehension + isinstance() \+ list slicing

