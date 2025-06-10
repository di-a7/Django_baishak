<!-- install virtual environment -->
pip install virtualenv

<!-- create virtual environment -->
virtualenv env_name(env or venv)
(or)
python -m venv env_name

<!-- activate virtual environment -->
env\Scripts\activate(windows)
source env/Scripts/activate(linux)
source my_env/bin/activate(mac)

<!-- install django -->
pip install django

<!-- start project -->
django-admin startproject project_name . ('.' is optional)

<!-- start server -->
python manage.py runserver

<!-- create app -->
python manage.py startapp app_name