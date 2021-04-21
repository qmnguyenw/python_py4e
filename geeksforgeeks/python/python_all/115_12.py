Python – Get Nth word in given String



Sometimes, while working with data, we can have a problem in which we need to
get the Nth word of a String. This kind of problem has many application in
school and day-day programming. Let’s discuss certain ways in which this
problem can be solved.

 **Method #1 : Using loop**  
This is one way in which this problem can be solved. In this, we run a loop
and check for spaces. The Nth word is when there is N-1th space. We return
that word.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get Nth word in String

# using loop

 

# initializing string 

test_str = "GFG is for Geeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing N 

N = 3

 

# Get Nth word in String

# using loop

count = 0

res = ""

for ele in test_str:

 if ele == ' ':

 count = count + 1

 if count == N:

 break

 res = ""

 else :

 res = res + ele

 

# printing result

print("The Nth word in String : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GFG is for Geeks
    The Nth word in String : for
    

**Method #2 : Usingsplit()**  
This is a shorthand with the help of which this problem can be solved. In
this, we split the string into a list and then return the Nth occurring
element.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get Nth word in String

# using split()

 

# initializing string 

test_str = "GFG is for Geeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing N 

N = 3

 

# Get Nth word in String

# using split()

res = test_str.split(' ')[N-1]

 

# printing result

print("The Nth word in String : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GFG is for Geeks
    The Nth word in String : for
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

