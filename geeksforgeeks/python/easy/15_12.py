Add the slug field inside Django Model



It is a way of generating a valid URL, generally using data already obtained.
For instance, using the title of an article to generate a URL. Let’s assume
our blog have a post with the title ‘The Django book by Geeksforgeeks’ with
primary key id= 2. We might refer to this post with

    
    
    www.geeksforgeeks.org/posts/2. 

Or, we can reference the title like

    
    
     www.geeksforgeeks.org/posts/The Django book by Geeksforgeeks. 

But the problem is spaces are not valid in URLs, they need to be replaced by
_%20_ which is ugly, making it the following

    
    
    www.geeksforgeeks.org/posts/The%20Django%20book%20by%20geeksforgeeks 

But it is not solving meaningful URL. Another option can be

    
    
     www.geeksforgeeks.org/posts/the-django-book-by-geeksforgeeks

So, the slug is now _the-django-book-by-geeksforgeeks_. All letters are down
cased and spaces are replaced by hyphens -.  

  

  

Assume that our Blog Post models look similar to this.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

STATUS_CHOICES= (

 ('draft', 'Draft'),

 ('published', 'Published'),

)

class Post(models.Model):

 title = models.CharField(max_length = 250)

 slug = models.SlugField(max_length = 250, null = True,
blank = True)

 text = models.TextField()

 published_at = models.DateTimeField(auto_now_add = True)

 updated = models.DateTimeField(auto_now = True)

 status = models.CharField(max_length = 10, choices =
STATUS_CHOICES,

 default ='draft')

 class Meta:

 ordering = ('-published_at', )

 def __str__(self):

 return self.title  
  
---  
  
 __

 __

###  **Adding Slugify** to **our project:**  

Now we need to find a way to convert the title into a slug automatically. We
want this script to be triggered every time a new instance of _Post_ model is
created. For this purpose, we will use signals.  

**Note:** Add new file util.py in the same directory where settings.py file is
saved.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import string, random

from django.db.models.signals import pre_save

from django.dispatch import receiver

from django.utils.text import slugify

def random_string_generator(size = 10, chars =
string.ascii_lowercase + string.digits):

 return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug = None):

 if new_slug is not None:

 slug = new_slug

 else:

 slug = slugify(instance.title)

 Klass = instance.__class__

 max_length = Klass._meta.get_field('slug').max_length

 slug = slug[:max_length]

 qs_exists = Klass.objects.filter(slug = slug).exists()

 

 if qs_exists:

 new_slug = "{slug}-{randstr}".format(

 slug = slug[:max_length-5], randstr =
random_string_generator(size = 4))

 

 return unique_slug_generator(instance, new_slug = new_slug)

 return slug  
  
---  
  
 __

 __

###  **Signals in Django:**

In many cases when there is a modification in a model’s instance we need to
execute some action. Django provides us with an elegant way to handle these
situations. The signals are utilities that allow associating events with
actions. We can develop a function that will run when a signal calls it.  
In models.py file of posts app where Post Model was defined, add this in the
same file:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

@receiver(pre_save, sender=Post)

def pre_save_receiver(sender, instance, *args, **kwargs):

 if not instance.slug:

 instance.slug = unique_slug_generator(instance)  
  
---  
  
 __

 __

The _pre_save_receiver_ function should be placed separately outside the Post
model.  

**Note:** In urls.py edit detail path with path(‘posts/’, detail). In views.py
edit the detail function with  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def detail(request, slug):

 q = Post.objects.filter(slug__iexact = slug)

 if q.exists():

 q = q.first()

 else:

 return HttpResponse('<h1>Post Not Found</h1>')

 context = {

 'post': q

 }

 return render(request, 'posts/details.html', context)  
  
---  
  
 __

 __

The last step is to add the link in HTML file <a href=”/posts/{{ a.slug }}”
class=”btn btn-primary”>View</a>. Now we are ready to go to
_127.0.0.1:8000/posts/title-you-have-added_ and it will show you the page
_details.html_.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

