Python – Segregate elements by delimiter



Given list of Strings, segregate each string by delimiter and output different
lists for prefix and suffix.

>  **Input** : test_list = [“7$2”, “8$5”, “9$1”], delim = “$”  
>  **Output** : [‘7’, ‘8’, ‘9’], [‘2’, ‘5’, ‘1’]  
>  **Explanation** : Different lists for prefix and suffix of “$”
>
>  **Input** : test_list = [“7*2”, “8*5”, “9*1”], delim = “*”  
>  **Output** : [‘7’, ‘8’, ‘9’], [‘2’, ‘5’, ‘1’]  
>  **Explanation** : Different lists for prefix and suffix of “*”

 **Method #1 : Using list comprehension + split()**

The is one of the way in which this task can be performed. In this, we perform
segregation using split(), the first part of split is compiled to one list
comprehension and next to other.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Segregate elements by delimiter

# Using list comprehension + split()

 

# initializing list

test_list = ["7$2", "8$5", "9$1", "8$10", "32$6"]

 

# printing original list

print("The original list : " + str(test_list))

 

# using delim 

delim = "$"

 

# using split() to split and different list comprehension

# assigns results to different lists 

res1, res2 = [ele.split(delim)[0] for ele in test_list],
[ele.split(delim)[1] for ele in test_list]

 

# printing result 

print("The filtered list 1 : " + str(res1))

print("The filtered list 2 : " + str(res2))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['7$2', '8$5', '9$1', '8$10', '32$6']
    The filtered list 1 : ['7', '8', '9', '8', '32']
    The filtered list 2 : ['2', '5', '1', '10', '6']
    

**Method #2 : Using map() + list + zip() + generator expression**

The combination of above functions can be used to solve this problem. In this,
we extend the list construction logic using map() and zip() is used to perform
split() functionality to each element.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Segregate elements by delimiter

# Using map() + list + zip() + generator expression

 

# initializing list

test_list = ["7$2", "8$5", "9$1", "8$10", "32$6"]

 

# printing original list

print("The original list : " + str(test_list))

 

# using delim 

delim = "$"

 

# map() used to cast different sections to different lists

res1, res2 = map(list, zip(*(ele.split(delim) for ele
in test_list)))

 

# printing result 

print("The filtered list 1 : " + str(res1))

print("The filtered list 2 : " + str(res2))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['7$2', '8$5', '9$1', '8$10', '32$6']
    The filtered list 1 : ['7', '8', '9', '8', '32']
    The filtered list 2 : ['2', '5', '1', '10', '6']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

