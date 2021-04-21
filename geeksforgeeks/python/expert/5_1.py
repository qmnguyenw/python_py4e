Optparse module in Python



 **Optparse** module makes easy to write command-line tools. It allows
argument parsing in the python program.

  *  **optparse** make it easy to handle the command-line argument.
  * It comes default with python.
  * It allows dynamic data input to change the output  

**Code: Creating an OptionParser object.**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import optparse

parser = optparse.OptionParser()  
  
---  
  
 __

 __

 **Defining options:**

It should be added one at a time using the **add_option()**. Each Option
instance represents a set of synonymous command-line option string.

  

  

Way to create an Option instance are:

> OptionParser. **add_option** ( _option_ )
>
> OptionParser. **add_option** ( _*opt_str, attr=value, .._.)

To define an option with only a short option string:

    
    
     parser.add_option("-f", attr=value, ....)
    

And to define an option with only a long option string:

    
    
    parser.add_option("--foo", attr=value, ....)
    

**Standard Option Actions:**

>   *  **“store”:** store this option’s argument (default).
>   *  **“store_const”:** store a constant value.
>   *  **“store_true”:** store True.
>   *  **“store_false”:** store False.
>   *  **“append”:** append this option’s argument to a list.
>   *  **“append_const”:** append a constant value to a list.
>

 **Standard Option Attributes:**

>   *  **Option.action:** (default: “store”)
>   *  **Option.type:** (default: “string”)
>   *  **Option.dest:** (default: derived from option strings)
>   *  **Option.default:** The value to use for this option’s destination if
> the option is not seen on the command line.
>

###

Here’s an example of using optparse module in a simple script:

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import OptionParser class

# from optparse module.

from optparse import OptionParser

 

# create a OptionParser

# class object

parser = OptionParser()

 

# ass options

parser.add_option("-f", "--file",

 dest = "filename",

 help = "write report to FILE", 

 metavar = "FILE")

parser.add_option("-q", "--quiet",

 action = "store_false", 

 dest = "verbose", default = True,

 help = "don't print status messages to stdout")

 

(options, args) = parser.parse_args()  
  
---  
  
 __

 __

With these few lines of code, users of your script can now do the “usual
thing” on the command-line, for example:

    
    
    <yourscript> --file=outfile -q
    
    

#### Lets, understand with an example:

 **Code:** Writing python script for print table of n.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import optparse module

import optparse

 

# define a function for 

# table of n

def table(n, dest_cheak):

 for i in range(1,11):

 tab = i*n

 

 if dest_cheak:

 print(tab)

 

 return tab

 

# define a function for 

# adding options

def Main():

 # create OptionParser object

 parser = optparse.OptionParser()

 

 # add options

 parser.add_option('-n', dest = 'num',

 type = 'int', 

 help = 'specify the n''th table number to output')

 parser.add_option('-o', dest = 'out',

 type = 'string', 

 help = 'specify an output file (Optional)')

 parser.add_option("-a", "--all", 

 action = "store_true",

 dest = "prin", 

 default = False,

 help = "print all numbers up to N")

 

 (options, args) = parser.parse_args()

 if (options.num == None):

 print (parser.usage)

 exit(0)

 else:

 number = options.num

 

 # function calling

 result = table(number, options.prin)

 

 print ("The " + str(number)+ "th table is " +
str(result))

 

 if (options.out != None):

 # open a file in append mode

 f = open(options.out,"a")

 

 # write in the file

 f.write(str(result) + '\n')

 

# Driver code

if __name__ == '__main__':

 

 # function calling

 Main()  
  
---  
  
 __

 __

**Output:**

    
    
    python file_name.py -n 4
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200716211815/n-660x171.png)

    
    
    python file_name.py -n 4 -o
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200716212007/filecode-660x143.png)

file.txt created

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200716212045/Screenshot16-660x147.png)

    
    
    python file_name.py -n 4 -a
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200716212333/a-660x394.png)

For knowing more about this module click here.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

