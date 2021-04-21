Python program to convert a list to string



Given a list, write a Python program to convert the given list to string.

There are various situation we might encounter when a list is given and we
convert it to string. For example, conversion to string from the list of
string or the list of integer.

 **Example:**

    
    
    Input: ['Geeks', 'for', 'Geeks']
    Output: Geeks for Geeks
    
    Input: ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
    Output: I want 4 apples and 18 bananas

Let’s see various ways we can convert the list to string.

 **Method #1:**  
Iterate through the list and keep adding the element for every index in some
empty string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert a list to string

 

# Function to convert 

def listToString(s): 

 

 # initialize an empty string

 str1 = "" 

 

 # traverse in the string 

 for ele in s: 

 str1 += ele 

 

 # return string 

 return str1 

 

 

# Driver code 

s = ['Geeks', 'for', 'Geeks']

print(listToString(s))   
  
---  
  
__

__

**Output:**

    
    
    GeeksforGeeks
    

**Method #2: Using .join() method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert a list

# to string using join() function

 

# Function to convert 

def listToString(s): 

 

 # initialize an empty string

 str1 = " "

 

 # return string 

 return (str1.join(s))

 

 

# Driver code 

s = ['Geeks', 'for', 'Geeks']

print(listToString(s))   
  
---  
  
__

__

**Output:**

    
    
    Geeks for Geeks
    

But what if the list contains both string and integer as its element. In those
cases, above code won’t work. We need to convert it to string while adding to
string.

 **Method #3: Using list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert a list

# to string using list comprehension

 

s = ['I', 'want', 4, 'apples', 'and', 18,
'bananas']

 

# using list comprehension

listToStr = ' '.join([str(elem) for elem in s])

 

print(listToStr)   
  
---  
  
__

__

**Output:**

    
    
    I want 4 apples and 18 bananas
    

**Method #4: Using map()**  
Use map() method for mapping str (for converting elements in list to string)
with given iterator, the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert a list

# to string using list comprehension

 

s = ['I', 'want', 4, 'apples', 'and', 18,
'bananas']

 

# using list comprehension

listToStr = ' '.join(map(str, s))

 

print(listToStr)   
  
---  
  
__

__

**Output:**

    
    
    I want 4 apples and 18 bananas
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

