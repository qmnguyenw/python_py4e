Pylint module in Python



We often get stuck in the middle or encounter errors when we code/run some
programs. We usually surf the internet for help and make our code run. But how
do we understand the published code on the internet? Some of the typical
answers to this question are docstrings, articles written above that code..,

One of the biggest problems in this era is understanding the other’s programs.
Situations are even worse if there are no explanatory things like comments,
docstrings in the code. As a programmer, we should make our code readable and
understandable.

To address the solution, Python provides a module **pylint**. This article
provides a brief introduction to the **pylint** module and provides tips to
get a good score on my code. Let’s Start.

Pylint is a tool that

  * Lists Errors which comes after execution of that Python code
  * Enforces a coding standard and looks for code smells
  * Suggest how particular blocks can be updated
  * Offer details about the code’s complexity

Pylint tool is similar to **pychecker** , **pyflakes** , **flake8** , and
**mypy**.

  

  

### Installation

To install pylint, make sure Python is installed on your PC. Open the command
prompt(Windows) / terminal(Linux) on your PC and type the following command

    
    
    pip install pylint 

To verify the pylint installation, type the following command

    
    
    pylint --version

You should see pylint “2.4.4” version. We can also verify the installation by
reinstalling the pylint. In that case, if pylint is already installed you
should see **Requirement already satisifed** on your screen.

### Working with Pylint

Consider the following program that accepts two numbers and prints their sum.

 __

 __  
 __

 __

 __  
 __  
 __

a= 1

b = 2

print(a + b)  
  
---  
  
 __

 __

Now save the above program in the file **gfg.py**  
Open your command prompt / terminal and type the following command

    
    
    pylint gfg.py

In the pylint 2.4.4 version, you will get a report as shown below. Messages
might change depending on the version.  
![pylint-python](https://media.geeksforgeeks.org/wp-
content/uploads/20200412171143/gfg156-1.png)

 **Score** for the code given above is -10.0/10.0(Very low). If we get a low
score it doesn’t mean that our code is wrong. The score represents how
good/bad your code is understandable by another programmer. We need to improve
our code by considering the suggestions given in the report.

Each message suggestion/point in the report will be given with a message
format that consists of an ID and its meaning. Each ID starts with an alphabet
and the rest will be numbered. Each alphabet denotes the type of message
object. Some of the message objects are

  

  
S.No| Message Object| Expansion| Explanation| 1.| C| Convention| It is
displayed when the program is not following the standard rules.| 2.| R|
Refactor| It is displayed for bad code smell| 3.| W| Warning| It is displayed
for python specific problems| 4.| E| Error| It is displayed when that
particular line execution results some error| 5.| F| Fatal| It is displayed
when pylint has no access to further process that line.  
---|---|---|---  
  
Let’s discuss some techniques to improve score.

  * ID **C0326** suggest a bad-white space error means we need to give a whitespace between **a** and **=** symbol. This rule is applicable to all declarations where an operator is used immediately after an identifier.
  * ID **C0304** comes under missing-new-line suggestion which means we have to add a blank line when we complete our code.
  * ID **C0114** comes under missing-module-docstring suggestion which means we need to add a docstring at the top which refers to the use of the program written below that.
  * ID **C0103** comes under invalid-name suggestion which can be avoided by writing the identifiers start with a capital letter. But, we usually believe that class names use CamelCasing i.e class names start with an upper-case letter. To avoid this suggestion we will add a regular expression to pylint that actually accepts all the variables in the lowercase letters. We will discuss this more in the further examples.

The modified version of the code is:

 __

 __  
 __

 __

 __  
 __  
 __

'''

This program adds two numbers and displays their results

'''

A = 1

B = 2

print('Sum of Numbers:', A + B)

   
  
---  
  
__

__

If we run the above code using pylint, we will get the following result  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200412173757/gfg221-2.png)

Here we improved our score from -10.0 to 10.0. That’s great. But, is my code
understandable? The answer is **no**. There are some more changes which we
need to specify the pylint module to score our code.

### Changing Invalid Name suggestion

As discussed earlier, the pylint module will use the uppercase naming
convention by default. The regular expression used to identify that uppercase
convention is (([A-Z_][A-Z1-9_]*)|(__.*__))$. We need to add our suggestion
as a regular expression that accepts identifiers starting with lowercase
alphabets. To do that, open your command prompt and execute the following
statement.

    
    
    pylint --const-rgx='[a-z\_][a-z0-9\_]{2, 30}$' filename.py

.  
This will avoid the use of the uppercase convention. We can modify that
permanently by changing rules in **pylint –generate-rcfile** which we will
discuss in future articles.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

