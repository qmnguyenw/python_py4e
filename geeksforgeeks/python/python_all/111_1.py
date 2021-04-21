Python – Sum elements matching condition



Checking a number/element by a condition is a common problem one faces and is
done in almost every program. Sometimes we also require to get the totals sum
that match the particular condition to have a distinguish which to not match
for further utilization. Lets discuss certain ways in which this task can be
achieved.

 **Method #1 : Using loop**  
This is brute force method to perform this particular task. In this, we
iterate list, find elements that match a particular condition and take sum.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Sum elements matching condition

# using loop

 

# initializing list

test_list = [3, 5, 1, 6, 7, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using loop

# Sum elements matching condition

# checks for odd

res = 0

for ele in test_list:

 if ele % 2 != 0:

 res = res + ele 

 

# printing result

print ("The sum of odd elements: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 5, 1, 6, 7, 9]
    The sum of odd elements: 25
    

**Method #2 : Usingsum() + generator expression**  
This method uses the trick of adding elelement to the sum whenever the
generator expression returns true. By the time list gets exhausted, summation
of numbers matching a condition is returned.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Sum elements matching condition

# using sum() + generator expression

 

# initializing list

test_list = [3, 5, 1, 6, 7, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using sum() + generator expression

# Sum elements matching condition

# checks for odd

res = sum(i for i in test_list if i % 2 != 0)

 

# printing result

print ("The sum of odd elements: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 5, 1, 6, 7, 9]
    The sum of odd elements: 25
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

