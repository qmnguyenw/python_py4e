Python program to print Calendar without calendar or datetime module



Given the month and year. The task is to show the calendar of that month and
in the given year without using any module or pre-defined functions.

 **Examples:**

    
    
    **Input :** 
    mm(1-12) :9
    yy :2010
    
    **Output :**    
    September 2010
    Su Mo Tu We Th Fr Sa
             01 02 03 04 
    05 06 07 08 09 10 11 
    12 13 14 15 16 17 18 
    19 20 21 22 23 24 25 
    26 27 28 29 30 
    

**Approach:**

In the program below, we first calculate the number of odd days to find the
day of the date 01-mm-yyyy.Then, we take in the year(yy) and the month(mm) as
input and displays the calendar for that month of the year.

Below is the implementation of the given approach.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to print Calendar

# Without use of Calendar module

 

mm = 2

yy = 2020

 

month ={1:'January', 2:'February', 3:'March', 

 4:'April', 5:'May', 6:'June', 7:'July',

 8:'August', 9:'September', 10:'October',

 11:'November', 12:'December'}

 

# code below for calculation of odd days

day =(yy-1)% 400

day = (day//100)*5 + ((day % 100) - (day %
100)//4) + ((day % 100)//4)*2

day = day % 7

 

nly =[31, 28, 31, 30, 31, 30, 

 31, 31, 30, 31, 30, 31]

ly =[31, 29, 31, 30, 31, 30, 

 31, 31, 30, 31, 30, 31]

s = 0

 

if yy % 4 == 0:

 for i in range(mm-1):

 s+= ly[i]

else:

 for i in range(mm-1):

 s+= nly[i]

 

day += s % 7

day = day % 7

 

# variable used for white space filling 

# where date not present

space =''

space = space.rjust(2, ' ')

 

# code below is to print the calendar

print(month[mm], yy)

print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr',
'Sa')

 

if mm == 9 or mm == 4 or mm == 6 or mm
== 11: 

 for i in range(31 + day):

 

 if i<= day:

 print(space, end =' ')

 else:

 print("{:02d}".format(i-day), end =' ')

 if (i + 1)% 7 == 0:

 print()

elif mm == 2:

 if yy % 4 == 0:

 p = 30

 else:

 p = 29

 

 for i in range(p + day):

 if i<= day:

 print(space, end =' ')

 else:

 print("{:02d}".format(i-day), end =' ')

 if (i + 1)% 7 == 0:

 print() 

else:

 for i in range(32 + day):

 

 if i<= day:

 print(space, end =' ')

 else:

 print("{:02d}".format(i-day), end =' ')

 if (i + 1)% 7 == 0:

 print()  
  
---  
  
 __

 __

 **Output:**

    
    
    February 2020
    Su Mo Tu We Th Fr Sa
                      01 
    02 03 04 05 06 07 08 
    09 10 11 12 13 14 15 
    16 17 18 19 20 21 22 
    23 24 25 26 27 28 29
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

