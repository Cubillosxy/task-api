# task-api
API Rest 


## get started

 - git clone https://github.com/Cubillosxy/task-api.git
 - cd task-api
 - run with docker or virtualenv


## run project with virtualenv

 - create virtual env python 3
 - install requirements `pip install -r requirements.txt`
 - create local_settings.py and ser `SECRET_KEY, ALLOWED_HOSTS`
 - run test `python manage.py test`
 
### test data
  - username: **test**
  - password: **testdemo**
  - admin url `/secret-4dm1n/`
  
  - get token `http post http://127.0.0.1:8000/login/ username=test password=testdemo`
  - list tasks `http get http://127.0.0.1:8000/api/`
  



 
 