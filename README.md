# User_Profile_Module
Implemented a User Profile System for a Job Portal Project using Flask and PostGresSQL
Here are the steps to run the Project
Step 1

Create a Enviornment Variable (Create Enviornment Variable Using Conda and venv here is the example using Conda)
python version = 3.10.13
conda create -n yourenvname python=x.x
Activate Variable Using command
conda activate yourenvname

Step 2

Install the required libraries
pip install -r requirements.txt

Step 3
In app.py
in the following line edit the "username","password","port","databasename" as per your own dbms
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://username:password@localhost:port/databasename"

Step 4
Restore database from "job_portal.tar" file provided using pgAdmin or PSQL

Step 5
Run the application using terminal using command python app.py

Something about project:
Logic is present in app.py the classes are created in models.py and some functions are present in functions.py
The edit functionality is yet to be completed
