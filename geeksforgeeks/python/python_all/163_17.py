Python | Ways to create triplets from given list



Given a list of words, write a Python program to create triplets from the
given list.

 **Examples :**

>  **Input:** [‘Geeks’, ‘for’, ‘Geeks’, ‘is’, ‘best’, ‘resource’, ‘for’,
> ‘study’]  
>  **Output:**  
>  [[‘Geeks’, ‘for’, ‘Geeks’], [‘for’, ‘Geeks’, ‘is’],  
> [‘Geeks’, ‘is’, ‘best’], [‘is’, ‘best’, ‘resource’],  
> [‘best’, ‘resource’, ‘for’], [‘resource’, ‘for’, ‘study’]]
>
>  **Input:** [‘I’, ‘am’, ‘Paras’, ‘Jain’, ‘I’, ‘Study’, ‘From’, ‘GFG’]  
>  **Output:**  
>  [[‘I’, ‘am’, ‘Paras’], [‘am’, ‘Paras’, ‘Jain’],  
> [‘Paras’, ‘Jain’, ‘I’], [‘Jain’, ‘I’, ‘Study’],  
> [‘I’, ‘Study’, ‘From’], [‘Study’, ‘From’, ‘GFG’]]

Let’s see some of the methods to do this task.

  

  

 **Method #1:** Using List comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to create triplets from list of words.

 

# List of word initialization

list_of_words = ['I', 'am', 'Paras', 'Jain',

 'I', 'Study', 'DS', 'Algo']

 

# Using list comprehension

List = [list_of_words[i:i + 3] 

 for i in range(len(list_of_words) - 2)]

 

# printing list

print(List)  
  
---  
  
 __

 __

 **Output:**

    
    
    [['I', 'am', 'Paras'], ['am', 'Paras', 'Jain'], 
     ['Paras', 'Jain', 'I'], ['Jain', 'I', 'Study'],
     ['I', 'Study', 'DS'], ['Study', 'DS', 'Algo']]
    

  
**Method #2:** Using Iteration

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to create triplets from list of words.

 

# List of word initialization

list_of_words = ['Geeks', 'for', 'Geeks', 'is',

 'best', 'resource', 'for', 'study']

 

# Output list initialization

out = []

 

# Finding length of list

length = len(list_of_words)

 

# Using iteration

for z in range(0, length-2):

 # Creating a temp list to add 3 words

 temp = []

 temp.append(list_of_words[z])

 temp.append(list_of_words[z + 1])

 temp.append(list_of_words[z + 2])

 out.append(temp)

 

# printing output

print(out)  
  
---  
  
 __

 __

 **Output:**

    
    
    [['Geeks', 'for', 'Geeks'], ['for', 'Geeks', 'is'],
     ['Geeks', 'is', 'best'], ['is', 'best', 'resource'],
     ['best', 'resource', 'for'], ['resource', 'for', 'study']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

