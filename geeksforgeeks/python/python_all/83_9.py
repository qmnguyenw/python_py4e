Python | Extract Strings with only Alphabets



Sometimes, while working with Python lists, we can have a problem in which we
need to extract only those strings which contains only alphabets and discard
those which include digits. This has application in day-day programming and
web development domain. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usingisalpha() \+ list comprehension**  
The combination of above functions can be used to perform this task. In this,
we extract the string which are alphabets only using isalpha() and compile
whole logic using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Alphabet only Strings

# Using isalpha() + list comprehension

 

# initializing list

test_list = ['gfg', 'is23', 'best', 'for2', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Extract Alphabet only Strings

# Using isalpha() + list comprehension

res = [sub for sub in test_list if sub.isalpha()]

 

# printing result 

print("Strings after filtering : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', 'is23', 'best', 'for2', 'geeks']
    Strings after filtering : ['gfg', 'best', 'geeks']
    

**Method #2 : Usingfilter() \+ lambda**  
The combination of above methods can be used to perform this task. In this, we
perform filtering using filter() and logic for extension to all strings is
done using lambda.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Alphabet only Strings

# Using filter() + lambda

 

# initializing list

test_list = ['gfg', 'is23', 'best', 'for2', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Extract Alphabet only Strings

# Using filter() + lambda

res = list(filter(lambda sub: sub.isalpha(), test_list))

 

# printing result 

print("Strings after filtering : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', 'is23', 'best', 'for2', 'geeks']
    Strings after filtering : ['gfg', 'best', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

