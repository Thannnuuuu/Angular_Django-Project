# Angular_Django-Project

# BACKEND
Firstly Run the project Download Visual Studio
 IN command Prompt Install Django
After install Django lets create the django Project
Create Django Project
    django-admin startproject EmployeeProject .
Lets Run the Project Using Following Command
    python manage.py runserver
Install Xampp
Now lets start the apache and mysql in Xampp control panel.
After that lets configure the database mysql.
    pip install pymysql
After that lets Upgrade the Version
    pip install pymysql --upgrade
After that go to mysql database i used in this example xampp server. and create the database employee.
Lets Create the Virtual Environment type the following command
    python -m my_venv Env
After run the command there is a folder created which name is my_venv.inside the my_venv folder there is file which is created Scripts. lets go inside the folder type the following command
     cd my_venv\Scripts
then need to activated so type the following command
     activate
Now you can see the Virtual Environment is activated successfully. then type the following command. come to backward
     cd ../..
Now you in the Virtual Environment lets install the Django again
     pip install django==3.2
After that will create the App which name is EmployeeApp
    python manage.py startapp EmployeeApp
Install the CORS
    pip install django-cors-headers
Install the Rest Framework
    pip install djangorestframework
Now Run the project using the following command
    python manage.py runserver


# FRONTEND
Installing Angular CLI
   npm install -g @angular/cli
After that create the new Project of Angular running by the following command
   ng new frond-end
After complete the installation then run the project using following command.
   ng serve
Now you see the Angular Welcome Page.
After that open the Angular project into VS code editor.
Creating a new Component Employee Crud
   ng g c crud
After that Run the Frontend using the following Command
   ng serve
