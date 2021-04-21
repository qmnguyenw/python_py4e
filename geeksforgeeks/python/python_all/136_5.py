Python | Count occurrences of each word in given text file (Using dictionary)



Many times it is required to count the occurrence of each word in a text file.
To achieve so, we make use of a dictionary object that stores the word as the
key and its count as the corresponding value. We iterate through each word in
the file and add it to the dictionary with count as 1. If the word is already
present in the dictionary we increment its count by 1.

 **Example #1:**  
First we create a text file of which we want to count the words. Let this file
be **sample.txt** with the following contents:

    
    
    Mango banana apple pear
    Banana grapes strawberry
    Apple pear mango banana
    Kiwi apple mango strawberry
    

**Note:** Make sure the text file is in same directory as the Python file.

 __

 __  
 __

 __

 __  
 __  
 __

# Open the file in read mode

text = open("sample.txt", "r")

 

# Create an empty dictionary

d = dict()

 

# Loop through each line of the file

for line in text:

 # Remove the leading spaces and newline character

 line = line.strip()

 

 # Convert the characters in line to 

 # lowercase to avoid case mismatch

 line = line.lower()

 

 # Split the line into words

 words = line.split(" ")

 

 # Iterate over each word in line

 for word in words:

 # Check if the word is already in dictionary

 if word in d:

 # Increment count of word by 1

 d[word] = d[word] + 1

 else:

 # Add the word to dictionary with count 1

 d[word] = 1

 

# Print the contents of dictionary

for key in list(d.keys()):

 print(key, ":", d[key])  
  
---  
  
 __

 __

 **Output:**

    
    
    mango : 3
    banana : 3
    apple : 3
    pear : 2
    grapes : 1
    strawberry : 2
    kiwi : 1
    

  
**Example #2:**

  

  

Consider a file **sample.txt** that has sentences with punctuation.

    
    
    Mango! banana apple pear.
    Banana, grapes strawberry.
    Apple- pear mango banana.
    Kiwi "apple" mango strawberry.
    

__

__  
__

__

__  
__  
__

import string

 

# Open the file in read mode

text = open("sample.txt", "r")

 

# Create an empty dictionary

d = dict()

 

# Loop through each line of the file

for line in text:

 # Remove the leading spaces and newline character

 line = line.strip()

 

 # Convert the characters in line to 

 # lowercase to avoid case mismatch

 line = line.lower()

 

 # Remove the punctuation marks from the line

 line = line.translate(line.maketrans("", "", string.punctuation))

 

 # Split the line into words

 words = line.split(" ")

 

 # Iterate over each word in line

 for word in words:

 # Check if the word is already in dictionary

 if word in d:

 # Increment count of word by 1

 d[word] = d[word] + 1

 else:

 # Add the word to dictionary with count 1

 d[word] = 1

 

# Print the contents of dictionary

for key in list(d.keys()):

 print(key, ":", d[key])  
  
---  
  
 __

 __

 **Output:**

    
    
    mango : 3
    banana : 3
    apple : 3
    pear : 2
    grapes : 1
    strawberry : 2
    kiwi : 1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

