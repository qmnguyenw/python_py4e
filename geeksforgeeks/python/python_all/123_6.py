Python | Convert Lists to column tuples



Sometimes, while working with data, we can have a problem in which we need to
get alike index elements in a single container. This means the columns of
Matrix/Multiple lists need to be converted to list of tuples, each comprising
of like index elements. Let’s discuss certain ways in which this task can be
done.

 **Method #1 : Usingzip() \+ list comprehension**  
The combination of above functions can work together to achieve this
particular task. In this, we combine the like index elements into column using
zip(), and binding all tuples into a list and iteration of dictionary lists is
performed by list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Lists to column tuples

# using zip() + list comprehension

 

# initialize dictionary

test_dict = {'list1' : [1, 4, 5], 

 'list2' : [6, 7, 4],

 'list3' : [9, 1, 11]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Lists to column tuples

# using zip() + list comprehension

res = list(zip(*(test_dict[key] for key in
test_dict.keys())))

 

# printing result

print("Like index column tuples are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary is : {‘list3’: [9, 1, 11], ‘list2’: [6, 7, 4],
> ‘list1’: [1, 4, 5]}  
> Like index column tuples are : [(9, 6, 1), (1, 7, 4), (11, 4, 5)]

  

  

**Method #2 : Usingzip() + values()**  
The combination of above functions can be used to perform this task. In this,
we access the values of dictionary values using the values() and aggregating
columns can be done using zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Lists to column tuples

# using zip() + values()

 

# initialize dictionary

test_dict = {'list1' : [1, 4, 5], 

 'list2' : [6, 7, 4], 

 'list3' : [9, 1, 11]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Lists to column tuples

# using zip() + values()

res = list(zip(*test_dict.values()))

 

# printing result

print("Like index column tuples are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary is : {‘list3’: [9, 1, 11], ‘list2’: [6, 7, 4],
> ‘list1’: [1, 4, 5]}  
> Like index column tuples are : [(9, 6, 1), (1, 7, 4), (11, 4, 5)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

