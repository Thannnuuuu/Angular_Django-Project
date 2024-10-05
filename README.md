# Angular_Django-Project

# BACKEND
STEP1: Firstly Run the project Download Visual Studio...



STEP2: IN command Prompt Install Django..




STEP3: After install Django lets create the django Project




STEP4: Create Django Project  ::
       django-admin startproject EmployeeProject .



       
STEP5: Lets Run the Project Using Following Command  ::
       python manage.py runserver



       
STEP6: Install Xampp..




STEP7: Now lets start the apache and mysql in Xampp control panel.




STEP8: After that lets configure the database mysql  ::
     pip install pymysql



     
STEP9: After that lets Upgrade the Version::
       pip install pymysql --upgrade



       
STEP10: After that go to mysql database i used in this example xampp server. and create the database employee.




STEP11: Lets Create the Virtual Environment type the following command::
        python -m my_venv Env



        
STEP12: After run the command there is a folder created which name is my_venv.inside the my_venv folder there is file which is created Scripts. lets go inside the folder type the following command::
        cd my_venv\Scripts



        
STEP13: then need to activated so type the following command::
     activate



     
STEP14: Now you can see the Virtual Environment is activated successfully. then type the following command. come to backward::
        cd ../..



        
STEP15: Now you in the Virtual Environment lets install the Django again::
        pip install django==3.2



        
STEP16: After that will create the App which name is EmployeeApp::
        python manage.py startapp EmployeeApp



        
STEP17: Install the CORS::
        pip install django-cors-headers



        
STEP18: Install the Rest Framework::
        pip install djangorestframework



        
STEP19: Now Run the project using the following command::
     python manage.py runserver


# FRONTEND
STEP1: Installing Angular CLI::
       npm install -g @angular/cli



       
STEP2: After that create the new Project of Angular running by the following command::
       ng new frond-end



       
STEP3: After complete the installation then run the project using following command::
       ng serve



       
STEP4: Now you see the Angular Welcome Page.




STEP5: After that open the Angular project into VS code editor.




STEP6: Creating a new Component Employee Crud::
       ng g c crud



       
STEP&: After that Run the Frontend using the following Command::
        ng serve






End
