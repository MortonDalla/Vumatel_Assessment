

1. cd and run pip install -r requirements.txt
1. Run the server-side Flask app in one terminal window:

    $ cd flask-vue-crud-master/server
    $ python3.7 -m venv env
    $ source env/bin/activate
    (env)$ python app.py
    ```

    Navigate to [http://localhost:5000](http://localhost:5000)

1. Run the client-side Vue app in a different terminal window:

    $ flask-vue-crud-master/client
    $ npm install
    $ npm run serve
    ```

    Navigate to [http://localhost:8080](http://localhost:8080)
