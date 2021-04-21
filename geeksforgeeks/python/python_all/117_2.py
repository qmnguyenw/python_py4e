Python | Remove prefix strings from list



Sometimes, while working with data, we can have a problem in which we need to
filter the strings list in such a way that strings starting with specific
prefix are removed. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop + remove() + startswith()**  
The combination of above functions can solve this problem. In this, we remove
the elements that start with particular prefix accessed using loop and return
the modified list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove prefix strings from list

# using loop + remove() + startswith()

 

# initialize list 

test_list = ['xall', 'xlove', 'gfg', 'xit', 'is',
'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize prefix 

pref = 'x'

 

# Remove prefix strings from list

# using loop + remove() + startswith()

for word in test_list[:]:

 if word.startswith(pref):

 test_list.remove(word)

 

# printing result

print("List after removal of Kth character of each string : " +
str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['xall', 'xlove', 'gfg', 'xit', 'is', 'best']
    List after removal of Kth character of each string : ['gfg', 'is', 'best']
    

**Method #2 : Using list comprehension +startswith()**  
This is another way in which this task can be performed. In this, we don’t
perform removal in place, instead, we recreate the list without the elements
that match the prefix.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove prefix strings from list

# using list comprehension + startswith()

 

# initialize list 

test_list = ['xall', 'xlove', 'gfg', 'xit', 'is',
'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize prefix 

pref = 'x'

 

# Remove prefix strings from list

# using list comprehension + startswith()

res = [ele for ele in test_list if not
ele.startswith(pref)]

 

# printing result

print("List after removal of Kth character of each string : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['xall', 'xlove', 'gfg', 'xit', 'is', 'best']
    List after removal of Kth character of each string : ['gfg', 'is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

