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

################################################################################
django blog
===========

.. code:: shell

   python manage.py makemigrations blog
   python manage.py migrate blog

.. code:: shell

   python manage.py createsuperuser

Heroku configuration
--------------------

``project_name=mysite``

| Нам необходимо внести следующие изменения в наш проект доски
  объявлений, чтобы
| развернуть его в интернете:

| [STRIKEOUT:• обновить Pipfile.lock]
| • новый **Procfile**
| • установить **gunicorn**
| • обновить **settings.py**

| [STRIKEOUT:В вашем Pipfile укажите версию Python мы используем 3.8
  Добавьте эти две строки в]
| [STRIKEOUT:конец файла.]
| \`\ [STRIKEOUT:# Pipfile]
| [STRIKEOUT:[requires]]
| [STRIKEOUT:python_version = "3.8"]
| [STRIKEOUT:Запустите pipenv lock для создания соответствующего
  Pipfile.lock.]
| [STRIKEOUT:(mb) $ pipenv lock]

Затем создайте **Procfile**, который указывает **Heroku**, как запустить
удаленный сервер.

``touch Procfile``

| Теперь мы укажем **Heroku** использовать **gunicorn** в качестве
  нашего рабочего сервера и
| посмотреть в наш **mb_project.wsgi** файл для получения дальнейших
  инструкций.

``web: gunicorn ${mb_project}.wsgi --log-file -``

| Далее установим **gunicorn** который мы будем использовать для
  **production** но при этом
| используя внутренний сервер **Django** для локальной разработки.

``pipenv install gunicorn``

Наконец, обновите **ALLOWED_HOSTS** в нашем файле **settings.py**

``# mb_project/settings.py``

``ALLOWED_HOSTS = ['*']``

| Все мы закончили! Добавьте и зафиксируйте наши новые изменения в
  **git**, а затем
| отправьте их в **Bitbucket.**

.. code:: shell

   (mb) $ git status
   (mb) $ git add -A
   (mb) $ git commit -m 'New updates for Heroku deployment'
   (mb) $ git push -u origin maste

Heroku развертывание 
--------------------

**Убедитесь, что вы вошли в свою учетную запись Heroku**

``heroku login``

| Затем запустите команду heroku create и Heroku случайным образом
  сгенерирует для вас имя приложения. Вы сможете настроить это позже,
  если будет необходимо.
| ``heroku create``

| Настройте **git** на использование имени вашего нового приложения,
  когда вы отправляете код на **Heroku**. Мое сгенерированное имя
  **Heroku** это {{project_name}} поэтому команда выглядит следующим
  образом
|  ``heroku git:remote -a {{project_name}}``

| Укажите Heroku игнорировать статические файлы, которые мы подробно
  рассмотрим при развертывании нашего приложения блога в книге позже.
|  ``heroku config:set DISABLE_COLLECTSTATIC=1``

Отправьте код в **Heroku** и добавьте бесплатное масштабирование, чтобы
он действительно работал в интернете, иначе код просто сидит там.

.. code:: 

   git push heroku master 
   heroku ps:scale web=1 

Если вы откроете новый проект ``heroku open``, он автоматически запустит
новое окно браузера с URL вашего приложения. Мой находится по адресу:
https://agile-inlet-25811.herokuapp.com

.. _™-easyquest:

™ EasyQuest
~~~~~~~~~~~
##########################################################################

Мы можем следовать предложению Django и добавить get_absolute_url в нашу модель. Это 
лучшая практика, которую вы всегда должны делать. Он устанавливает канонический URLадрес для объекта, поэтому, даже если структура ваших URL-адресов изменится в будущем, 
ссылка на конкретный объект будет одинаковой. Короче говоря, вы должны добавить 
get_absolute_url() и __ str_ _ () метод к каждой модели, которую вы пишете.