Using Iterations in Python Effectively



Prerequisite : Iterators in Python

Following are different ways to use iterators.

 **C-style approach:** This approach requires prior knowledge of total number
of iterations.

 __

 __  
 __

 __

 __  
 __  
 __

# A C-style way of accessing list elements

cars = ["Aston", "Audi", "McLaren"]

i = 0

while (i < len(cars)):

 print cars[i]

 i += 1  
  
---  
  
 __

 __

 **Output:**

    
    
    Aston
    Audi 
    McLaren 
    

**Important Points:**

  

  

  * This style of looping is rarely used by python programmers.
  * This 4-step approach creates no compactness with single-view looping construct.
  * This is also prone to errors in large-scale programs or designs.
  * There is no C-Style for loop in Python, i.e., a loop like for (int i=0; i<n; i++)

**Use of for-in (orfor each) style:**  
This style is used in python containing iterator of lists, dictonary, n
dimensional-arrays etc. The iterator fetches each component and prints data
while looping. The iterator is automatically incremented/decremented in this
construct.

 __

 __  
 __

 __

 __  
 __  
 __

# Accessing items using for-in loop

 

cars = ["Aston", "Audi", "McLaren"]

for x in cars:

 print x  
  
---  
  
 __

 __

 **Output:**

    
    
    Aston
    Audi 
    McLaren 
    

See this for more examples of different data types.

 **Indexing using Range function:** We can also use indexing using range() in
Python.

 __

 __  
 __

 __

 __  
 __  
 __

# Accessing items using indexes and for-in

 

cars = ["Aston", "Audi", "McLaren"]

for i in range(len(cars)):

 print cars[i]  
  
---  
  
 __

 __

 **Output:**

    
    
    Aston
    Audi 
    McLaren 
    

**Enumerate:**  
Enumerate is built-in python function that takes input as iterator, list etc
and returns a tuple containing index and data at that index in the iterator
sequence. For example, enumerate(cars), returns a iterator that will return
(0, cars[0]), (1, cars[1]), (2, cars[2]), and so on.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Accessing items using enumerate()

 

cars = ["Aston" , "Audi", "McLaren "]

for i, x in enumerate(cars):

 print (x)  
  
---  
  
 __

 __

 **Output :**

    
    
    Aston
    Audi
    McLaren 

Below solution also works.

 __

 __  
 __

 __

 __  
 __  
 __

# Accessing items and indexes enumerate()

 

cars = ["Aston" , "Audi", "McLaren "]

for x in enumerate(cars):

 print (x[0], x[1])  
  
---  
  
 __

 __

 **Output :**

    
    
    (0, 'Aston')
    (1, 'Audi')
    (2, 'McLaren ')

We can also directly print returned value of enumerate() to see what it
returns.

 __

 __  
 __

 __

 __  
 __  
 __

# Printing return value of enumerate()

 

cars = ["Aston" , "Audi", "McLaren "]

print enumerate(cars)  
  
---  
  
 __

 __

 **Output :**

    
    
    [(0, 'Aston'), (1, 'Audi'), (2, 'McLaren ')]

Enumerate takes parameter start which is default set to zero. We can change
this parameter to any value we like. In the below code we have used start as
1.

 __

 __  
 __

 __

 __  
 __  
 __

# demonstrating the use of start in enumerate

 

cars = ["Aston" , "Audi", "McLaren "]

for x in enumerate(cars, start=1):

 print (x[0], x[1])  
  
---  
  
 __

 __

 **Output :**

    
    
    (1, 'Aston')
    (2, 'Audi')
    (3, 'McLaren ')

enumerate() helps to embed solution for accessing each data item in the
iterator and fetching index of each data item.

**Looping extensions:**  
 **i)** Two iterators for a single looping construct:

