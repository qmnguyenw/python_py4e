Django – Upload files with FileSystemStorage



Django ships with the FileSystemStorage class that helps to store files
locally so that these files can be served as media in development. In this
article, we will see how to implement a file upload system using
FileSystemStorage API to store the files locally.  
 **Note:** This method should only be used in development and not in
production.

### How to Upload Files with FileSystemStorage?

  *  **Step 1** : We will start off by making a template form to upload files.

 **Template**

 __

 __  
 __

 __

 __  
 __  
 __

<form method = 'POST' class="col s12"
enctype="multipart/form-data">

 

 {% csrf_token %}

 

 {{new_form.as_p}}

 

 <!--Below is our main file upload input -->

 <input type = "file" name = 'document'>

 <p><button type = "submit" class = "waves-effect waves-
light btn" style = "background-color:
teal">Publish</button></p>

</form>  
  
---  
  
 __

 __

Here, note that the input(through which the user may input a file) has the
name ‘document’.

  *  **Step 2:** Now, we will write the view for the same in the views.py file

 **View**  
First, import the FileSystemStorage class on the top of the file using

  

  

    
        from django.core.files.storage import FileSystemStorage

 __

 __  
 __

 __

 __  
 __  
 __

if request.method == "POST":

 # if the post request has a file under the input name 'document', then
save the file.

 request_file = request.FILES['document'] if 'document' in
request.FILES else None

 if request_file:

 # save attatched file

 

 # create a new instance of FileSystemStorage

 fs = FileSystemStorage()

 file = fs.save(request_file.name, request_file)

 # the fileurl variable now contains the url to the file. This can be used
to serve the file when needed.

 fileurl = fs.url(file)

 

return render(request, "template.html")  
  
---  
  
 __

 __

Here, the FileSystemStorage class’ constructor takes the parameter ‘location’
which is the path to the directory where you want to store the files. By
default, it is the path in the variable ‘settings.MEDIA_ROOT’. It also takes
the parameter ‘base_url’ which is the url you would want the media to
correspond to. By default, it is set to the value of the variable
‘settings.MEDIA_URL’ (make sure you have those constants set in the
settings.py file).

The function FileSystemStorage.save takes in 3 arguments; name, content(the
file itself) and max_length(default value = None).  
This function stores the file – ‘content’ under the name ‘name’. If a file
with the same name exists, then it modifies the file name a little to generate
a unique name.

Read about more constructor parameters and methods of the FileSystemStorage
class in the django documentation for the same

  *  **Step 3:** Define MEDIA_ROOT and MEDIA_URL if not already defined.  
 **Settings**  
Make sure you configure the MEDIA_ROOT and MEDIA_URL in settings.py.

 __

 __  
 __

 __

 __  
 __  
 __

MEDIA_ROOT= os.path.join(BASE_DIR, 'media') # media directory in
the root directory

MEDIA_URL = '/media/'  
  
---  
  
 __

 __

  *  **Step 4:** Finally, we add a route to MEDIA_URL.  
 **URLs**  
In urls.py, import

    
        from django.conf.urls.static import static
    from django.conf import settings

and add the following at the end of the file

 __

 __  
 __

 __

 __  
 __  
 __

# only in development

if settings.DEBUG:

 urlpatterns += static(settings.MEDIA_URL, document_root =
settings.MEDIA_ROOT)  
  
---  
  
 __

 __

This will add a route to the MEDIA_URL and serve the file from MEDIA_ROOT when
a user makes a GET request to MEDIA_URL/(file name). Once all this is done,
the files uploaded should show up in the directory specified in the MEDIA_ROOT
constant.

 **Output –**  
The frontend should look something like this  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200513180156/Screenshot-
from-2020-05-13-17-57-26-300x124.png)

As mentioned earlier, this method should only be used to serve media in
development and not in production. You might want to use something like nginx
in production.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

