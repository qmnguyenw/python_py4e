Python – Modulo K elements removal



Due to the upcoming of Machine Learning, focus has now moved on handling the
certain values than ever before, the reason behind this is that it is the
essential step of data preprocessing before it is fed into further techniques
to perform. Hence removal of certain values in essential and knowledge of it
is a must. Lets discuss certain ways in which removal of modulo K values is
achieved.

 **Method #1 : Naive Method**  
In naive method, we iterate through whole list and append all the filtered,
non modulo K values into a new list, hence ready to be performed with
subsequent operations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Modulo K elements removal

# using naive method 

 

# initializing list

test_list = [1, 9, 4, 7, 6, 5, 8, 3]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using naive method 

# Modulo K elements removal

res = []

for val in test_list:

 if (val % K) :

 res.append(val)

 

# printing result

print ("List after removal of modulo K values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 9, 4, 7, 6, 5, 8, 3]
    List after removal of modulo K values : [1, 4, 7, 5, 8]
    

**Method #2 : Using list comprehension**  
The longer task of using the naive method and increasing line of codes can be
done in compact way using this method. We just check for non modulo K values
and construct the new filtered list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Modulo K elements removal

# using list comprehension

 

# initializing list

test_list = [1, 9, 4, 7, 6, 5, 8, 3]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# using list comprehension

# Modulo K elements removal

res = [i for i in test_list if(i % K != 0)]

 

# printing result

print ("List after removal of modulo K values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 9, 4, 7, 6, 5, 8, 3]
    List after removal of modulo K values : [1, 4, 7, 5, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

