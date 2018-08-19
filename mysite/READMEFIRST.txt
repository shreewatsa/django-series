Prerequisite : XAMPP , Python, Django, Web browser, Text editor, CLI .

Must know commands for Django :

 1) Installing must have applications : pip install django , mysqlclient
 2) Confirm successful installation : 
    - $ python -m django --version
    - print(django.get_version()) in script.
3) Create project : $ django-admin startproject mysite
4) Navigating to project folder : $ cd mysite
5) Running server : $ python manage.py runserver <port_num : optional>
6) Setting admin login credentials : $ python manage.py createsuperuser --username=shreewatsa --email=shreewatsa@gmail.com
7) Pinging web server : http://<localhost or 127.0.0.1>:8080/admin
8) Create new app : $ python manage.py startapp <app-name>
9) Map models to database tabels : $ python manage.py migrate
10) Checking errors before migration : $ python manage.py check
11) Actual migration : $ python manage.py makemigrations <app-name>
12) Inspection after migration : $ python manage.py sqlmigrate <app-name> <0001 : number in filename created after migration>
