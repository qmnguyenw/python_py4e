Markdown cell in Jupyter notebook



**Jupyter Notebook** (formerly IPython Notebook) is a web-based interactive
computational environment for creating Jupyter notebook documents. Markdown is
a light weight and popular Markup language which is a writing standard for
data scientists and analysts. It is often converted into the corresponding
HTML by which the Markdown processor allows it to be easily shared between
different devices and people. In this tutorial, you’ll learn how to use and
write with different markup tags using Jupyter Notebook.

In this tutorial you will learn how to use the following :

  * Headings
  * Colored note boxes
  * Indented block
  * Bullets
  * Monospace font
  * Embedded code
  * Mathematical symbols and LaTeX equations
  * Line Break
  * Bold and Italic text
  * Horizontal lines
  * Geometric shapes
  * Ordered and Unordered lists
  * Internal and external links
  * Table
  * Image
  * GitHub flavored markdown

## Activating a Markdown cell

Text can be added to Jupyter Notebooks using Markdown cells. You can change
the cell type to Markdown by using the Cell menu, the toolbar, or the key
shortcut **m**. Markdown is a popular markup language that is a superset of
**HTML**. It can be activated in Jupyter notebook as follows :

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721101853/Screenshot241.png)

select the markdown option from the tab above.

### Headings

You can add headings by starting a line with one (or multiple) ‘#’ followed by
a space, as in the following example:

  

  

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803095123/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200720172732/Screenshot222.png)

Use the required heading according to the context

Headings can also be used with “<h1> heading here <h1>” tag.

### Colored note boxes

Use the div tags to create a colored note box. Not all markdown code works
within a div tag, so review your colored boxes carefully! For example, to make
a word bold, surround it with <b>text</b> instead of two asterisks or
underscores.

 **Note boxes :** Use blue boxes for tips and notes. If it’s a note you don’t
have to include the word “Note”.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803095330/jupyterr.PNG)

  

  

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200720172925/Screenshot233.png)

This is a note markdown cell

 **Example boxes :** Use yellow boxes for examples that are not inside code
cells, or use for mathematical formulas if needed.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803095437/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200720173146/Screenshot235.png)

This is an example markdown cell

 **Warning boxes :** Try to avoid warning boxes as much as possible.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803095540/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200720173541/Screenshot237.png)

This is a warning markdown cell

 **Success boxes :** Use green boxes(or success boxes) in a restricted or
infrequent manner. For example, if you have a lot of related content to link
to, maybe you decide to use green boxes for related links from each section of
a notebook.

**Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803095631/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721103013/Screenshot243.png)

This is a success markdown cell

### Indenting

Use a greater than sign “>” and then a space, then type the text. Everything
is indented until the next carriage return.

use ‘>’ * x times. where x is the number of times you want to indent the given
text.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803095718/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721112657/Screenshot245.png)

Example of a nested indented bolck

They can also be obtained with <blockquote>text</blockquote>

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803095814/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721112956/Screenshot247.png)

Example of a block quote using <blockquote> tag

### Bullets

Use the dash sign “- ” with two spaces after it or a space, a dash, and a
space ” – “, to create a circular bullet. To create a sub bullet, use a tab
followed a dash and two spaces. You can also use an asterisk(“*”) instead of a
dash, and it works the same.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803095918/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721114028/Screenshot249.png)

Example of circular, square and sub-bullets

### Monospacefont

Surround text with a back single quotation mark (  ). Use monospace for file
path and file names and for text users enter or message text users see.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803100003/jupyterr-200x22.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721115442/Screenshot251.png)

Example of a monospace font

### Embedded code

You can embed code meant for illustration instead of execution in Python:

The Code section is the part that specifies the code of different programming
languages and can be rendered where inline code starts with ‘ inline code
goes here ‘ back-ticks around it, but the block of code starts with three
back-ticks ‘ “ block line code goes here “ ‘. Also, the Markup tag for a
Code section is ‘ <code>code goes here<code> ‘.

 **Input :**

Using Markdown

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803100052/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721115816/Screenshot253.png)

Using markdown to represent python code section

 **Input :**

Using Markup tags

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803100142/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721120343/Screenshot255.png)

Using markup tags to represent python code

###  **Mathematical symbol and LaTeX equations**

The mathematical symbol in Markdown is included in ‘$ mathematical expression
goes here $’ enclosed in a dollar symbol and in Markup you can follow this
link for more detail: Mathematical Operators. You can see the example of using
the mathematical symbols below.

Use this code: $ mathematical symbols $. You can include mathematical
expressions both inline: **ei?+1=0** and displayed:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721093622/Screenshot239.png)

Expression in a separate line

Inline expressions can be added by surrounding the latex code with $:

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803100226/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721120913/Screenshot258.png)

This is an inline representation of math expression

Expressions on their own line are surrounded by $$:

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803100321/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721093622/Screenshot239.png)

this is a outline representation of math expression

###  **Line Break**

The line break tag starts with <br> tag with no closing tag which breaks the
line, and the remaining contents begin with a new line with the example shown
below.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803100406/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721121539/Screenshot260.png)

“br tags and it is awesome” appears in a new line.”

###  **Bold and Italic text**

You can use **< b>** tags, **‘**’** i.e. ‘double asterisk’ or **‘__’** i.e.
‘double underscore’ to get bold text with the following syntax.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803100501/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721121910/Screenshot263.png)

Example of bold text.

You can use **< i>** tags, **‘*’** i.e., single asterisk or **‘_’** i.e.,
single underscore to get the italic text for the following syntax. Don’t leave
a space between the asterisk and the text because it counts as a bullet.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803101356/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721122057/Screenshot263.png)

Example of italic text

###  **Horizontal lines**

You can obtain a horizontal line by using Markdown ‘—‘ three hyphens or Markup
tags <hr>

Both of the syntaxes above will render the horizontal line across from one end
to another end after clicking “Run”.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803101432/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200721122242/Screenshot265.png)

Example of horizontal lines

###

### Ordered and Unordered lists

 **Ordered lists :**

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803101620/jupyterr.PNG)

or

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803101706/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200725145136/Screenshot302.png)

This is an example of an ordered list

 **Unordered lists :** The Unordered list is a bullet list which is obtained
by using the <ul> tag and ending with the </ul> tag, see the example below:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803101903/jupyterr.PNG)

Alternatively, the Unordered list can start with the ‘-‘ symbol with space,
which gives the black circle symbol and can also start with the ‘*’ symbol
with space, which gives the black square symbol.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803102003/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200725145512/Screenshot304.png)

This is an example of unordered list

###  **Internal and External Links**

 **Internal link :** The id defined above can be linked to the section of the
notebook by following the code which makes the link clickable.

 **[Section title](#division_ID)**

The example of the above can be seen below where the id defined is linked with
the section and clickable link obtained after clicking “Run” in the toolbar.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803102051/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200725145940/Screenshot307.png)

This is an internal link

or

Internal Link in Markdown starts with <a> tag with unique id defined by the
attribute ‘id’ which can be linked in the notebook with the example below :

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803102157/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200725150254/Screenshot307.png)

Internal link using <a></a> tag

 **External links :** External Link in Markdown starts with <a> and ends with
<a> tag, i.e., <a> stands for the anchor which defines the link, and it has
attribute ‘href’ also called as hyper reference which contains the destination
address of the link or URL and texts between tags is visible and is clickable
to open the destination address as shown below.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803102256/jupyterr.PNG)

Alternatively, it could also start with the __(URL for the site)__ where the
double underscore is on both sides with the text link enclosed in a square
bracket and the URL for the site is enclosed in a parenthesis followed by the
URL.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803102355/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200725151817/Screenshot309.png)

Example of an external link

### Table

The Table contains the information in rows and columns and is built by the
combination of ‘|’ i.e. ‘vertical pipe’ to separate each column and ‘-‘ i.e.,
hyphen symbol to create the header where the blank line, i.e., a combination
of vertical pipe and dashes to render the table format.

Also, you can vary the cells by roughly aligning with the columns, and the
notebook will automatically resize the content in the given cell.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803102442/jupyterr.PNG)

Alternatively, the Markdown can be used to build tables where < table > is
used to define a table with its width in percentages.<tr> sets table row which
gives the bold with centered text along with table heading is described by
<th> is at the top of the table with the other entries in the table are set by
the <td> i.e., table data tag.

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803102552/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200725152543/Screenshot311.png)

Example of a table

### Image

You can insert an image from the toolbar by choosing the ‘Insert Image’ from
an Edit menu and can browse the required image as shown below.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200725152931/Screenshot313LI.jpg)

Inserting an image using Toolbar

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200725153434/Screenshot315.png)

choose a file from your PC

or you can also insert an image using <img> tag :

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803102654/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200725153834/Screenshot317.png)

inserting a image using <img> tag

### GitHub flavored markdown

The Notebook webapp supports Github flavored markdown meaning that you can use
triple backticks for code blocks :

 **Input :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200803102754/jupyterr.PNG)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200725155020/Screenshot319.png)

This is GitHub flavored markdown

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

