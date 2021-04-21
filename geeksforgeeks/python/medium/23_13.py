stdev() method in Python statistics module



Statistics module in Python provides a function known as **stdev()** ,
which can be used to calculate the standard deviation. stdev() function only
calculates standard deviation from a sample of data, rather than an entire
population.  
To calculate standard deviation of an entire population, another function
known as **pstdev()** is used.

 ** _Standard Deviation_** is a measure of spread in Statistics. It is used to
quantify the measure of spread, variation of a set of data values. It is very
much similar to variance, gives the measure of deviation whereas variance
provides the squared value.

A low measure of Standard Deviation indicates that the data are less spread
out, whereas a high value of Standard Deviation shows that the data in a set
are spread apart from their mean average values. A useful property of the
standard deviation is that, unlike the variance, it is expressed in the same
units as the data.

    
    
    Standard Deviation is calculated by :
    
    ![ {\\displaystyle s = {\\sqrt {\\frac {\\sum _{i=1}^{N}\(x_{i}-{\\overline {x}}\)^{2}}{N-1}}} } ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-5f8955e2080392826fd89458cd55d3d5_l3.png)
    
    where x1, x2, x3.....xn are observed values in sample data,
    ![\\scriptstyle {\\overline {x}}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-ad07f0d53d82215c734a54b5a1f6c016_l3.png) is the mean value of observations and
    N is the number of sample observations.
    

> **Syntax :**

