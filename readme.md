```
python manage.py makemigrations blog
python manage.py migrate blog
```
```
python manage.py createsuperuser
```

# Heroku configuration

Нам необходимо внести следующие изменения в наш проект доски объявлений, чтобы 
развернуть его в интернете:

• обновить Pipfile.lock
• новый Procfile
• установить gunicorn
• обновить settings.py

В вашем Pipfile укажите версию Python мы используем 3.8 Добавьте эти две строки в 
конец файла.
Code
# Pipfile
[requires]
python_version = "3.8"
Запустите pipenv lock для создания соответствующего Pipfile.lock.