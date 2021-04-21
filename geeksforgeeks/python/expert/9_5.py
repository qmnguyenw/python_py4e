Python | User groups with Custom permissions in Django



Let’s consider a trip booking service, how they work with different plans and
packages. There is a list of product which subscriber gets on subscribing to
different packages, provided by the company. Generally, the idea they follow
is the level-wise distribution of different products.

Let’s see the different packages available on tour booking service :

  1.  **Starter plan** : In this package, subscriber will get the facility of non-AC bus travel and 1-day stay in a non-AC room only. Let’s say the trip is from Delhi to Haridwar(a religious place in Uttarakhand).
  2.  **Golden Plan** : It will be somewhat costly than the Starter Plan. In this plan, subscriber will be given 2-day stay in a non-AC room, travelling in a AC bus and the trip will be from Delhi to Haridwar, Rishikesh and Mussoorie.
  3.  **Diamond Plan** : This is the most costly plan, in which subscriber will be provided 3-day plan with AC bus and AC room stay, along with the trip to Haridwar, Rishikesh and Mussoorie and also trip to the Water Park.

Our main objective is to design and write code for the back-end in a very
efficient way(following the DRY Principle).

There are multiple methods of implementing this in Django but the most
suitable and efficient method is Grouping the Users and defining the
permissions of these groups . User of that particular group will automatically
inherit the permission of that particular group. Let’s define the User model
first :

Create a Django application **users**

