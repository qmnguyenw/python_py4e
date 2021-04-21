Plotting cross-spectral density in Python using Matplotlib



 **Matlplotlib** is a comprehensive library consisting of modules that are
used for Data Visualization just like MATLAB. Pyplot is a further module which
makes functions and methods executable.

## Plotting Cross-Spectral Density

The cross-spectral density compares two signals, each from different source
taking into account both amplitude and phase difference of the two signals. In
Python, this function is carried out using the Pyplot module’s method
matplotlib.pyplot.csd()

 **Syntax:**

    
    
    matplotlib.pyplot.csd(x, y)

Here, x and y are 1-D arrays or a sequence having the data.

 **Let us take two signals and plot their CSD:**

  

  

  1. Signal 1 has time period from 0 to 1 second and 0.1 radian phase angle with frequency being calculated using sin() function.
  2. Similarly, Signal 2 has time period from 5 to 10 seconds and 0.25 radians phase angle.
  3. Taking these two signals, we plot their cross spectral density.

 **Example 1:** Plotting Signal 1

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import matplotlib.pyplot as plt

 

 

time = np.arange(0, 1, 0.1)

amp = np.sin(time)

 

plt.plot(time, amp)

plt.title("Signal 1")

 

plt.show()  
  
---  
  
 __

 __

 **Output:**

![csd-python-1](https://media.geeksforgeeks.org/wp-
content/uploads/20200511145049/csd-python-1.png)

 **Example 2:** Plotting Signal 2

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import matplotlib.pyplot as plt

 

 

t = np.arange(5, 10, 0.25)

ampl = np.sin(t)

 

plt.plot(t, ampl)

plt.title("Signal 2")

 

plt.show()  
  
---  
  
 __

 __

 **Output:**

![csd-python2](https://media.geeksforgeeks.org/wp-
content/uploads/20200511145859/csd-python2.png)

 **Example 3:** Plotting the cross-spectral density

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import matplotlib.pyplot as plt

 

 

# Signal 1

time = np.arange(0, 1, 0.1)

amp = np.sin(time)

 

# Signal 2

t = np.arange(5, 10, 0.25)

ampl = np.sin(t)

 

# Cross-spectral density

plt.csd(amp, ampl)

 

plt.show()  
  
---  
  
 __

 __

 **Output:**

![cross-spectral-density-python](https://media.geeksforgeeks.org/wp-
content/uploads/20200511150219/cross-spectral-density-python.png)

 **Example 4:** Using discrete lists or arrays

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import matplotlib.pyplot as plt

 

 

a = np.arange(5)

b = np.arange(10, 30)

 

plt.csd(a, b)

plt.show()  
  
---  
  
 __

 __

 **Output:**

![cross-spectral-density-python-2](https://media.geeksforgeeks.org/wp-
content/uploads/20200511150407/cross-spectral-density-python-2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

