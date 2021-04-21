Python: Passing Dictionary as Arguments to Function



A dictionary in Python is a collection of data which is unordered and mutable.
Unlike, numeric indices used by lists, a dictionary uses the key as an index
for a specific value. It can be used to store unrelated data types but data
that is related as a real-world entity. The keys themselves are employed for
using a specific value.

>  **Refer to the below article to get the idea about Python Dictionary.**
>
>   * Python Dictionary
>

#### Passing Dictionary as an argument

In Python, everything is an object, so the dictionary can be passed as an
argument to a function like other variables are passed.

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# passing dictionary as argument

 

 

# A function that takes dictionary

# as an argument

def func(d):

 

 for key in d:

 print("key:", key, "Value:", d[key])

 

# Driver's code

D = {'a':1, 'b':2, 'c':3}

func(D)  
  
---  
  
 __

 __

 **Output:**

    
    
    key: b Value: 2
    key: a Value: 1
    key: c Value: 3
    

**Passing Dictionary as kwargs**

“kwargs” stands for keyword arguments. It is used for passing advanced data
objects like dictionaries to a function because in such functions one doesn’t
have a clue about the number of arguments, hence data passed is be dealt
properly by adding “**” to the passing type.

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# passing dictionary as kwargs

 

 

def display(**name):

 

 print (name["fname"]+" "+name["mname"]+"
"+name["lname"])

 

def main():

 

 # passing dictionary key-value 

 # pair as arguments

 display(fname ="John",

 mname ="F.", 

 lname ="Kennedy")

# Driver's code

main()  
  
---  
  
 __

 __

 **Output:**

    
    
    John F. Kennedy
    

**Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# passing dictionary as kwargs

 

 

def display(x = 0, y = 0, **name):

 

 print (name["fname"]+" "+name["mname"]+"
"+name["lname"])

 print ("x =", x)

 print ("y =", y)

 

def main():

 # passing dictionary key-value 

 # pair with other arguments

 display(2, fname ="John", mname ="F.", lname
="Kennedy")

 

# Driver's code

main()  
  
---  
  
 __

 __

 **Output:**

    
    
    John F. Kennedy
    x = 2
    y = 0
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

