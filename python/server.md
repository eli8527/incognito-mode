Server Setup
===

Install mongodb using either brew or manually. Requires at least 3.2.0 release.

Create a `db` folder in the root of this repo. Then from the root of the repo, run:

```
mongod --dbpath db
```

Python side requires `Flask`, `Flask-PyMongo` and `PyMongo`. Once these packages are installed, fill the db with some fake data using: 

```
python python/filldb.py
```

Then, start the server using:

```
python python/server.py
```

I recommend using Robomongo for a Mongo GUI and Postman for POST/GET request testing.

API details can be found in [Google Doc](https://docs.google.com/document/d/1NBPKT-VvXealgVBVw30_xVoTiBgs9PkxJhbELzEFckg/edit).