Python | Remove None values from list



Due to the upcoming of Machine Learning, the focus has now moved on handling
the _None_ values than ever before, the reason behind this is that it is the
essential step of data preprocessing before it is fed into further techniques
to perform. Hence, removal of _None_ values in essential and knowledge of it
is a must. Let’s discuss certain ways in which this is achieved.

 **Method #1 : Naive Method**  
In naive method, we iterate through the whole list and append all the
filtered, non-None values into a new list, hence ready to be performed with
subsequent operations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing None values in list

# using naive method 

 

# initializing list

test_list = [1, None, 4, None, None, 5, 8,
None]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using naive method 

# to remove None values in list

res = []

for val in test_list:

 if val != None :

 res.append(val)

 

# printing result

print ("List after removal of None values : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, None, 4, None, None, 5, 8, None]
    List after removal of None values : [1, 4, 5, 8]
    

  
**Method #2 : Using list comprehension**  
The longer task of using the naive method and increasing line of codes can be
done in a compact way using this method. We just check for True values and
construct the new filtered list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing None values in list

# using list comprehension

 

# initializing list

test_list = [1, None, 4, None, None, 5, 8,
None]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list comprehension

# to remove None values in list

res = [i for i in test_list if i]

 

# printing result

print ("List after removal of None values : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : [1, None, 4, None, None, 5, 8, None]
    List after removal of None values : [1, 4, 5, 8]
    

