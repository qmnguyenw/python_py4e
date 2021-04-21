Python | Numpy np.hermegrid2d() method



With the help of **np.hermegrid2d()** method, we can evaluate a 2-D hermite
series on cartesian product of (x, y), where (x, y) is defined in the
np.hermegrid2d() method.

>  **Syntax :** np.hermegrid2d(x, y, series)  
>  **Return :** Return the evaluated 2-D hermite series.

 **Example #1 :**  
In this example we can see that by using np.hermegrid2d() method, we are
able to evaluate the 2-D hermite series on cartesian product of x and y by
using this method.

 __

 __  
 __

 __

 __  
 __  
 __

# import numpy and hermegrid2d

import numpy as np

from numpy.polynomial.hermite_e import hermegrid2d

 

series = np.array([[1, 2, 3, 4], [5, 6, 7,
8]])

# using np.hermegrid2d() method

gfg = hermegrid2d(3, 4, series)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> 1912.0
>
>  
>
>
>  
>

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import numpy and hermegrid2d

import numpy as np

from numpy.polynomial.hermite_e import hermegrid2d

 

series = np.array([[1, 2, 3, 4], [5, 6, 7,
8]])

# using np.hermegrid2d() method

gfg = hermegrid2d([2, 3], [5, 6], series)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> [[2689. 4650.]  
> [3772. 6520.]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

