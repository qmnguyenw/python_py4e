Statistical Functions in Python | Set 2 ( Measure of Spread)



Statistical Functions in Python | Set 1(Averages and Measure of Central
Location)

Measure of spread functions of statistics are discussed in this article.

 **1\. variance()** :- This function calculates the variance i.e **measure of
deviation of data, more the value of variance, more the data values are
spread**. Sample variance is computed in this function, assuming data is of a
part of population. If passed argument is empty, **StatisticsError** is
raised.

 **2\. pvariance()** :- This function computes the **variance of the entire
population**. The data is interpreted as it is of the whole population. If
passed argument is empty, **StatisticsError** is raised.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# variance() and pvariance()

 

# importing statistics to handle statistical operations

import statistics

 

# initializing list

li = [1.5, 2.5, 2.5, 3.5, 3.5, 3.5]

 

# using variance to calculate variance of data

print ("The variance of data is : ",end="")

print (statistics.variance(li))

 

# using pvariance to calculate population variance of data

print ("The population variance of data is : ",end="")

print (statistics.pvariance(li))  
  
---  
  
 __

 __

Output:

  

  

    
    
    The variance of data is : 0.6666666666666667
    The population variance of data is : 0.5555555555555556
    

**3\. stdev()** :- This function returns the **standard deviation ( square
root of sample variance )** of the data. If passed argument is empty,
**StatisticsError** is raised.

 **4\. pstdev()** :- This function returns the population **standard deviation
( square root of population variance )** of the data. If passed argument is
empty, **StatisticsError** is raised.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# stdev() and pstdev()

 

# importing statistics to handle statistical operations

import statistics

 

# initializing list

li = [1.5, 2.5, 2.5, 3.5, 3.5, 3.5]

 

# using stdev to calculate standard deviation of data

print ("The standard deviation of data is : ",end="")

print (statistics.stdev(li))

 

# using pstdev to calculate population standard deviation of data

print ("The population standard deviation of data is : ",end="")

print (statistics.pstdev(li))  
  
---  
  
 __

 __

Output:

    
    
    The standard deviation of data is : 0.816496580927726
    The population standard deviation of data is : 0.7453559924999299
    

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

