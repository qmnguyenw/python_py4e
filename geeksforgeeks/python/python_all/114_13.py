Python program to find birthdate on the same day you were born



Write a program to find birthdates till a given year on the same day you were
born. Let the input be of the format: YYYY-MM-DD

 **Examples:**

>  **Input:** 1996-11-12  
>  **Output:** [‘1996-11-12’, ‘2002-11-12’, ‘2013-11-12’, ‘2019-11-12’,
> ‘2024-11-12’, ‘2030-11-12’, ‘2041-11-12’, ‘2047-11-12’]
>
>  **Input:** 1992-11-2  
>  **Output:** [‘1992-11-2’, ‘1998-11-2’, ‘2009-11-2’, ‘2015-11-2’,
> ‘2020-11-2’, ‘2026-11-2’, ‘2037-11-2’, ‘2043-11-2’, ‘2048-11-2’]

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Functions created:**

  

  

  *  **split_date(birthdate):** This function splits the date given by user into year, month and day.
  *  **get_birthday(birthdate):** This function is used to return the day of the week the user was born.
  *  **true_birthdays(birthdate):** This function is used to return a list of dates having the same week day the user was born.

To find the birthdates having the same day the user was born above three
methods will help us. Firstly, The user will enter the date and split_date()
function will split the date into year, month and day. Then the function
get_birthday() will be used to find weekday for that particular date.
Finally, the true_birthdays() function will be used to find the list of all
the dates having the same weekday. Inside this function, a for loop will be
iterating from birth year to a specific year and will check if the birthdate
in any particular year having the same weekday or not. If the weekday is same
then that date will be added to the list of dates.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

import datetime

import calendar

 

weekdays = ["Monday", "Tuesday", "Wednesday", 

 "Thursday", "Friday", "Saturday", "Sunday"]

 

 

# get_birth day

def split_date(birthday):

 

 # Split it to year, month and day

 year, month, day = birthday.split('-') 

 return year, month, day

 

 

def get_birthday(birthday):

 

 year, month, day = split_date(birthday)

 

 # Get a date object for the day of birth

 bdate = datetime.datetime(int(year), int(month),
int(day))

 

 # Get the integer weekday for the day of birth

 weekday = bdate.weekday()

 

 # Tell the user

 day = weekdays[weekday]

 

 return day 

 

 

def listToString(x):

 

 # initialize an empty string 

 String = " "

 

 # return string 

 return (String.join(x))

 

 

def true_birthdays(birthdate):

 year, month, day = split_date(birthdate)

 

 # get the year from birthday

 year = birthdate[:4].split('-')

 

 # convert list to string 

 year = listToString(year)

 

 # get the weekday you are born

 d_day = get_birthday(birthdate) 

 

 # list of true birthdate[birthday that have same 

 # weekday as the day you were born] 

 true_BD = [] 

 

 j = 0

 

 for i in range(int(year), 2050):

 

 # add + j to birth year 

 new_year = int(year)+j 

 

 # construct new birthday

 new_birthday =
str(str(new_year)+"-"+month+"-"+day) 

 

 # get weekday of the new birthday

 new_d_day = get_birthday(new_birthday)

 

 # if birthday that have same weekday 

 # as the day you were born

 if d_day == new_d_day: 

 

 # add to the list of true birthdate

 true_BD.append(new_birthday)

 else:

 pass

 j += 1

 

 return true_BD

 

 

def main():

 

 # Get the birth date

 birthdate = "1996-11-12"

 

 # year_limit = input("search limit from your birthday- ")

 dates = true_birthdays(birthdate) 

 

 print(dates)

 

 

# Driver's code

main()  
  
---  
  
 __

 __

 **Output:**

> [‘1996-11-12’, ‘2002-11-12’, ‘2013-11-12’, ‘2019-11-12’, ‘2024-11-12’,
> ‘2030-11-12’, ‘2041-11-12’, ‘2047-11-12’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

