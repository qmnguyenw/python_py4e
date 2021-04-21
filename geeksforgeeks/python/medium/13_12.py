How to move Files and Directories in Python



Python provides functionality to move files or directories from one location
to another location. This can be achieved using shutil.move() function from
**shutil** module. shutil.move() method Recursively moves a file or
directory (source) to another location (destination) and returns the
destination. If the destination directory already exists then src is moved
inside that directory. If the destination already exists but is not a
directory then it may be overwritten depending on os.rename() semantics.

>  **Syntax:** shutil.move(source, destination, copy_function = copy2)
>
>  **Parameters:**  
>  **source:** A string representing the path of the source file.  
>  **destination:** A string representing the path of the destination
> directory.  
>  **copy_function (optional):** The default value of this parameter is copy2.
> We can use other copy functions like copy, copytree, etc for this parameter.
>
>  **Return Value:** This method returns a string that represents the path of
> a newly created file.

 **Example #1:** Suppose the structure of directory looks like this –

