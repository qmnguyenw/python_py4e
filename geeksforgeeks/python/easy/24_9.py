Python Convert Html to PDF



There are many websites that do not allow to download the content in form of
pdf, they either ask to buy their premium version or don’t have such download
service in form of pdf.

### Conversion in 3 Steps from Webpage/HTML to PDF

 **Step1: Download library pdfkit**

    
    
     $ pip install pdfkit

 **Step2: Download wkhtmltopdf**  
For Ubuntu/Debian:

    
    
     sudo apt-get install wkhtmltopdf

For Windows:  
(a)Download link: WKHTMLTOPDF  
(b)Set: PATH variable set binary folder in Environment variables.  
![](https://media.geeksforgeeks.org/wp-content/uploads/rough-4-271x300.png)

 **Step3: Code in Python to Download:**  
(i) Already Saved HTML page

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import pdfkit

pdfkit.from_file('test.html', 'out.pdf')  
  
---  
  
 __

 __

(ii) Convert by website URL

 __

 __  
 __

 __

 __  
 __  
 __

import pdfkit

pdfkit.from_url('https://www.google.co.in/','shaurya.pdf')  
  
---  
  
 __

 __

(iii) Store text in PDF

 __

 __  
 __

 __

 __  
 __  
 __

import pdfkit

pdfkit.from_string('Shaurya GFG','GfG.pdf')  
  
---  
  
 __

 __

 **Congratulations** : Your pdf file would be created and saved in the same
directory where python file exists.

Miscellaneous Knowledge Content:  
1\. You can pass a list with multiple URLs or files:

 __

 __  
 __

 __

 __  
 __  
 __

pdfkit.from_url(['google.com', 'geeksforgeeks.org',
'facebook.com'], 'shaurya.pdf')

pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')  
  
---  
  
 __

 __

2\. Save content in a variable

 __

 __  
 __

 __

 __  
 __  
 __

# Use False instead of output path to save pdf to a variable

pdf = pdfkit.from_url('http://google.com', False)  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

