Python program to print sorted number formed by merging all elements in array



Given an array arr[], the task is to combine all the elements in the array
sequentially and sort the digits of this number in ascending order.

 **Note:** Ignore leading zeros.

 **Examples:**

>  **Input:** arr =[7, 845, 69, 60]
>
>  **Output:** 4566789
>
>  
>
>
>  
>
>
>  **Explanation:** The number formed by combining all the elements is
> “78456960” after sorting the digits we get 4566789
>
>  **Input:** arr =[8, 5603, 109, 53209]
>
>  **Output:** 1233556899
>
>  **Explanation:** The number formed by combining all the elements is
> “8560310953209” after sorting the digits we get “1233556899”

 **Approach:**

  * Convert each element of the list to a string using map() function.
  * Join the list using join() function.
  * Sort the string using join() and sorted()
  * Convert string to an integer using type casting
  * Return the result

 **Below is the implementation of the above approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# python program to print sorted number by merging

# all the elements in array function to print

# sorted number

 

def getSortedNumber(number):

 

 # sorting the string

 number = ''.join(sorted(number))

 

 # converting string to integer

 number = int(number)

 

 # returning the result

 print(number)

 

# function to merge elements in array

def mergeArray(lis):

 

 # convert the elements of list to string

 lis = list(map(str, lis))

 

 # converting list to string

 string = ''.join(lis)

 

 # passing this string to sortednumber function

 getSortedNumber(string)

 

# Driver code

lis = [7, 845, 69, 60]

 

# passing list to merge array function to merge

# the elements

mergeArray(lis)  
  
---  
  
 __

 __

 **Output:**

    
    
    4566789

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

