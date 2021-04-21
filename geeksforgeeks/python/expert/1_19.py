Google Cloud Platform – Running Different Versions of Python on Google Cloud
Run



 **Problem Statement:**

Rinki works for StoreCraft(Say) as a site reliability engineer, where she’s
on-call maintaining their custom storefront. StoreCraft’s systems are
developed in-house in Python and have been running on virtual machines for
years, a set up that evolved as StoreCraft’s businesses did. These virtual
machines use slightly different versions of Python. This is causing extra pain
and work for Rinki and her team. Rinki is looking for a way to reduce this
pain by updating all the components to current Python and also migrating away
from virtual machines onto something more scalable, like serverless.
StoreCraft is about to launch a new recommendation engine, which is written
using Python 3.8 (the latest version in 2020). However, it has a dependency on
the _sweet-ldap package_ , which doesn’t yet support Python 3.

Rinki knows that this upgrade will take time. And her team needs to make sure
the existing system keeps running. How will Rinki solve this problem on GCP?

 **Solution:**

She realizes that she can best achieve this by completing the upgrade in two
steps. First, moving to serverless, then making the language upgrades. As
StoreCraft is about to launch a new recommendation engine, which is written
using Python 3.9. Rinki sees this as the perfect candidate to deploy a
serverless by skipping the virtual machine altogether. Looking at the options
available on Google Cloud, Rinki sees that while she could deploy on **Cloud
Functions** , she would be forced to use only specific versions of Python.
However, she sees that the newest serverless offering from Google Cloud,
called **Cloud Run** , doesn’t have this limitation.

  

  

![](https://media.geeksforgeeks.org/wp-content/uploads/20210108050506/105.PNG)

So she chooses to deploy there instead. Creating this service on Cloud Run,
Rinki has complete control over the container. Making use of the official
Python images on the **Docker hub** , she can pick the exact version of
Python(ie, Python 3.8) she needs down to the patch level by specifying the
base image in the front line of the _Dockerfile_. As each Cloud Run service is
based on its own container image, which is each defined by its own Docker
file, Rinki has complete control over the languages used in each part of her
setup.

Since each Cloud Run service has this level of isolation, Rinki can move each
of them to Cloud Run one at a time. She is also able to maintain the services
running on the original virtual machines until the team has the availability
to upgrade.

It has a dependency on the _sweet-ldap package_ , which doesn’t yet support
Python 3. Rinki is able to keep the service running on the now deprecated
Python 2.7 by specifying the latest version of Python 2 in the Docker file as
shown below:

    
    
    $ cat sweet-ldap/setup.py
    ...
     classifiers = [
                    'Programming Language : : Python : : 2.7'
                   ]
    ...
    $ head Dockerfile
    From python : 2.7.18 #final

As soon as the _sweet-ldap package_ has Python 3 support, Rinki can test this
new version by gradually rolling out a new revision of the service using the
**traffic splitting** feature of Cloud Run.

![](https://media.geeksforgeeks.org/wp-content/uploads/20210108050839/107.PNG)

She can set the new revision of the count service to, say, service only 5% of
visitors, that way only some of her customers end up using the new code. If
she notices that something isn’t working as intended, she can easily rollback
to the old version. By migrating each service in turn, Rinki is able to
control them in isolation, allowing for a more incremental upgrade process and
a more reliable environment.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

