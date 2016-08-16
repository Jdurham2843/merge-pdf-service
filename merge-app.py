import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['pdf'])
UPLOAD_FOLDER = 'uploads/'

# creating the application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config.from_envvar('MERGE SETTINGS', silent=True)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# helper functions
def allowed_file(filename):
    """checks to see if the file has the correct extension"""
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'GET':
        flash('sup buddy')
        return render_template('index.html')

    elif request.method == 'POST':
        files = request.files.getlist('file[]', None)
        filenames = []
        if not files:
            flash('No file part')
            abort(404)
        for file in files:
            if allowed_file(file.filename):
                filenames.append(file.filename)
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
            else:
                abort(404)
        flash(filenames)
        return render_template('index.html')
