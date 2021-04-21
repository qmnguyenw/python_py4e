Python | Convert numeric String to integers in mixed List



Sometimes, while working with data, we can have a problem in which we receieve
mixed data and need to convert the integer elements in form of strings to
integers. This kind of operation might be required in data preprocessing step.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +isdigit()**  
This is one way in which this task can be performed. In this, we check for
each element of string whether it is a number using isdigit and then converted
to int if it is one. The iteration is using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String numbers to integers in mixed List

# using list comprehension + isdigit()

 

# initialize list 

test_list = ["gfg", "1", "is", "6", "best"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert String numbers to integers in mixed List

# using list comprehension + isdigit()

res = [int(ele) if ele.isdigit() else ele for ele in
test_list]

 

# printing result

print("List after converting string numbers to integers : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', '1', 'is', '6', 'best']
    List after converting string numbers to integers : ['gfg', 1, 'is', 6, 'best']
    

**Method #2 : Usingmap() + lambda + isdigit()**  
This task can also be performed using above functions. In this, we perform the
task of iteration using map() and lambda function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String numbers to integers in mixed List

# using map() + lambda + isdigit()

 

# initialize list 

test_list = ["gfg", "1", "is", "6", "best"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert String numbers to integers in mixed List

# using map() + lambda + isdigit()

res = list(map(lambda ele : int(ele) if ele.isdigit() 

 else ele, test_list))

 

# printing result

print("List after converting string numbers to integers : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', '1', 'is', '6', 'best']
    List after converting string numbers to integers : ['gfg', 1, 'is', 6, 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

