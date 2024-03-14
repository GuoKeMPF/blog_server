# create project

django-admin startproject websist

# start project

python manage.py runserver

# update datebase

python manage.py makemigrations

# update model

python manage.py migrate

# create model

python manage.py startapp XXX

# create user

python manage.py createsuperuser

# create dependence to requirements.txt

pip freeze > requirements.txt

# install dependence form requirements.txt

pip install -r requirements.txt



# clear session

django manage.py clearsessions