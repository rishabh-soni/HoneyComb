
<a href="https://honeycombiiti.pythonanywhere.com"><img alt="![Unable to load image]" src="https://github.com/rishabh-soni/Online_Resource_Sharing_Platform/blob/master/static/images/logohorizontal.png?raw=true"></a>
## Online Resource Sharing Platform

HoneyComb is an interactive platform for buying, selling, and renting any students' resources within a college community.
The project is made using **django** while **MySQL** is used for database management.

Visit our website [here](https://honeycombiiti.pythonanywhere.com) or alternatively by clicking on the link https://honeycombiiti.pythonanywhere.com

## Project Details
This is the course procject for CS-258 i.e., Software Engineering Lab

Group no. - P008

## Contributors
* Rahul Mahbubani - 190001050
* Rishabh Soni - 190001052
* Saket Kumar - 190001054

## Project Requirements (for local hosting)
* Python 3.8 and above
* MySQL server and MySQL Workbench (recommended 8.0 and above)
* Git

### To run the project on local server,
* Clone the remote repository on your system.
* Install all the dependencies by running the command:
```
pip install -r requirements.txt
```
* Create a new connection in MySQL Workbench and import the database from database.sql file in the **/sqldump** directory.
* Create a user in MySQL Workbench with the name **dbadmin** and leave the password field blank, granting all permissions to the user.
* Run the command:
```
python manage.py makemigrations
```
* Run the command:
``` 
python manage.py migrate
```
* Run the command and browse the corresponding URL provided.
```
python manage.py runserver
```

## Command to run test cases
Test cases can be run using the command:
```
python manage.py test
```

## ER diagram (database design)
![Untitled Document](https://user-images.githubusercontent.com/72018907/118021653-18000000-b379-11eb-8586-d0ae2401f1ac.png)

## User Manual
Find more details about interacting with the interface and setting up the project at local host: [P008_User_Manual.pdf](https://github.com/rishabh-soni/HoneyComb/files/6468000/P008_User_Manual.pdf)
