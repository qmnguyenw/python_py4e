A Beginners Guide To Streamlit



The trend of Data Science and Analytics is increasing day by day. From the
data science pipeline, one of the most important steps is model deployment. We
have a lot of options in python for deploying our model. Some popular
frameworks are Flask and Django. But the issue with using these frameworks is
that we should have some knowledge of HTML, CSS, and JavaScript. Keeping these
prerequisites in mind, Adrien Treuille, Thiago Teixeira, and Amanda Kelly
created “Streamlit”. Now using streamlit you can deploy any machine learning
model and any python project with ease and without worrying about the
frontend. Streamlit is very user-friendly.

In this article, we will learn some important functions of streamlit, create a
python project, and deploy the project on a local web server.

Let’s install streamlit. Type the following command in the command prompt.

    
    
    pip install streamlit
    

Once Streamlit is installed successfully, run the given python code and if you
do not get an error, then streamlit is successfully installed and you can now
work with streamlit.

## How to run Streamlit file?

Open command prompt or Anaconda shell and type

  

  

    
    
    streamlit run filename.py
    

![](https://media.geeksforgeeks.org/wp-content/uploads/20201120002133/cmd.png)

Run Streamlit file

Here my filename is ‘sample.py’. Open the local URL in the web browser.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120002530/cmd2.png)

##

### Understanding the Streamlit basic functions

 **1\. Title:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import streamlit as st

 

# Title

st.title("Hello GeeksForGeeks !!!")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120022612/hello.png)

Title

 **2\. Header and Subheader:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Header

st.header("This is a header") 

 

# Subheader

st.subheader("This is a subheader")  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120004148/header.png)

Header/Subheader

 **3\. Text:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Text

st.text("Hello GeeksForGeeks!!!")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120004151/text.png)

Text

 **4\. Markdown:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Markdown

st.markdown("### This is a markdown")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120004149/markdown-300x95.png)

Markdown

 **5\. Success, Info, Warning, Error, Exception:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# success

st.success("Success")

 

# success

st.info("Information")

 

# success

st.warning("Warning")

 

# success

st.error("Error")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120004150/success-660x242.png)

Success, Info, Warning and Error

 **6\. Write:**

Using write function, we can also display code in coding format. This is not
possible using st.text(”).

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Write text

st.write("Text with write")

 

# Writing python inbuilt function range()

st.write(range(10))  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120005057/write.png)

write() function

 **7\. Display Images:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Diaplay Images

 

# import Image from pillow to open images

from PIL import Image

img = Image.open("streamlit.png")

 

# display image using streamlit

# width is used to set the width of an image

st.image(img, width=200)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120005056/image-300x181.png)

Display image using streamlit

 **8\. Checkbox:**

A checkbox returns a **boolean value**. When the box is checked, it returns a
**True** value else returns a **False** value.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# checkbox

# check if the checkbox is checked

# title of the checkbox is 'Show/Hide'

if st.checkbox("Show/Hide"):

 

 # dispaly the text if the checkbox returns True value

 st.text("Showing the widget")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201120005514/cb1.png)

Checkbox is not checked

![](https://media.geeksforgeeks.org/wp-content/uploads/20201120005514/cb2.png)

The text is displayed when the box is checked

 **9\. Radio Button:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# radio button

# first argument is the title of the radio button

# second argument is the options for the ratio button

status = st.radio("Select Gender: ", ('Male', 'Female'))

 

# conditional statement to print 

# Male if male is selected else print female

# show the result using the success function

if (status == 'Male'):

 st.success("Male")

else:

 st.success("Female")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120010542/male-660x150.png)

Success shows Male when male option is selected

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120010540/female-660x148.png)

Success shows Female when Female option is selected

 **10\. Selection Box:**

You can select any one option from the select box.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Selection box

 

# first argument takes the titleof the selectionbox

# second argument takes options

hobby = st.selectbox("Hobbies: ",

 ['Dancing', 'Reading', 'Sports'])

 

# print the selected hobby

st.write("Your hobby is: ", hobby)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120011026/sb1-660x220.png)

Selectbox showing options to select from

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120011027/sb2-660x125.png)

Selected option is printed

 **11\. Multi-Selectbox:**

The multi-select box returns the output in the form of a list. You can select
multiple options.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# multi select box

 

# first argument takes the box title

# second argument takes the options to show

hobbies = st.multiselect("Hobbies: ",

 ['Dancing', 'Reading', 'Sports'])

 

# write the selected options

st.write("You selected", len(hobbies), 'hobbies')  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120013507/ms1-660x125.png)

Multi-SelectBox

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120013508/ms2-660x125.png)

Selected 2 options

 **12\. Button:**

st.button() returns a **boolean value**. It returns a **True** value when
clicked else returns **False**.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Create a simple button that does nothing

st.button("Click me for no reason")

 

# Create a button, that when clicked, shows a text

if(st.button("About")):

 st.text("Welcome To GeeksForGeeks!!!")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201120012024/bt1.png)

Click the first button

![](https://media.geeksforgeeks.org/wp-content/uploads/20201120012025/bt2.png)

Click the About button

 **13\. Text Input:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Text Input

 

# save the input text in the variable 'name'

# first argument shows the title of the text input box

# second argument displays a default text inside the text input area

name = st.text_input("Enter Your name", "Type Here ...")

 

# display the name when the submit button is clicked

# .title() is used to get the input text string 

if(st.button('Submit')):

 result = name.title()

 st.success(result)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120012807/ti1-660x124.png)

Text Input

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120012808/ti2-660x188.png)

Display success message when the Submit button is clicked

 **14\. Slider:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# slider

 

# first argument takes the title of the slider

# second argument takes thr starting of the slider

# last argument takes the end number

level = st.slider("Select the level", 1, 5)

 

# print the level

# format() is used to print value 

# of a variable at a specific position

st.text('Selected: {}'.format(level))  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120014223/slider-660x119.png)

Slider

#### Mini Project:

Let us recollect everything that we learn above and create a BMI Calculator
web app.

The formula of BMI Index when weight is in Kgs and height is in meters is:

![bmi = weight/height^2   ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-0adc298fd5556ee23457a45d051d7aab_l3.png)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import the streamlit library

import streamlit as st

 

# give a title to our app

st.title('Welcome to BMI Calculator')

 

# TAKE WEIGHT INPUT in kgs

weight = st.number_input("Enter your weight (in kgs)")

 

# TAKE HEIGHT INPUT

# radio button to choose height format

status = st.radio('Select your height format: ',

 ('cms', 'meters', 'feet'))

 

# compare status value

if(status == 'cms'):

 # take height input in centimeters

 height = st.number_input('Centimeters')

 

 try:

 bmi = weight / ((height/100)**2)

 except:

 st.text("Enter some value of height")

 

elif(status == 'meters'):

 # take height input in meters

 height = st.number_input('Meters')

 

 try:

 bmi = weight / (height ** 2)

 except:

 st.text("Enter some value of height")

 

else:

 # take height input in feet

 height = st.number_input('Feet')

 

 # 1 meter = 3.28

 try:

 bmi = weight / (((height/3.28))**2)

 except:

 st.text("Enter some value of height")

 

# check if the button is pressed or not

if(st.button('Calculate BMI')):

 

 # print the BMI INDEX

 st.text("Your BMI Index is {}.".format(bmi))

 

 # give the interpretation of BMI index

 if(bmi < 16):

 st.error("You are Extremely Underweight")

 elif(bmi >= 16 and bmi < 18.5):

 st.warning("You are Underweight")

 elif(bmi >= 18.5 and bmi < 25):

 st.success("Healthy") 

 elif(bmi >= 25 and bmi < 30):

 st.warning("Overweight")

 elif(bmi >= 30):

 st.error("Extremely Overweight")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120021047/bmi1-660x483.png)

Calculate BMI Indec, Scenario 1

#### Height in Meters:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120021049/bmi2-660x471.png)

Calculate BMI Indec, Scenario 2

#### Height in Feet:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120021050/bmi3-660x469.png)

Calculate BMI Indec, Scenario 3

## Conclusion

This way we can use streamlit to deploy our projects without having any
knowledge of HTML, CSS, or JavaScript.

**Note:** Streamlit is still under development and the team is bringing new
concepts.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

