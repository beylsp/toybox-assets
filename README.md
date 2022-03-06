# HTTP assets server

A JSON Restful API for storing and serving assets.

These assets can be binary files or structured data retrieved from a database.

## Local Development

First, prepare the project:

``` bash
$ make setup                                # Prepare the project
```

The simplest way to run the site makes use of SQLite, which is not the same as production where it will use PostgreSQL:

``` bash
$ make init                                 # Provision the database
```

To interact with the assets server, you'll need to generate an authentication token:

``` bash
$ pipenv run flask token create devtoken     # Create a token
Loading .env environment variables...
Token created: devtoken - a8348f736e834f99b460e0813a750a14
```

Save the output token.

``` bash
$ pipenv run flask run                       # Run the development server
```

Upon invoaction, `pipenv` automatically loads environment variables from a file named `.env`:

``` bash
$ cat .env
FLASK_RUN_PORT=8017
FLASK_DEBUG=1
FLASK_APP=app:app
```

You can now access this token in your requests to the assets server API - e.g.: 

``` bash
http://0.0.0.0:8017/api/v1/tokens?token=a8348f736e834f99b460e0813a750a14  # List all existing tokens in JSON format
```

Whenever you make any changes to the database scheme, don't forget to run the migrations script:

``` bash
$ pipenv run flask deploy
```

If you prefer not to use the `pipenv` wrapper, you need to activate the virtual environment:

``` bash
$ pipenv shell                               # Activate virtual environment
$ flask run                                  # Run the development server
```

Type `deactivate` to exit the virtual environment:

``` bash
$ deactivate
```

### Using PostgreSQL

``` bash
# Spin up a Docker postgresql database
$ docker run --rm --name db -e POSTGRES_PASSWORD=pw -d postgres

# Configure the database location
$ export DEV_DATABASE_URL=postgres://postgres:pw@`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db`/postgres

# Provision the database
pipenv run flask db upgrade

# Create a token
pipenv run flask token create devtoken
```

Now save the token that's output, and run the site with:

``` bash
pipenv run flask run                         # Run the development server
```

You can now access the API with your token in your browser - e.g.:

```
http://0.0.0.0:8017/api/v1/tokens?token=a8348f736e834f99b460e0813a750a14  # List all existing tokens in JSON format
```
