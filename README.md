API with FastAPI

CRUD Categories and products

Products with Psycopg

Categories with Sqlalchemy


## How to run the code
- Create a ```DATABASE_URL``` variable in a ```.env``` file. This must be a Postgresql database URI.
- Install all project requirements from the ```requirements.txt``` file using ```pip install -r requirements.txt```
- Create the database by running ``` python create_db ```
- Finally run your server with ```uvicorn main:app```

options to run

Run app
uvicorn main:app 

Run app with specific port
--port 5000

Run app with detect changes
--reload 

Access by Other device
--port 0.0.0.0