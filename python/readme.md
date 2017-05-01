Server Setup
===

Install mongodb using either brew or manually. Requires at least 3.2.0 release.

Create a `db` folder in the root of this repo. Then from the root of the repo, run:

```
mongod --dbpath db
```

Python side requires `flask`, `flask_pymongo`, `flask_cors`, `python-escpos`, and `pymongo`. Once these packages are installed, fill or reset the db with questions using:

```
python python/fillQuestions.py
```

Then, start the server using:

```
python python/server.py
```

I recommend using Robomongo for a Mongo GUI and Postman for POST/GET request testing.

Questions are located at `python/questions.csv`

API details can be found in [Google Doc](https://docs.google.com/document/d/1NBPKT-VvXealgVBVw30_xVoTiBgs9PkxJhbELzEFckg/edit).
