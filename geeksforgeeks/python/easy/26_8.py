Calendar in Python



Python has a built-in function, calendar to work with date related tasks. You
will learn to display the calendar of a given date in this example.

Examples:

    
    
    Input 1 : 
    yy = 2017
    mm = 11
    
    Output :    November 2017
    Mo Tu We Th Fr Sa Su
           1  2  3  4  5
     6  7  8  9 10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30
    
    Input 2 :
    yy = 2017
    
    Output:
    
                                      2017
    
          January                   February                   March
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                       1             1  2  3  4  5             1  2  3  4  5
     2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
     9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
    16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
    23 24 25 26 27 28 29      27 28                     27 28 29 30 31
    30 31
    
           April                      May                       June
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                    1  2       1  2  3  4  5  6  7                1  2  3  4
     3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
    10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
    17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
    24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30
    
            July                     August                  September
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                    1  2          1  2  3  4  5  6                   1  2  3
     3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
    10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
    17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
    24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
    31
    
          October                   November                  December
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                       1             1  2  3  4  5                   1  2  3
     2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
     9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
    16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
    23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
    30 31
    
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Implementation 1 : **Displaying Month**  

In the program below, we import the calendar module. The built-in function
month() inside the module takes in the year and the month and displays the
calendar for that month of the year.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to display calendar of

# given month of the year

 

# import module

import calendar

 

yy = 2017

mm = 11

 

# display the calendar

print(calendar.month(yy, mm))  
  
---  
  
 __

 __

Output:

    
    
    
        November 2017
    Mo Tu We Th Fr Sa Su
           1  2  3  4  5
     6  7  8  9 10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30
    

**OR** you can directly run

    
    
    python -m calendar [YEAR] [MONTH]

from command line (CMD in windows or TERMINAL in Linux ) for displaying a
month of a year

for example :

    
    
    C:\Users\chatu\Desktop>python -m calendar 2019 7
         July 2019
    Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29 30 31
    

Implementation 2 : **Displaying Year**  

In the program below, we import the calendar module. The built-in function
calender() inside the module takes in the year and displays the calendar for
that year.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to display calendar of

# given year

 

# import module

import calendar

 

yy = 2017

 

# display the calendar

print(calendar.calendar(yy))  
  
---  
  
 __

 __

Output:

    
    
                                      2017
    
          January                   February                   March
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                       1             1  2  3  4  5             1  2  3  4  5
     2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
     9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
    16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
    23 24 25 26 27 28 29      27 28                     27 28 29 30 31
    30 31
    
           April                      May                       June
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                    1  2       1  2  3  4  5  6  7                1  2  3  4
     3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
    10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
    17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
    24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30
    
            July                     August                  September
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                    1  2          1  2  3  4  5  6                   1  2  3
     3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
    10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
    17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
    24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
    31
    
          October                   November                  December
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                       1             1  2  3  4  5                   1  2  3
     2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
     9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
    16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
    23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
    30 31
    

**OR** you can directly run

    
    
    python -m calendar [YEAR] 

from command line (CMD in windows or TERMINAL in Linux ) for displaying a year

This article is contributed by **ajay0007**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
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

