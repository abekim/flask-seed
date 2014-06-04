Flask seed app
=======

A simple task manager (aka. to-do list) built on Python's Flask microframework

### to-do's (irony much?)

- modularize into smaller chunks (templates, routes, models, etc.)
- use SASS

### Running it locally

Here are the steps for running the app locally

1. First, you need to clone the repo

    ```Shell
    $ git clone git@github.com:abekim/flask-seed 
    $ cd flask-seed
    ```

2. Download `pip` and `virtualenv`

    ```Shell
    $ sudo easy_install pip 
    $ sudo sudo pip install virtualenv
    ```

3. Optionally, install `foreman` Ruby gems

    ```Shell
    $ sudo gem install foreman
    ```

    If on Mac OS X, download the `pkg` file from [here](https://github.com/ddollar/foreman#foreman) and install it

4. Optionally, you can setup an isolated environment using `virtualenv`

    ```Shell
    $ virtualenv --no-site-packages env 
    $ source env/bin/activate
    ```

5. Install system dependencies. You may need to include `sudo` at the front of the command if on Linux

    ```Shell
    $ pip install -r requirements.txt
    ```

6. For a local instance of mongo, install mongodb by following these [instructions](http://docs.mongodb.org/manual/installation/)

7. Run the application locally

    If you've installed `foreman` earlier,

    ```Shell
    $ foreman start
    ```

    Otherwise,

    ```Shell
    $ python manage.py run
    ```

