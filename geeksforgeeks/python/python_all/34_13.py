Competitive Coding Setup for C++ and Python in VS Code using Python Script



Most of us struggle with using heavy software to run C++ and python code and
things become more complicated when we have too many files in a folder. In
this blog, we are going to create a python script with VS-code-editor that
works out to do all your works.

It creates the folder + numbers of files required by the user in that folder
with proper extension and the best feature is you can easily run your c++ and
python files with one single command. I am also providing the best user-
snippets for c++ and python and how to add them to your VS-code-editor.

####  **Requirement**

  * VS Code editor
  * C++ compiler
  * Python installed with the path of the environment variable.

 **Note:** You can search for tutorials on Google if you don’t know how to set
a path in your system.

 **Step 1:** Clone or download the git repository from the link:-
**https://github.com/AkhilRautela/Competitive-Coding-Helpful-Script-for-
VScode-**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200818101259/firstgithub.jpg)

CLONE OR DOWNLOAD IT

 **Step 2:** After cloning or downloading it open the folder in your VS Code
editor. Make sure there is no .vscode folder in the above directories. This
will give you multiple build options.

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200818112301/vscode.png)

 **All the files downloaded can be seen on the left side**

 **Step 3:** Once the file is downloaded, open the terminal and create a
folder and files using the command **Terminal→New Terminal.** This will give
you a new terminal at the bottom of the VSCode editor.

  *  **Syntax:** python cp.py {folder-name} {number-of-files} {cpp/py}
    * Example for c++ files :- **python cp.py div2_126 3 cpp**
    * Example for python files:- **python cp.py div1_123 5 py**
  * Both the above commands will create 2 folders one naming div2_126 with 3 files A, B, and C with cpp extension and div1_123 with files A to E with py extension.
  * You can create your own custom folder, it’s not necessary to use the script for creating a folder.
  * With code, you can only create up to 26 files (A-Z) (usually preferred during the contest) with the command but you can create any number of files manually.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200818121653/terminal.png)

 **You can see the files created on the left side**

  * After that, you can start coding in your required file.
  * You can easily use the snippet by calling **lets** for c++ and **pystart** for python. You can change the prefix name in the .snippets file in the .vscode folder. Before that lets set up the layout as in our snippet our code will take input from **input.txt** and output to **output.txt.**
  * You can split the vs code by going to **View- >EditorLayout.** Let’s first split the current window to left then the right window to down.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200818123130/terminal.png)

 **SPLIT LEFT.**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200818123505/terminal.png)

 **SPLIT DOWN THE LEFT PART.**

  * Now our setup is ready now you can put your **input.txt** in the top right cell, **output.txt** to the bottom-right cell, and main code in the left cell by dragging them from the files from the left file menu.
  * I have dragged the py file to the left cell.
  * To use snippet write **pystart** and we will get the snippet.
  * If you are using c++ then use **lets** keyword for the snippet.
  * Write input to the **input.txt.**
  * Write the code in the py file and press **Ctrl+Shift+B** to execute it **.** This will execute my script that will run the python or c++ file automatically without asking for any build selection.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200818124552/terminal.png)

 **you can see the output occurs in output.txt**

 **Step 4:** The same can be done for C++. Write the code and press
**Ctrl+Shift+B.**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200818125440/terminal.png)

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL.

My Personal Notes _arrow_drop_up_

Save

