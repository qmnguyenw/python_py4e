Python – Print the last word in a sentence



Given a string, the task is to write a Python program to print the last word
in that string.

 **Examples:**

>  **Input** : sky is blue in color
>
>  **Output** : color
>
>  **Explanation:** color is last word in the sentence.
>
>  
>
>
>  
>
>
>  **Input** : Learn algorithms at geeksforgeeks
>
>  **Output** : geeksforgeeks
>
>  **Explanation:** color is last word in the sentence.

 **Approach #1:** Using For loop \+ String Concatenation

  * Scan the sentence
  * Take an empty string, **newstring.**
  * Traverse the string in reverse order and add character to **newstring** using string concatenation.
  * Break the loop till we get first space character.
  * Reverse **newstring** and return it (it is the last word in the sentence).

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Function which returns last word

def lastWord(string):

 

 # taking empty string

 newstring = ""

 

 # calculating length of string

 length = len(string)

 

 # traversing from last

 for i in range(length-1, 0, -1):

 

 # if space is occured then return

 if(string[i] == " "):

 

 # return reverse of newstring

 return newstring[::-1]

 else:

 newstring = newstring + string[i]

 

 

# Driver code

string = "Learn algorithms at geeksforgeeks"

print(lastWord(string))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeksforgeeks

 **Approach #2:** Using split() method

  * As all the words in a sentence are separated by spaces.
  * We have to split the sentence by spaces using **split()**.
  * We split all the words by spaces and store them in a list.
  * The last element in the list is the answer

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Function which returns last word

def lastWord(string):

 

 # split by space and converting 

 # string to list and

 lis = list(string.split(" "))

 

 # length of list

 length = len(lis)

 

 # returning last element in list

 return lis[length-1]

 

 

# Driver code

string = "Learn algorithms at geeksforgeeks"

print(lastWord(string))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeksforgeeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

