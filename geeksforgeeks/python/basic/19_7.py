Python | Count the Number of matching characters in a pair of string



  
Given a pair of non empty strings. Count the number of matching characters in
those strings (consider the single count for the character which have
duplicates in the strings).

 **Examples:**

    
    
    **Input :** str1 = 'abcdef'
            str2 = 'defghia'
    **Output :** 4 
    (i.e. matching characters :- a, d, e, f)
    
    **Input :** str1 = 'aabcddekll12@'
            str2 = 'bb22ll@55k'
    **Output :** 5 
    (i.e. matching characters :- b, 1, 2, @, k)
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach 1:**  
1\. Initialize a counter variable with 0.  
2\. Iterate over the first string from the starting character to ending
character.  
3\. If the character extracted from first string is found in the second string
and also first occurrence index of that extracted character in first string is
same as that of index of current extracted character then increment the value
of counter by 1.

>  **Note:** For this, use **string.find(character)** in python.
>
> This returns the first occurrence index of character in string, if found,
> otherwise return -1.
>
>  
>
>
>  
>
>
> For example : str=’abcdedde’  
> str.find(‘d’) –> 3  
> str.find(‘e’) –> 4  
> str.find(‘g’) –> -1

 **4.** Output the value of counter.

Below is the implementation of above approach.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to count number of matching

# characters in a pair of strings

 

# count function

def count(str1, str2): 

 c, j = 0, 0

 

 # loop executes till length of str1 and 

 # stores value of str1 character by character 

 # and stores in i at each iteration.

 for i in str1: 

 

 # this will check if character extracted from

 # str1 is present in str2 or not(str2.find(i)

 # return -1 if not found otherwise return the 

 # starting occurrence index of that character

 # in str2) and j == str1.find(i) is used to 

 # avoid the counting of the duplicate characters

 # present in str1 found in str2

 if str2.find(i)>= 0 and j == str1.find(i): 

 c += 1

 j += 1

 print ('No. of matching characters are : ', c)

 

# Main function

def main(): 

 str1 ='aabcddekll12@' # first string

 str2 ='bb2211@55k' # second string

 count(str1, str2) # calling count function 

 

# Driver Code

if __name__=="__main__":

 main()  
  
---  
  
 __

 __

 **Output :**

    
    
    No. of matching characters are : 5
    

**Approach 2:**  
1.In this approach set() is used to remove duplicate on a given string.  
2.After that concept of set(intersection) is used on given string.  
3.After that we find a length using len() method.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to count number of unique matching

# characters in a pair of strings

 

# count function count the common unique

# characters present in both strings .

def count(str1 ,str2) :

 # set of characters of string1

 set_string1 = set(str1)

 

 # set of characters of string2

 set_string2 = set(str2)

 

 # using (&) intersection mathematical operation on sets

 # the unique characters present in both the strings

 # are stored in matched_characters set variable

 matched_characters = set_string1 & set_string2

 

 # printing the length of matched_characters set

 # gives the no. of matched characters

 print("No. of matching characters are : " +
str(len(matched_characters)) )

 

 

# Driver code

if __name__ == "__main__" :

 

 str1 = 'aabcddekll12@' # first string

 str2 = 'bb2211@55k' # second string

 

 # call count function 

 count( str1 , str2 )

   
  
---  
  
__

__

  
**Output :**

    
    
    No. of matching characters are : 5
    

**Approach 3:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Count the Number of matching characters in

# a pair of string

import re

ip1 = "geeks"

ip2 = "geeksonly"

 

c = 0

for i in ip1:

 if re.search(i,ip2):

 c=c+1

print("No. of matching characters are ", c)  
  
---  
  
 __

 __

]  

  
 **Output :**

    
    
    No. of matching characters are : 5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

