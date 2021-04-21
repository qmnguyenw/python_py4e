Python – Create a Dictionary with Key as First Character and Value as Words
Starting with that Character



In this article, we will code a python program to create a dictionary with the
key as the first character and value as words starting with that character.

Dictionary in Python is an unordered collection of data values, used to store
data values like a map, which unlike other Data Types that hold only a single
value as an element, Dictionary holds the key: value pair. Key-value is
provided in the dictionary to make it more optimized.

 **Examples:**

    
    
     **Input:** Hello World
    **Output:** {'H': ['Hello'], 
             'W': ['World']}
    
    **Input:** Welcome to GeeksForGeeks
    **Output:** {'W': ['Welcome'], 
             't': ['to'], 
             'G': ['GeeksForGeeks']}
    
    

### Approach:

  * We will save the string in a variable and declare an empty **dictionary**.
  * Then we will **split** the string into words and form a list of those words.
  * For each word, we will check if the key for that word is present or not.
  * If it is not then we will add that key and word to the dictionary and if it is already present then we will append that word to that key’s sublist.

 **Below is the implementation of the above approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to Create a Dictionary with Key as First

# Character and Value as Words Starting with that Character

 

# Driver Code

 

# Declaring String Data

string_input = '''GeeksforGeeks is a Computer Science portal for geeks.

 It contains well written, well thought and well explained

 computer science and programming articles, quizzes etc.'''

 

# Storing words in the input as a list

words = string_input.split()

 

# Declaring empty dictionary

dictionary = {}

 

for word in words:

 

 # If key is not present in the dictionary then we

 # will add the key and word to the dictionary.

 if (word[0] not in dictionary.keys()):

 

 # Creating a sublist to store words with same

 # key value and adding it to the list.

 dictionary[word[0]] = []

 dictionary[word[0]].append(word)

 

 # If key is present then checking for the word

 else:

 

 # If word is not present in the sublist then

 # adding it to the sublist of the proper key

 # value

 if (word not in dictionary[word[0]]):

 dictionary[word[0]].append(word)

 

# Printing the dictionary

print(dictionary)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    {'G': ['GeeksforGeeks'], 
     'i': ['is'], 
     'a': ['a', 'and', 'articles,'], 
     'C': ['Computer'],
     'S': ['Science'], 
     'p': ['portal', 'programming'], 
     'f': ['for'], 
     'g': ['geeks.'], 
     'I': ['It'], 
     'c': ['contains', 'computer'], 
     'w': ['well', 'written,'], 
     't': ['thought'],
     'e': ['explained', 'etc.'], 
     's': ['science'], 
     'q': ['quizzes']}
    

You can see that in the above program’s output the words starting with **G**
have two keys ‘ **G** ‘ and ‘ **g** ‘ so to remove that issue and make the
code case-insensitive we will make use of the **lower() function** in python.
We will save all keys with the lower case so that whenever we will check for
the key both the words starting with ‘ **G** ‘ and ‘ **g** ‘ both will come
under the same key. Below is the implementation:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to Create a Dictionary with Key as First

# Character and Value as Words Starting with that Character

 

# Driver Code

 

# Declaring String Data

string_input = '''GeeksforGeeks is a Computer Science portal for geeks.

 It contains well written, well thought and well explained

 computer science and programming articles, quizzes etc.'''

 

# Storing words in the input as a list

words = string_input.split()

 

# Declaring empty dictionary

dictionary = {}

 

for word in words:

 

 # If key is not present in the dictionary then we

 # will add the key and word to the dictionary.

 if (word[0].lower() not in dictionary.keys()):

 

 # Creating a sublist to store words with same

 # key value and adding it to the list.

 dictionary[word[0].lower()] = []

 dictionary[word[0].lower()].append(word)

 

 # If key is present then checking for the word

 else:

 

 # If word is not present in the sublist then

 # adding it to the sublist of the proper key

 # value

 if (word not in dictionary[word[0].lower()]):

 dictionary[word[0].lower()].append(word)

 

# Printing the dictionary

print(dictionary)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'g': ['GeeksforGeeks', 'geeks.'],
     'i': ['is', 'It'],
     'a': ['a', 'and', 'articles,'], 
     'c': ['Computer', 'contains', 'computer'], 
     's': ['Science', 'science'], 
     'p': ['portal', 'programming'], 
     'f': ['for'], 
     'w': ['well', 'written,'], 
     't': ['thought'], 
     'e': ['explained', 'etc.'], 
     'q': ['quizzes']}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

