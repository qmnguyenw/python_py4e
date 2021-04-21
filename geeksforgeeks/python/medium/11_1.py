Customize Django Admin Interface



Django admin by default is highly responsive GUI, which offers various
features and an overall CRUD application to help developers and users.
Moreover, Django admin can be customized to fulfill one’s needs such as
showing fields on the home page of the table, etc. In this article, we will
discuss how to enhance Django-admin Interface.

Project structure looks like:  
![customize-django-admin-interface](https://media.geeksforgeeks.org/wp-
content/uploads/20200226140100/oie_t4ltkL0TqbSu.png)

Let us create an app called **state** which has one model with the same
name(state). When we register app to admin.py it shows like.

 **state/model.py**

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

from django.utils import timezone

 

class State(models.Model):

 name = models.CharField(max_length = 50)

 is_active = models.IntegerField(default = 1,

 blank = True,

 null = True,

 help_text ='1->Active, 0->Inactive', 

 choices =(

 (1, 'Active'), (0, 'Inactive')

 ))

 created_on = models.DateTimeField(default = timezone.now)

 updated_on = models.DateTimeField(default = timezone.now,

 null = True, 

 blank = True

 )

 def __str__(self):

 return self.name

 

 class Meta:

 db_table = 'state'  
  
---  
  
 __

 __

 **state/admin.py:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from .models import State

 

admin.site.register(State)  
  
---  
  
 __

 __

Check it in the django admin interface  
![django-admin-interface](https://media.geeksforgeeks.org/wp-
content/uploads/20200226140539/django-admin-dashboard.png)  
Now lets’ customize django admin according to available options.

#### Customize Django Admin Interface

 **1\. Change model name:**  
If you want to change name of model which is States here so open model.py file
and add verbose_name attribute in meta section.

 **state/model.py**

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

from django.utils import timezone

 

class State(models.Model):

 name = models.CharField(max_length = 50)

 is_active = models.IntegerField(default = 1,

 blank = True,

 null = True,

 help_text ='1->Active, 0->Inactive', 

 choices =(

 (1, 'Active'), (0, 'Inactive')

 ))

 created_on = models.DateTimeField(default = timezone.now)

 updated_on = models.DateTimeField(default = timezone.now,

 null = True, 

 blank = True

 )

 def __str__(self):

 return self.name

 class Meta:

 db_table = 'state'

 # Add verbose name

 verbose_name = 'State List'  
  
---  
  
 __

 __

 **Output :**  
![change model title](https://media.geeksforgeeks.org/wp-
content/uploads/20200226141845/modal_title.png)

 **2\. By default django admin shows only object name in listing.**

![admin-listing-page](https://media.geeksforgeeks.org/wp-
content/uploads/20200226142119/admin-listing-page.png)

One can show multiple fields data from model. Add some lines of code in your
admin.py file.

 **state/admin.py:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from .models import State

 

class StateAdmin(admin.ModelAdmin):

 list_display = ('name', 'active', 'created_on')

 

 def active(self, obj):

 return obj.is_active == 1

 

 active.boolean = True

 

admin.site.register(State, StateAdmin)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200226143031/admin-
listing-modify.png)

 **3\. By default there is only one option which is delete option.**  
One can add more option on Action dropdown:

 **state/admin.py:**

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.contrib import messages

from .models import State

 

class StateAdmin(admin.ModelAdmin):

 list_display = ('name', 'active', 'created_on')

 

 def active(self, obj):

 return obj.is_active == 1

 

 active.boolean = True

 

 def make_active(modeladmin, request, queryset):

 queryset.update(is_active = 1)

 messages.success(request, "Selected Record(s) Marked as Active
Successfully !!")

 

 def make_inactive(modeladmin, request, queryset):

 queryset.update(is_active = 0)

 messages.success(request, "Selected Record(s) Marked as Inactive
Successfully !!")

 

 admin.site.add_action(make_active, "Make Active")

 admin.site.add_action(make_inactive, "Make Inactive")

 

admin.site.register(State, StateAdmin)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200226144703/django-
admin-action-modify.png)

 **4\. Disable Delete option:**

 **state/admin.py:**

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.contrib import messages

from .models import State

 

class StateAdmin(admin.ModelAdmin):

 list_display = ('name', 'active', 'created_on')

 

 def active(self, obj):

 return obj.is_active == 1

 

 active.boolean = True

 

 def make_active(modeladmin, request, queryset):

 queryset.update(is_active = 1)

 messages.success(request, "Selected Record(s) Marked as Active
Successfully !!")

 

 def make_inactive(modeladmin, request, queryset):

 queryset.update(is_active = 0)

 messages.success(request, "Selected Record(s) Marked as Inactive
Successfully !!")

 

 admin.site.add_action(make_active, "Make Active")

 admin.site.add_action(make_inactive, "Make Inactive")

 

 def has_delete_permission(self, request, obj = None):

 return False

 

admin.site.register(State, StateAdmin)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200226145301/disable-
del-option.png)

 **5\. Remove Add option:**

 **state/admin.py:**

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from .models import State

 

class StateAdmin(admin.ModelAdmin):

 list_display = ('name', 'active', 'created_on')

 

 def active(self, obj):

 return obj.is_active == 1

 

 active.boolean = True

 

 def has_add_permission(self, request):

 return False

 

admin.site.register(State, StateAdmin)  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200226145516/remove_add_option.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

