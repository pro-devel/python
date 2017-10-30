# What this folder is ? 

that's  my first python Project (Django).

Django version 2.1



# Installation 

1. Django

   go ahead to and install django 2.1 officially by 

   `pip install Django==2.0b1` at the time I write this code,

    when 2.1 become the latest official version  install will be 

   `pip install Django==2.1.x`  

   or download the latest version from github repo then navigate to the folder then 

   `pip install -e django/` where *django/* is the folder .


2. if you want to add, remove or edit models after you finish your code do :

   `python manager.py makemigration blog` where *blog* is your app name .

   then do `python manage.py migrate` now you are free to go .

3. you can manage your models and data from admin `https://root/admin` you can change url from `mysite/urls.py`.

   for creating a user to login use `python manage.py createsuperuser` then walk through .