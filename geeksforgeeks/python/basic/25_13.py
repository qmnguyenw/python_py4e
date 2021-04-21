Why is python best suited for Competitive Coding?



When it comes to **Product Based Companies** , they need good coders and one
needs to clear the **Competitive Coding** round in order to reach the
interview rounds. Competitive coding is one such platform which will test your
mental ability and speed at the same time.

    
    
    **Who should read this?**
        Any programmer who still hasn't tried python for
        Competitive Coding MUST give this article a read.
        This should clear up any doubts one has before 
        shifting to python. **No matter how comfortable
        a programming language may seem to you right now
        Python is bound to feel even better**.
        Python has a tendency of sticking to people
        like a bad habbit !!
    

**SPEED** is a factor where python is second to none. The amount of code to be
typed decreases drastically in comparison to conventional programming
languages like C, C++, JAVA. Another most important point is that python arms
its users with a **wide variety of functionality, packages and libraries**
which act like a supplement to the programmer’s mental ability.  
Ultimately the best thing about python is that its very Simple and we need not
waste much time on trivial matters like input,output etc. It helps shift our
focus to the problem at hand.

Here I’m gonna list out some of my favourite features of python which I’m sure
will encourage you to start trying python for Competitive Coding.

  1.  **Variable Independence**  
Python doesn’t require us to declare variables and their Data-Types before
using them. This also gives us the flexibility of range as long as its within
reasonable limits of the Hardware i.e. no need to worry about integer and long
integer. Type conversion is internally handled with flawless results.

    
         **Amazing Fact !!**
              For nested loops in python we can use the 
              same variable name in both inner and outer
              for-loop variables without fear of 
              inconsistent data or any errors !!

  2.  **Common Functions like sorted, min, max, count etc.**  
The min/max function helps us to find the minimum/maximum element from a
list.The Sorted function allows us to sort a list and **count function** helps
us to count the number of occurences of a particular element in a list.  
The **best thing is that we can be rest assured that the python libraries use
the best possible algorithms for each of the above operations.** For example
the sorted function is a very special sorting algorithm called **TIMSORT**
that has a worst case time complexity of O(n log n) which is the best a
sorting algorithm can offer.  
Reference:Python sorting algorithm

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of min(),

# max(), sorted() and count()

arr = [10, 76, 87, 45, 22, 87, 90, 87,
66, 84, 87]

 

print("Maximum = ",max(arr))

print("Minimum = ",min(arr))

print("The sorted array is = ",sorted(arr))

print('Number of occurrences of 87 is = ',arr.count(87))  
  
---  
  
 __

 __

Output:

    
    
    ('Maximum = ', 90)
    ('Minimum = ', 10)
    ('The sorted array is = ', [10, 22, 45, 66, 76, 84, 87, 87, 87, 87, 90])
    ('Number of occurrences of 87 is = ', 4)
    

* **Lists in python combine the best aspects of arrays and linked lists.**  
Python lists provide the unique functionality of deleting specific elements
while keeping the memory locations in a contiguous manner. **This feature
renders the concept of Linked lists null and void**. Its like a linked list on
STEROIDS ! Moreover Insertions can be performed at any desired locations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate list operations

arr = [00, 11, 22, 33, 44, 55, 66, 77,
88, 99]

 

# deletion via index position

del arr[5]

print(arr)

 

# deletion via specifying particular element

arr.remove(22)

print(arr)

 

# insertion at any arbitrary position

arr[-1] = "A random number"

print(arr)

 

# concept of sub-lists

k = arr[:2]

print(k)  
  
---  
  
 __

 __

Output:

    
    
    [0, 11, 22, 33, 44, 66, 77, 88, 99]
    [0, 11, 33, 44, 66, 77, 88, 99]
    [0, 11, 33, 44, 66, 77, 88, 'A random number']
    [0, 11]
    

* **Unique list operations – Backtracking , Sub-Lists.**  
In case we are not sure about the list size then we can use the index position
of -1 to access the last element. Similarly -2 can be used for second last
element and so on. Thus we can back track a list. Also we don’t have to
specify any particular list size so it also works like a dynamic allocation
array.  
A specific portion of a list can be extracted without having to traverse the
list as is seen in the above example. **A very astonishing fact about lists is
that it can hold different datatypes.** Gone are the days where lists used to
be a homogeneous collection of data elements!!

*  **Functions can return more than one value.**  
Typically functions in other programming languages can return only one value
but **in python we can return more than one value!!** as is seen in the
following code snippet.  

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate that a function

# can easily return multiple values.

def multi_return(*arr):

 k1 = arr[0]

 k2 = arr[1]

 return k1,k2

 

a,b = multi_return(11,22)

print(a,' ',b)

 

a,b = multi_return(55,66,77,88,99)

print(a,' ',b)  
  
---  
  
 __

 __

Output:

    
    
    11   22
    55   66
    

* **Flexible number of arguments to a function.**  
Arguments to a function may be passed in the form of a list whose size may
vary every time we need to call the function. In the above example we first
called the function with 2 arguments and then with 5 arguments!!  
 ****

* If else and for loops are much more User Friendly.

