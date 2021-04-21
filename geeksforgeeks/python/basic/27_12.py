Output of Python Program | Set 1



Predict the output of following python programs:

 **Program 1:**

 __

 __  
 __

 __

 __  
 __  
 __

r= lambda q: q * 2

s = lambda q: q * 3

x = 2

x = r(x)

x = s(x)

x = r(x)

print (x)  
  
---  
  
 __

 __

 **Output:**

    
    
    24
    

**Explanation :** In the above program r and s are lambda functions or
anonymous functions and q is the argument to both of the functions. In first
step we have initialized x to 2. In second step we have passed x as argument
to the lambda function r, this will return x*2 which is stored in x. That is,
x = 4 now. Similarly in third step we have passed x to lambda function s, So x
= 4*3. i.e, x = 12 now. Again in the last step, x is multiplied by 2 by
passing it to function r. Therefore, x = 24.

  

  

**Program 2:**

 __

 __  
 __

 __

 __  
 __  
 __

a= 4.5

b = 2

print (a//b)  
  
---  
  
 __

 __

 **Output:**

    
    
    2.0

 **Explanation :** This type of division is called truncating division where
the remainder is truncated or dropped.

**Program 3:**

 __

 __  
 __

 __

 __  
 __  
 __

a= True

b = False

c = False

 

if a or b and c:

 print ("GEEKSFORGEEKS")

else:

 print ("geeksforgeeks")  
  
---  
  
 __

 __

 **Output:**

    
    
    GEEKSFORGEEKS

 **Explanation :** In Python, AND operator has higher precedence than OR
operator. So, it is evaluated first. i.e, (b and c) evaluates to false.Now OR
operator is evaluated. Here, (True or False) evaluates to True. So the if
condition becomes True and GEEKSFORGEEKS is printed as output.

  

  

 **Program 4:**

 __

 __  
 __

 __

 __  
 __  
 __

a= True

b = False

c = False

 

if not a or b:

 print (1)

elif not a or not b and c:

 print (2)

elif not a or b or not b and a:

 print (3)

else:

 print (4)  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Explanation:** In Python the precedence order is first NOT then AND and in
last OR. So the if condition and second elif condition evaluates to False
while third elif condition is evaluated to be True resulting in 3 as output.

**Program 5:**

 __

 __  
 __

 __

 __  
 __  
 __

count= 1

 

def doThis():

 

 global count

 

 for i in (1, 2, 3): 

 count += 1

 

doThis()

 

print (count)  
  
---  
  
 __

 __

 **Output:**

    
    
     4 

**Explanation:** The variable count declared outside the function is global
variable and also the count variable being referenced in the function is the
same global variable defined outside of the function. So, the changes made to
variable in the function is reflected to the original variable. So, the output
of the program is 4.

Python Quizzes

This article is contributed by **Harsh Agarwal**. If you like GeeksforGeeks
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

