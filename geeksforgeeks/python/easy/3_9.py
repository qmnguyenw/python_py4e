Prefetch_related and select_related functions in django



In Django, select_related and prefetch_related are designed to stop the deluge
of database queries that are caused by accessing related objects.In this
article we will see how it reduces number of queries and make program much
faster.

  * **select_related()** “follows” foreign-key relationships, selecting additional related-object data when it executes its query.
  *  **prefetch_related()** does a separate lookup for each relationship, and does the “joining” in Python.

One uses select_related when the object that you’re going to be selecting is a
single object, so OneToOneField or a ForeignKey. You use prefetch_related when
you’re going to get a “set” of things, so ManyToManyFields as you stated or
reverse ForeignKeys. Just to clarify what I mean by “reverse ForeignKeys” .

**Example to illustrate the concept of Prefetch_related and select_related –**

The above classification might be not so clear let see an example :

 __

 __  
 __

 __

 __  
 __  
 __

class A(models.Model):

 pass

 

class B(models.Model):

 a = ForeignKey(ModelA)

 

 

# Forward ForeignKey relationship

A.objects.select_related('a').all()

 

# Reverse ForeignKey relationship

A.objects.prefetch_related('modelb_set').all()   
  
---  
  
__

__

select_related obtains all data at one time through multi-table join
Association query, and improves performance by reducing the number of database
queries. It uses JOIN statements of SQL to optimize and improve performance by
reducing the number of SQL queries.The latter is to solve the problem in the
SQL query through JOIN statement. However, for many-to-many relationships, it
is not wise to use SQL statements to solve them, because the tables obtained
by JOIN will be very long, which will lead to the increase of running time and
memory occupation of SQL statements. The solution to prefetch_related() is to
query each table separately and then use Python to handle their relationship!

  

  

Here are some examples :

Models.py reads as follows:

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

 

class Province(models.Model):

 name = models.CharField(max_length = 10)

 def __unicode__(self):

 return self.name

 

class City(models.Model):

 name = models.CharField(max_length = 5)

 province = models.ForeignKey(Province)

 def __unicode__(self):

 return self.name

 

class Person(models.Model):

 firstname = models.CharField(max_length = 10)

 lastname = models.CharField(max_length = 10)

 visitation = models.ManyToManyField(City, related_name =
"visitor")

 hometown = models.ForeignKey(City, related_name = "birth")

 living = models.ForeignKey(City, related_name = "citizen")

 def __unicode__(self):

 return self.firstname + self.lastname  
  
---  
  
 __

 __

 **select_related –**

we use the select_related() function:

    
    
    >>> citys = City.objects.select_related().all()
    >>> for c in citys:
    ...   print c.province
    ...

There is only one SQL query, which obviously greatly reduces the number of SQL
queries:

    
    
    SELECT Optimize_city.id, Optimize_city.name,
    Optimize_city.province_id, Optimize_province.id, Optimize_province.name
    FROMOptimize_city
    INNER JOIN Optimize_province ON
    (Optimize_city.province_id=Optimize_province.id);

 **prefetch_related –**

Here we can see that Django uses INNER JOIN. I would like to clear one thing
that Optimize is a name of our app. If we want to get all the city names of
Hubei, we can do this:

    
    
    > HB=Province.objects.prefetch_related('city_set').get(name__iexact=u"Hubei Province")
    >>> for city in hb.city_set.all():
    ...   city.name
    ...

Triggered SQL queries:

    
    
    SELECT Optimize_province.id, Optimize_province.name
    FROM Optimize_province
    WHERE Optimize_province', name LIKE'Hubei Province';
    
    SELECT Optimize_city.id, Optimize_city.name, Optimize_city.province_id
    FROM Optimize_city
    WHERE Optimize_city.province_id IN (1);

As we can see, prefetch is implemented using the IN statement. In this way,
when there are too many objects in QuerySet, performance problems may arise
depending on the characteristics of the database.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

