arctic-bear
===========

Arctic backend with Flask

- Expose webservice standard APIs.
- Business logic handling.
- Communicate with database.
- Integrate with third-party application.
- ...

### Preparation
---

- Make [Homebrew](http://brew.sh) installed.

- Install MySQL and make it running.

    ```
    $ brew install mysql
    $ mysql.server start
    ```

- Install pip.

    ```
    $ sudo easy_install pip
    ```

- Install virtualenv and build dependencies.

    ```
    $ pip install virtualenv
    $ ./setenv.sh
    ```
- Start server

    ```
    $ make server
    ```

- Translation Text

    ```
    $ make babel-update
    $ make babel-compile
    ```

## TODO:

- Integrate Travis CI and auto deploy to Heroku.
