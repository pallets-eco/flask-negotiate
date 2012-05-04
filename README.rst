Flask-Negotiate
===============

Content negotiation utility for Flask apps

Usage
-----

Create an app::

    from flask import Flask
    from flask_negotiate import consumes, produces

    app = Flask(__name__)
    

Setup a route that will only consume requests with a `Content-Type` of 
`application/json`, otherwise return a HTTP 415 (Unsupported Media Type)
error::

    @app.route('/consumes_json_only')
    @consumes('application/json')
    def consumes_json_only():
        return 'json only'

Setup a route that will only allow an `Accept` header of `application/json`,
otherwise return a HTTP 406 (Unacceptable) error::

    @app.route('/accepts_json_only')
    @produces('application/json')
    def consumes_json_and_html():
        return 'json and html'

If you want to specify more than one Content-Type or Accept header just
pass additional paramters::

    @consumes('application/json', 'text/html')
    def route():
        ...

Install
-------

Installation is simple too::

    $ pip install Flask-Negotiate