import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, send_from_directory, current_app
from werkzeug.utils import secure_filename

import merge

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
        return render_template('index.html')

    elif request.method == 'POST':
        os.remove('uploads/merged.pdf')
        files = request.files.getlist('file[]', None)
        filenames = []
        flash_message = ''
        file_was_merged = False
        if not files:
            flash('No file part')
            return render_template('index.html', file_was_merged=file_was_merged)
        for file in files:
            if allowed_file(file.filename):
                filenames.append(file.filename)
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
            else:
                flash_message = '%s is of a file type that is not allowed.' % (file.filename)
        file_list_ordered = request.form.get('merge-order').split(',')
        file_list_ordered = merge.format_files(file_list_ordered)

        if flash_message == '' and file_list_ordered != '':
            try:
                merge.merge(file_list_ordered)
            except Exception as e:
                flash_message = str(e)
            else:
                file_was_merged = True

        if flash_message:
            flash(flash_message)
        else:
            uploads = os.path.join(os.path.dirname(os.path.realpath(__file__)),  app.config['UPLOAD_FOLDER'])
            flash(uploads)
        return render_template('index.html', file_was_merged=file_was_merged)

@app.route('/download/', methods=['GET'])
def download_file():
    #uploads = os.path.join(current_app.root_path,  app.config['UPLOAD_FOLDER'])
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename='merged.pdf', as_attachment=True)
