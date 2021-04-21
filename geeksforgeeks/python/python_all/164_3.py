Python | Spilt a sentence into list of words



Given a Sentence, write a Python program to convert the given sentence into
list of words.

 **Examples:**

    
    
    **Input :** ['Hello World']
    **Output :** ['Hello', 'world']
    
    **Input :** ['Geeks For geeks']
    **Output :** ['Geeks', 'for', 'geeks']
    

The simplest approach provided by Python to convert the given list of Sentence
into words with separate indices is to use **split()** method. This method
split a string into a list where each word is a list item. We have alternative
ways to use this function in order to achive the required output.

 **Method #1 :** Splitting the first index element

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert single

# indexed list into multiple indexed list

 

def convert(lst):

 return (lst[0].split())

 

# Driver code

lst = ["Geeks For geeks"]

print( convert(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Geeks', 'For', 'geeks']
    

  
**Method #2 :** Using for loop  
We can also use a for loop to split the first element. This method is also
beneficial if we have more than one element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert single

# indexed list into multiple indexed list

 

def convert(lst):

 return ([i for item in lst for i in item.split()])

 

# Driver code

lst = ['Geeksforgeeks is a portal for geeks']

print( convert(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Geeksforgeeks', 'is', 'a', 'portal', 'for', 'geeks']
    

  
**Method #3 :** Using join()  
We can split the given list and than join using join() function. We can also
use this when you have a list of string or single string inside a list.

 __

 __  
 __

 __

 __  
 __  
 __



# Python3 program to Convert single

# indexed list into multiple indexed list

 

def convert(lst):

 return ' '.join(lst).split()

 

 

# Driver code

lst = ['Hello Geeks for geeks']

print( convert(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Hello', 'Geeks', 'for', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

