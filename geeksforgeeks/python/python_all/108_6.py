Python – Maximum element till K value



One of the problem that is basically a subproblem for many complex problems,
finding maximum number till a certain number in list in python, is commonly
encountered and this particular article discusses possible solutions to this
particular problem.

 **Method #1 : Naive method**  
The most common way this problem can be solved is using a loop and just max
the occurrences of elements that are till given number K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Maximum element till K value

# using naive method 

 

# initializing list

test_list = [1, 7, 5, 6, 3, 8]

 

# initializing k

k = 4

 

# printing list 

print ("The list : " + str(test_list))

 

# using naive method 

# Maximum element till K value

res = 0

for i in test_list :

 if i <= k :

 res = max(res, i)

 

# printing the intersection 

print ("The maximum number till K : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The list : [1, 7, 5, 6, 3, 8]
    The maximum number till K : 3
    

**Method #2 : Using list comprehension**  
This method achieves this task in a similar way, but in a more concise manner.
List comprehension always lowers the lines of codes in the program even though
runs a similar approach in the background.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Maximum element till K value

# using list comprehension

 

# initializing list

test_list = [1, 7, 5, 6, 3, 8]

 

# initializing k

k = 4

 

# printing list 

print ("The list : " + str(test_list))

 

# using list comprehension

# Maximum element till K value

res = max([i for i in test_list if i <= k])

 

# printing the intersection 

print ("The maximum number till K : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The list : [1, 7, 5, 6, 3, 8]
    The maximum number till K : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

