Statistical Functions in Python | Set 1 (Averages and Measure of Central
Location)



Python has the ability to manipulate some statistical data and calculate
results of various statistical operations using the file “ **statistics** “,
useful in domain of mathematics.

 **Important Average and measure of central location functions** :

 **1\. mean()** :- This function returns the **mean or average** of the data
passed in its arguments. If passed argument is empty, **StatisticsError** is
raised.

 **2\. mode()** :- This function returns the **number with maximum number of
occurrences**. If passed argument is empty, **StatisticsError** is raised.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# mean() and mode()

 

# importing statistics to handle statistical operations

import statistics

 

# initializing list

li = [1, 2, 3, 3, 2, 2, 2, 1]

 

# using mean() to calculate average of list elements

print ("The average of list values is : ",end="")

print (statistics.mean(li))

 

# using mode() to print maximum occurring of list elements

print ("The maximum occurring element is : ",end="")

print (statistics.mode(li))  
  
---  
  
 __

 __

Output:

  

  

    
    
    The average of list values is : 2.0
    The maximum occurring element is  : 2
    

**3\. median()** :- This function is used to calculate the median, i.e
**middle element of data.** If passed argument is empty, **StatisticsError**
is raised.

 **4\. median_low()** :- This function returns the median of data in case of
odd number of elements, but in case of even number of elements, returns the
**lower of two middle** elements. If passed argument is empty,
**StatisticsError** is raised.

 **5\. median_high()** :- This function returns the median of data in case of
odd number of elements, but in case of even number of elements, **returns the
higher of two middle** elements. If passed argument is empty,
**StatisticsError** is raised.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# median(), median_low() and median_high()

 

# importing statistics to handle statistical operations

import statistics

 

# initializing list

li = [1, 2, 2, 3, 3, 3]

 

# using median() to print median of list elements

print ("The median of list element is : ",end="")

print (statistics.median(li))

 

# using median_low() to print low median of list elements

print ("The lower median of list element is : ",end="")

print (statistics.median_low(li))

 

# using median_high() to print high median of list elements

print ("The higher median of list element is : ",end="")

print (statistics.median_high(li))  
  
---  
  
 __

 __

Output:

    
    
    The median of list element is : 2.5
    The lower median of list element is : 2
    The higher median of list element is : 3
    

**6\. median_grouped()** :- This function is used to compute group median, i.e
**50th percentile** of the data. If passed argument is empty,
**StatisticsError** is raised.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# median_grouped()

 

# importing statistics to handle statistical operations

import statistics

 

# initializing list

li = [1, 2, 2, 3, 3, 3]

 

# using median_grouped() to calculate 50th percentile

print ("The 50th percentile of data is : ",end="")

print (statistics.median_grouped(li))  
  
---  
  
 __

 __

Output:

    
    
    The 50th percentile of data is : 2.5
    

Statistical Functions in Python | Set 2 ( Measure of Spread)

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

