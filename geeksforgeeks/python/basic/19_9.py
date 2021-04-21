Find frequency of each word in a string in Python



Write a python code to find the frequency of each word in a given string.

Examples:

    
    
    Input :  str[] = "Apple Mango Orange Mango Guava Guava Mango" 
    Output : frequency of Apple is : 1
             frequency of Mango is : 3
             frequency of Orange is : 1
             frequency of Guava is : 2
    
    Input :  str = "Train Bus Bus Train Taxi Aeroplane Taxi Bus"
    Output : frequency of Train is : 2
             frequency of Bus is : 3
             frequency of Taxi is : 2
             frequency of Aeroplane is : 1
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach 1 using list():**  
 **1.** Split the string into a list containing the words by using split
function (i.e. string.split()) in python with delimiter space.

    
    
    **Note:**
    **string_name.split(separator)** method is used to split the string 
    by specified separator(delimiter) into the list.
    If delimiter is not provided then white space is a separator. 
    
    **For example:**
    CODE   : str='This is my book'
             str.split()
    OUTPUT : ['This', 'is', 'my', 'book']
    

**2.** Initialize a new empty list.  
 **3.** Now append the word to the new list from previous string if that word
is not present in the new list.  
 **4.** Iterate over the new list and use count function (i.e.
string.count(newstring[iteration])) to find the frequency of word at each
iteration.

    
    
    **Note:**
    **string_name.count(substring)** is used to find no. of occurrence of 
    substring in a given string.
    
    **For example:**
    CODE   : str='Apple Mango Apple'
             str.count('Apple')
             str2='Apple'
             str.count(str2)
    OUTPUT : 2
             2
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find frequency of each word

def freq(str):

 

 # break the string into list of words 

 str = str.split() 

 str2 = []

 

 # loop till string values present in list str

 for i in str: 

 

 # checking for the duplicacy

 if i not in str2:

 

 # insert value in str2

 str2.append(i) 

 

 for i in range(0, len(str2)):

 

 # count the frequency of each word(present 

 # in str2) in str and print

 print('Frequency of', str2[i], 'is :', str.count(str2[i])) 

 

def main():

 str ='apple mango apple orange orange apple guava mango mango'

 freq(str) 

 

if __name__=="__main__":

 main() # call main function  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Frequency of  apple  is :  3
    Frequency of  mango  is :  3
    Frequency of  orange  is :  2
    Frequency of  guava  is :  1
    

**Approach 2 using set():**  
 **1.** Split the string into a list containing the words by using split
function (i.e. string.split()) in python with delimiter space.  
 **2.** Use **set()** method to remove a duplicate and to give a set of unique
words  
 **3.** Iterate over the set and use count function (i.e.
string.count(newstring[iteration])) to find the frequency of word at each
iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to find frequency of each word

# function for calculating the frequency

def freq(str):

 

 # break the string into list of words

 str_list = str.split()

 

 # gives set of unique words

 unique_words = set(str_list)

 

 for words in unique_words :

 print('Frequency of ', words , 'is :', str_list.count(words))

 

# driver code

if __name__ == "__main__":

 

 str ='apple mango apple orange orange apple guava mango mango'

 

 # calling the freq function

 freq(str)  
  
---  
  
 __

 __

 **Output:**

    
    
    Frequency of  apple  is :  3
    Frequency of  mango  is :  3
    Frequency of  orange  is :  2
    Frequency of  guava  is :  1
    

**  
Approach 3 (Using Dictionary)**

 __

 __  
 __

 __

 __  
 __  
 __

# Find frequency of each word in a string in Python

# using dictionary.

 

def count(elements):

 # check if each word has '.' at its last. If so then ignore '.'

 if elements[-1] == '.':

 elements = elements[0:len(elements) - 1]

 

 # if there exists a key as "elements" then simply

 # increase its value.

 if elements in dictionary:

 dictionary[elements] += 1

 

 # if the dictionary does not have the key as "elements" 

 # then create a key "elements" and assign its value to 1.

 else:

 dictionary.update({elements: 1})

 

 

# driver input to check the program.

 

Sentence = "Apple Mango Orange Mango Guava Guava Mango"

 

# Declare a dictionary

dictionary = {}

 

# split all the word of the string.

lst = Sentence.split()

 

# take each word from lst and pass it to the method count.

for elements in lst:

 count(elements)

 

# print the keys and its corresponding values.

for allKeys in dictionary:

 print ("Frequency of ", allKeys, end = " ")

 print (":", end = " ")

 print (dictionary[allKeys], end = " ")

 print() 

 

# This code is contributed by Ronit Shrivastava.  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

