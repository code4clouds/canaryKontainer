#!/usr/bin/python3

import os
from flask import Flask, render_template, request, current_app, json
from flask_api import status
import requests

app = Flask(__name__)  # Instantiate Flask

''' Configure app.config, otherwise use defaults '''
app.config['PORT'] = os.getenv('PORT', 5000)

@app.route('/', methods=['GET'])
def root():
    ''' Read the root document and load form'''
    return current_app.send_static_file('index.html')


@app.errorhandler(404)
def page_not_found(request):
    ''' Page no found message '''
    return render_template('404.html')


@app.errorhandler(500)
def internal_server_error():
    ''' Server error message '''
    return render_template('500.html')


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            threaded=True,
            port=int(app.config['PORT']),
            ssl_context=None  # self-sign cert
        )