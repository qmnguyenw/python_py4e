Python | Convert heterogenous type String to List



Sometimes, while working with data, we can have a problem in which we need to
convert data in string into a list and string contains elements from different
data types like boolean. This problem can occur in domains in which lot of
data types are used. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Using list comprehension +split() + strip()**  
The combination of above methods can be used to solve this problem. In this,
we perform the split of elements and then strip the stray character to convert
data types and compile the whole logic of list construction using list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String of Heterogenous types to List

# using list comprehension + split() + strip()

 

# initializing string 

test_str = "'gfg', 'is', True, 'best', False"

 

# printing original string 

print("The original string is : " + test_str)

 

# Convert String of Heterogenous types to List

# using list comprehension + split() + strip()

res = [ele.strip() if ele.strip().startswith("'") else ele
== 'True'

 for ele in test_str.split(', ')]

 

# printing result

print("List after conversion from string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 'gfg', 'is', True, 'best', False
    List after conversion from string : ["'gfg'", "'is'", True, "'best'", False]
    

**Method #2 : Usingeval()**  
This inbuilt function auto-detects the data type and performs the conversion.
It is single phrase solution and also provides solution even if integers are
in string and hence recommended for this solution.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String of Heterogenous types to List

# using eval()

 

# initializing string 

test_str = "'gfg', 'is', True, 'best', False, 1, 2"

 

# printing original string 

print("The original string is : " + test_str)

 

# Convert String of Heterogenous types to List

# using eval()

res = list(eval(test_str))

 

# printing result

print("List after conversion from string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 'gfg', 'is', True, 'best', False, 1, 2
    List after conversion from string : ["'gfg'", "'is'", True, "'best'", False, 1, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

