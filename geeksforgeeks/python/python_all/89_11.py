Python – Test if Substring occurs in specific position



Sometimes, while working with python strings, we can have a problem in which
we need to test occurrence of substring. There is straight forward way to test
this. But sometimes, we have a more specific problem in which we need to test
if substring occurs at that particular position. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Using loop**  
This is brute method to solve this problem. In this we iterate the string and
when index occur we test for substring characters simultaneously.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if Substring occurs in specific position

# Using loop

 

# initializing string 

test_str = "Gfg is best"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing range 

i, j = 7, 11

 

# initializing substr

substr = "best"

 

# Test if Substring occurs in specific position

# Using loop

res = True

k = 0

for idx in range(len(test_str)):

 if idx >= i and idx < j:

 if test_str[idx] != substr[k]:

 res = False

 break

 k = k + 1

 

# printing result 

print("Does string contain substring at required position ? : " +
str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Gfg is best
    Does string contain substring at required position ? : True
    

**Method #2 : Using string slicing**  
This is one-liner way to perform this task. In this, we check the substring in
string using string slicing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if Substring occurs in specific position

# Using string slicing 

 

# initializing string 

test_str = "Gfg is best"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing range 

i, j = 7, 11

 

# initializing substr

substr = "best"

 

# Test if Substring occurs in specific position

# Using string slicing

res = test_str[i : j] == substr

 

# printing result 

print("Does string contain substring at required position ? : " +
str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Gfg is best
    Does string contain substring at required position ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

