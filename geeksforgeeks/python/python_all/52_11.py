Python – Convert delimiter seperated Mixed String to valid List



Given a string with elements and delimiters, split elements on delimiter to
extract with elements ( including containers).

>  **Input** : test_str = “6*2*9*[3, 5, 6]*(7, 8)*8*4*10”, delim = “*”  
>  **Output** : [6, 2, 9, [3, 5, 6], (7, 8), 8, 4, 10]  
>  **Explanation** : Containers and elements separated using *.
>
>  **Input** : test_str = “[3, 5, 6]*(7, 8)*8*4*10”, delim = “*”  
>  **Output** : [[3, 5, 6], (7, 8), 8, 4, 10]  
>  **Explanation** : Containers and elements separated using *.

 **Method #1 : Using loop + eval() + split()**

This is one way in which this task can be done. In this the separation is done
using split() and eval() does the important task of performing evaluation of
data types to be containers or simpler elements.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert delimiter seperated Mixed String to valid List

# Using loop + split() + eval()

 

# initializing string

test_str = "6# 2# 9#[3, 5, 6]#(7, 8)# 8# 4# 10"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing delim 

delim = "#"

 

# spliting using split()

temp = test_str.split(delim) 

res = []

 

# using loop + eval() to convert to 

# required result

for ele in temp:

 res.append(eval(ele))

 

# printing result 

print("List after conversion : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 6#2#9#[3, 5, 6]#(7, 8)#8#4#10
    List after conversion : [6, 2, 9, [3, 5, 6], (7, 8), 8, 4, 10]
    

**Method #2 : Using eval() + split() + list comprehension**

This is yet another way in which this task can be performed. In this, we
perform similar task as above method. The only difference being that entire
logic is encapsulated as one liner using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert delimiter seperated Mixed String to valid List

# Using eval() + split() + list comprehension

 

# initializing string

test_str = "6# 2# 9#[3, 5, 6]#(7, 8)# 8# 4# 10"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing delim 

delim = "#"

 

# encapsulating entire result in list comprehension 

res = [eval(ele) for ele in test_str.split(delim)]

 

# printing result 

print("List after conversion : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 6#2#9#[3, 5, 6]#(7, 8)#8#4#10
    List after conversion : [6, 2, 9, [3, 5, 6], (7, 8), 8, 4, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

