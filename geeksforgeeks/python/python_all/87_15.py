Python – Combine Strings to Matrix



Sometimes while working with data, we can receive separate data in the form of
strings and we need to compile them into Matrix for its further use. This can
have applications in many domains. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Using list comprehension +split() + zip()**  
The combination of the above functions can be used to perform this task. In
this, we combine strings into Matrix row elements using zip() and split
performs the task of extracting word from strings.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Combine Strings to Matrix

# Using list comprehension + zip() + split()

 

# initializing strings

test_str1 = "Gfg is best"

test_str2 = "1 2 3"

 

# printing original strings

print("The original string 1 is : " + test_str1)

print("The original string 2 is : " + test_str2)

 

# Combine Strings to Matrix

# Using list comprehension + zip() + split()

res = [[idx, int(j)] for idx, j in zip(test_str1.split('
'), test_str2.split(' '))]

 

# printing result 

print("Does Matrix after construction : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list 1 is : [‘Gfg’, ‘is’, ‘best’]  
> The original list 2 is : [[‘Gfg’, 1], [‘is’, 2], [‘best’, 1], [‘Gfg’, 4],
> [‘is’, 8], [‘Gfg’, 7]]  
> The dictionary after grouping : {‘is’: [2, 8], ‘Gfg’: [1, 4, 7], ‘best’:
> [1]}

  

  

**Method #2 : Usingmap() + split() + zip()**  
The combination of above functions can be used to perform this task. This
performs in similar way as above. The difference is that the logic of
extension is done using map().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Combine Strings to Matrix

# Using map() + zip() + split()

 

# initializing strings

test_str1 = "Gfg is best"

test_str2 = "1 2 3"

 

# printing original strings

print("The original string 1 is : " + test_str1)

print("The original string 2 is : " + test_str2)

 

# Combine Strings to Matrix

# Using map() + zip() + split()

res = list(map(list, zip(test_str1.split(' '),
map(int, test_str2.split(' ')))))

 

# printing result 

print("Does Matrix after construction : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list 1 is : [‘Gfg’, ‘is’, ‘best’]  
> The original list 2 is : [[‘Gfg’, 1], [‘is’, 2], [‘best’, 1], [‘Gfg’, 4],
> [‘is’, 8], [‘Gfg’, 7]]  
> The dictionary after grouping : {‘is’: [2, 8], ‘Gfg’: [1, 4, 7], ‘best’:
> [1]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

