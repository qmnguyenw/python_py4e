Python | Convert String ranges to list



Sometimes, while working in applications we can have a problem in which we are
given a naive string which provides ranges separated by a hyphen and other
numbers separated by commas. This problem can occur across many places. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Usingsum() + split() \+ list comprehension + enumerate()**  
The combination of above functions can be used to perform these tasks. In
this, the split is performed on hyphen and comma and accordingly range,
numbers are extracted and compiled into a list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String ranges to list

# Using sum() + list comprehension + enumerate() + split()

 

# initializing string 

test_str = "1, 4-6, 8-10, 11"

 

# printing original string 

print("The original string is : " + test_str)

 

# Convert String ranges to list

# Using sum() + list comprehension + enumerate() + split()

res = sum(((list(range(*[int(b) + c 

 for c, b in enumerate(a.split('-'))]))

 if '-' in a else [int(a)]) for a in
test_str.split(', ')), [])

 

# printing result

print("List after conversion from string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 1, 4-6, 8-10, 11
    List after conversion from string : [1, 4, 5, 6, 8, 9, 10, 11]
    

**Method #2 : Usingmap() + split() \+ lambda**  
This task can also be performed using above functions. Similar to method
above. The only difference is that we use map() and lambda function to reduce
complex readability. Works only with Python2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python2 code to demonstrate working of

# Convert String ranges to list

# Using map() + lambda + split()

 

# initializing string 

test_str = "1, 4-6, 8-10, 11"

 

# printing original string 

print("The original string is : " + test_str)

 

# Convert String ranges to list

# Using map() + lambda + split()

temp = [(lambda sub: range(sub[0], sub[-1] +
1))(map(int, ele.split('-')))\

 for ele in test_str.split(', ')]

 

res = [b for a in temp for b in a]

 

# printing result

print("List after conversion from string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 1, 4-6, 8-10, 11
    List after conversion from string : [1, 4, 5, 6, 8, 9, 10, 11]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

