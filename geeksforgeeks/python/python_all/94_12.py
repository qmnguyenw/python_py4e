Python | Values Frequency till Maximum K



One of the problem that is basically a subproblem for many complex problem,
finding numbers smaller than certain number in list in python, is commonly
encountered and this particular article discusses possible solutions to this
particular problem.

 **Method 1 : Naive method**  
The most common way this problem can be solved is using loop and just counting
the occurrences of elements that are smaller than the given number K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Values Frequency till Maximum K

# using naive method 

 

# initializing list

test_list = [1, 7, 5, 6, 3, 8]

 

# initializing k

k = 4

 

# printing list 

print ("The list : " + str(test_list))

 

# using naive method 

# to get numbers < k

count = 0

for i in test_list :

 if i < k :

 count = count + 1

 

# printing the result

print ("The numbers smaller than 4 : " + str(count))  
  
---  
  
 __

 __

 **Output :**

    
    
    The list : [1, 7, 5, 6, 3, 8]
    The numbers smaller than 4 : 2
    

**Method 2 : Usingsum()**  
The sum() can also help us achieving this task. We can return 1 when the
number smaller than k is found and then compute the summation of is using
sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Values Frequency till Maximum K

# using sum()

 

# initializing list

test_list = [1, 7, 5, 6, 3, 8]

 

# initializing k

k = 4

 

# printing list 

print ("The list : " + str(test_list))

 

# using sum()

# to get numbers < k

count = sum(i < k for i in test_list)

 

# printing the result

print ("The numbers smaller than 4 : " + str(count))  
  
---  
  
 __

 __

 **Output :**

    
    
    The list : [1, 7, 5, 6, 3, 8]
    The numbers smaller than 4 : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

