Python | Reading contents of PDF using OCR (Optical Character Recognition)



Python is widely used for analyzing the data but the data need not be in the
required format always. In such cases, we convert that format (like PDF or JPG
etc.) to the text format, in order to analyze the data in better way. Python
offers many libraries to do this task.

There are several ways of doing this, including using libraries like PyPDF2 in
Python. The major disadvantage of using these libraries is the encoding
scheme. PDF documents can come in a variety of encodings including UTF-8,
ASCII, Unicode, etc. So, converting the PDF to text might result in the loss
of data due to the encoding scheme.

Let’s see how to read all the contents of a PDF file and store it in a text
document using OCR.

Firstly, we need to convert the pages of the PDF to images and then, use OCR
(Optical Character Recognition) to read the content from the image and store
it in a text file.

 **Required Installations:**

  

  

    
    
    pip3 install PIL
    pip3 install pytesseract
    pip3 install pdf2image
    sudo apt-get install tesseract-ocr

There are two parts to the program.

 **Part #1** deals with converting the PDF into image files. Each page of the
PDF is stored as an image file. The names of the images stored are:  
PDF page 1 -> page_1.jpg  
PDF page 2 -> page_2.jpg  
PDF page 3 -> page_3.jpg  
….  
PDF page n -> page_n.jpg

 **Part #2** deals with recognizing text from the image files and storing it
into a text file. Here, we process the images and convert it into text. Once
we have the text as a string variable, we can do any processing on the text.
For example, in many PDFs, when a line is completed, but a particular word
cannot be written entirely in the same line, a hyphen (‘-‘) is added, and the
word is continued on the next line. For example –

    
    
    This is some sample text but this parti-  
    
    cular word could not be written in the same line.

Now for such words, a fundamental pre-processing is done to convert the hyphen
and the new line into a full word. After all the pre-processing is done, this
text is stored in a separate text file.

To get the input PDF files used in the code, click d.pdf

Below is the implementation:

 __

 __  
 __

 __

 __  
 __  
 __

# Import libraries

from PIL import Image

import pytesseract

import sys

from pdf2image import convert_from_path

import os

 

# Path of the pdf

PDF_file = "d.pdf"

 

'''

Part #1 : Converting PDF to images

'''

 

# Store all the pages of the PDF in a variable

pages = convert_from_path(PDF_file, 500)

 

# Counter to store images of each page of PDF to image

image_counter = 1

 

# Iterate through all the pages stored above

for page in pages:

 

 # Declaring filename for each page of PDF as JPG

 # For each page, filename will be:

 # PDF page 1 -> page_1.jpg

 # PDF page 2 -> page_2.jpg

 # PDF page 3 -> page_3.jpg

 # ....

 # PDF page n -> page_n.jpg

 filename = "page_"+str(image_counter)+".jpg"

 

 # Save the image of the page in system

 page.save(filename, 'JPEG')

 

 # Increment the counter to update filename

 image_counter = image_counter + 1

 

'''

Part #2 - Recognizing text from the images using OCR

'''

 3

# Variable to get count of total number of pages

filelimit = image_counter-1

 

# Creating a text file to write the output

outfile = "out_text.txt"

 

# Open the file in append mode so that 

# All contents of all images are added to the same file

f = open(outfile, "a")

 

# Iterate from 1 to total number of pages

for i in range(1, filelimit + 1):

 

 # Set filename to recognize text from

 # Again, these files will be:

 # page_1.jpg

 # page_2.jpg

 # ....

 # page_n.jpg

 filename = "page_"+str(i)+".jpg"

 

 # Recognize the text as string in image using pytesserct

 text =
str(((pytesseract.image_to_string(Image.open(filename)))))

 

 # The recognized text is stored in variable text

 # Any string processing may be applied on text

 # Here, basic formatting has been done:

 # In many PDFs, at line ending, if a word can't

 # be written fully, a 'hyphen' is added.

 # The rest of the word is written in the next line

 # Eg: This is a sample text this word here GeeksF-

 # orGeeks is half on first line, remaining on next.

 # To remove this, we replace every '-\n' to ''.

 text = text.replace('-\n', '') 

 

 # Finally, write the processed text to the file.

 f.write(text)

 

# Close the file after writing all the text.

f.close()  
  
---  
  
 __

 __

 **Output:**

Input PDF file:  
![](https://media.geeksforgeeks.org/wp-content/uploads/pdf_file.png)

Output Text file:  
![](https://media.geeksforgeeks.org/wp-content/uploads/text_output.png)  
As we see, the pages of the PDF were converted to images. Then the images were
read, and the content was written into a text file.

 **Advantages of this method include:**

  1. Avoiding text-based conversion because of encoding scheme resulting in loss of data.
  2. Even handwritten content in PDF can be recognized due to the usage of OCR.
  3. Recognizing only particular pages of the PDF is also possible.
  4. Getting the text as a variable so that any amount of required pre-processing can be done.

 **Disadvantages of this method include:**

  1. Disk storage is used to store the images in the local system. Although these images are tiny in size.
  2. Using OCR cannot guarantee 100% accuracy. Given a computer typed PDF document results in very high accuracy.
  3. Handwritten PDFs are still recognized, but the accuracy depends on various factors like handwriting, page color, etc.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

