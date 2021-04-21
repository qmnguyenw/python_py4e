Make PWA of a Django Project



Progressive Web Apps or PWA are a type of application that is developed using
web technologies and can be installed on any device like a normal application.

**Prerequisites:** A django project that is ready to be deployed. For Django
tutorial you can refer the following link
https://www.geeksforgeeks.org/django-tutorial/

The below steps have to be followed to create a progressive web application of
a Django project.

 **STEP 1:** Firstly use the following command to install django pwa

    
    
    pip install django-pwa
    
    

**STEP 2:** In **settings.py** of project inside installed apps section add ‘
**pwa** ’ and in **urls.py** of project give the following path –  

  

  

    
    
    path(“, include(‘pwa.urls’))
    
    

**settings.py**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200918155401/1-660x390.png)

 **urls.py**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200918160001/2-660x376.png)

 **STEP 3:** In the js folder, create a file named **serviceworker.js** and
add the following code to it.

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {

 event.waitUntil(

 caches.open(staticCacheName).then(function(cache) {

 return cache.addAll([

 '',

 ]);

 })

 );

});

self.addEventListener('fetch', function(event) {

 var requestUrl = new URL(event.request.url);

 if (requestUrl.origin === location.origin) {

 if ((requestUrl.pathname === '/')) {

 event.respondWith(caches.match(''));

 return;

 }

 }

 event.respondWith(

 caches.match(event.request).then(function(response) {

 return response || fetch(event.request);

 })

 );

});  
  
---  
  
 __

 __

 **STEP 4:** Now in settings.py add the path to service worker as
**PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, ‘static/js’,
‘serviceworker.js’).**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200918162140/3-660x276.png)

  

  

 **STEP 5:** Now to create manifest.json file go into settings file of your
Django Project and add rhe following details. Django will automatically builds
the manifest.json for your project

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

PWA_APP_NAME= 'geeksforgeeks'

PWA_APP_DESCRIPTION = "GeeksForGeeks PWA"

PWA_APP_THEME_COLOR = '#000000'

PWA_APP_BACKGROUND_COLOR = '#ffffff'

PWA_APP_DISPLAY = 'standalone'

PWA_APP_SCOPE = '/'

PWA_APP_ORIENTATION = 'any'

PWA_APP_START_URL = '/'

PWA_APP_STATUS_BAR_COLOR = 'default'

PWA_APP_ICONS = [

 {

 'src': 'static/images/icon-160x160.png',

 'sizes': '160x160'

 }

]

PWA_APP_ICONS_APPLE = [

 {

 'src': 'static/images/icon-160x160.png',

 'sizes': '160x160'

 }

]

PWA_APP_SPLASH_SCREEN = [

 {

 'src': 'static/images/icon.png',

 'media': '(device-width: 320px) and (device-height: 568px) and
(-webkit-device-pixel-ratio: 2)'

 }

]

PWA_APP_DIR = 'ltr'

PWA_APP_LANG = 'en-US'  
  
---  
  
 __

 __

 **STEP 6:** Add {% load pwa %} and {% progressive_web_app_meta %} in index or
first page of the project.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200918165126/5-660x377.png)

**STEP 7:** Right click on browser and choose inspect element option. In the
application section you will see that manifest file and service worker file
are present there.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200918172751/6-257x300.png)![](https://media.geeksforgeeks.org/wp-
content/uploads/20200918172852/7-300x189.png)

 **STEP 8:** Our PWA is ready to be installed now. You will see the install
icon in the address tab.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200918173116/5-660x371.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

