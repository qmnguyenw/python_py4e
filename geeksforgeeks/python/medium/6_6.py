Check 12th Class Result Using Selenium in Python



We are going to collect the data of 12th class in CSV file with the following
information:

  1. Candidate name
  2. Pass or fail status
  3. Division
  4. Obtain marks

This task will be done by using selenium library of Python.

 **Requirement:**

You need to install chrome driver and set path. Click here To download. For
more information follow this link.

**Approach:**

  

  

  1. First to go 12th website follow this LINK(this is for up board 12th result).
  2. Then click on investigate element by urgent ctrl + shift + i or stepping into setting of browser and clicking on investigate detail manually.
  3. Then navigate to the box where the district is select then copy the x_path.
  4. Then navigate to the box where the roll number is filled then copy the x_path.
  5. Then navigate the view result button then copy the x_path.
  6. I want to store the result in CSV file then also navigate student name, fail-pass status, division, obtain marks. Then fill up roll number automatically by script go to next page find x_path of student name, fail-pass status, division, obtain marks.

 **Follow step-by-step with the help of screenshots and copy the x_path of
element and put into the code:**

 **Step 1:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805180640/Screenshot351.png)

 **Step 2:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805180738/Screenshot353.png)

 **Step 3:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805180736/Screenshot352.png)

 **Step 4:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805180924/Screenshot354.png)

 **Step 5:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805180954/Screenshot355.png)

 **Step 6:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805181039/Screenshot356.png)

 **Step 7:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805181108/Screenshot357.png)

 **Step 8:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805181134/Screenshot358.png)

 **Step 9:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805181205/Screenshot359.png)

 **Step 10:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805181302/Screenshot360.png)

 **Step 11:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805181444/Screenshot361.png)

 **Step 12:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805181527/Screenshot362.png)

Below is the implementation:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required libraries

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException

import csv 

import time

 

# give name of csv file

filename = "abc.csv"

 

# open file in write mode

f = open(filename, 'w')

 

# creat header in file

header = "NAME,STATUS,DIV,NUM\n"

 

# write into the file

f.write(header)

 

# put rollnumber without zero like

# your number 0477593 then

# put 477593 upto XXXXX.

start_rollNum = 926840

end_rollNum = 926841

 

# put range of rollnumber

for i in range(start_rollNum, end_rollNum ):

 

 # use try and except because if any rollnumber

 # is invalid then whole program is not stop.

 try:

 driver = webdriver.Chrome()

 

 # link is given above copy and paste

 driver.get("https://results.upmsp.edu.in/ResultIntermediate.aspx")

 

 # add zero in rollnumber in starting

 t = '0' + str(i)

 

 # district xpath

 state =
driver.find_element_by_xpath('//*[@id="ctl00_cphBody_ddl_districtCode"]')

 drp1 = Select(state)

 

 # select district

 drp1.select_by_visible_text('LUCKNOW')

 

 # put rollnumber


driver.find_element_by_xpath('//*[@id="ctl00_cphBody_txt_RollNumber"]').send_keys(t)

 

 # view result xpath


driver.find_element_by_xpath('//*[@id="ctl00_cphBody_btnSubmit"]').click()

 

 # student name

 name =
driver.find_element_by_xpath('//*[@id="ctl00_cphBody_lbl_C_NAME"]').text

 

 # status pass or fail

 status =
driver.find_element_by_xpath('//*[@id="ctl00_cphBody_lbl_RESULT"]').text

 

 # division

 div =
driver.find_element_by_xpath('//*[@id="ctl00_cphBody_lbl_DIVISION"]').text

 

 # obatin marks

 num =
driver.find_element_by_xpath('//*[@id="ctl00_cphBody_lbl_MRK_OBT"]').text

 

 # all details fill into csv file

 f.write(name + "," + status + "," +

 div[1 : ] + "," + num + "\n")

 

 # close the driver

 driver.close()

 

 except NoSuchElementException as exception:

 continue

 

# close and save the file

f.close()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805182140/Screenshot363.png)

CSV file screenshot

 **Note:** If you Want to find a topper then apply a filter on CSV file.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

