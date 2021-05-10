
<a href="https://honeycombiiti.pythonanywhere.com"><img alt="![Unable to load image]" src="https://github.com/rishabh-soni/Online_Resource_Sharing_Platform/blob/master/static/images/logohorizontal.png?raw=true"></a>
## Online Resource Sharing Platform

HoneyComb is an interactive platform for buying, selling, and renting any students' resources within a college community.
The project is made using **django** while **MySQL** is used for database management.

## Project Requirements (for local hosting)
* Python 3.8 and above
* MySQL server and MySQL Workbench (recommended 8.0 and above)
* Git

### To run the project on local server,
* Clone the remote repository on your system.
* Install all the dependencies by running the command **pip install -r requirements.txt**
* Create a new connection in MySQL Workbench and import the database from database.sql file in the **/sqldump** directory.
* Run the command **python manage.py makemigrations**
* Run the command **python manage.py migrate**
* Run the command **python manage.py runserver** and browse the corresponding URL provided.
* Create a user in MySQL Workbench with the name **dbadmin** and leave the password field blank.
* Granting all permissions to the user.
