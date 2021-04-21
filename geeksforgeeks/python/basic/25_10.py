Reverse string in Python (5 different ways)



Python string library does’nt support the in-built “ **reverse()** ” as done
by other python containers like list, hence knowing other methods to reverse
string can prove to be useful. This article discusses several ways to achieve
it.  

 **Using loop**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to reverse a string

# using loop

 

def reverse(s):

 str = ""

 for i in s:

 str = i + str

 return str

 

s = "Geeksforgeeks"

 

print ("The original string is : ",end="")

print (s)

 

print ("The reversed string(using loops) is : ",end="")

print (reverse(s))  
  
---  
  
 __

 __

Output:

    
    
    The original string  is : Geeksforgeeks
    The reversed string(using loops) is : skeegrofskeeG
    

**Explanation :** In above code, we call a function to reverse a string, which
iterates to every element and intelligently **join each character in the
beginning** so as to obtain the reversed string.  

 **Using recursion**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to reverse a string

# using recursion

 

def reverse(s):

 if len(s) == 0:

 return s

 else:

 return reverse(s[1:]) + s[0]

 

s = "Geeksforgeeks"

 

print ("The original string is : ",end="")

print (s)

 

print ("The reversed string(using recursion) is : ",end="")

print (reverse(s))  
  
---  
  
 __

 __

Output:

    
    
    The original string  is : Geeksforgeeks
    The reversed string(using recursion) is : skeegrofskeeG
    

**Explanation :** In the above code, string is passed as an argument to a
recursive function to reverse the string. In the function, the base condition
is that if the length of the string is equal to 0, the string is returned. If
not equal to 0, the reverse function is recursively called to slice the part
of the string except the first character and concatenate the first character
to the end of the sliced string.  

  

  

 **Using stack**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to reverse a string

# using stack

 

# Function to create an empty stack. It 

# initializes size of stack as 0

def createStack():

 stack=[]

 return stack

 

# Function to determine the size of the stack

def size(stack):

 return len(stack)

 

# Stack is empty if the size is 0

def isEmpty(stack):

 if size(stack) == 0:

 return true

 

# Function to add an item to stack . It

# increases size by 1 

def push(stack,item):

 stack.append(item)

 

# Function to remove an item from stack. 

# It decreases size by 1

def pop(stack):

 if isEmpty(stack): return

 return stack.pop()

 

# A stack based function to reverse a string

def reverse(string):

 n = len(string)

 

 # Create a empty stack

 stack = createStack()

 

 # Push all characters of string to stack

 for i in range(0,n,1):

 push(stack,string[i])

 

 # Making the string empty since all

 # characters are saved in stack 

 string=""

 

 # Pop all characters of string and put

 # them back to string

 for i in range(0,n,1):

 string+=pop(stack)

 

 return string

 

# Driver code

s = "Geeksforgeeks"

print ("The original string is : ",end="")

print (s)

print ("The reversed string(using stack) is : ",end="")

print (reverse(s))  
  
---  
  
 __

 __

Output:

    
    
    The original string  is : Geeksforgeeks
    The reversed string(using stack) is : skeegrofskeeG
    

**Explanation :** An empty stack is created. One by one characters of string
are pushed to stack.  
One by one all characters from stack are popped, and put them back to string.  

 **Using extended slice syntax**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to reverse a string

# using extended slice syntax

 

# Function to reverse a string

def reverse(string):

 string = string[::-1]

 return string

 

s = "Geeksforgeeks"

 

print ("The original string is : ",end="")

print (s)

 

print ("The reversed string(using extended slice syntax) is :
",end="")

print (reverse(s))  
  
---  
  
 __

 __

Output:

    
    
    The original string  is : Geeksforgeeks
    The reversed string(using extended slice syntax) is : skeegrofskeeG
    

**Explanation :** Extended slice offers to put a “step” field as
**[start,stop,step]** , and giving no field as start and stop indicates
default to 0 and string length respectively and “ **-1** ” denotes starting
from end and stop at the start, hence reversing string.  

 **Using reversed**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to reverse a string

# using reversed()

 

# Function to reverse a string

def reverse(string):

 string = "".join(reversed(string))

 return string

 

s = "Geeksforgeeks"

 

print ("The original string is : ",end="")

print (s)

 

print ("The reversed string(using reversed) is : ",end="")

print (reverse(s))  
  
---  
  
 __

 __

Output:

    
    
    The original string  is : Geeksforgeeks
    The reversed string(using reversed) is : skeegrofskeeG
    

**Explanation :** The reversed() returns the reversed iterator of the given
string and then its elements are joined empty string separated using join().
And reversed order string is formed.  

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

