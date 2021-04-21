Python | Filter dictionary key based on the values in selective list



In Python, sometimes we require to get only some of the dictionary keys and
not all. This problem is quite common in web development that we require to
get only the selective dictionary keys from some given list. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension**  
The list comprehension can be used to solve this particular problem. This is
just the shorthand way of performing it instead of writing a loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# getting selective dictionary keys

# using list comprehension

 

# initializing dictionary

test_dict = {"Akash" : 1, "Akshat" : 2, "Nikhil" :
3, "Manjeet" : 4}

 

# initializing selective list keys 

select_list = ['Manjeet', 'Nikhil']

 

# printing original dictionary

print ("The original dictionary is : " + str(test_dict))

 

# printing selective list 

print ("The selective list is : " + str(select_list))

 

# using list comprehension

# getting selective dictionary keys 

res = [test_dict[i] for i in select_list if i in
test_dict]

 

# printing result 

print ("The selected values from list keys is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Nikhil’: 3, ‘Akshat’: 2, ‘Manjeet’: 4,
> ‘Akash’: 1}  
> The selective list is : [‘Manjeet’, ‘Nikhil’]  
> The selected values from list keys is : [4, 3]

  
**Method #2 : Usingset.intersection()**  
This is the most elegant method in which this task can be performed. The
intersection property of sets can give the common keys that can be extracted
and then values can be computed.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# getting selective dictionary keys

# using set.intersection()

 

# initializing dictionary

test_dict = {"Akash" : 1, "Akshat" : 2, "Nikhil" :
3, "Manjeet" : 4}

 

# initializing selective list keys 

select_list = ['Manjeet', 'Nikhil']

 

# printing original dictionary

print ("The original dictionary is : " + str(test_dict))

 

# printing selective list 

print ("The selective list is : " + str(select_list))

 

# using set.intersection()

# getting selective dictionary keys 

temp = list(set(select_list).intersection(test_dict))

res = [test_dict[i] for i in temp]

 

# printing result 

print ("The selected values from list keys is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Akshat’: 2, ‘Manjeet’: 4, ‘Nikhil’: 3,
> ‘Akash’: 1}  
> The selective list is : [‘Manjeet’, ‘Nikhil’]  
> The selected values from list keys is : [4, 3]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

