Pyscaffold module in Python



Starting off with a Python project is usually quite complex and complicated as
it involves setting up and configuring some files. This is where
**Pyscaffold** comes in. It is a tool to set up a new python project, is very
easy to use and sets up your project in less than 10 seconds! To use
Pyscaffold, **Git is a must** , especially Windows users should have “Git
Bash” installed. Additionally, the installation of PyScaffold also requires a
recent version of “setup tools”.

Each Python package project is internally represented by PyScaffold as a tree
data structure that directly relates to a directory entry in the file system.
This tree is implemented as a simple dictionary in which keys indicate the
path where files will be generated, while values indicate their content.

#### Installation

To install Pyscaffold using pip, carry out the following command which
installs the latest Pyscaffold version:

    
    
    pip install --upgrade pyscaffold

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200314194038/one7.png)

In case you do not have pip installed, refer to this article: How to install
pip command

  

  

PyScaffold can also be installed with conda by carrying out the following on
Anaconda Command Prompt:

    
    
    conda install -c conda-forge pyscaffold

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200314194528/teo1.png)

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200314194534/three4.png)

If you see anything like this, then this means Pyscaffold has been installed
successfully!

#### Setting the new Project

PyScaffold comes with a lot of characteristics and configuration defaults to
make the frequent tasks in developing, maintaining and distributing your own
Python package as easy as possible.  
To set up a new python project, use the putup command:

    
    
    putup Your_Project

This creates a folder Your_Project with the project layout of a Python project
and it has a Your_Project package folder along with documents and tests
folders and the files setup.py, setup.cfg, AUTHORS.txt, README.txt, and
LICENSE.txt. All configuration is done in “setup.cfg” instead of setup.py.
Here, you can change all the settings related to the package (i.e., author,
URL, license, etc.). Also, to add additional data files, we can add their
names in the setup.cfg and they’ll be automatically added.

PyScaffold is designed to cover the essentials of authoring and distributing
Python packages. Most of the time, setting up putup options is enough to
ensure the proper configuration of a project. PyScaffold can be extended at
runtime by other Python packages. It is also possible to write an external
script or program that embeds PyScaffold and use it to perform some user-
defined actions.

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Temporarily adjust padding

# while executing a context.

from pyscaffold.log import logger

 

 

logger.report('invoke', 'custom_action')

with logger.indent():

 logger.report('create', 'some / file / path')

 

# Expected logs:

# --------------------------------------

# invoke custom_action

# create some / file / path

# --------------------------------------

# Note how the spacing between activity and

# subject in the

# second entry is greater than the equivalent

# in the first one.  
  
---  
  
 __

 __

 **Updates:**

  * Whenever a new update of PyScaffold gets released, you can use this command to update the  
structure/scaffold of your project:

    
        putput --update my_project

  * An update will only update files that are not usually used or modified by the user, therefore, to  
update all the files, use force update:

    
        --update --force

 **Note:**

    * If you are updating from a PyScaffold version before 2.0, you must manually remove the files versioneer.py and MANIFEST.in.
    * If you are updating from a version before 2.2, you must remove ${PACKAGE}/_version.py.

#### How to migrate to PyScaffold

Initially, the project (let’s say my_project) has to be on a Git repository
and includes a package (let’s say my_package) along with your python modules.

 **Note:** Your working tree is not dirty, i.e. all changes are committed and
all important files are under version control.

  * Start by changing into the parent folder of my_project and type the following command in order to deploy the new project structure in your repository.
    
        putup my_project --force --no-skeleton -p my_package

  * Change into my_project and move your old package folder into src with this command and use the same technique if the project has a test folder other than tests or a documentation folder other than docs.
    
        git mv my_package/* src/my_package/

  * Use git status to check for untracked files and add them with git add.
  * . Eventually, use git difftool to check all overwritten files for changes that need to be transferred. All configuration that you may have done in setup.py, need to be moved to setup.cfg. In most cases you will not need to make changes to the new setup.py file provided by PyScaffold.
  * Run these commands to check everything works:
    
        run python setup.py install and python setup.pysdist

  * Also run python setup.py docs and python setup.py test to check that Sphinx and PyTest runs correctly.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

