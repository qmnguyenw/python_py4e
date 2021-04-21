Python | Reverse Order Sort in String List



Sometimes, while working with Python, we can have a problem in which we need
to perform the reverse sort operation in all the Strings that are present in a
list. This problem can occur in general programming and web development. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension +sorted() + join() + reverse**  
This is one way in which this problem can be solved. In this, we use sorted()
functionality to perform sort operation and join() is used to reconstruct the
string list. The reverse logic is implemented by passing “reverse” as True
parameter to sorted().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Order Sort in String List

# using list comprehension + sorted() + join() + reverse

 

# initialize list 

test_list = ['gfg', 'is', 'good'] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# Reverse Order Sort in String List

# using list comprehension + sorted() + join() + reverse

res = [''.join(sorted(ele, reverse = True)) for ele in
test_list] 

 

# printing result 

print("List after string reverse sorting : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : ['gfg', 'is', 'good']
    List after string reverse sorting : ['ggf', 'si', 'oogd']
    

**Method #2 : Usingmap() + sorted() + reverse + join() \+ lambda**  
The combination of above method can also be used to perform this task. In
this, we perform the functionality of traversal using map() and lambda rather
than list comprehension. The reverse logic is implemented by passing “reverse”
as True parameter to sorted().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Order Sort in String List

# using map() + sorted() + join() + lambda + reverse

 

# initialize list 

test_list = ['gfg', 'is', 'good'] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# Reverse Order Sort in String List? + reverse

# using map() + sorted() + join() + lambda 

res = list(map(lambda ele: "".join(sorted(ele, reverse =
True)), test_list)) 

 

# printing result 

print("List after string reverse sorting : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : ['gfg', 'is', 'good']
    List after string reverse sorting : ['ggf', 'si', 'oogd']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

