Blog Flask Backend

How to setup the project

Step 1: First Create Database named "blog" and Add Datbase URL to the .env file

Step 2: Now, Install the project requirements.
```
    pip install -r requirements.txt
```

Step 3: Initialize the DB and make migrations.
```
    flask db init && flask db migrate
```

Step 4: Now Apply Migrations to the Database.
```
    flask db upgrade
```

Step 5: Run the App
```
    flask run
```