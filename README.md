# locallibrary

This django project is inspired by the local library app developed by https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction tutorial.

It has a catalogue app


# To use app 

```bash
# activate virtual environment Windows

python3 -mvenv djangoenv
cd djangoenv/Scripts
activate 

# 

git clone https://github.com/schawanji/locallibrary.git
cd locallibrary\locallibrary

pip3 install -r requirements.txt
python3 manage.py  makemigrations
python3 manage.py  migrate
python3 manage.py  runserver
```
App is running on http://localhost:8081/catalog/ 

username: admin
password: admin

