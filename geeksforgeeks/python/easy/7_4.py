Wand function() function in Python



 **function()** function is similar to evaluate function. In **function()**
function pixel channels can be manipulated by applis a multi-argument function
to pixel channels.  
Following are the list of FUNCTION_TYPES in Wand:

  * ‘undefined’
  * ‘arcsin’
  * ‘arctan’
  * ‘polynomial’
  * ‘sinusoid’

>  **Syntax :**
>  
>
>     wand.image.function(function, arguments, channel)
>  
>
> **Parameters :** Parameter| Input Type| Description| function|
> collections.abc.Sequence| a sequence of doubles to apply against function|
> arguments| numbers.Real| Number to calculate with operator| channel|
> basestring| Optional channel to apply operation on.  
> ---|---|---  
  
 **Example 1:**

 **Source Image:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200329231051/koala-300x225.jpeg)

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Import Image from wand.image module

from wand.image import Image

 

frequency = 3

phase_shift = -90

amplitude = 0.2

bias = 0.7

 

# Read image using Image function

with Image(filename ="koala.jpeg") as img:

 # appying sinusoid FUCTION_TYPE

 img.function('sinusoid', [frequency, phase_shift, amplitude, bias])

 img.save(filename ="kl-functioned.jpeg")  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200424143201/kl-
functioned-300x225.jpeg)

 **Example 2:**

 **Sorce Image:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200330142032/road-285x300.jpeg)

 __

 __  
 __

 __

 __  
 __  
 __

# Import Image from wand.image module

from wand.image import Image

 

frequency = 3

phase_shift = -90

amplitude = 0.2

bias = 0.7

 

# Read image using Image function

with Image(filename ="road.jpeg") as img:

 # appying sinusoid FUCTION_TYPE

 img.function('polynomial', [frequency, phase_shift, amplitude, bias])

 img.save(filename ="rd-functioned.jpeg")  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200424143704/rd-
functioned1-285x300.jpeg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

