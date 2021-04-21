Python | How to make a terminal progress bar using tqdm



Whether you’re installing software, loading a page or doing a transaction, it
always eases your mind whenever you see that small progress bar giving you an
estimation of how long the process would take to complete or render. If you
have a simple progress bar in your script or code, it looks very pleasing to
the eye and gives proper feedback to the user whenever he executes the code.
You can use the Python external library **tqdm** , to create simple & hassle-
free progress bars which you can add in your code and make it look lively!

## Installation

Open your command prompt or terminal and type:

    
    
    pip install tqdm

If you are using Python3 then type:

    
    
    pip3 install tqdm

This command would successfully install the library on your computer and is
now ready to use.

## Usage

Using tqdm is very simple, you just need to add your code between tqdm()
after importing the library in your code. You need to make sure that the code
you put in between the tqdm() function must be iterable or it would not work
at all.

  

  

Let us see the following example that would help you understand better:

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

from tqdm import tqdm

 

 

for i in tqdm(range(int(9e6))):

 pass  
  
---  
  
 __

 __

 **Output:**

![python-tqdm](https://media.geeksforgeeks.org/wp-
content/uploads/20200302215050/woring_1_geeks.jpg)

Now that we know how to implement tqdm, let’s take a look at some of the
important parameters it offers and how it can be used to tweak the progress
bar.

 ****

* desc:

