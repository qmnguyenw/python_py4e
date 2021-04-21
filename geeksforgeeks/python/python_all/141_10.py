Interquartile Range and Quartile Deviation using NumPy and SciPy



 **Quartiles :**  
A quartile is a type of quantile. The **first quartile (Q1)** , is defined as
the middle number between the smallest number and the median of the data set,
the **second quartile (Q2)** – **median** of the given data set while the
**third quartile (Q3)** , is the middle number between the median and the
largest value of the data set.

 **Algorithm to find Quartiles :**  
Quartiles are calculated by the help of the median. If the number of entries
is an even number i.e. of the form 2n, then, first quartile (Q1) is equal to
the median of the **n** smallest entries and the third quartile (Q3) is equal
to the median of the **n** largest entries.

If the number of entries is an odd number i.e. of the form (2n + 1), then

  * the first quartile (Q1) is equal to the median of the **n** smallest entries
  * the third quartile (Q3) is equal to the median of the **n** largest entries
  * the second quartile(Q2) is the same as the ordinary median.

 **Range:** It is the difference between the largest value and the smallest
value in the given data set.  
 **Interquartile Range :**  
The interquartile range (IQR), also called as **midspread or middle 50%** , or
technically H-spread is the difference between the third quartile (Q3) and the
first quartile (Q1). It covers the center of the distribution and contains 50%
of the observations. **IQR = Q3 – Q1**

 **Uses :**

  

  

  * The interquartile range has a breakdown point of 25% due to which it is often preferred over the total range.
  * The IQR is used to build box plots, simple graphical representations of a probability distribution.
  * The IQR can also be used to identify the outliers in the given data set.
  * The IQR gives the central tendency of the data.

 **Decision Making**

  * The data set has a higher value of interquartile range (IQR) has more variability.
  * The data set having a lower value of interquartile range (IQR) is preferable.

Suppose if we have two data sets and their interquartile ranges are IR1 and
IR2, and if IR1 > IR2 then the data in IR1 is said to have more variability
than the data in IR2 and data in IR2 is preferable.

 **Example:**

  * Following are the number of candidates enrolled each day in last 20 days for the course –  
Data Structures & Algorithms-DSA Online 3 at GeeksforGeeks:  
75, 69, 56, 46, 47, 79, 92, 97, 89, 88, 36, 96, 105, 32, 116, 101, 79, 93, 91,
112

  * After sorting the above data set:  
32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 101, 105, 112,
116

  * Here the total number of terms is 20.
  * The second quartile (Q2) or the median of the above data is (88 + 89) / 2 = 88.5
  * The first quartile (Q1) is median of first n i.e. 10 terms (or n i.e. 10 smallest values) = 62.5
  * The third quartile (Q3) is the median of n i.e. 10 largest values (or last n i.e. 10 values) = 96.5
  * Then, IQR = Q3 – Q1 = 96.5 – 62.5 = 34.0

 **Interquartile range using numpy.median**

 __

 __  
 __

 __

 __  
 __  
 __

# Import the numpy library as np

import numpy as np

 

data = [32, 36, 46, 47, 56, 69, 75, 79,
79, 88, 89, 91, 92, 93, 96, 97, 

 101, 105, 112, 116]

 

# First quartile (Q1)

Q1 = np.median(data[:10])

 

# Third quartile (Q3)

Q3 = np.median(data[10:])

 

# Interquartile range (IQR)

IQR = Q3 - Q1

 

print(IQR)  
  
---  
  
 __

 __

    
    
     **Output:** 34.0

 **Interquartile range using numpy.percentile**

 __

 __  
 __

 __

 __  
 __  
 __

# Import numpy library

import numpy as np

 

data = [32, 36, 46, 47, 56, 69, 75, 79,
79, 88, 89, 91, 92, 93, 96, 97, 

 101, 105, 112, 116]

 

# First quartile (Q1)

Q1 = np.percentile(data, 25, interpolation = 'midpoint')

 

# Third quartile (Q3)

Q3 = np.percentile(data, 75, interpolation = 'midpoint')

 

# Interquaritle range (IQR)

IQR = Q3 - Q1

 

print(IQR)  
  
---  
  
 __

 __

    
    
     **Output:** 34.0

 **Interquartile range using scipy.stats.iqr**

 __

 __  
 __

 __

 __  
 __  
 __

# Import stats from scipy library

from scipy import stats

 

data = [32, 36, 46, 47, 56, 69, 75, 79,
79, 88, 89, 91, 92, 93, 96, 97, 

 101, 105, 112, 116]

 

# Interquartile range (IQR)

IQR = stats.iqr(data, interpolation = 'midpoint')

 

print(IQR)  
  
---  
  
 __

 __

    
    
     **Output:** 34.0

 **Quartile Deviation**  
Quartile deviation is the half of the difference of third quartile (Q3) and
first quartile (Q1) i.e. half of the interquartile range (IQR). **(Q3 – Q1) /
2 = IQR / 2**

 **Decision making**  
The data set having higher value of quartile deviation has higher variability.

 **Quartile deviation using numpy.median**

 __

 __  
 __

 __

 __  
 __  
 __

# import the numpy library as np

import numpy as np

 

data = [32, 36, 46, 47, 56, 69, 75, 79,
79, 88, 89, 91, 92, 93, 96, 97, 

 101, 105, 112, 116]

 

# First quartile (Q1)

Q1 = np.median(data[:10])

 

# Third quartile (Q3)

Q3 = np.median(data[10:])

 

# Interquartile range (IQR)

IQR = Q3 - Q1

 

# Quartile Deviation

qd = IQR / 2

 

print(qd)   
  
---  
  
__

__

    
    
    **Output:** 17.0

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

