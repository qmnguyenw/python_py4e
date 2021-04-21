Python PIL | ImageDraw.Draw.text()



  
PIL is the Python Imaging Library which provides the python interpreter with
image editing capabilities. The ImageDraw module provide simple 2D graphics
for Image objects. You can use this module to create new images, annotate or
retouch existing images, and to generate graphics on the fly for web use.

 **ImageDraw.Draw.text()** Draws the string at the given position.

>  **Syntax:**  
>  ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None, spacing=0,
> align=”left”)
>
>  **Parameters:**  
>  **xy** – Top left corner of the text.  
>  **text** – Text to be drawn. If it contains any newline characters, the
> text is passed on to multiline_text()  
>  **fill** – Color to use for the text.  
>  **font** – An ImageFont instance.  
>  **spacing** – If the text is passed on to multiline_text(), the number of
> pixels between lines.  
>  **align** – If the text is passed on to multiline_text(), “left”, “center”
> or “right”.
>
>  **Return Type:**  
>  returns an image with text.
>
>  
>
>
>  
>

 **Image Used:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190829231116/rose2.jpg)

 **Code : Using PIL | ImageDraw.Draw.text()**

 __

 __  
 __

 __

 __  
 __  
 __



 

# Importing Image and ImageFont, ImageDraw module from PIL package 

from PIL import Image, ImageFont, ImageDraw 

 

# creating a image object 

image = Image.open(r'C:\Users\System-Pc\Desktop\rose.jpg') 

 

draw = ImageDraw.Draw(image) 

 

# specified font size

font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf',
20) 

 

text = 'LAUGHING IS THE \n BEST MEDICINE'

 

# drawing text size

draw.text((5, 5), text, font = font, align ="left") 

 

image.show()   
  
---  
  
__

__

**Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190829232351/roseoutput1.png)

 **Another Example:** Here we changing parameter.

 **Image Used:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190829233745/flower2.jpg)

 **Code : Using PIL | ImageDraw.Draw.text()**

 __

 __  
 __

 __

 __  
 __  
 __



 

# Importing Image and ImageFont, ImageDraw module from PIL package 

from PIL import Image, ImageFont, ImageDraw 

 

# creating a image object 

image = Image.open(r'C:\Users\System-Pc\Desktop\flower.jpg') 

 

draw = ImageDraw.Draw(image) 

 

# specified font size

font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf',
20) 

 

text = 'LAUGHING IS THE \n BEST MEDICINE'

 

# drawing text size

draw.text((5, 5), text, fill ="red", font = font, align
="right") 

 

image.show()   
  
---  
  
__

__

**Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190829234040/floweroutput1.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

