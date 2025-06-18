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

<!-- create migration file -->
python manage.py makemigrations

<!-- changes in database using makemigration file -->
python manage.py migrate

<!-- open shell -->
python manage.py shell

<!-- list all objects of class/models -->
model_name.objects.all()

<!-- create ojects/data -->
model_name.objects.create(name = "asjdkl", descriptoin = "skjdfkj")

model_name.objects.all().values()

<!-- single data fetch -->
a = model_name.objects.get(id = 5)

<!-- update -->
a.title = "new data"
a.save()

<!-- delete -->
a.delete()

<!-- to filter the objects -->
model_name.objects.filter(field1 = "data", field2 = "data", field3~ = "data")

<!-- create superuser -->
python manage.py createsuperuser