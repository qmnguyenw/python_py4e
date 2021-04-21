Stem and Leaf Plots in Python



Stem and Leaf Plot is a way of representing the data. This plot is used to
show the absolute frequency in different classes similar to the frequency
distribution table or a histogram. It presents the quantitative data in the
graphical format, and the stem-and-leaf plot of quantitative data is said as
textual graph as that presents the data according to their most significant
numeric digit. Stem and Leaf Plot graph is mainly suitable for smaller data
sets.

Stem-and-leaf plot is a tabular presentation where each data value is split
into a “stem” (the first digit or digits) and a “leaf” (usually the last
digit).

 **Interpretations:**

    
    
    "17" is split into "1" (stem) and "7" (leaf)
    "69" is split into "6" (stem) and "9" (leaf)

 **Procedure to make stem-and-leaf plot:**

  1. Separate each observation/data into a stem which will consist of all except rightmost digit and leaf, the rightmost digit.
  2. Leaf must have only one digit while stem can have as many digits as possible.
  3. Write the stem in a vertical column with smallest at the top(but in Python, you will get largest at the top) then draw a vertical line by the right of this column.
  4. Write each corresponding leaf in the row to the right of its stem just after the vertical line, in ascending order out from the stem.

 **Example:**

  

  

Let’s say there are 10 Technical Content Writers at GeeksforGeeks. Each of
them submitted 100 articles  
to publish at the site. Out of 100 articles, the number of articles which had
some errors are given below for each 10 content writers –

    
    
    16, 25, 47, 56, 23, 45, 19, 55, 44, 27

 **Stem-and-leaf plot will be –**

    
    
    1 | 69
    2 | 357
    4 | 457
    5 | 56

 **Plot in Python using stemgraphic module –**  
To plot stem-and-leaf plot in Python, we need to install the
<strong>stemgraphic

