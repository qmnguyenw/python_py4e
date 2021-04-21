Python | Percentage increase in hemisphere volume if radius is increased



Given that the radius of a hemisphere is increased by a fixed percentage so,
the target is to calculate the percentage increase in the volume of the
hemisphere.

>  **Examples:**  
>  **Input :**  
>  20  
>  **Output :**  
>  72.8 %
>
>  **Input :**  
>  70  
>  **Output :**  
>  391.3 %

 **Approach:**  
Let, the radius of the hemisphere = ![a](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-7c040e8debfcd59c929ba6521698aa6d_l3.png)  
Given percentage increase = ![x%](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d249f9496e6617adcd81613c9839328e_l3.png)  
Volume before increase = ![\\frac{2}{3} *
3.14*a^3](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1036e264d32233aa481a57fc73219332_l3.png)  
New radius after increase = ![a +
\\frac{ax}{100}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-3eb19befa89097e034bc3a2386d8f8d2_l3.png)  
So, new volume = ![\\frac{2}{3}*3.14*\(a^3 + \(\\frac{ax}{100}\)^3 +
\\frac{3a^3x}{100} +
\\frac{3a^3x^2}{10000}\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-575e979345b55ae136e8a221da072ee2_l3.png)  
Change in volume = ![\\frac{2}{3}*3.14*\(\(\\frac{ax}{100}\)^3 +
\\frac{3a^3x}{100} +
\\frac{3a^3x^2}{10000}\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-404dc538c54a0c73e30b852805390987_l3.png)  
Percentage increase in volume = ![\(\\frac{2}{3}*3.14*\(\(\\frac{ax}{100}\)^3
+ \\frac{3a^3x}{100} + \\frac{3a^3x^2}{10000}\)/\\frac{2}{3}*3.14*a^3\) * 100
= \\frac{x^3}{10000} + 3x +
\\frac{3x^2}{100}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-b389aec781ebcad0619b2cbb6c1b0e8b_l3.png)

**Below is the Python code implementation of the above mentioned approach.**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find percentage increase

# in the volume of the hemisphere 

# if the radius is increased by a given percentage 

 

def newvol(x): 

 

 print("percentage increase in the volume of the"

 " hemisphere is ", pow(x, 3) / 10000 + 3 * x 

 + (3 * pow(x, 2)) / 100, "%") 

 

# Driver code 

x = 10.0

newvol(x)   
  
---  
  
__

__

**Output :**

    
    
    percentage increase in the volume of the hemisphere is  33.1 %

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

