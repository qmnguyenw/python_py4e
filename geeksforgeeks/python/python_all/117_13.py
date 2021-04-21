Python | Construct N Range Equilength String list



Sometimes, while working with Python, we can have a problem in which we need
to construct a string list which contains N range numbers. But we have
requirement in which we need to keep each element of equal length. Let’s
discuss certain ways in which this task can be performed.

 **Method #1: Using list comprehension +zfill()**  
The combination of above functionalities can be used to perform this task. In
this, we perform the task of adding numbers using list comprehension and
zfill() takes care of length required for each string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct N Range Equilength String list

# using list comprehension + zfill()

 

# initialize N 

N = 6

 

# printing N 

print("Number of elements required : " + str(N))

 

# initialize K 

K = 3

 

# Construct N Range Equilength String list

# using list comprehension + zfill()

res = [str(ele).zfill(K) for ele in range(N)]

 

# printing result

print("K Length range strings list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Number of elements required : 6
    K Length range strings list : ['000', '001', '002', '003', '004', '005']
    

**Method #2 : Using map() \+ string formatting**  
This task can also be performed using above functions. In this, we extend the
logic of length using string formatting. And is used for constructing the N
range.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct N Range Equilength String list

# using map() + string formatting

 

# initialize N 

N = 6

 

# printing N 

print("Number of elements required : " + str(N))

 

# initialize K 

K = 3

 

# Construct N Range Equilength String list

# using map() + string formatting

temp = '{:0' + str(K) + '}'

res = list(map(temp.format, range(N)))

 

# printing result

print("K Length range strings list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Number of elements required : 6
    K Length range strings list : ['000', '001', '002', '003', '004', '005']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

