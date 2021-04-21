Python Program to Sort A List Of Names By Last Name



Given a list of names, the task is to write a Python program to sort the list
of names by their last name.

 **Examples:**

>  **Input:** [‘John Wick’, ‘Jason Voorhees’]
>
>  **Output:** [‘Jason Voorhees’, ‘John Wick’]
>
>  **Explanation:** V in Voorhees of Jason Voorhees is less than W in Wick of
> John Wick.
>
>  
>
>
>  
>
>
> **Input:** [‘Freddy Krueger’, ‘Keyser Söze’,’Mohinder Singh Pandher’]
>
>  **Output:** [‘Freddy Krueger’, ‘Mohinder Singh Pandher’, ‘Keyser Soze’]
>
>  **Explanation:** K< P < S

 **Method #1:** Using _sorted()_ method on a converted 2D List.

Convert the list of names into a 2D list of names, in which the first index
refers to the first names and the last index refers to the last name. Apply
_sorted()_ method with _key_ as the last index of each element in the 2D list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# explicit function sort names

# by their surnames

def sortSur(nameList):

 l2 = []

 

 # create 2d list of names

 for ele in nameList:

 l2.append(ele.split())

 nameList = []

 

 # sort by last name

 for ele in sorted(l2, key=lambda x: x[-1]):

 nameList.append(' '.join(ele))

 

 # return sorted list

 return nameList

 

 

# Driver Code

 

# assign list of names

nameList = ['John Wick', 'Jason Voorhees',

 'Freddy Krueger', 'Keyser Soze',

 'Mohinder Singh Pandher']

 

# display original list

print('\nList of Names:\n', nameList)

print('\nAfter sorting:\n', sortSur(nameList))  
  
---  
  
 __

 __

 **Output:**

> List of Names:  
> [‘John Wick’, ‘Jason Voorhees’, ‘Freddy Krueger’, ‘Keyser Soze’, ‘Mohinder
> Singh Pandher’]
>
> After sorting:  
> [‘Freddy Krueger’, ‘Mohinder Singh Pandher’, ‘Keyser Soze’, ‘Jason
> Voorhees’, ‘John Wick’]
>
>  
>
>
>  
>

 **Method #2:** Using _sort()_ method + _lambda_

Use _sort()_ method on the given list of names with _key_ as _lambda x:
x.split()[-1]) which_ represents the last string in each element of the list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# explicit function sort names

# by their surnames

def sortSur(nameList):

 

 # sort list by last name

 nameList.sort(key=lambda x: x.split()[-1])

 

 # return sorted list

 return nameList

 

 

# Driver Code

 

# assign list of names

nameList = ['John Wick', 'Jason Voorhees',

 'Freddy Krueger', 'Keyser Soze',

 'Mohinder Singh Pandher']

 

# display original list

print('\nList of Names:\n', nameList)

print('\nAfter sorting:\n', sortSur(nameList))  
  
---  
  
 __

 __

 **Output:**

> List of Names:  
> [‘John Wick’, ‘Jason Voorhees’, ‘Freddy Krueger’, ‘Keyser Soze’, ‘Mohinder
> Singh Pandher’]
>
> After sorting:  
> [‘Freddy Krueger’, ‘Mohinder Singh Pandher’, ‘Keyser Soze’, ‘Jason
> Voorhees’, ‘John Wick’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

