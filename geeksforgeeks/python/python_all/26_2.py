Python – Sort by Maximum digit in Element



Given a List of Elements, sort by the maximum digit of the element present in
the List.

>  **Input** : test_list = [234, 92, 8, 721]  
> **Output** : [234, 721, 8, 92]  
> **Explanation** : 4 < 7 < 8 < 9, sorted by maximum digits.
>
>  **Input** : test_list = [92, 8, 721]  
> **Output** : [721, 8, 92]  
> **Explanation** : 7 < 8 < 9, sorted by maximum digits.

**Method #1 : Using** **max()** **\+ sort()**

In this, we perform task of inplace sort using sort() and maximum element is
extracted using max().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Maximum digit in Element

# Using max() + sort()

 

def max_dig(ele):

 

 # getting maximum digit by magnitude

 return max(str(ele))

 

# initializing list

test_list = [234, 92, 15, 8, 721]

 

# printing original list

print("The original list is : " + str(test_list))

 

# calling sort fnc. to sort with key

test_list.sort(key = max_dig)

 

# printing result 

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [234, 92, 15, 8, 721]
    Sorted List : [234, 15, 721, 8, 92]
    

**Method #2 : Using** **sorted()** **+** **lambda** **\+ max()**

In this, we use sorted() perform non-inplace sort, and avoid usage of external
function using lambda function to get maximum digit.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Maximum digit in Element

# Using sorted() + lambda + max()

 

# initializing list

test_list = [234, 92, 15, 8, 721]

 

# printing original list

print("The original list is : " + str(test_list))

 

# lambda fnc. used to get maximum Element logic

res = sorted(test_list, key = lambda ele :
max(str(ele)))

 

# printing result 

print("Sorted List " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [234, 92, 15, 8, 721]
    Sorted List [234, 15, 721, 8, 92]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

