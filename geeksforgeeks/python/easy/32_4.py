Calendar Functions in Python | Set 2(monthrange(), prcal(), weekday()…)



  
Some of calendar functions are discussed in the Set 1

 **1\. monthrange(year, month)** :- This function returns **two integers,
first, the starting day number of week(0 as monday) , second, the number of
days in the month**.

 **2\. prcal(year, w, l, c)** :- This function also **prints the calendar of
specific year** but there is no need of “print” operation to execute this.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# monthrange() and prcal()

 

# importing calendar module for calendar operations

import calendar

 

# using monthrange() to print start week day and 

# number of month

print ("The start week number and no. of days of month : ",end="")

print (calendar.monthrange(2008, 2))

 

# using prcal() to print calendar of 1997

print ("The calendar of 1997 is : ")

calendar.prcal(1997, 2,1,6)  
  
---  
  
 __

 __

Output:

    
    
    The start week number and no. of days of month : (4, 29)
    The calendar of 1997 is : 
                                      1997
    
          January                   February                   March
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
           1  2  3  4  5                      1  2                      1  2
     6  7  8  9 10 11 12       3  4  5  6  7  8  9       3  4  5  6  7  8  9
    13 14 15 16 17 18 19      10 11 12 13 14 15 16      10 11 12 13 14 15 16
    20 21 22 23 24 25 26      17 18 19 20 21 22 23      17 18 19 20 21 22 23
    27 28 29 30 31            24 25 26 27 28            24 25 26 27 28 29 30
                                                        31
    
           April                      May                       June
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6                1  2  3  4                         1
     7  8  9 10 11 12 13       5  6  7  8  9 10 11       2  3  4  5  6  7  8
    14 15 16 17 18 19 20      12 13 14 15 16 17 18       9 10 11 12 13 14 15
    21 22 23 24 25 26 27      19 20 21 22 23 24 25      16 17 18 19 20 21 22
    28 29 30                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                        30
    
            July                     August                  September
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6                   1  2  3       1  2  3  4  5  6  7
     7  8  9 10 11 12 13       4  5  6  7  8  9 10       8  9 10 11 12 13 14
    14 15 16 17 18 19 20      11 12 13 14 15 16 17      15 16 17 18 19 20 21
    21 22 23 24 25 26 27      18 19 20 21 22 23 24      22 23 24 25 26 27 28
    28 29 30 31               25 26 27 28 29 30 31      29 30
    
          October                   November                  December
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
           1  2  3  4  5                      1  2       1  2  3  4  5  6  7
     6  7  8  9 10 11 12       3  4  5  6  7  8  9       8  9 10 11 12 13 14
    13 14 15 16 17 18 19      10 11 12 13 14 15 16      15 16 17 18 19 20 21
    20 21 22 23 24 25 26      17 18 19 20 21 22 23      22 23 24 25 26 27 28
    27 28 29 30 31            24 25 26 27 28 29 30      29 30 31
    

**3\. prmonth(year, month, w, l)** :- This function also **prints the month of
specific year** but there is no need of “print” operation to execute this.

  

  

 **4\. setfirstweekday(num)** :- This function sets the **day start number**
of week.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# prmonth() and setfirstweekday()

 

# importing calendar module for calendar operations

import calendar

 

# using prmonth() to print calendar of 1997

print ("The 4th month of 1997 is : ")

calendar.prmonth(1997, 4, 2, 1)

 

 

# using setfirstweekday() to set first week day number

calendar.setfirstweekday(4)

 

print ("\r")

 

# using firstweekday() to check the changed day

print ("The new week day number is : ",end="")

print (calendar.firstweekday())  
  
---  
  
 __

 __

Output:

    
    
    The 4th month of 1997 is : 
         April 1997
    Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6
     7  8  9 10 11 12 13
    14 15 16 17 18 19 20
    21 22 23 24 25 26 27
    28 29 30
     
    The new week day number is : 4
    

**5\. weekday(year, month, date)** :- This function returns the **week day
number** (0 is Monday) of the date specified in its arguments.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# weekday()

 

# importing calendar module for calendar operations

import calendar

 

# using weekday() to print day number of date

print ("The day number of 25 April 1997 is : ",end="")

print (calendar.weekday(1997,4,25))  
  
---  
  
 __

 __

Output:

    
    
    The day number of 25 April 1997 is : 4
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

