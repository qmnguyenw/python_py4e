Python – Elements Product till K value



One of the problem that is basically a subproblem for many complex problems,
finding product number till a certain number in list in python, is commonly
encountered and this particular article discusses possible solutions to this
particular problem.

 **Method #1 : Naive method**  
The most common way this problem can be solved is using a loop and just
multiplying the occurrences of elements that are till given number K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Elements Product till K value

# using naive method 

 

# initializing list 

test_list = [1, 7, 5, 6, 3, 8] 

 

# initializing k 

k = 6

 

# printing list 

print ("The list : " + str(test_list)) 

 

# using naive method 

# Elements Product till K value

res = 1

for i in test_list : 

 if i <= k : 

 res *= i 

 

# printing the product

print ("The product till K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The list : [1, 7, 5, 6, 3, 8]
    The product till K : 90
    

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

# Elements Product till K value

# using list comprehension

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list 

test_list = [1, 7, 5, 6, 3, 8] 

 

# initializing k 

k = 6

 

# printing list 

print ("The list : " + str(test_list)) 

 

# using list comprehension 

# Elements Product till K value

res = prod([i for i in test_list if i <= k]) 

 

# printing the intersection 

print ("The product till K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The list : [1, 7, 5, 6, 3, 8]
    The product till K : 90
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

