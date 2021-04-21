Movie tickets Booking management system in Python



In this article, we are going to code a simple program for book movie tickets.
It will be very useful to the passionate beginners who wanted to work on any
project.

Write a program to build a simple Movie tickets Booking Management System
using Python.

We had used six functions as follows :

  * t_movie()
  * theater()
  * timing(a)
  * movie(theater)
  * center()
  * city()

 **Approach:** Below is the approach to do the above operations:

 **1\. t_movie:** This method is used to select the movie name.

  

  

    
    
    #this t_movie function is used to select movie name 
    def t_movie():
        global f
        f = f+1
        print("which movie do you want to watch?")
        print("1,movie 1 ")
        print("2,movie 2 ")
        print("3,movie 3")
        print("4,back")
        movie = int(input("choose your movie: "))
        if movie == 4:
          # in this it goes to center function and
          # from center it goes to movie function 
          # and it comes back here and then go to theater 
          center()
          theater()
          return 0
        if f == 1:
          theater()
    

**2\. theater():** This method is used to select the screen.

    
    
    # this theater function used to select screen 
    def theater():
        print("which screen do you want to watch movie: ")
        print("1,SCREEN 1")
        print("2,SCREEN 2")
        print("3,SCREEN 3")
        a = int(input("chosse your screen: "))
        ticket = int(input("number of ticket do you want?: "))
        timing(a)
    

**3\. timing(a):** This method is used to select timing for movies.

    
    
    # this timing function used to select timing for movie 
    def timing(a):
        time1 = {
            "1": "10.00-1.00",
            "2": "1.10-4.10",
            "3": "4.20-7.20",
            "4": "7.30-10.30"
        }
        time2 = {
            "1": "10.15-1.15",
            "2": "1.25-4.25",
            "3": "4.35-7.35",
            "4": "7.45-10.45"
        }
        time3 = {
            "1": "10.30-1.30",
            "2": "1.40-4.40",
            "3": "4.50-7.50",
            "4": "8.00-10.45"
        }
        if a == 1:
            print("choose your time:")
            print(time1)
            t = input("select your time:")
            x = time1[t]
            print("successfull!, enjoy movie at "+x)
        elif a == 2:
            print("choose your time:")
            print(time2)
            t = input("select your time:")
            x = time2[t]
            print("successfull!, enjoy movie at "+x)
        elif a == 3:
            print("choose your time:")
            print(time3)
            t = input("select your time:")
            x = time3[t]
            print("successfull!, enjoy movie at "+x)
        return 0
    

**4\. movie(theater):** This method is used to select movies accordingly to
the theater.

    
    
    def movie(theater):
        if theater == 1:
            t_movie()
        elif theater == 2:
            t_movie()
        elif theater == 3:
            t_movie()
        elif theater == 4:
            city()
        else:
            print("wrong choice")
    

**5\. center():** This method is used to select the theater.

    
    
    def center():
        print("which theater do you wish to see movie? ")
        print("1,Inox")
        print("2,Icon")
        print("3,pvp")
        print("4,back")
        a = int(input("choose your option: "))
        movie(a)
        return 0
    

**6\. city():** This method is used to select the city.

    
    
    # this function is used to select city 
    def city():
        print("hi welcome to movie ticket booking: ")
        print("where you want to watch movie?:")
        print("1,city 1")
        print("2,city 2 ")
        print("3,city 3 ")
        place = int(input("choose your option: "))
        if place == 1:
          center()
        elif place == 2:
          center()
        elif place == 3:
          center()
        else:
          print("wrong choice")
    

**Full implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

global f

f = 0

 

#this t_movie function is used to select movie name 

def t_movie():

 global f

 f = f+1

 print("which movie do you want to watch?")

 print("1,movie 1 ")

 print("2,movie 2 ")

 print("3,movie 3")

 print("4,back")

 movie = int(input("choose your movie: "))

 if movie == 4:

 # in this it goes to center function and from center it goes to movie
function and it comes back here and then go to theater 

 center()

 theater()

 return 0

 if f == 1:

 theater()

 

# this theater function used to select screen 

def theater():

 print("which screen do you want to watch movie: ")

 print("1,SCREEN 1")

 print("2,SCREEN 2")

 print("3,SCREEN 3")

 a = int(input("chosse your screen: "))

 ticket = int(input("number of ticket do you want?: "))

 timing(a)

 

# this timing function used to select timing for movie 

def timing(a):

 time1 = {

 "1": "10.00-1.00",

 "2": "1.10-4.10",

 "3": "4.20-7.20",

 "4": "7.30-10.30"

 }

 time2 = {

 "1": "10.15-1.15",

 "2": "1.25-4.25",

 "3": "4.35-7.35",

 "4": "7.45-10.45"

 }

 time3 = {

 "1": "10.30-1.30",

 "2": "1.40-4.40",

 "3": "4.50-7.50",

 "4": "8.00-10.45"

 }

 if a == 1:

 print("choose your time:")

 print(time1)

 t = input("select your time:")

 x = time1[t]

 print("successfull!, enjoy movie at "+x)

 elif a == 2:

 print("choose your time:")

 print(time2)

 t = input("select your time:")

 x = time2[t]

 print("successfull!, enjoy movie at "+x)

 elif a == 3:

 print("choose your time:")

 print(time3)

 t = input("select your time:")

 x = time3[t]

 print("successfull!, enjoy movie at "+x)

 return 0

 

 

def movie(theater):

 if theater == 1:

 t_movie()

 elif theater == 2:

 t_movie()

 elif theater == 3:

 t_movie()

 elif theater == 4:

 city()

 else:

 print("wrong choice")

 

 

def center():

 print("which theater do you wish to see movie? ")

 print("1,Inox")

 print("2,Icon")

 print("3,pvp")

 print("4,back")

 a = int(input("choose your option: "))

 movie(a)

 return 0

 

# this function is used to select city 

def city():

 print("Hi welcome to movie ticket booking: ")

 print("where you want to watch movie?:")

 print("1,city 1")

 print("2,city 2 ")

 print("3,city 3 ")

 place = int(input("choose your option: "))

 if place == 1:

 center()

 elif place == 2:

 center()

 elif place == 3:

 center()

 else:

 print("wrong choice")

 

 

city() # it calls the function city   
  
---  
  
__

__

**Output:**

> Hi welcome to movie ticket booking:  
> where you want to watch movie?:  
> 1,city 1  
> 2,city 2  
> 3,city 3  
> choose your option: 2  
> which theater do you wish to see movie?  
> 1,Inox  
> 2,Icon  
> 3,pvp  
> 4,back  
> choose your option: 1  
> which movie do you want to watch?  
> 1,movie 1  
> 2,movie 2  
> 3,movie 3  
> 4,back  
> choose your movie: 3  
> which screen do you want to watch movie:  
> 1,SCREEN 1  
> 2,SCREEN 2  
> 3,SCREEN 3  
> chosse your screen: 1  
> number of ticket do you want?: 4  
> choose your time:  
> {‘1’: ‘10.00-1.00’, ‘2’: ‘1.10-4.10’, ‘3’: ‘4.20-7.20’, ‘4’: ‘7.30-10.30’}  
> select your time:2  
> successfull!, enjoy movie at 1.10-4.10

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

