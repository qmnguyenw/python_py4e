Python | Filter a list based on the given list of strings



Given a List, the task is to filter elements from list based on another list
of strings. These type of problems are quite common while scraping websites.

 **Examples:**

    
    
    **Input:**
    List_string1 = ['key', 'keys', 'keyword', 'keychain', 'keynote']
    List_string2 = ['home/key/1.pdf',
             'home/keys/2.pdf', 
             'home/keyword/3.pdf', 
             'home/keychain/4.pdf',
             'home/Desktop/5.pdf', 
             'home/keynote/6.pdf']
    **Output:**
    ['home/Desktop/5.pdf']
    
    **Explanation:** We filter only those element from 
    list_string2 that do not have string in list_string1
    

Below are some ways to achieve the above task.

 **Method #1: Using Iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to filter element from list

# based on another list of string.

 

# List Initialization

Input = ['key', 'keys', 'keyword', 'keychain',
'keynote']

Input_string = ['home/key/1.pdf',

 'home/keys/2.pdf', 

 'home/keyword/3.pdf', 

 'home/keychain/4.pdf',

 'home/Desktop/5.pdf', 

 'home/keynote/6.pdf']

 

Output = Input_string.copy()

temp = []

 

# Using iteration

for elem in Input_string:

 for n in Input:

 if n in elem:

 temp.append(elem)

 

for elem in temp:

 if elem in Output:

 Output.remove(elem)

 

# Printing

print("List of keywords are:", Input)

print("Given list:", Input_string)

print("filtered list is :", Output)  
  
---  
  
 __

 __

 **Output:**

  

  

> List of keywords are: [‘key’, ‘keys’, ‘keyword’, ‘keychain’, ‘keynote’]  
> Given list: [‘home/key/1.pdf’, ‘home/keys/2.pdf’, ‘home/keyword/3.pdf’,
> ‘home/keychain/4.pdf’, ‘home/Desktop/5.pdf’, ‘home/keynote/6.pdf’]  
> filtered list is : [‘home/Desktop/5.pdf’]

