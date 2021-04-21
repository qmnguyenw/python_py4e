Python – Replace Substrings from String List



Sometimes while working with data, we can have a problem in which we need to
perform replace substrings with the mapped string to form a shortform of some
terms. This kind of problem can have application in many domains involving
data. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +replace() + enumerate()**  
The combination of above functions can be used to perform this task. In this,
we perform the task of iteration using loop and enumerate() and replacement
with a shorter form is done using replace().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Replace Substrings from String List

# using loop + replace() + enumerate()

 

# Initializing list1

test_list1 = ['GeeksforGeeks', 'is', 'Best', 'For',
'Geeks', 'And', 'Computer Science']

test_list2 = [['Geeks', 'Gks'], ['And', '&'],
['Computer', 'Comp']]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Replace Substrings from String List

# using loop + replace() + enumerate()

sub = dict(test_list2)

for key, val in sub.items():

 for idx, ele in enumerate(test_list1):

 if key in ele:

 test_list1[idx] = ele.replace(key, val)

 

# printing result 

print ("The list after replacement : " + str(test_list1))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
    The original list 2 is : [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]
    The list after replacement : ['GksforGks', 'is', 'Best', 'For', 'Gks', '&', 'Comp Science']
    

**Method #2 : Usingreplace() \+ list comprehension**  
This is another way in which this task can be performed. In this, we perform
the task of replacing using the replace() and rest of task is performed using
list comprehension. It removes list that don’t have replacements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Replace Substrings from String List

# using replace() + list comprehension

 

# Initializing list1

test_list1 = ['GeeksforGeeks', 'is', 'Best', 'For',
'Geeks', 'And', 'Computer Science']

test_list2 = [['Geeks', 'Gks'], ['And', '&'],
['Computer', 'Comp']]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Replace Substrings from String List

# using replace() + list comprehension

res = [sub.replace(sub2[0], sub2[1]) for sub in
test_list1

 for sub2 in test_list2 if sub2[0] in sub]

 

# printing result 

print ("The list after replacement : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
    The original list 2 is : [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]
    The list after replacement : ['GksforGks', 'Gks', '&', 'Comp Science']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

