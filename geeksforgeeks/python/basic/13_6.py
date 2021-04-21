How to use Google Colab



If you want to create a machine learning model but say you don’t have a
computer that can take the workload, **Google Colab** is the platform for you.
Even if you have a GPU or a good computer creating a local environment with
anaconda and installing packages and resolving installation issues are a
hassle.  
Colaboratory is a free Jupyter notebook environment provided by Google where
you can use free GPUs and TPUs which can solve all these issues.

#### Getting Started

To start working with Colab you first need to log in to your google account,
then go to this link https://colab.research.google.com.

 **Opening Jupyter Notebook:**  
On opening the website you will see a pop-up containing following tabs –  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430115728/Screenshot-3912.png)

>  **EXAMPLES:** Contain a number of Jupyter notebooks of various examples.  
>  **RECENT:** Jupyter notebook you have recently worked with.  
>  **GOOGLE DRIVE:** Jupyter notebook in your google drive.  
>  **GITHUB:** You can add Jupyter notebook from your GitHub but you first
> need to connect Colab with GitHub.  
>  **UPLOAD:** Upload from your local directory.

Else you can _create a new Jupyter notebook_ by clicking New Python3 Notebook
or New Python2 Notebook at the bottom right corner.

  

  

 **Notebook’s Description:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430120025/Screenshot-4012.png)  
On creating a new notebook, it will create a Jupyter notebook with
Untitled0.ipynb and save it to your google drive in a folder named **Colab
Notebooks**. Now as it is essentially a Jupyter notebook, all commands of
Jupyter notebooks will work here. Though, you can refer the details in Getting
started with Jupyter Notebook.

 **Let’s talk about what different here.**

 **Change Runtime Environment:**  
Click the **“Runtime”** dropdown menu. Select **“Change runtime type”**.
Select python2 or 3 from **“Runtime type”** dropdown menu.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430120211/Screenshot-426.png)
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430120905/Screenshot-452.png)

**Use GPU and TPU:**  
Click the **“Runtime”** dropdown menu. Select **“Change runtime type”**. Now
select anything(GPU, CPU, None) you want in the **“Hardware accelerator”**
dropdown menu.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430120211/Screenshot-426.png)  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430121157/Screenshot-4910.png)

 **Verify GPU:**

 __

 __  
 __

 __

 __  
 __  
 __

import tensorflow as tf

tf.test.gpu_device_name()  
  
---  
  
 __

 __

If gpu is connected it will output following –

    
    
    '/device:GPU:0'
    

Otherwise, it will output following

    
    
    ''
    

**Verify TPU:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import os

 

if 'COLAB_TPU_ADDR' not in os.environ:

 print('Not connected to TPU')

else:

 print("Connected to TPU")  
  
---  
  
 __

 __

If gpu is connected it will output following

    
    
    Connected to TPU
    

Otherwise, it will output following

    
    
    Not connected to TPU
    

  
**Install Python packages –**  
Use can use **pip** to install any package. For example:

 __

 __  
 __

 __

 __  
 __  
 __

! pip install pandas  
  
---  
  
 __

 __

  
**Clone GitHub repos:**  
Use **git clone** command. For example:

 __

 __  
 __

 __

 __  
 __  
 __

! git clone
https://github.com/souvik3333/Testing-and-Debugging-Tools  
  
---  
  
 __

 __

  
**Upload File:**

 __

 __  
 __

 __

 __  
 __  
 __

from google.colab import files

uploaded = files.upload()  
  
---  
  
 __

 __

Select “Choose file” and upload the file you want. Enable third-party cookies
if they are disabled.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430130639/Screenshot-554.png)

Then you can save it in a dataframe.

 __

 __  
 __

 __

 __  
 __  
 __

import io

df2 = pd.read_csv(io.BytesIO(uploaded['file_name.csv']))  
  
---  
  
 __

 __

 **Upload File By Mounting Google Drive:**  
To mount your drive inside “mntDrive” folder execute following –

 __

 __  
 __

 __

 __  
 __  
 __

from google.colab import drive

drive.mount('/mntDrive')  
  
---  
  
 __

 __

Then you’ll see a link, click on link, then allow access, copy the code that
pops up, paste it at “Enter your authorization code:”.

Now to see all data in your google drive you need to execute following:

 __

 __  
 __

 __

 __  
 __  
 __

! ls"/mntDrive/My Drive"  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430123759/Screenshot-502.png)

 **File Hierarchy:**  
You can also see file hierarchy by clicking “>” at top left below the control
buttons (CODE, TEXT, CELL).  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430123759/Screenshot-502.png)

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430124049/Screenshot-516.png)

 **Download Files:**  
Let’s say you want to download “file_name.csv”. You can copy the file to your
google drive (In “data” folder, you need to create the “data” folder in google
drive) by executing this:

 __

 __  
 __

 __

 __  
 __  
 __

cp file_name.csv"/mntDrive/My Drive/data/renamed_file_name.csv"  
  
---  
  
 __

 __

The file will be saved at “data” folder with “renamed_file_name.csv” name. Now
you can directly download from there, Or, you can just open file hierarchy and
right clicking will give download option.

 **Download Jupyter Notebook:**  
Click **“File”** dropdown menu at top left corner. Choose **“download
.ipynb”** or **“download .py”**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430124403/Screenshot-522.png)

 **Share Jupyter Notebook:**  
You can share your notebook by adding others email address or by creating a
shareable link.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430131722/Screenshot-576.png)  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190430131456/Screenshot-583.png)

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

