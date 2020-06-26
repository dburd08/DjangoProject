# DjangoProject



requirements

Use Django to create an app with:

A lightweight database (if possible, MongoDB is ideal)
A logic layer that calls a data-rich API (Yummly, Napa, etc.) and stores data from different endpoints in the database
A simple text search feature that allows users to find keywords/phrases from the stored data

### Endpoints:
/index - loads data from MTG api into mondoDB
/      - landing page with search form and search operators
/searchRults - shows the search results of from user input

### App start up
Start mongo db using **mongod** command in a terminal window

Start the django app using **python manage.py runserver** in directory with the *manage.py* in a new terminal window
Navigate to **localhost:8000/index** in a browser to load magic card and set data into the mongo database

Naviagte to **localhost:8000/** in a browser to see the search form. Using the search syntax provided preform a search, you will be redirected to a results page




