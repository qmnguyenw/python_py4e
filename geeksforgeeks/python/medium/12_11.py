Data Visualization Using Chartjs and Django



 **Prerequisite :** django installation  
With the growth of data, data visualization in become a import part here we
will implement chart for our data in our web apps using chartjs with django.
_Django_ is a high-level Python Web framework based web framework and
_chartjs_ is an easy way to include animated, interactive graphs.

 **Modules required :**

  *  **django :** install django
  *  **djangorestframework**
    
        $ pip install djangorestframework

 **basic setup :**

Start a project by the following command –

    
    
    $ django-admin startproject charts

Change directory to charts –

  

  

    
    
    $ cd charts

Start the server- Start the server by typing following command in terminal –

    
    
    $ python manage.py runserver

To check whether the server is running or not go to a web browser and enter
_http://127.0.0.1:8000/_ as URL.

Now stop the server by pressing ctrl+C

 **Let’s create an app now.**

    
    
    $ python manage.py startapp chartjs

Goto chartjs/ folder by doing:

    
    
    $ cd chartjs

and create a folder with index.html file: templates/chartjs/index.html

    
    
    $ mkdir -p templates/chartjs && cd templates/chartjs && touch index.html

Open the project folder using a text editor. The directory structure should
look like this :  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20191228161323/Screenshot-from-2019-12-28-16-12-59.png)

Now add _chartjs_ app and _rest_framework_ in your charts in **settings.py**.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20191228161512/Screenshot-from-2019-12-28-16-14-53.png)

  

  

 **Edit urls.py file in charts :**

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.urls import path

from chartjs import views

 

urlpatterns = [

 path('admin/', admin.site.urls),

 path('', views.HomeView.as_view()),

 # path('test-api', views.get_data),

 path('api', views.ChartData.as_view()),

]  
  
---  
  
 __

 __

 **Edit views.py in chartjs :**

 __

 __  
 __

 __

 __  
 __  
 __

# from django.http import JsonResponse

 

from django.shortcuts import render

from django.views.generic import View

 

from rest_framework.views import APIView

from rest_framework.response import Response

 

class HomeView(View):

 def get(self, request, *args, **kwargs):

 return render(request, 'chartjs/index.html')

 

 

####################################################

 

## if you don't want to user rest_framework

 

# def get_data(request, *args, **kwargs):

#

# data ={

# "sales" : 100,

# "person": 10000,

# }

#

# return JsonResponse(data) # http response

 

 

#######################################################

 

## using rest_framework classes

 

class ChartData(APIView):

 authentication_classes = []

 permission_classes = []

 

 def get(self, request, format = None):

 labels = [

 'January',

 'February', 

 'March', 

 'April', 

 'May', 

 'June', 

 'July'

 ]

 chartLabel = "my data"

 chartdata = [0, 10, 5, 2, 20, 30, 45]

 data ={

 "labels":labels,

 "chartLabel":chartLabel,

 "chartdata":chartdata,

 }

 return Response(data)  
  
---  
  
 __

 __

Navigate to templates/chartjs/index.html and edit it.

 __

 __  
 __

 __

 __  
 __  
 __

<!DOCTYPE html>

<html lang="en" dir="ltr">

 

<head>

 <meta charset="utf-8">

 <title>chatsjs</title>

 <!-- Latest compiled and minified CSS -->

 <link rel="stylesheet"
href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

 

 <!-- jQuery library -->

 <script
src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

 

 <!-- Latest compiled JavaScript -->

 <script
src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

 

 

 

</head>

 

<body class="container-fluid">

 <center class="row">

 <h1>implementation of <b>chartJS</b> using
<b>django</b></h1>

 </center>

 <hr />

 <div class="row">

 <div class="col-md-6">

 <canvas id="myChartline"></canvas>

 </div>

 <div class="col-md-6">

 <canvas id="myChartBar"></canvas>

 </div>

 </div>

 

 <script
src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>

 

 <script>

 var endpoint = '/api';

 

 $.ajax({

 method: "GET",

 url: endpoint,

 success: function(data) {

 drawLineGraph(data, 'myChartline');

 drawBarGraph(data, 'myChartBar');

 console.log("drawing");

 },

 error: function(error_data) {

 console.log(error_data);

 }

 })

 

 

 function drawLineGraph(data, id) {

 var labels = data.labels;

 var chartLabel = data.chartLabel;

 var chartdata = data.chartdata;

 var ctx = document.getElementById(id).getContext('2d');

 var chart = new Chart(ctx, {

 // The type of chart we want to create

 type: 'line',

 

 // The data for our dataset

 data: {

 labels: labels,

 datasets: [{

 label: chartLabel,

 backgroundColor: 'rgb(255, 100, 200)',

 borderColor: 'rgb(55, 99, 132)',

 data: chartdata,

 }]

 },

 

 // Configuration options go here

 options: {

 scales: {

 xAxes: [{

 display: true

 }],

 yAxes: [{

 ticks: {

 beginAtZero: true

 }

 }]

 }

 }

 

 });

 }

 

 function drawBarGraph(data, id) {

 var labels = data.labels;

 var chartLabel = data.chartLabel;

 var chartdata = data.chartdata;

 var ctx = document.getElementById(id).getContext('2d');

 var myChart = new Chart(ctx, {

 type: 'bar',

 data: {

 labels: labels,

 datasets: [{

 label: chartLabel,

 data: chartdata,

 backgroundColor: [

 'rgba(255, 99, 132, 0.2)',

 'rgba(54, 162, 235, 0.2)',

 'rgba(255, 206, 86, 0.2)',

 'rgba(75, 192, 192, 0.2)',

 'rgba(153, 102, 255, 0.2)',

 'rgba(255, 159, 64, 0.2)'

 ],

 borderColor: [

 'rgba(255, 99, 132, 1)',

 'rgba(54, 162, 235, 1)',

 'rgba(255, 206, 86, 1)',

 'rgba(75, 192, 192, 1)',

 'rgba(153, 102, 255, 1)',

 'rgba(255, 159, 64, 1)'

 ],

 borderWidth: 1

 }]

 },

 options: {

 scales: {

 yAxes: [{

 ticks: {

 beginAtZero: true

 }

 }]

 }

 }

 });

 }

 </script>

</body>

 

</html>  
  
---  
  
 __

 __

 **Make migrations and migrate it :**

    
    
    $ python manage.py makemigrations
    $ python manage.py migrate
    

**Now you can run the server to see your app :**

    
    
    $ python manage.py runserver

![](https://media.geeksforgeeks.org/wp-
content/uploads/20191228162017/img44.png)

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

