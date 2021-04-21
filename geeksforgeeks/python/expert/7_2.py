Python code formatting using Black



Writing good format code is very important, small programs are easy to
understand but as programs complex it get harder and harder to understand at
some point you can’t even understand code written by you. For this, it is
needed to write code in a format that is more readable and here **Black**
comes into play, Black ensure code quality.

#### What is Black?

Linters such as pycodestyle or flake8 show weather your code is according
to PEP8 format, which is official Python style guide. But the promble is this
gives burden to the developers to fix this formatting style. Here Black comes
into play it not only report format errors but also fix them.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20191229125111/Screenshot-from-2019-12-29-12-36-35.png)

To quote the project README:

> Black is the uncompromising Python code formatter. By using it, you agree to
> cede control over minutiae of hand-formatting. In return, Black gives you
> speed, determinism, and freedom from pycodestyle nagging about formatting.
> You will save time and mental energy for more important matters.
>
>  
>
>
>  
>

 **Note:** Black can be easily integrated with many editors such as Vim,
Emacs, VSCode, Atom or a version control system like GIT.

#### Installing and using Black :

Black requires **Python 3.6.0+** with pip installed :

    
    
    $ pip install black

It is very simple to use black. Run the below command in the terminal.

    
    
    $ black [file or directory]

This will reformat your code using the Black codestyle.

 **Example 1:** Let’s create an unformatted file name “sample.py” and we want
to format it using black. Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

def is_unique(

 s

 ):

 s = list(s

 )

 s.sort()

 

 

 for i in range(len(s) - 1):

 if s[i] == s[i + 1]:

 return 0

 else:

 return 1

 

 

if __name__ == "__main__":

 print(

 is_unique(input())

 )  
  
---  
  
 __

 __

After creating this file run the below command.

![python-black](https://media.geeksforgeeks.org/wp-
content/uploads/20191231121250/python-black.png)

 **Output file:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

def is_unique(s):

 s = list(s)

 s.sort()

 

 for i in range(len(s) - 1):

 if s[i] == s[i + 1]:

 return 0

 else:

 return 1

 

 

if __name__ == "__main__":

 print(is_unique(input()))  
  
---  
  
 __

 __

In the above example, both are the same piece code but after using black it is
formatted and thus easy to understand.

 **Example 2:** Let’s create another file “sample1.py” containing the
following code.

 __

 __  
 __

 __

 __  
 __  
 __

def function(name, default=None, *args, variable="1123", a,
b, c, employee, office, d, e, f, **kwargs):

 """This is function is created to demonstrate black"""

 

 

string = 'GeeksforGeeks'

 

j = [1,

 2,

 3]  
  
---  
  
 __

 __

After writing the above command again in the terminal.

![python-black](https://media.geeksforgeeks.org/wp-
content/uploads/20191231123233/python-black-2.png)

 **Output file:**

 __

 __  
 __

 __

 __  
 __  
 __

def function(

 name,

 default=None,

 *args,

 variable="1123",

 a,

 b,

 c,

 employee,

 office,

 d,

 e,

 f,

 **kwargs

):

 """This is function is created to demonstrate black"""

 

 

string = "GeeksforGeeks"

 

j = [1, 2, 3]  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

