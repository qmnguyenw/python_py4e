Python | Sort list of dates given as strings



Given a list of dates in string format, write a Python program to sort the
list of dates in ascending order.

 **Examples:**

>  **Input :** dates = [“24 Jul 2017”, “25 Jul 2017”, “11 Jun 1996”, “01 Jan
> 2019”, “12 Aug 2005”, “01 Jan 1997”]
>
>  **Output :** 01 Jan 2007  
> 10 Jul 2016  
> 2 Dec 2017  
> 11 Jun 2018  
> 23 Jun 2018  
> 01 Jan 2019

  
**Approach:**  
In Python, we can use sort() (for in-place sorting) and sorted() (returns
a new sorted list) functions for sorting lists. But by default, these in-built
sorting functions will sort the list of strings in alphabetical order which
would result in a wrong order in our case. Hence, we need to pass a key
argument to tell the sorting function that we need to compare the list items
in a particular way and sort them accordingly.

  

  

In Python, we have the datetime module which makes date based comparison
easier. The datetime.strptime() function is used to convert a given string
into datetime object. It accepts two arguments: _date_ (string) and _format_
(used to specify the format. for eg: %Y is used for specifying year) and
returns a datetime object.

 **Syntax:**

    
    
    datetime.strptime(date, format)

The formatting that we require for this problem is as follows:

    
    
    **%d** ---> for Day
    **%b** ---> for Month
    **%Y** ---> for Year
    

Hence, we need to pass the datetime object as the key argument in the
sorting function to tell the sorting function that it needs to compare the
strings by converting them into dates and sort them in the increasing order.

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to sort the list of dates

# given in string format

 

# Import the datetime module

from datetime import datetime

 

# Function to print the data stored in the list 

def printDates(dates): 

 

 for i in range(len(dates)): 

 print(dates[i]) 

 

 

if __name__ == "__main__": 

 

 dates = ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018", 

 "01 Jan 2019", "10 Jul 2016", "01 Jan 2007"] 

 

 # Sort the list in ascending order of dates 

 dates.sort(key = lambda date: datetime.strptime(date, '%d %b
%Y'))

 

 # Print the dates in a sorted order 

 printDates(dates)   
  
---  
  
__

__

**Output:**

    
    
    01 Jan 2007
    10 Jul 2016
    2 Dec 2017
    11 Jun 2018
    23 Jun 2018
    01 Jan 2019
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

