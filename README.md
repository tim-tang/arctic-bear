       _____                     __   .__          __________                         
      /  _  \  _______   ____  _/  |_ |__|  ____   \______   \  ____  _____   _______ 
     /  /_\  \ \_  __ \_/ ___\ \   __\|  |_/ ___\   |    |  _/_/ __ \ \__  \  \_  __ \
    /    |    \ |  | \/\  \___  |  |  |  |\  \___   |    |   \\  ___/  / __ \_ |  | \/
    \____|__  / |__|    \___  > |__|  |__| \___  >  |______  / \___  >(____  / |__|   
            \/              \/                 \/          \/      \/      \/         

----

Arctic backend with Flask

- Expose webservice standard APIs.
- Business logic handling.
- Communicate with database.
- Integrate with third-party applications.
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
