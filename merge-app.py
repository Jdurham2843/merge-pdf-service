import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# creating the application
app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('MERGE SETTINGS', silent=True)

@app.route('/')
def index_page():
    return render_template('index.html')
