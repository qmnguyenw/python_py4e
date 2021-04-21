Python | Adding value to sublists



Sometimes, we just have to manipulate a list of lists by appending a similar
value to all the sublists. Using a loop for achieving this particular task can
be an option but sometimes leads to sacrifice the readability of code. It is
always wanted to have a oneliner to perform this particular task. Let’s
discuss certain ways in which this can be done.

 **Method #1 : Using list comprehension**  
List comprehension can be used to perform this particular task using a similar
looping construct but in just a single line. This increases code readability.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# appending single value 

# using list comprehension 

 

# initializing list of lists

test_list = [[1, 3], [3, 4], [6, 5], [4,
5]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# declaring element to be inserted

K = "GFG"

 

# using list comprehension 

# appending single value

res = [[i, j, K ] for i, j in test_list]

 

# printing result 

print("The list after adding element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [[1, 3], [3, 4], [6, 5], [4, 5]]  
> The list after adding element : [[1, 3, ‘GFG’], [3, 4, ‘GFG’], [6, 5,
> ‘GFG’], [4, 5, ‘GFG’]]

  

  

**Method #2 : Using list comprehension +"+" operator**  
This method is quite similar to the above method, but the difference is that
plus operator is used to add the new element to each sublist.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# appending single value 

# using list comprehension + "+" operator

 

# initializing list of lists

test_list = [[1, 3], [3, 4], [6, 5], [4,
5]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# declaring element to be inserted

K = "GFG"

 

# using list comprehension + "+" operator

# appending single value

res = [sub + [K] for sub in test_list]

 

# printing result 

print("The list after adding element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [[1, 3], [3, 4], [6, 5], [4, 5]]  
> The list after adding element : [[1, 3, ‘GFG’], [3, 4, ‘GFG’], [6, 5,
> ‘GFG’], [4, 5, ‘GFG’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

