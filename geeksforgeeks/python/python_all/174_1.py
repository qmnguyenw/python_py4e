Python program to remove Nth occurrence of the given word



Given a list of words in Python, the task is to remove the Nth occurrence of
the given word in that list.

 **Examples:**

    
    
    **Input:** list - ["geeks", "for", "geeks"]
           word = geeks, N = 2
    **Output:** list - ["geeks", "for"]
    
    **Input:** list - ["can", "you",  "can", "a", "can" "?"]
           word = can, N = 1
    **Output:** list - ["you",  "can", "a", "can" "?"]

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

**Approach #1:** By taking another list.

Make a new list, say _newList_. Iterate the elements in the list and check if
the word to be removed matches the element and the occurrence number,
otherwise, append the element to _newList_.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to remove Nth

# occurrence of the given word

 

# Function to remove Ith word

def RemoveIthWord(lst, word, N):

 newList = []

 count = 0

 

 # iterate the elements

 for i in lst:

 if(i == word):

 count = count + 1

 if(count != N):

 newList.append(i)

 else:

 newList.append(i)

 

 lst = newList

 

 if count == 0:

 print("Item not found")

 else:

 print("Updated list is: ", lst) 

 

 return newList

 

# Driver code

list = ["geeks", "for", "geeks"]

word = "geeks"

N = 2

 

RemoveIthWord(list, word, N)  
  
---  
  
 __

 __

 **Output :**

    
    
    Updated list is:  ['geeks', 'for']

  
**Approach #2:** Remove from the list itself.

Instead of making a new list, delete the matching element from the list
itself. Iterate the elements in the list and check if the word to be removed
matches the element and the occurrence number, If yes delete that item and
return true. If True is returned, print List otherwise, print “Item not
Found”.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to remove Nth

# occurrence of the given word

 

# Function to remove Ith word

def RemoveIthWord(list, word, N):

 count = 0

 

 for i in range(0, len(list)):

 if (list[i] == word):

 count = count + 1

 

 if(count == N):

 del(list[i])

 return True

 

 return False

 

# Driver code

list = ['geeks', 'for', 'geeks']

word = 'geeks'

N = 2

 

flag = RemoveIthWord(list, word, N)

 

if (flag == True):

 print("Updated list is: ", list)

else:

 print("Item not Updated")   
  
---  
  
__

__

**Output :**

    
    
    Updated list is:  ['geeks', 'for']

 **Approach #3:** Remove from the list using **pop()**.

Instead of creating a new list and using if/else statement we can pop the
matching element from the list using pop( ). We need to use an additional
counter to keep track of the index.  
Why we need an index ? because pop( ) needs index to pass inside i.e
pop(index).

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to remove Nth

# occurrence of the given word

 

# Function to remove nth word

def omit(list1,word,n1):

 

 # for counting the occurence of word

 count=0

 

 # for counting the index number

 # where we are at present 

 index=0

 

 for i in list1:

 index+=1

 if i==word:

 count+=1

 if count==n1:

 

 # (index-1) because in list

 # indexing start from 0th position

 list1.pop(index-1) 

 return list1

 

# Driver code

list1 = ["he", "is", "ankit", "is",

 "raj", "is","ankit raj"]

 

word="is"

n1=3

 

print("new list is :",omit(list1,word,n1))  
  
---  
  
 __

 __

 **Output :**

    
    
    new list is : ['he', 'is', 'ankit', 'is', 'raj', 'ankit raj']

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

