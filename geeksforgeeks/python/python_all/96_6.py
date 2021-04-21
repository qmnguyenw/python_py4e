Intermediate Coding Problems in Python



Python, being a very dynamic and versatile programming language, is used in
almost every field. From software development to machine learning, it covers
them all. This article will focus on some interesting coding problems which
can be used to sharpen our skills a bit more and at the same time, have fun
solving these list of specially curated problems. Although this article will
focus on solving these problems using Python, one can feel free to use any
other language of their choice. So let’s head right into it!

#### Infinite Monkey Theorem

The theorem states that a monkey hitting keys at random on a typewriter
keyboard for an infinite amount of time will almost surely type a given text,
such as the complete works of William Shakespeare. Well, suppose we replace a
monkey with a Python function. How long would it take for a Python function to
generate just one sentence? The sentence we will go for is: “a computer
science portal for geeks”.  
The way we will simulate this is to write a function that generates a string
that is 35 characters long by choosing random letters from the 26 letters in
the alphabet plus space. We will write another function that will score each
generated string by comparing the randomly generated string to the goal. A
third function will repeatedly call generate and score, then if 100% of the
letters are correct we are done. If the letters are not correct then we will
generate a whole new string. To make it easier to follow, our program should
keep track of the best string generated so far.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import random

 

 

# function to generate 

# a random string 

def generateOne(strlen): 

 

 # string with all the alphabets

 # and a space

 alphabet = "abcdefghijklmnopqrstuvwxyz "

 res =""

 

 for i in range(strlen):

 res+= alphabet[random.randrange(27)]

 

 return res

 

# function to determine the 

# score of the generated string

def score(goal, testString): 

 numSame = 0

 

 for i in range(len(goal)):

 if goal[i] == testString[i]:

 numSame+= 1

 

 return numSame / len(goal)

 

# main function to call the previous

# two functions until the goal is achieved

def main(): 

 goalString = "a computer science portal for geeks"

 newString = generateOne(35)

 best = 0

 newScore = score(goalString, newString)

 

 while newScore<1:

 if newScore>best:

 print(newString)

 best = newScore

 newString = generateOne(35)

 newScore = score(goalString, newString)

 

# Driver code

main()  
  
---  
  
 __

 __

 **Output:**

    
    
    pxwvkdfwpbzneycy rifcrnczxqtsfowgjm
    wfgytnakffjty ggfy trylljfhurazyxow
    docujzolvswarzqszridmejyluhwviujlkj
     qbtvqanrbwsximmnlhjgkaacufhskiooxm
    w jnlhvvinzrlimtesllsroqqqf wwteela
    mjcevludro yoigewqudxjsad bxrl qnlv
    f pomksbzrjizegcjwyoqftjz wwx   ges

Here, we wrote three functions. One will generate a random string using the 26
characters of the alphabet and space. The second function will then score the
generated string by comparing each letter of it with the goalString. The
third function will repeatedly call the first two functions until the task is
completed. It will also take note of the best string generated so far by
comparing their scores. The one with the highest score will be the best one.
Finally, we run this program in our IDE and see it work.

  

  

#### The substring dilemma

This is a really interesting program as it generates some really funny
outputs. It is also a healthy practice problem for beginners who want to
understand the “string” type more clearly. Let’s look into the problem.

Given a string, find a substring based on the following conditions:

  * The substring must be the longest one of all the possible substring in the given string.
  * There must not be any repeating characters in the substring.
  * If there is more than one substring satisfying the above two conditions, then print the substring which occurs first.
  * If there is no substring satisfying all the aforementioned conditions then print -1.

Although there can be many methods of approach to this problem, we will look
at the most basic one.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

def test_1(string =""):

 

 # initializing the substring

 substring = "" 

 testList = []

 initial = 0

 

 for char in string:

 

 for i in range(initial, len(string)):

 substring+= string[i]

 

 # checking conditions

 if substring.count(string[i])>1:

 testList.append(substring[:-1])

 initial+= 1

 substring = ""

 break

 maxi =""

 

 for word in testList:

 

 if len(word)>len(maxi):

 maxi = word

 

 if len(maxi)<3:

 return "-1"

 else:

 return maxi

 

# Driver code

print(test_1("character"))

print(test_1("standfan"))

print(test_1("cass"))  
  
---  
  
 __

 __

Here, we write a single function that will carry out the entire task. First it
will initialize variables calledsubstring and testList to store the
substring and a list of possible outputs respectively. Then it will loop over
the entire string provided and break every time it finds a repetition and
appends that word to testList. Finally, the longest word out of the possible
outputs is returned.

 **Output:**

    
    
    racte
    standf
    cas

#### Mastermind

A low-level implementation of the classic game “Mastermind”. We need to write
a program that generates a four-digit random code and the user needs to guess
the code in 10 tries or less. If any digit out of the guessed four-digit code
is wrong, the computer should print out “B”. If the digit is correct but at
the wrong place, the computer should print “Y”. If both the digit and position
is correct, the computer should print “R”. Example:

![mastermind-python](https://media.geeksforgeeks.org/wp-
content/uploads/20200213172401/mastermind-python.jpg)

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import random

 

 

# generates a four-digit code

def gen_code(): 

 set_code = []

 

 for i in range(4):

 val = random.randint(0, 9)

 set_code.append(val)

 

 return set_code

 

# asks for input from the user

def input_code(): 

 code = input("Enter your four digit guess code: ")

 return code

 

 

# plays the game

def mastermind(): 

 

 genCode = gen_code()

 i = 0

 

 while i < 10:

 result = ""

 inputCode = [int(c) for c in input_code()]

 

 if len(inputCode) != 4:

 print("Enter only 4 digit number")

 continue

 

 if inputCode == genCode:

 print("You guessed it !", genCode)

 break

 

 for element in inputCode:

 

 if element in genCode:

 

 if inputCode.index(element) == genCode.index(element):

 result+="R"

 else:

 result+="Y"

 else:

 result+="B"

 print(result)

 

 i += 1

 else: 

 print("You ran out of trys !", genCode) 

 

 

# Driver Code

mastermind()  
  
---  
  
 __

 __

First, we write a function to generate a random four digit code using
Python’srandom module. Next, we define a function that asks for user input.
Finally, we write a function that compares the generated code to the guessed
code and gives appropriate results.

#### Direction Catastrophe

A very simple problem with many different solutions, but the main aim is to
solve it in the most efficient way. A man was given directions to go from
point A to point B. The directions were: “SOUTH”, “NORTH”, “WEST”, “EAST”.
Clearly “NORTH” and “SOUTH” are opposite, “WEST” and “EAST” too. Going to one
direction and coming back in the opposite direction is a waste of time and
energy. So, we need to help the man by writing a program that will eliminate
the useless steps and will contain only the necessary directions.  
For example: The directions [“NORTH”, “SOUTH”, “SOUTH”, “EAST”, “WEST”,
“NORTH”, “WEST”] should be reduced to [“WEST”]. This is because going “NORTH”
and then immediately “SOUTH” means coming back to the same place. So we cancel
them and we have [“SOUTH”, “EAST”, “WEST”, “NORTH”, “WEST”]. Next, we go
“SOUTH”, take “EAST” and then immediately take “WEST”, which again means
coming back to the same point. Hence we cancel “EAST” and “WEST” to giving us
[“SOUTH”, “NORTH”, “WEST”]. It’s clear that “SOUTH” and “NORTH” are opposites
hence canceled and finally we are left with [“WEST”].

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

opposite= {'NORTH': 'SOUTH', 

 'EAST': 'WEST', 

 'SOUTH': 'NORTH', 

 'WEST': 'EAST'}

 

 

# Function to find the reduced

# direction

def dirReduc(givenDirections):

 finalDirections = []

 

 for d in range(0, len(givenDirections)):

 

 if finalDirections:

 

 if finalDirections[-1] == opposite[givenDirections[d]]:

 finalDirections.pop()

 else:

 finalDirections.append(givenDirections[d])

 

 else:

 finalDirections.append(givenDirections[d])

 

 return finalDirections

 

# Driver Code

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST",
"WEST", "NORTH", "WEST"]))  
  
---  
  
 __

 __

In the above solution, we create a dictionary of opposites to help us
determine if a given direction is opposite of the other. Next we initialize a
variable calledfinalDirections which will be our output. If the direction
which is in the givenDirections is opposite of the last element in
finalDirections, we pop it out of finalDirections otherwise we append it
to finalDirections.

 **Output:**

    
    
    ['WEST']

#### Comparing arrays

This problem helps one to understand the key concepts of an array(list) in
Python. Two arrays are said to be the same if they contain the same elements
and in the same order. However, in this problem, we will compare two arrays to
see if they are same, but with a slight twist. Here, two arrays are the same
if the elements of one array are squares of elements of other arrays and
regardless of the order. Consider two arrays **a** and **b**.

> a = [121, 144, 19, 161, 19, 144, 19, 11]  
> b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

Here **b** can be written as:

> b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

which is a square of every element of **a**. Hence, they are same. If **a** or
**b** are None, our program should written False

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# function to compare the arrays

def comp(array1, array2):

 

 # checking if any array is None

 if array1 is None or array2 is None: 

 return False

 

 # checking if any of the array 

 # is a square of the other

 if (sorted(array1) == sorted([i ** 2 for i in
array2])) or (sorted(array2) == sorted([i ** 2 for
i in array1])): 

 return True

 

 return False

 

# Driver Code

comp([1,2,3,4], [1,4,9,16])  
  
---  
  
 __

 __

 **Output:**

    
    
    True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

