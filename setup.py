"""
Flask-Negotiate
===============

Content negotiation utility for Flask apps.


Resources
---------

- `Documentation <http://packages.python.org/Flask-Negotiate/>`_
- `Issue Tracker <http://github.com/mattupstate/flask-negotiate/issues>`_
- `Code <http://github.com/mattupstate/flask-negotiate/>`_
- `Development Version
  <http://github.com/mattupstate/flask-negotiate/zipball/develop#egg=Flask-Negotiate-dev>`_

"""
from setuptools import setup

setup(
    name='Flask-Negotiate',
    version='0.1.0',
    url='https://github.com/mattupstate/flask-negotiate',
    license='MIT',
    author='Matthew Wright',
    author_email='matt@nobien.net',
    description='Content negotiation utility for Flask apps',
    long_description=__doc__,
    py_modules=['flask_negotiate'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)