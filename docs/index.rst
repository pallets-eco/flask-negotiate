.. Flask-Negotiate documentation master file, created by
   sphinx-quickstart on Thu Jul 19 11:37:23 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: ../README.rst


Install
-------

Install with pip::

    $ pip install Flask-Negotiate


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
        return 'consumes json only'

Setup a route that will only allow an `Accept` header of `application/json`,
otherwise return a HTTP 406 (Unacceptable) error::

    @app.route('/accepts_json_only')
    @produces('application/json')
    def consumes_json_and_html():
        return 'produces json only'

If you want to specify more than one Content-Type or Accept header just
pass additional paramters::

    @consumes('application/json', 'text/html')
    def route():
        ...


Changelog
=========

.. toctree::
   :maxdepth: 2

   changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

