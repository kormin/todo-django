release: python manage.py makemigrations tasks
release: python manage.py migrate
web: gunicorn todo.wsgi --log-file -