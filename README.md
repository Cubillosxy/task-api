# task-api
API Rest 


## get started

 - git clone https://github.com/Cubillosxy/task-api.git
 - cd task-api
 - run with docker or virtualenv
 - create task_api/local_settings.py and set `SECRET_KEY, ALLOWED_HOSTS` 

## docker 

 - cd task-api
 - `docker-compose build`
 - `docker-compose up`

## run project with virtualenv

 - create virtual env python 3
 - install requirements `pip install -r requirements.txt`
 - run test `python manage.py test`
 
### test data
  - username: **test**
  - password: **testdemo**
  - admin url `/secret-4dm1n/`
  
  - get token `http post http://127.0.0.1:8000/login/ username=test password=testdemo` or 
  - list tasks `http get http://127.0.0.1:8000/api/`
  
  
  



 
 