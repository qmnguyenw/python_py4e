Installing MongoDB on Windows with Python



We would explain the installation of MongoDB in steps. Before you install, I
would suggest everyone use ide spyder, Anaconda.

 **Step 1 - > Install the community Edition**  
Installation Link

 **Step 2 - > Run the installed MongoDB windows installer package that you
just downloaded.**

MongoDB get installed here->

    
    
     **C:\Program Files\MongoDB\Server\3.4\**

 **Step 3 - > Let’s set MongoDB environment**

  

  

  * (a) **Create data directory where all data is stored.**  
On C: drive create a folder data inside it create a folder db  
or  
Run

    
        md C:\data\db

  * (b) **To start MongoDB**  
Run ->

    
        "C:\Program Files\MongoDB\Server\3.4\bin\mongod.exe"
    

Wait till the connection message appears

  * (c) **Verify Environment Path or set path if not correctly set**  
Open environment variables, you can search this by windows search.  
![](https://media.geeksforgeeks.org/wp-content/uploads/rough.png)

Open Environment Variable under the System variables section open Path.  
This would look like this.  
![](https://media.geeksforgeeks.org/wp-content/uploads/rough2.png)  
Add the path of bin folder as shown in the image above.

  * (d) **To Connect to MongoDB**  
Open other command prompt and run->

    
        "C:\Program Files\MongoDB\Server\3.4\bin\mongo.exe
    

**Step 4- > Ready MongoDB**  
Open Command Prompt(Admin mode) type->

    
    
    mongod

![](https://media.geeksforgeeks.org/wp-content/uploads/rough6.png)

 **NOTE :** Till step 4 MongoDB will work only when the Command Prompt is open
and it’s listening.  
Now we’ll see Extension to make it better.

 **Below steps from step 5 to step 8 are optional :**  
 **Step 5- > Open command prompt and run-**

  

  

    
    
    mkdir c:\data\db
    mkdir c:\data\log
    

****Step 6-** > Create a configuration file at C:\Program
Files\MongoDB\Server\3.4\mongod.cfg (name of file mongod.cfg)**

    
    
    systemLog:
        destination: file
        path: c:\data\log\mongod.log
    storage:
        dbPath: c:\data\db
    

This can be created and saved in _Admin mode of Notepad_ or Notepad++ or any
other editor to run notepad admin mode _press Ctrl + Shift + Enter_. Admin
mode of notepad will let you create mongod.cfg and save above text file.

 ** **Step 7** -> Install the MongoDB service by starting mongod.exe with the
–install option and the -config option to specify the previously created
configuration file.**  
Now run this command on command prompt

    
    
    "C:\Program Files\MongoDB\Server\3.4\bin\mongod.exe" 
    --config "C:\Program Files\MongoDB\Server\3.4\mongod.cfg" --install

 ** **Step 8** -> To start & stop MongoDB run**  
To start :

    
    
    net start MongoDB

To stop :

    
    
    net stop MongoDB
    

![](https://media.geeksforgeeks.org/wp-content/uploads/rough3.png)  
**  
NOTE :** ALL commands are run on Command Prompt Admin mode, to open command
prompt Admin Mode either open normal command prompt and press Ctrl+Shift+Enter
or Right click on left windows icon start button where you can see the
options.  
 **  
Step 9** -> Open Anaconda Command Prompt as shown in the image.  
![](https://media.geeksforgeeks.org/wp-content/uploads/rough4.png)

 **Step 10** -> Install package to use MongoDB  
To install this package with conda run:

    
    
    conda install -c anaconda pymongo 
    

![](https://media.geeksforgeeks.org/wp-content/uploads/rough5.png)

Congratulations!! Installation completed.( Pymongo works only when MongoDB is
started, use net start MongoDB to start it and then work on spyder)  
You can study and understand MongoDB in python here.

This article is contributed by **SHAURYA UPPAL**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

