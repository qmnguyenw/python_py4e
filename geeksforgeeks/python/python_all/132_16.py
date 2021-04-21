Python program to print calendar of given year



Given a valid year as input, write a Python program to print the calendar of
given year. In order to do this, we can simply use calendar module provided in
Python. For more details about calendar module, refer this article.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print calendar for given year

 

# importing calendar library

import calendar

 

def printcalendar(year):

 

 # printing calendar

 print(calendar.calendar(year))

 

# driver program to test above function

year = 2019

printcalendar(year)  
  
---  
  
 __

 __

 **Output :**

    
    
    Calendar of 2019
    
          January                   February                   March
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6                   1  2  3                   1  2  3
     7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
    14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
    21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
    28 29 30 31               25 26 27 28               25 26 27 28 29 30 31
    
           April                      May                       June
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7             1  2  3  4  5                      1  2
     8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
    15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
    22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
    29 30                     27 28 29 30 31            24 25 26 27 28 29 30
    
            July                     August                  September
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7                1  2  3  4                         1
     8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
    15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
    22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
    29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                        30
    
          October                   November                  December
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6                   1  2  3                         1
     7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
    14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
    21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
    28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                        30 31
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

