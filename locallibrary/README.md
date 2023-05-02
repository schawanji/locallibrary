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
python3 manage.py  runserver 8081
```
App is running on http://localhost:8081/catalog/ 

username: admin
password: hp

## 4 user groups with different priviledges 

* admin
* libraians 
* members 
* anonymous

 anonymous Search functionality for authors and books and view catalogue
members  :
* Search functionality for authors and books, 
* View information about authors and books
* borrow and return books 
* See a list of books that they have borrowed including return date
* change passwords and update user information(inprogress)
libraians add and update  new books and authors and renew books
admin everything 
