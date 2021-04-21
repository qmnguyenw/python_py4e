Python – Count % K elements



Checking a number/element by a condition is a common problem one faces and is
done in almost every program. Sometimes we also require to get the totals that
match the particular condition to have a distinguish which to not match for
further utilization. Lets discuss certain ways in which the task of checking
count of numbers divisible to K can be achieved.

 **Method #1 : Usingsum() \+ generator expression**  
This method uses the trick of adding 1 to the sum whenever the generator
expression returns true. By the time list gets exhausted, summation of count
of numbers matching % K is returned.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Count % K elements

# using sum() + generator expression

 

# initializing list

test_list = [3, 5, 1, 6, 7, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using sum() + generator expression

# to get count of elements matching condition 

# Count % K elements

res = sum(1 for i in test_list if i % K != 0)

 

# printing result

print ("The number of % K elements: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 5, 1, 6, 7, 9]
    The number of % K elements: 3
    

**Method #2 : Usingsum() + map()**  
map() does the task almost similar to the generator expression, difference is
just the internal data structure employed by it is different hence more
efficient.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Count % K elements

# using sum()+ map()

 

# initializing list

test_list = [3, 5, 1, 6, 7, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using sum()+ map()

# to get count of elements matching condition 

# Count % K elements

res = sum(map(lambda i: i % K != 0, test_list))

 

# printing result

print ("The number of % K elements: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 5, 1, 6, 7, 9]
    The number of % K elements: 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

