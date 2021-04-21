Python – Remove suffix from string list



Sometimes, while working with data, we can have a problem in which we need to
filter the strings list in such a way that strings ending with specific suffix
are removed. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +remove() + endswith()**  
The combination of above functions can solve this problem. In this, we remove
the elements that end with particular suffix accessed using loop and return
the modified list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Suffix removal from String list

# using loop + remove() + endswith()

 

# initialize list 

test_list = ['allx', 'lovex', 'gfg', 'xit', 'is',
'bestx']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize suffix

suff = 'x'

 

# Suffix removal from String list

# using loop + remove() + endswith()

for word in test_list[:]:

 if word.endswith(suff):

 test_list.remove(word)

 

# printing result

print("List after removal of suffix elements : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
    List after removal of suffix elements : ['gfg', 'xit', 'is']
    

**Method #2 : Using list comprehension +endswith()**  
This is another way in which this task can be performed. In this, we don’t
perform removal in place, instead, we recreate the list without the elements
that match the suffix.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Suffix removal from String list

# using list comprehension + endswith()

 

# initialize list 

test_list = ['allx', 'lovex', 'gfg', 'xit', 'is',
'bestx']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize suff

suff = 'x'

 

# Suffix removal from String list

# using list comprehension + endswith()

res = [ele for ele in test_list if not ele.endswith(suff)]

 

# printing result

print("List after removal of suffix elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
    List after removal of suffix elements : ['gfg', 'xit', 'is']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

