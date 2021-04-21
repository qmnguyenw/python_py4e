Django+React Full Stack Development Setup using Dact



When we work on a project having **Django as our Back-end** and having a
powerful **front-end using React** , the development setup takes a significant
amount of time to setup – configuring Babel, Webpack, URLs, views, etc. We
used to set up this earlier to get started with ReactJS before **npx create-
react-app** came.

The **npx create-react-app** command enables us to work on react without
thinking about all the Babel, Webpack, etc. It **becomes a problem when we try
to use npx create-react-app in our Django app**. So in this article, we are
going to use a Python CLI App or Package- Dact. **Dact** enables us to set up
a React-Django Development setup **** in just a **single command**. It’s open-
sourced and its code is available on **GitHub**.

    
    
    **Note:** Make sure you have **Python, pip** and **npm** installed in your system.

Follow the below steps to successfully set up a React-Django project in your
system:

 **Step 1:** First we need to install **dact** using pip as shown below:

    
    
    pip install dact

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210127114408/Screenshotfrom20210127114358.png)

  

  

 **Step 2:** Check if dact is successfully installed by typing “dact” in your
terminal.

    
    
    dact 

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210127114522/Screenshotfrom20210127114512.png)

**Step 3:** To start a Django-React Full stack development project, just type-

    
    
    dact {your_project_name}

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210127115010/Screenshotfrom20210127115001.png)

It creates a Django project with the name you provided and a frontend app
named- “reactfrontend”. You may also set up the project using your custom
front-end app name using

    
    
    dact {your_project_name} {react_front_end_app_name}

 **Step 4:** Enter the Project

    
    
    cd my_project

 **Step 5:** Run Django Server

    
    
    python manage.py runserver

Your Welcome Page serves at localhost:8000

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210127115524/Screenshotfrom20210127115511.png)

Step 6: **Watch the changes** in React file.

Open a different terminal and type

    
    
    dact-watch

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210127120922/Screenshotfrom20210127120906.png)

    
    
    Note: Make sure you are in the same directory as **manage.py**.

Let dact-watch run in the background while you work on your Front-end.

 **Step 7:** Edit your React Front-end. To edit the React file, you need to go
to :

    
    
    reactfrontend > static > src > App.js

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210127115932/Screenshotfrom20210127115922.png)

Let’s write Hello GeeksForGeeks.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210127120641/Screenshotfrom20210127120627.png)

Make the changes. Make sure **dact-watch** is running in the background.
Refresh your Welcome Page.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210127120745/Screenshotfrom20210127120737.png)

Now you may create your own Django app for the back-end and develop your dream
project using **React and Django** with the help of **Dact**..

![react-js-img](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200604102104/GFG-FSRNL-Article-2.png)

My Personal Notes _arrow_drop_up_

Save

