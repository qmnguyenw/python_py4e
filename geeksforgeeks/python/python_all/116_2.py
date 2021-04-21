Python | Average String length in list



Sometimes, while working with data, we can have a problem in which we need to
gather information of average length of String data in list. This kind of
information might be useful in Data Science domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using list comprehension +sum() + len()**  
The combination of above functions can be used to perform this task. In this
we compute lengths of all Strings using list comprehension and then divide the
sum by length of list using len() and sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Average String lengths in list

# using list comprehension + sum() + len()

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Average String lengths in list

# using list comprehension + sum() + len()

temp = [len(ele) for ele in test_list]

res = 0 if len(temp) == 0 else (float(sum(temp))
/ len(temp)) 

 

# printing result

print("The Average length of String in list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    The Average length of String in list is : 3.4
    

**Method #2 : Usingmap() + sum() + len()**  
The combination of above functions can also be used to perform this task. In
this, we compute lengths using map(). Rest all the logic is similar to above
method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Average String lengths in list

# using map() + sum() + len()

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Average String lengths in list

# using map() + sum() + len()

res = sum(map(len, test_list))/float(len(test_list))

 

# printing result

print("The Average length of String in list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    The Average length of String in list is : 3.4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

