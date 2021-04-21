Python | Grouped Flattening of list



The problem of flattening a list is quite common, but sometimes, we need to
perform the flattening but in the grouped manner, i.e getting the sublists of
size K and flatten them. This particular utility has use-cases in many domains
including web-development and day-day programming as well. Let’s discuss
certain ways in which this can be done.

 **Method #1 : Using list comprehension + list slicing**  
This problem can be approached by using the list comprehension and also
applying list slicing to limit the grouping and binding the list is done as a
part of list comprehension logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# group flattening of list 

# using list comprehension + list slicing

 

# initializing list of lists

test_list = [[1, 3], [3, 4], [6, 5], [4,
5], [7, 6], [7, 9]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# declaring K 

K = 3

 

# using list comprehension + list slicing

# group flattening of list 

res = [[i for sub in test_list[j : j + K] for i in
sub]

 for j in range(0, len(test_list), K)]

 

# printing result 

print("The grouped flattened list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 3], [3, 4], [6, 5], [4, 5], [7, 6], [7, 9]]
    The grouped flattened list :  [[1, 3, 3, 4, 6, 5], [4, 5, 7, 6, 7, 9]]
    

**Method #2 : Using list comprehension +zip() + map()**  
This problem can also be solved using the combination of the above 3
functions. The zip function is used to get all the groups into one and map
function is used to convert the iterator into list and list comprehension
performs the task of grouping.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# group flattening of list 

# using list comprehension + zip() + map()

 

# initializing list of lists

test_list = [[1, 3], [3, 4], [6, 5], [4,
5], [7, 6], [7, 9]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# declaring K 

K = 3

 

# using list comprehension + zip() + map()

# group flattening of list 

res = list(map(list, zip(*[iter([i for sub
in test_list

 for i in sub])]*(K * len(test_list[0])))))

 

# printing result 

print("The grouped flattened list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 3], [3, 4], [6, 5], [4, 5], [7, 6], [7, 9]]
    The grouped flattened list :  [[1, 3, 3, 4, 6, 5], [4, 5, 7, 6, 7, 9]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

