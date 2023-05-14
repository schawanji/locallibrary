# LocalLibrary

LocalLibrary is a Django project inspired by the [local library app tutorial](https://github.com/mdn/django-locallibrary-tutorial/) developed by [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction). The project features a catalogue app that allows users to manage and browse a local library's collection of books.

## Usage

To use the LocalLibrary app, follow the instructions below:

1. Activate the virtual environment (Windows):

```bash
python3 -m venv djangoenv
cd djangoenv/Scripts
activate
```

2. Clone the repository:

```bash
git clone https://github.com/schawanji/locallibrary.git
cd locallibrary/locallibrary
```

3. Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

4. Apply database migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

5. Create a superuser:

```bash
python3 manage.py createsuperuser
```

6. Run the development server:

```bash
python3 manage.py runserver
```

7. Access the app in your browser at [http://localhost:8000](http://localhost:8000).

8. Log in using the credentials you created with the `createsuperuser` command.

Feel free to explore the LocalLibrary app and manage the catalogue of books using its intuitive interface.

Note: Make sure you have Python 3.x and Django installed on your system before proceeding with the above steps.
