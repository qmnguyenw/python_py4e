Python | Test if String is Monotonous



Sometimes, while working with Python strings, we can have a problem in which
we have a string and we wish to check if a string is consecutively increasing
or decreasing. This kind of problem has application in both data and day-day
programming. Lets discuss certain ways in which this problem can be solved.

 **Method #1 : Usingmap() + split() \+ list comprehension**  
The combination of above functions can be used to perform this task. In this,
we split the string to list, separated by delim and then for monotonous in
list problem test we employ list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if String is Monotonous

# Using list comprehension + map() + split()

 

# initializing string

test_str = "6, 5, 4, 3, 2, 1"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing delim 

delim = ", "

 

# Test if String is Monotonous

# Using list comprehension + map() + split()

temp = list(map(int, test_str.split(delim)))

direc = temp[-1] > temp[0] or -1

res = temp == list(range(temp[0], temp[-1] +
direc, direc))

 

# printing result 

print("Is string Monotonous ? : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : 6, 5, 4, 3, 2, 1
    Is string Monotonous ? : True
    

**Method #2 : Usingmap() + split() + zip() + len()**  
The combination of above functions can be used to perform this task. In this,
we perform the task of split as above, but the task of performing the
monotonous is done by zip() and len().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if String is Monotonous

# Using map() + split() + zip() + len()

 

# initializing string

test_str = "6, 5, 4, 3, 2, 1"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing delim 

delim = ", "

 

# Test if String is Monotonous

# Using map() + split() + zip() + len()

temp = list(map(int, test_str.split(delim)))

diff = set(i - j for i, j in zip(temp, temp[1:]))

res = len(diff) == 1 and diff.pop() in (1, -1)

 

# printing result 

print("Is string Monotonous ? : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : 6, 5, 4, 3, 2, 1
    Is string Monotonous ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

