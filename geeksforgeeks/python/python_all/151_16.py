Python | Remove additional spaces in list



Sometimes, we have a list that contains strings and spaces in between them. We
desire to have uniformity, so that later if we decide them, we just have
single spaces between the lists. Hence its sometimes necessary to remove the
additional unnecessary spaces between the words in a list.

Let’s discuss certain ways in which this can be done.

 **Method #1 : Using list comprehension +enumerate()**  
In this method we create a whole new list rather than modifying the original
one, and check for element and its preceding element for spaces and add only
add one occurrence of space and leaving the rest.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing multiple spaces

# using list comprehension + enumerate()

 

# initializing list of lists

test_list = ["GfG", "", "", "", "", "is", "", "",
"best"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + enumerate()

# removing multiple spaces

res = [val for idx, val in enumerate(test_list)

 if val or (not val and test_list[idx - 1])]

 

# printing result 

print("The list after removing additional spaces : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['GfG', '', '', '', '', 'is', '', '', 'best']
    The list after removing additional spaces :  ['GfG', '', 'is', '', 'best']
    

  

  

**Method #2 : Using list comprehension +zip() \+ list slicing**  
In this method, we take a pair at a time and check if it’s both elements are
empty, if so, we discard it. If anyone is empty or both are non-empty, we keep
it in the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing multiple spaces

# using list comprehension + zip() + list slicing

 

# initializing list of lists

test_list = ["GfG", "", "", "", "", "is", "", "",
"best"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + zip() + list slicing

# removing multiple spaces

res = test_list[ : 1] + [j for i, j in

 zip(test_list, test_list[1 : ]) if i or j]

 

# printing result 

print("The list after removing additional spaces : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['GfG', '', '', '', '', 'is', '', '', 'best']
    The list after removing additional spaces :  ['GfG', '', 'is', '', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

