Output of Python Programs | (Dictionary)



 **Prerequisite:** Dictionary  
 **Note:** Output of all these programs is tested on Python3  
 **1.What is the output of the following of code?**

 __

 __  
 __

 __

 __  
 __  
 __

a= {i: i * i for i in range(6)}

print (a)  
  
---  
  
 __

 __

Options:  
a) Dictionary comprehension doesn’t exist  
b) {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6:36}  
c) {0: 0, 1: 1, 4: 4, 9: 9, 16: 16, 25: 25}  
d) {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    
    
    Ans. (d)

 **Explanation:** The above piece of code written in curly braces generate the
whole Dictionary.  
 **2.What is the output of the following of code?**

 __

 __  
 __

 __

 __  
 __  
 __

a={}

a.fromkeys(['a', 'b', 'c', 'd'], 98)

print (a)  
  
---  
  
 __

 __

Options:  
a) Syntax error  
b) {‘a’:98, ‘b’:98, ‘c’:98, ‘d’:98}  
c) {}  
d) {‘a’:None, ‘b’:None, ‘c’:None.’d’:None}

    
    
    Ans. (c)
    

**Explanation:** **fromkeys()** create a new dictionary with keys from list
given to it as an argument and set values of the key, the default value given
in it as an argument.  
Input:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

a={}

dict = a.fromkeys(['a', 'b', 'c', 'd'], 98)

print (a)

print (dict)  
  
---  
  
 __

 __

Output:

    
    
    {}
    {'d': 98, 'b': 98, 'a': 98, 'c': 98}
    

**3.What is the output of the following of code?**

 __

 __  
 __

 __

 __  
 __  
 __

dict ={}

print (all(dict))  
  
---  
  
 __

 __

Options:  
a) { }  
b) False  
c) True  
d) An exception is thrown

    
    
    Ans.(c)
    

**Explanation:** The all() method returns:

* True – If all elements in an iterable are true ot iterable is empty.
* False – If any element in an iterable is false.

Input:

 __

 __  
 __

 __

 __  
 __  
 __

a= {}

b = a.fromkeys([1, False, 3], 'True')

print (all(a))

print (all(b))  
  
---  
  
 __

 __

Output:

    
    
    True
    False
    

**4.What is the output of the following of code?**

 __

 __  
 __

 __

 __  
 __  
 __

a= {'geeks' : 1, 'gfg' : 2}

b = {'geeks' : 2, 'gfg' : 1}

print (a == b)   
  
---  
  
__

__

a) True  
b) False  
c) Error  
d) None

    
    
    Ans. (b)
    

**Explanation:** If two dictionary are same it returns true, otherwise it
returns false.

 **5.Which of these about a dictionary is false?**  
a) The values of a dictionary can be accessed using keys  
b) The keys of a dictionary can be accessed using values  
c) Dictionaries may or may not be ordered  
d) None of the above

    
    
    Ans.(b)
    

**Explanation:** The values of a dictionary can be accessed using keys but the
keys of a dictionary can’t be accessed using values.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

