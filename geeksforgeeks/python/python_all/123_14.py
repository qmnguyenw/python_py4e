Python | Common words among tuple strings



Sometimes, while working with tuples, we can have a problem in which we need
to find the intersection of words that occur in strings inside single tuple
with string as its elements. Let’s discuss certain ways in which this problem
can be solved.

 **Method #1 : Usingjoin() + set() + & operator + split()**  
The combination of above functions can be used to perform this particular
task. In this, we first convert each tuple to set and then perform
intersection of the element’s words splitted by split(). Last step is to
join all common elements using join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Common words among tuple strings

# Using join() + set() + & operator + split()

 

# Initializing tuple 

test_tup = ('gfg is best', 'gfg is for geeks', 'gfg is for
all')

 

# printing original tuple 

print("The original tuple is : " + str(test_tup))

 

# Common words among tuple strings

# Using join() + set() + & operator + split()

res = ", ".join(sorted(set(test_tup[0].split()) &\

 set(test_tup[1].split()) &\

 set(test_tup[2].split())))

 

# printing result

print("Common words among tuple are : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ('gfg is best', 'gfg is for geeks', 'gfg is for all')
    Common words among tuple are : gfg, is
    

**Method #2 : Usingmap() + reduce() \+ lambda**  
The combination of above methods can also be used to perform this particular
task. In this, we just combine all elements of tuple to check for common
elements using lambda and reduce(). The advantage of this method is that it
can work with tuple with more than countable elements easily. Works with
Python3 only.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Common words among tuple strings

# Using map() + reduce() + lambda

 

# Initializing tuple 

test_tup = ('gfg is best', 'gfg is for geeks', 'gfg is for
all')

 

# printing original tuple 

print("The original tuple is : " + str(test_tup))

 

# Common words among tuple strings

# Using map() + reduce() + lambda

res = ", ".join(reduce(lambda i, j : i & j, 

 map(lambda x: set(x.split()), test_tup)))

 

# printing result

print("Common words among tuple are : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ('gfg is best', 'gfg is for geeks', 'gfg is for all')
    Common words among tuple are : gfg, is
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

