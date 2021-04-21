Python | Write multiple files data to master file



Given a number of input files in a source directory, write a Python program to
read data from all the files and write it to a single master file.

Source directory contains _n_ number of files, and structure is same for all
files. The objective of this code is to read all the files one by one and then
append the output into a single master file having structure same as source
files.

Taking three input files as example, named _emp_1.txt_ , _emp_2.txt_ ,
_emp_3.txt_ , output will contain data from all the input files.

    
    
    **Input:**
    ![](https://media.geeksforgeeks.org/wp-content/uploads/20190502100733/e14.png)
    ![](https://media.geeksforgeeks.org/wp-content/uploads/20190502100425/e22.png)
    ![](https://media.geeksforgeeks.org/wp-content/uploads/20190502101146/e33.png)
    
    **Output:**
    ![](https://media.geeksforgeeks.org/wp-content/uploads/20190421171628/output50.png)

**Method #1:** Using os module

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import os

# list the files in directory

lis = os.listdir('D:\\python'

 '\\data_files\\data_files')

print(lis)

tgt = os.listdir('D:\\python'

 '\\data_files\\target_file')

 

file_dir ='D:\\python\\data_files\\data_files'

out_file = r'D:\\python\\data_files\\target_file\\master.txt'

ct = 0

 

print('target file :', tgt)

try:

 # check for if file exists

 # if yes delete the file 

 # otherwise data will be appended to existing file

 if len(tgt)>0:

 os.remove('D:\\python'

 '\\data_files\\target_file\\master.txt')

 

 open(tgt, 'a').close()

 else:

 # create an empty file

 open(tgt, 'a').close()

except:

 head = open('D:\\python'

 '\\data_files\\target_file\\master.txt', 'a+')

 

 line ='empno, ename, sal'

 # write header to output

 print(head, line)

 head.close()

 # below loop to write data to output file

 for line1 in lis:

 f_dir = file_dir+'\\'+line1

 # open files in read mode

 in_file = open(f_dir, 'r+')

 

 # open output in append mode

 w = open(out_file, 'a+')

 d = in_file.readline()

 d = in_file.readlines()

 w.write("\n")

 for line2 in d:

 print(line2)

 w.write(line2)

 

 ct = ct + 1

 w.close()   
  
---  
  
__

__

**Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190421171628/output50.png)

  
**Method #2:** Using pandas

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

# pd.read_csv creates dataframes

df1 = pd.read_csv('D:\python\data_files\data_files\emp_1.txt')

df2 = pd.read_csv('D:\python\data_files\data_files\emp_2.txt')

df3 = pd.read_csv('D:\python\data_files\data_files\emp_3.txt')

 

frames = [df1, df2, df3]

 

# concat function concatenates the frames 

result = pd.concat(frames)

# to_csv function writes output to file

result.to_csv('D:\\python\\data_files'

 '\\target_file\\master.txt', encoding ='utf-8', index =
False)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190421171628/output50.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

