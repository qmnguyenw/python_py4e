Matplotlib.pyplot.rcdefaults() in Python



 **Matplotlib** is a library in Python and it is numerical – mathematical
extension for NumPy library. **Pyplot** is a state-based interface to a
**Matplotlib** module which provides a MATLAB-like interface. There are
various plots which can be used in Pyplot are Line Plot, Contour, Histogram,
Scatter, 3D Plot, etc.

## matplotlib.pyplot.rcdefaults() Function

The **rcdefaults() function** in pyplot module of matplotlib library is used
to restore the rc params from Matplotlib’s internal default style.

>  **Syntax:** matplotlib.pyplot.rcdefaults()
>
>  **Parameters:** This method does not accepts any parameter.
>
>  **Returns:** This method does not return any value.
>
>  
>
>
>  
>

Below examples illustrate the matplotlib.pyplot.rcdefaults() function in
matplotlib.pyplot:

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# implementation of the matplotlib function

import matplotlib.pyplot as plt

 

plt.subplot(211)

plt.rc('font', weight ='bold')

plt.rc('xtick.major', size = 5, pad = 7)

plt.rc('xtick', labelsize = 15)

plt.plot([1, 2, 3])

 

plt.text(0.4, 3.5, 'matplotlib.pyplot.rcdefaults() Example')

 

plt.rcdefaults()

plt.subplot(212)

plt.plot([1, 2, 3])

plt.grid(True)

 

plt.show()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200408232419/rcd1.jpg)

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# implementation of the matplotlib function

import matplotlib.pyplot as plt

import numpy as np

 

np.random.seed(19680801)

 

plt.rcdefaults()

fig, ax = plt.subplots()

 

people = ('Geek1', 'Geek2', 'Geek3', 'Geek4',
'Geek5')

y_pos = np.arange(len(people))

performance = 3 + 5 * np.random.rand(len(people))

error = np.random.rand(len(people))

 

ax.bar(y_pos, performance, xerr = error, align ='center')

ax.set_yticks(y_pos)

ax.set_yticklabels(people)

ax.invert_yaxis()

plt.grid(True)

 

plt.title('matplotlib.pyplot.rcdefaults() Example')

plt.show()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200408232421/rcd2.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

