Add CSS to the Jupyter Notebook using Pandas



In Jupyter Notebook, when we print the output table of our data, it shows a
very basic table containing the data. But what if we want to customize this
default style? In this article, we will see how we can add styles to our
output data table.

This is how a default data table looks like in Jupyter Notebook:

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

 

df = pd.DataFrame({'A':[1, 2, 3, 4, 5, 6,
7, 8], 

 'B':[1, 2, 3, 4, 5, 6, 7, 8], 

 'C':[1, 2, 3, 4, 5, 6, 7, 8],

 'D':[1, 2, 3, 4, 5, 6, 7, 8]})

 

df.head()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20191128230704/table16.jpg)

Now let’s try to change the style. We can do it by the **set_table_styles**
method of pandas module.

    
    
    df.style.set_table_styles()

Now we need to pass the ‘selectors’ and ‘props’ as argument to this method,
i.e. we need to select the CSS tags of the table (eg: th, td etc) and change
the values of their properties (eg: background, font-color, font-family etc).

  

  

So, if we need to change the font-family of the text in the data section of
the table, we can do it like this:

 __

 __  
 __

 __

 __  
 __  
 __

df.style.set_table_styles(

 

[{'selector': 'td',

 'props': [('font-family', 'Sans-serif')]},

])  
  
---  
  
 __

 __

  
Let’s try to add more changes and see the output.

 __

 __  
 __

 __

 __  
 __  
 __

df= pd.DataFrame({'A':[1, 2, 3, 4, 5, 6,
7, 8], 

 'B':[1, 2, 3, 4, 5, 6, 7, 8], 

 'C':[1, 2, 3, 4, 5, 6, 7, 8],

 'D':[1, 2, 3, 4, 5, 6, 7, 8],

 'E':[1, 2, 3, 4, 5, 6, 7, 8]})

 

 

df.style.set_table_styles(

[

 {'selector': 'th',

 'props': [('background', '# 606060'), 

 ('color', 'white'), ]},

 {'selector': 'td',

 'props': [('color', 'blue')]},

])  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20191128232308/table21.jpg)

We can also hide the index column by **hide_index()** method:

 __

 __  
 __

 __

 __  
 __  
 __

df.style.set_table_styles(

[

 {'selector': 'th',

 'props': [('background', '# 606060'), 

 ('color', 'yellow'), ]},

 {'selector': 'td',

 'props': [('color', 'red')]},

]

).hide_index()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20191128232627/table32.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

