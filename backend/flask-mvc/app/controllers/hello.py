"""
    Example Controllers
"""

from app import app
from flask import render_template, redirect, url_for
"""
    Import MOdels
from app.models.Hello import Hello
//Call HelloService
"""
#route index
@app.route('/', methods = ['GET'])
def index():
    data = {
        "title": "Hello World",
        "body": "Flask simple MVC"
    }
    return render_template('index.html.j2', data = data)
