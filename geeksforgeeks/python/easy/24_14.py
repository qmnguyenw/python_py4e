Python | Remove empty tuples from a list



In this article, we will see how can we remove an empty tuple from a given
list of tuples. We will find various ways, in which we can perform this task
of removing tuples using various methods and ways in Python.  
Examples:

    
    
    Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                      ('krishna', 'akbar', '45'), ('',''),()]
    Output : [('ram', '15', '8'), ('laxman', 'sita'), 
              ('krishna', 'akbar', '45'), ('', '')]
    
    Input : tuples = [('','','8'), (), ('0', '00', '000'), 
                     ('birbal', '', '45'), (''), (),  ('',''),()]
    Output : [('', '', '8'), ('0', '00', '000'), ('birbal', '', 
              '45'), ('', '')]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1: Using the concept ofList Comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove empty tuples from a

# list of tuples function to remove empty tuples 

# using list comprehension

def Remove(tuples):

 tuples = [t for t in tuples if t]

 return tuples

 

# Driver Code

tuples = [(), ('ram','15','8'), (), ('laxman',
'sita'), 

 ('krishna', 'akbar', '45'), ('',''),()]

print(Remove(tuples))  
  
---  
  
 __

 __

Output:

    
    
    [('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 
                               'akbar', '45'), ('', '')]
    

**Method 2: Using the filter() method**  
Using the inbuilt method filter() in Python, we can filter out the empty
elements by passing the _None_ as the parameter. This method works in both
Python 2 and Python 3 and above, but the desired output is only shown in
Python 2 because Python 3 returns a generator. filter() is the faster than the
method of list comprehension. Let’s see what happens when we run the program
in Python 2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python2 program to remove empty tuples

# from a list of tuples function to remove 

# empty tuples using filter

def Remove(tuples):

 tuples = filter(None, tuples)

 return tuples

 

# Driver Code

tuples = [(), ('ram','15','8'), (), ('laxman',
'sita'), 

 ('krishna', 'akbar', '45'), ('',''),()]

print Remove(tuples)  
  
---  
  
 __

 __

Output:

    
    
    [('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]

Now let’s see what happens when we try running the program in Python 3 and
above. On running the program in Python 3, as mentioned a generator is
returned.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove empty tuples from

# a list of tuples function to remove empty 

# tuples using filter

def Remove(tuples):

 tuples = filter(None, tuples)

 return tuples

 

# Driver Code

tuples = [(), ('ram','15','8'), (), ('laxman',
'sita'), 

 ('krishna', 'akbar', '45'), ('',''),()]

print (Remove(tuples))  
  
---  
  
 __

 __

Output:

    
    
    <filter object at 0x7fe26eb0f3c8>

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

