Python | Convert List of String List to String List



Sometimes while working in Python, we can have problems of interconversion of
data. This article talks about conversion of list of List Strings to joined
string list. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingmap() + generator expression + join() + isdigit()**  
This task can be performed using combination of above functions. In this, we
join the numbers using join and construct a string integers. The map() is used
to apply logic to each element in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List of String List to String List

# using map() + generator expression + join() + isdigit()

 

# helper function 

def convert(sub):

 return "".join(ele if ele.isdigit() else "" for ele in sub)

 

# initialize list 

test_list = ["[1, 4]", "[5, 6]", "[7, 10]"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert List of String List to String List

# using map() + generator expression + join() + isdigit()

res = list(map(convert, test_list))

 

# printing result

print("List after performing conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['[1, 4]', '[5, 6]', '[7, 10]']
    List after performing conversion : ['14', '56', '710']
    

**Method #2 : Usingeval() \+ list comprehension**  
The combination of above functionalities can be used to perform this task. In
this, eval() interprets each strings as list and then we can convert that list
to strings using join(). List comprehension is used to iterate through the
list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List of String List to String List

# using eval() + list comprehension

 

# initialize list 

test_list = ["[1, 4]", "[5, 6]", "[7, 10]"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert List of String List to String List

# using eval() + list comprehension

res = [''.join(str(b) for b in eval(a)) for a in
test_list]

 

# printing result

print("List after performing conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['[1, 4]', '[5, 6]', '[7, 10]']
    List after performing conversion : ['14', '56', '710']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

