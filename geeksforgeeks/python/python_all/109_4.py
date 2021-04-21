Python | Count unmatched elements



Checking a number/element by a condition is a common problem one faces and is
done in almost every program. Sometimes we also require to get the totals
number that does not match the particular condition to have a distinguish
which match for further utilization. Lets discuss certain ways in which this
task can be achieved.

 **Method #1 : Using loop**  
This is brute force method to perform this particular task. In this, we
iterate list, find elements that does not match a particular condition and
take count.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Count unmatched elements

# using loop

 

# initializing list

test_list = [3, 5, 1, 6, 7, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using loop

# Count unmatched elements

# checks for odd

res = 0

for ele in test_list:

 if not ele % 2 != 0:

 res = res + 1

 

# printing result

print ("The number of non-odd elements: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 5, 1, 6, 7, 9]
    The number of non-odd elements: 1
    

**Method #2 : Using len() \+ generator expression**  
This method uses the trick of counting elelement to the add 1 whenever the
generator expression returns False. By the time list gets exhausted, count of
numbers not matching a condition is returned.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Count unmatched elements

# using len() + generator expression

 

# initializing list

test_list = [3, 5, 1, 6, 7, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using len() + generator expression

# Count unmatched elements

# checks for odd

res = len(list(i for i in test_list if not i % 2
!= 0))

 

# printing result

print ("The number of non-odd elements: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 5, 1, 6, 7, 9]
    The number of non-odd elements: 1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

