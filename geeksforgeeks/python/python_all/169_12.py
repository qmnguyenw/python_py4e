Python | Splitting string to list of characters



Sometimes we need to work with just the lists and hence strings might need to
be converted into lists. It has to be converted in list of characters for
certain tasks to be performed. This is generally required in Machine Learning
to preprocess data and text classifications.

Let’s discuss certain ways in which this task is performed.

 **Method #1 : Using list slicing**  
List slicing can be used for this particular purpose, in which we assign to
each index element of list the next occurring character of string using the
slice operation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# splitting string to list of characters.

# using list slicing

 

# initializing string

test_string = "GeeksforGeeks"

 

# printing original string 

print ("The original string is : " + str(test_string))

 

# using list slicing

# for splitting string to list of characters

res = []

res[:] = test_string

 

# printing result

print ("The resultant list of characters : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : GeeksforGeeks  
> The resultant list of characters : [‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’,
> ‘G’, ‘e’, ‘e’, ‘k’, ‘s’]
>
>  
>
>
>  
>

 **Method #2 : Usinglist()**  
The most concise and readable way to perform splitting is to type case string
into list and the splitting of list is automatically handled internally. This
is recommended method to perform this particular task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# splitting string to list of characters.

# using list()

 

# initializing string

test_string = "GeeksforGeeks"

 

# printing original string 

print ("The original string is : " + str(test_string))

 

# using list()

# for splitting string to list of characters

res = list(test_string)

 

# printing result

print ("The resultant list of characters : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : GeeksforGeeks  
> The resultant list of characters : [‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’,
> ‘G’, ‘e’, ‘e’, ‘k’, ‘s’]

  
**Method #3 : Usingmap() + lambda**  
This is yet another way to perform this particular task. Though not
recommended but can be used in certain situations. But drawback is readability
of code gets sacrificed.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# splitting string to list of characters.

# using map() + lambda

 

# initializing string

test_string = "GeeksforGeeks"

 

# printing original string 

print ("The original string is : " + str(test_string))

 

# using map() + lambda

# for splitting string to list of characters

res = list(map(lambda i:i, test_string))

 

# printing result

print ("The resultant list of characters : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : GeeksforGeeks  
> The resultant list of characters : [‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’,
> ‘G’, ‘e’, ‘e’, ‘k’, ‘s’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

