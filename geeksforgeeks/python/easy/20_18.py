Python | Sort Python Dictionaries by Key or Value



 **Prerequisite:**

  * Dictionary
  * List
  * Merging Two Dictionaries
  * Dictionary Methods

 **Problem Statement – Here are the major tasks that are needed to be
performed.**

  1. Create a dictionary and display its keys alphabetically.
  2. Display both the keys and values sorted in alphabetical order by the key.
  3. Same as part (ii), but sorted in alphabetical order by the value.

 **Approach –**  
Load the Dictionary and perform the following operations:

  1. First, sort the keys alphabetically using _key_value.iterkeys()_ function.
  2. Second, sort the keys alphabetically using _sorted (key_value)_ function & print the value corresponding to it.
  3. Third, sort the values alphabetically using _key_value.iteritems(), key = lambda (k, v) : (v, k))_

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Let’s try performing the above-mentioned tasks:

  

  

  1. Displaying the Keys Alphabetically:

 **Examples:**

    
    
    Input:
    key_value[2] = '64'       
    key_value[1] = '69'
    key_value[4] = '23'
    key_value[5] = '65'
    key_value[6] = '34'
    key_value[3] = '76'
    
    Output:
    1 2 3 4 5 6 
    

**Program:**

 __

 __  
 __

 __

 __  
 __  
 __

# Function calling

def dictionairy(): 

 # Declare hash function 

 key_value ={} 

 

# Initializing value 

 key_value[2] = 56

 key_value[1] = 2

 key_value[5] = 12

 key_value[4] = 24

 key_value[6] = 18

 key_value[3] = 323

 

 print ("Task 1:-\n")

 print ("Keys are")

 

 # iterkeys() returns an iterator over the 

 # dictionary’s keys.

 for i in sorted (key_value.keys()) : 

 print(i, end = " ")

 

def main():

 # function calling

 dictionairy() 

 

# Main function calling

if __name__=="__main__": 

 main()  
  
---  
  
 __

 __

 **Output:**

    
    
    Task 1:-
    
    Keys are
    1 2 3 4 5 6
    

  2. Sorting the Keys and Values in Alphabetical Order using the Key.

 **Examples:**

    
    
    Input:
    key_value[2] = '64'       
    key_value[1] = '69'
    key_value[4] = '23'
    key_value[5] = '65'
    key_value[6] = '34'
    key_value[3] = '76'
    
    Output:
    (1, 69) (2, 64) (3, 76) (4, 23) (5, 65) (6, 34)
    

**Program:**

 __

 __  
 __

 __

 __  
 __  
 __

# function calling

def dictionairy(): 

 

 # Declaring the hash function 

 key_value ={} 

 

# Initialize value 

 key_value[2] = 56

 key_value[1] = 2

 key_value[5] = 12

 key_value[4] = 24

 key_value[6] = 18

 key_value[3] = 323

 

 print ("Task 2:-\nKeys and Values sorted in", 

 "alphabetical order by the key ") 

 

 # sorted(key_value) returns an iterator over the 

 # Dictionary’s value sorted in keys. 

 for i in sorted (key_value) :

 print ((i, key_value[i]), end =" ")

 

def main():

 # function calling

 dictionairy() 

 

# main function calling

if __name__=="__main__": 

 main()  
  
---  
  
 __

 __

 **Output:**

    
    
    Task 2:-
    Keys and Values sorted in alphabetical order by the key  
    (1, 2) (2, 56) (3, 323) (4, 24) (5, 12) (6, 18)
    

  3. Sorting the Keys and Values in alphabetical using the value

 **Examples:**

    
        Input:
    key_value[2] = '64'       
    key_value[1] = '69'
    key_value[4] = '23'
    key_value[5] = '65'
    key_value[6] = '34'
    key_value[3] = '76'
    
    Output:
    (4, 23), (6, 34), (2, 64), (5, 65), (1, 69), (3, 76)
    

**Program:**

 __

 __  
 __

 __

 __  
 __  
 __

# Function calling

def dictionairy(): 

 

 # Declaring hash function 

 key_value ={} 

 

# Initializing the value 

 key_value[2] = 56

 key_value[1] = 2

 key_value[5] = 12

 key_value[4] = 24

 key_value[6] = 18

 key_value[3] = 323

 

 

 print ("Task 3:-\nKeys and Values sorted", 

 "in alphabetical order by the value")

 

 # Note that it will sort in lexicographical order

 # For mathematical way, change it to float

 print(sorted(key_value.items(), key =

 lambda kv:(kv[1], kv[0]))) 

 

def main():

 # function calling

 dictionairy() 

 

# main function calling

if __name__=="__main__": 

 main()  
  
---  
  
 __

 __

 **Output:**

    
    
    Task 3:-
    Keys and Values sorted in alphabetical order by the value
    [(1, 2), (5, 12), (6, 18), (4, 24), (2, 56), (3, 323)]
    

**Sort the dictionary by key**  
 **Note:** it will sort in lexicogrphical order  
Taking key’s type as string  
 **Program:**

 __

 __  
 __

 __

 __  
 __  
 __

# Creates a sorted dictionary (sorted by key)

from collections import OrderedDict

 

dict =
{'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}

dict1 = OrderedDict(sorted(dict.items()))

print(dict1)  
  
---  
  
 __

 __

Here, Output is Soretd Dictionary using key in Lexicolographical order  
 **Lexicographical order:**
https://en.wikipedia.org/wiki/Lexicographical_order

 **Learning Outcome:**

  * How to handle a dictionary.
  * Dictionary has O(1) search time complexity whereas List has O(n) time complexity. So it is recommended to use the dictionary where ever possible.
  * The best application of dictionary can be seen in _Twitter Sentiment Analysis_ where analysis Twitter sentiments are analysed, using Lexicon approach.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

