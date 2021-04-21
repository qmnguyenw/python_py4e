Python | Strings with similar front and rear character



Sometimes, while programming, we can have a problem in which we need to check
for front and rear character of each string. We may require to extract count
of all strings with similar front and rear characters. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force method by which this task can be performed. In this,
iterate each element of list and check for each string’s front and rear
character and increase the counter in case we find a match.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Similar front and rear elements

# Using loop

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'treat']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Similar front and rear elements

# Using loop

count = 0

for ele in test_list:

 if ele[0] == ele[-1]:

 count = count + 1

 

# printing result

print("Total Strings with similar front and rear elements : " +
str(count))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'treat']
    Total Strings with similar front and rear elements : 2
    

**Method #2 : Usingsum() \+ generator expression**  
This is one liner alternative to perform this task. In this, we perform the
task of iteration using generator expression and summation using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Similar front and rear elements

# Using sum() + generator expression

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'treat']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Similar front and rear elements

# Using sum() + generator expression

res = sum(1 for ele in test_list if ele[0] ==
ele[-1])

 

# printing result

print("Total Strings with similar front and rear elements : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'treat']
    Total Strings with similar front and rear elements : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

