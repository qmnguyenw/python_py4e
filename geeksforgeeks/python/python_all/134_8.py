Python | Segregating key’s value in list of dictionaries



While working with dictionaries, we may encounter with problem in which we
need to segregate all the similar keys’ values together. This kind of problem
can occur in web development domain while working with database. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using generator expression**  
A generator expression can be used to perform this particular task. In this we
take one key at a time and check for the matching keys in all dictionaries.
The drawback is that we need to know the key’s in advanced.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Segregating key's value in list of dictionaries

# Using generator expression

 

# Initialize list

test_list = [{'gfg' : 1, 'best' : 2}, {'gfg' : 4,
'best': 5}]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using generator expression

# Segregating key's value in list of dictionaries

res = [tuple(sub["gfg"] for sub in test_list),

 tuple(sub["best"] for sub in test_list)]

 

# printing result 

print("Segregated values of keys are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [{‘best’: 2, ‘gfg’: 1}, {‘best’: 5, ‘gfg’: 4}]  
> Segregated values of keys are : [(1, 4), (2, 5)]

  

  

**Method #2 : Usingzip() + map() + values()**  
The combination of above functions can also perform the similar task in one
line. In this, values() is used to extract values, map() is used to link
individual keys with one other and finally zip() joins the their
corresponding values to single tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Segregating key's value in list of dictionaries

# Using zip() + map() + values()

 

# Initialize list

test_list = [{'gfg' : 1, 'best' : 2}, {'gfg' : 4,
'best': 5}]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using zip() + map() + values()

# Segregating key's value in list of dictionaries

res = list(zip(*map(dict.values, test_list)))

 

# printing result 

print("Segregated values of keys are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [{‘best’: 2, ‘gfg’: 1}, {‘best’: 5, ‘gfg’: 4}]  
> Segregated values of keys are : [(1, 4), (2, 5)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

