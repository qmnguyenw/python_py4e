Matplotlib.pyplot.savefig() in Python



Matplotlib is highly useful visualization library in Python. It is a multi-
platform data visualization library built on NumPy arrays and designed to work
with the broader SciPy stack. Visualization plays a very important role as it
helps us to understand huge chunks of data and extract knowledge.

## Matplotlib.pyplot.savefig()

As the name suggests savefig() method is used to save the figure created after
plotting data. The figure created can be saved to our local machines by using
this method.

>  **Syntax:** savefig(fname, dpi=None, facecolor=’w’, edgecolor=’w’,
> orientation=’portrait’, papertype=None, format=None, transparent=False,
> bbox_inches=None, pad_inches=0.1, frameon=None, metadata=None)

 **Parameters:** PARAMETERS| DESCRIPTION| fname| Filename .png for image, .pdf
for pdf format.  
File location can also be specified here.| dpi| Number of dots per
inch.(picture quality)| papertype| Paper type could be “a0 to a10”,
“executive”,  
“b0 to b10”, “letter”, “legal”, “ledger”.| format| File format such as .png,
.pdf.| facecolor and edgecolor| Default as White.| bbox_inches| Set it as
“tight” for proper fit of the saved figure.| pad_inches| Padding around the
saved figure.| transparent| Makes background of the picture transparent.|
Orientation| Landscape or Portrait.  
---|---  
  
 **Example 1:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing required modules

import matplotlib.pyplot as plt

 

# creating plotting data

xaxis =[1, 4, 9, 16, 25, 36, 49, 64,
81, 100]

yaxis =[1, 2, 3, 4, 5, 6, 7, 8, 9,
10]

 

# plotting 

plt.plot(xaxis, yaxis)

plt.xlabel("X")

plt.ylabel("Y")

 

# saving the file.Make sure you 

# use savefig() before show().

plt.savefig("squares.png")

 

plt.show()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200520101906/squaresedit.png)

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing the modules

import matplotlib.pyplot as plt

 

 

# creating data and plotting a histogram

x =[1, 4, 9, 16, 25, 36, 49, 64, 81,
100]

plt.hist(x)

 

# saving the figure.

plt.savefig("squares1.png",

 bbox_inches ="tight",

 pad_inches = 1,

 transparent = True,

 facecolor ="g",

 edgecolor ='w',

 orientation ='landscape')

 

plt.show()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200520101712/squares1edit.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

