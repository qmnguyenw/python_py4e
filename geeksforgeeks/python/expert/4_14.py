Creating Decorator inside a class in Python



We can easily create decorators inside a class and it is easily accessible for
its child classes. During Decorator creation, we must take care that the
function that we are defining inside the decorator must take current object
reference (self) as a parameter, and while we are accessing that decorator
from child class that time we must call that decorator using the class
name(class in which Decorator is present).

 **Example 1:** Here in this example we are creating a decorator function
inside Class A. Inside Class A “fun1” Instance Method is calling the decorator
function “Decorators” inside Class B “fun2”. Instance Method is calling the
decorator function of Class A. To use the decorator of Class A, we must
require using Class name in which decorator is present that’s why we use
“@A.Decorators” here.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# creating class A

class A :

 def Decorators(func) :

 def inner(self) :

 print('Decoration started.')

 func(self)

 print('Decoration of function completed.\n')

 return inner

 

 @Decorators

 def fun1(self) :

 print('Decorating - Class A methods.')

 

# creating class B

class B(A) :

 @A.Decorators

 def fun2(self) :

 print('Decoration - Class B methods.')

 

obj = B()

obj.fun1()

obj.fun2()  
  
---  
  
 __

 __

 **Output:**

    
    
    Decoration started.
    Decorating - Class A methods.
    Decoration of function completed.
    
    Decoration started.
    Decoration - Class B methods.
    Decoration of function completed.
    

**Example 2:** Checking number is Even or Odd using Decorator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

class Check_no :

 

 # decorator function

 def decor(func) : 

 def check(self, no) :

 func(self, no)

 if no % 2 == 0 :

 print('Yes, it\'s EVEN Number.')

 else :

 print('No, it\'s ODD Number.')

 return check

 

 @decor

 

 #instance method

 def is_even(self, no) : 

 print('User Input : ', no)

 

obj = Check_no()

obj.is_even(45)

obj.is_even(2)

obj.is_even(7)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    User Input :  45
    No, it's ODD Number.
    User Input :  2
    Yes, it's EVEN Number.
    User Input :  7
    No, it's ODD Number.
    

**Example 3:** Checking Grade from Marks.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# parent class

class Student : 

 

 # decorator function

 def decor(func) : 

 def grade(self,marks) :

 func(self,marks)

 if marks < 35 :

 print('Grade : F')

 elif marks < 50 :

 print('Grade : E')

 elif marks < 60 :

 print('Grade : D')

 elif marks < 70 :

 print('Grade : C')

 elif marks < 80 :

 print('Grade : B')

 elif marks < 100 :

 print('Grade : A')

 return grade

 

# child class

class Result(Student) : 

 @Student.decor

 

 # instance method

 def result(self,marks) : 

 print('Your Score : ',marks)

 

# creating object of parent class

obj = Result() 

obj.result(89) 

obj.result(34)  
  
---  
  
 __

 __

 **Output:**

    
    
    Your Score :  89
    Grade : A
    Your Score :  34
    Grade : F
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

