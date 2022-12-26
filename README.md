# swimsite
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --settings=swimsite.pro_settings
uwsgi --ini /home/tanaka/swimsite/swimsite/uwsgi.ini
```

```
ps -Af | grep wsgi
```