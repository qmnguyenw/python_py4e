Python: Map VS For Loop



 **Map in Python :**

  * Map is used to compute a function for different values _‘in a single line of code ‘_.
  * It takes two arguments, first is function name, that is defined already and the other is list, tuple or any other iterables .
  * It is a way of applying same function for multiple numbers .
  * It generates a map object at a particular location .
  * It works fast when we call an already defined function on the elements
  *      map(functionname, iterable)

 **Note:** For more information refer to Python map() function.

 **for loop in Python :**

  * We use for loop to repeat a block of code for fixed number of times .
  * Used when no results are required .
  * To perform sequential traversal .
  * Loop from 0 to n runs n+1 times .
  *      for var in iterable :
                   statements 

**Note:** Here, var is the name given to iterating variable, iterable can be
replaced by range() function and they can be of any data type . Statements are
the step of actions to be performed .

 **Note:** For more information, refer to Python For Loops.

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# function to square a given number

def squareNum (a) :

 return a * a

 

 

listt = [0, -1, 3, 4.5, 99, .08]

 

# using 'map' to call the function

# 'squareNum' for all the elements

# of 'listt'

x = map(squareNum, listt)

 

# map function returns a map

# object at this particular 

# location

print(x) 

 

# convert map to list

print(list(x)) 

 

 

# alternate way to square all

# elements of 'listt' using

# 'for loop'

 

for i in listt :

 square = i * i

 print(square)  
  
---  
  
 __

 __

 **Output:**

    
    
    <map object at 0x7fe413cf9b00>
    [0, 1, 9, 20.25, 9801, 0.0064]
    0
    1
    9
    20.25
    9801
    0.0064
    

#### Map vs for loop

  1. Comparing performance , map() wins! map() works way faster than for loop. Considering the same code above when run in this ide.

 **Using map():**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200119150011/gfg-map-
output.jpg)

 **using for loop:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200119150412/gfg-for-
loop-output.jpg)

  2. for loop can be with no content, no such concept exist in map() function.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# we use the keyword 'pass'

# to simply get a for loop 

# with no content

for i in range (10) :

 pass  
  
---  
  
 __

 __

  3. There can be anelse condition in for loop which only runs when no break statement is used. There is nothing like this in map.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

# for loop with else condition

 

for i in range(10) :

 print(i)

else : 

 print("Finished !")  
  
---  
  
 __

 __

 **Output :**

    
    
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    Finished !
    

  4. for loop can exit before too. We can do that using break statement. Exiting before expected is not possible in map.
  5. map generates a map object, for loop does not return anything.
  6. syntax of map and for loop are completely different.
  7. for loop is for executing the same block of code for a fixed number of times, the map also does that but in a single line of code.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

