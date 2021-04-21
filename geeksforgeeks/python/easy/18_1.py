Python | Remove empty strings from list of strings



In many scenarios, we encounter the issue of getting an empty string in a huge
amount of data and handling that sometimes becomes a tedious task. Let’s
discuss certain way outs to remove empty strings from list of strings.

 **Method #1 : Using remove()**

This particular method is quite naive and not recommended to use, but is
indeed a method to perform this task. remove() generally removes the first
occurrence of empty string and we keep iterating this process until no empty
string is found in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing empty strings 

# using remove()

 

# initializing list 

test_list = ["", "GeeksforGeeks", "", "is", "best",
""]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using remove() to

# perform removal

while("" in test_list) :

 test_list.remove("")

 

# Printing modified list 

print ("Modified list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list is : ['', 'GeeksforGeeks', '', 'is', 'best', '']
    Modified list is : ['GeeksforGeeks', 'is', 'best']
    

  
**Method #2 : Using List Comprehension**  
More concise and better approach to remove all the empty strings, it just
checks if the string is not empty and re-makes the list with all strings that
are not empty.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# removing empty strings 

# using list comprehension

 

# initializing list 

test_list = ["", "GeeksforGeeks", "", "is", "best",
""]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using list comprehension to

# perform removal

test_list = [i for i in test_list if i]

 

# Printing modified list 

print ("Modified list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list is : ['', 'GeeksforGeeks', '', 'is', 'best', '']
    Modified list is : ['GeeksforGeeks', 'is', 'best']
    

  
**Method #3 : Usingjoin() + split()**  
Combining both the join() and split() operations, this task can also be
achieved. We first join all the strings so that empty space is removed, and
then split it back to list so that new list made now has no empty string.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing empty strings 

# using join() + split()

 

# initializing list 

test_list = ["", "GeeksforGeeks", "", "is", "best",
""]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using join() + split() to

# perform removal

test_list = ' '.join(test_list).split()

 

# Printing modified list 

print ("Modified list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list is : ['', 'GeeksforGeeks', '', 'is', 'best', '']
    Modified list is : ['GeeksforGeeks', 'is', 'best']
    

  
**Method #4 : Usingfilter()**  
Using filter() is the most elegant and fastest way to perform this task.
This method is highly recommended because speed matters when we deal with
large machine learning data set that may potentially contain empty string.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# removing empty strings 

# using filter()

 

# initializing list 

test_list = ["", "GeeksforGeeks", "", "is", "best",
""]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using filter() to

# perform removal

test_list = list(filter(None, test_list))

 

# Printing modified list 

print ("Modified list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list is : ['', 'GeeksforGeeks', '', 'is', 'best', '']
    Modified list is : ['GeeksforGeeks', 'is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

