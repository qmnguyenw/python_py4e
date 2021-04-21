Python | Remove Kth character from strings list



Sometimes, while working with data, we can have a problem in which we need to
remove a particular column, i.e the Kth character from string list. String are
immutable, hence removal just means re creating a string without the Kth
character. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension + list slicing**  
This is the shorthand that can be used to perform this task. In this we just
recreate the required string using slicing and extend logic to each string
element in list using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Kth character from strings list

# using list comprehension + list slicing

 

# initialize list 

test_list = ['akash', 'nikhil', 'manjeet', 'akshat']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize K 

K = 3

 

# Remove Kth character from strings list

# using list comprehension + list slicing

res = [ele[:K] + ele[K + 1:] for ele in test_list]

 

# printing result

print("List after removal of Kth character of each string : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['akash', 'nikhil', 'manjeet', 'akshat']
    List after removal of Kth character of each string : ['akah', 'nikil', 'maneet', 'aksat']
    

**Method #2 : Usingmap() \+ slicing**  
This method is similar to above one, only difference is that the extension of
logic part to each element of list is done with the help of map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Kth character from strings list

# using list comprehension + list slicing

 

# initialize list 

test_list = ['akash', 'nikhil', 'manjeet', 'akshat']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize K 

K = 3

 

# Remove Kth character from strings list

# using list comprehension + list slicing

res = list(map(lambda ele: ele[ :K] + ele[K + 1 : ],
test_list))

 

# printing result

print("List after removal of Kth character of each string : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['akash', 'nikhil', 'manjeet', 'akshat']
    List after removal of Kth character of each string : ['akah', 'nikil', 'maneet', 'aksat']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

