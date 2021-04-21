Python – Odd elements removal in List



Due to the upcoming of Machine Learning, focus has now moved on handling the
certain values than ever before, the reason behind this is that it is the
essential step of data preprocessing before it is fed into further techniques
to perform. Hence removal of certain values in essential and knowledge of it
is a must. Lets discuss certain ways in which removal of odd values is
achieved.

 **Method #1 : Naive Method**  
In naive method, we iterate through whole list and append all the filtered,
non odd values into a new list, hence ready to be performed with subsequent
operations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Odd elements removal in List

# using naive method 

 

# initializing list

test_list = [1, 9, 4, 7, 6, 5, 8, 3]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using naive method 

# Odd elements removal in List

res = []

for val in test_list:

 if not (val % 2 != 0) :

 res.append(val)

 

# printing result

print ("List after removal of Odd values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 9, 4, 7, 6, 5, 8, 3]
    List after removal of Odd values : [4, 6, 8]
    

**Method #2 : Using list comprehension**  
The longer task of using the naive method and increasing line of codes can be
done in compact way using this method. We just check for non odd values and
construct the new filtered list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Odd elements removal in List

# using list comprehension

 

# initializing list

test_list = [1, 9, 4, 7, 6, 5, 8, 3]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list comprehension

# Odd elements removal in List

res = [i for i in test_list if not (i % 2 !=
0)]

 

# printing result

print ("List after removal of odd values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 9, 4, 7, 6, 5, 8, 3]
    List after removal of Odd values : [4, 6, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

