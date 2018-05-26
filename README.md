
prerequisite: Python3,pip3,Django 2.0.5 ,Ubuntu/Mac terminal
Since this project has been done on Python3 running with Python2 or Lower may prop up fatal errors
Here is the link to the git repository.
Install Python3,pip3,Django2.0.5,django-admin
You need to clone the file and do cd Movie in terminal
do ls and search for manage.py file 
Create a super-user using the command >>python3 manage.py createsuperuser
Enter the name and the password to create the superuser.
Perform the migrations to create the DB according the CRUD provided.
>>python3 manage.py makemigrations
>>python3 migrate
After creating the super user you and run the project by typing the command >>python3 manage.py runserver
By default the server will run on 127.0.0.1:8000
to view the Admin Page enter url as 127.0.0.1:8080/admin
create entries for the gender(male and female)
create entries for the tables Actors,Movies,Producers,ActorMovie
the Dashboard page is 127.0.0.1:8000/imdb
all the functionalities are listed here.
Each column in 127.0.0.1:8000/admin sorting mechanism is provided.
Moreover filters are also provided so that are can sort the required data accordingly.
Date Selector is provided for selecting the appropriate date from the pop-up
