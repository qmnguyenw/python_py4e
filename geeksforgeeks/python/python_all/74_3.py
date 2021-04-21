Python Program to Convert any Positive Real Number to Binary string



Given any Real Number greater than or equal to zero that is passed in as
float, print binary representation of entered real number.

 **Examples:**

    
    
    **Input:** 123.5
    **Output:** 1 1 1 1 0 1 1 . 1
    
    **Input:** 0.25
    **Output:** .01

 **Mathematical Logic along with steps done in programming:**

Any real number is divided into two parts: **The integer part and the Fraction
part**. For both parts operations and logic are different to convert them to
binary representation.

  *  **Integer Part:**

 **Step 1:** Divide Integer part by 2 and note its Remainder(it will be either
0 or 1).  
 **Step 2:** Again divide integer part by 2(integer obtained from step 1 by
dividing initial integer by 2) and note its Remainder.  
Repeat these steps until your integer does not becomes zero.  
 **Step 3:** Now reverse the sequence of Remainders you noted at each step.and
this is your binary representation of integer part.

  

  

 **Programming steps:**

    
        def intpartbinary(m):
    
        a=[]
        n=int(m)
    
        while n!=0:
            a.append(n%2)
            n=n//2
        a.reverse()
    
        return a

Defining a function intpartbinary() to convert integer part to binary
representation. Define an Empty list taking integer part of an entered real
number and divide it by 2 and store its remainder into an empty list each time
while n==0, reverse the list and that will be the binary representation of
integer part.

  *  **Fractional Part:**  
 **Step 1:** Multiply fractional part by 2 and write its integer part only.  
 **Step 2:** Subtract integer part from the number obtained in step
1(multiplying fraction part by 2) and again multiply fractional part by 2.  
Repeat these steps until the Fractional part does not become Zero. The
sequence obtained is Binary representation of given fractional part.

 **Programming Steps:**

    
        def decimalpartbinary(m):
    
        a=[]
        n=m-int(m)
    
        while n!=0:
            x=2*n
            y=int(x)
            a.append(y)
            n=x-y
    
        return a

Defining a function decimalpartbinary() to convert fractional part to
binary. Again define an empty list, extracting fractional part from entered
real number by subtracting integer part of entered real number from entered
real number. Now multiply it by 2 and store only integer part of resulting
number into the list and again taking fractional part and multiply by 2, store
its integer part. Repeat this process until the fractional part does not
become zero, and that will be the binary representation of the fractional
part.

Now at last combining, all the binary conversion in given below format will be
the binary representation of entered real number. Firstly write the reversed
sequence of remainders and a dot(point) then write integer part sequence which
we obtained by multiplying fraction part by 2 and extracting integer part
only.

    
    
    def binarycode(m):
    
        a = intpartbinary(m)
        b = decimalpartbinary(m)
        c = []
    
        for i in range(0, len(a)):
            c.append(a[i])
    
        c.append('.')
    
        for j in range(0, len(b)):
            c.append(b[j])
    
        print('Binary code of given function is\n')
    
        for k in range(0, len(c)):
            print(c[k], end=' ')

For this, we will define a function named binarycode(). Define an empty
list c=[], firstly store reversed list of remainder obtained by dividing
integer part by 2 each time and then store a decimal in that list c, now store
the list of integer part obtained by multiplying fraction part by 2 each time
and storing only integer part. Now print list c. Finally, we will have our
Binary Representation of Real Number into Binary Representation.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# defining a function to convert

# integer part to binary

def intpartbinary(m):

 

 a = []

 n = int(m)

 

 while n != 0:

 

 a.append(n % 2)

 n = n//2

 

 a.reverse()

 return a

 

# defining a function to convert 

# fractional part to binary

def decimalpartbinary(m):

 

 a = []

 n = m-int(m)

 

 while n != 0:

 

 x = 2 * n

 y = int(x)

 a.append(y)

 n = x-y

 

 return a

# arranging all data into suitable format

def binarycode(m):

 

 # arranging all data to our desired 

 # format

 a = intpartbinary(m)

 b = decimalpartbinary(m)

 c =[]

 

 for i in range(0, len(a)):

 c.append(a[i])

 

 c.append('.')

 

 for j in range(0, len(b)):

 c.append(b[j])

 

 print('Binary code of given function is\n')

 

 for k in range(0, len(c)):

 print(c[k], end =' ')

 

 

# Driver Code

binarycode(123.5)  
  
---  
  
 __

 __

 **Output:**

    
    
    Binary code of given function is
    
    1 1 1 1 0 1 1 . 1 

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

