Python Program to Return the Length of the Longest Word from the List of Words



The problem is to go through all the words in an array and the program should
return the word with the longest one. Consider for example we are having an
array, and we have numbers in alphabetic form, now when we pass this array as
an input then we should get the word with the longest one. Below I had
explained it with an example in order to give an elaborate view.  
**Example:**

>  **Input :** [“one”, “two”, “three”, “four”]  
>  **Output:** three
>
>  **Explanation:**  
>  As we pass the above array as a input, our program will check which word or
> which value has the maximum length and after completly iterating through the
> array then it returns the word with longest length.

 **Methods 1#:** Iterating and finding the greater length word.

 **Approach:**

  

  

  1. First declare a function with the name ‘longest Length ‘ which accepts a list as an argument.
  2. Now, take a list where you have all the values.
  3. We are going to take this list, and we will iterate through each item using for loop.
  4. Then we take two variables max1 and temp to store the maximum length and the word with the longest length.
  5. After completing the above steps then we take the first value in the list and the first value length in order to compare.
  6. Once the above steps are completed we compare the items in the list using for loop. Below I had mentioned the logic.
  7. After completing the above steps run the program, and then we’ll get the required result. 

**Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function to find the longest

# length in the list

def longestLength(a):

 max1 = len(a[0])

 temp = a[0]

 

 # for loop to traverse the list

 for i in a:

 if(len(i) > max1):

 

 max1 = len(i)

 temp = i

 

 print("The word with the longest length is:", temp,

 " and length is ", max1)

 

 

# Driver Program

a = ["one", "two", "third", "four"]

longestLength(a)  
  
---  
  
 __

 __

 **Output:**

    
    
    The word with the longest length is: third  and length is  5
    

**Methods 2#:** Using sort().

 **Approach:**

  1. First declare a function with the name ‘longest Length ‘ which accepts a list as an argument.
  2. Now, take a list where you have all the values.
  3. We are going to take this list, and we will iterate through each item using for loop.
  4. Then we take an empty list with the name final List and will append all the items.
  5. After appending we will sort the list using the sort() method.
  6. Now, as the list is sorted we can get the longest length, and we can display it.
  7. After completing the above steps run the program, and then we’ll get the required result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function to find the longest length in the list

def longestLength(words):

 finalList = []

 

 for word in words:

 finalList.append((len(word), word))

 

 finalList.sort()

 

 print("The word with the longest length is:",
finalList[-1][1],

 " and length is ", len(finalList[-1][1]))

 

 

# Driver Program

a = ["one", "two", "third", "four"]

longestLength(a)  
  
---  
  
 __

 __

 **Output:**

    
    
    The word with the longest length is: third  and length is  5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

