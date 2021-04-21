Print Colors in Python terminal



There are several methods to output colored text to the terminal, in
Python.The most common ways to do are:

 **Using built-in modules**

  1.  **‘colorama’ module :** Cross-platform printing of colored text can then be done using Colorama’s constant shorthand for ANSI escape sequences:  
 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# red text with green background

 

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')

print(Back.GREEN + 'and with a green background')

print(Style.DIM + 'and in dim text')

print(Style.RESET_ALL)

print('back to normal now')  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20201022165532/4101.png)

 **Example 2:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# green text with red background

 

from colorama import init

from termcolor import colored

 

init()

 

print(colored('Hello, World!', 'green', 'on_red'))  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20201022170020/4112.png)

  2.  **‘termcolor’ module :** termcolor is a python module for ANSII Color formatting for output in terminal.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# colored text and background

import sys

from termcolor import colored, cprint

 

text = colored('Hello, World!', 'red', attrs=['reverse',
'blink'])

print(text)

cprint('Hello, World!', 'green', 'on_red')

 

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')

print_red_on_cyan('Hello, World!')

print_red_on_cyan('Hello, Universe!')

 

for i in range(10):

 cprint(i, 'magenta', end=' ')

 

cprint("Attention!", 'red', attrs=['bold'],
file=sys.stderr)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/wgrwef-1024x592.jpg)

 **Using ANSI Escape Codes**

The most common way to print colored text is by printing ANSI escape sequences
directly. This can be delivered in different formats such as:

  1.  **Build Functions to call :** We can build functions to call particular color named functions to execute the relevant ANSI Escape Sequence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# colored text and background

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

def prLightPurple(skk): print("\033[94m {}\033[00m"
.format(skk))

def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

def prLightGray(skk): print("\033[97m {}\033[00m"
.format(skk))

def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

 

prCyan("Hello World, ")

prYellow("It's")

prGreen("Geeks")

prRed("For")

prGreen("Geeks")  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/sjdvfg-1024x508.jpg)

  2.  **Build a class of colors :** Create a class to allot background and foreground colors and call them.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# colored text and background

class colors:

'''Colors class:reset all colors with colors.reset; two 

sub classes fg for foreground 

and bg for background; use as colors.subclass.colorname.

i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable, 

underline, reverse, strike through,

and invisible work with the main class i.e. colors.bold'''

 reset='\033[0m'

 bold='\033[01m'

 disable='\033[02m'

 underline='\033[04m'

 reverse='\033[07m'

 strikethrough='\033[09m'

 invisible='\033[08m'

 class fg:

 black='\033[30m'

 red='\033[31m'

 green='\033[32m'

 orange='\033[33m'

 blue='\033[34m'

 purple='\033[35m'

 cyan='\033[36m'

 lightgrey='\033[37m'

 darkgrey='\033[90m'

 lightred='\033[91m'

 lightgreen='\033[92m'

 yellow='\033[93m'

 lightblue='\033[94m'

 pink='\033[95m'

 lightcyan='\033[96m'

 class bg:

 black='\033[40m'

 red='\033[41m'

 green='\033[42m'

 orange='\033[43m'

 blue='\033[44m'

 purple='\033[45m'

 cyan='\033[46m'

 lightgrey='\033[47m'

 

print(colors.bg.green, "SKk", colors.fg.red, "Amartya")

print(colors.bg.lightgrey, "SKk", colors.fg.red, "Amartya")  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/ewe-1024x179.jpg)

  3.  **Iterating functions :** We can design iterating & self generating ANSI Escape sequence, functions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# colored text and background

def print_format_table():

 """

 prints table of formatted text format options

 """

 for style in range(8):

 for fg in range(30, 38):

 s1 = ''

 for bg in range(40, 48):

 format = ';'.join([str(style), str(fg), str(bg)])

 s1 += '\x1b[%sm %s \x1b[0m' % (format, format)

 print(s1)

 print('\n')

 

print_format_table()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/adfesfw-1024x394.jpg)

This article is contributed by **Amartya Ranjan Saikia**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

