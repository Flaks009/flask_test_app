
import os
import json
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, TestForm, UploadForm
from app.db import insert, list_db_sql
from werkzeug.utils import secure_filename

@app.route('/')
@app.route('/index')
def index():
    rpi = open('/home/ubuntu/flask_test_app/app/json_files/rpi.json')
    rpi = json.load(rpi)
    return render_template('index.html', title = 'Home', rpi = rpi)

@app.route('/login', methods = ['GET', 'POST'])
def login():

    form = LoginForm()
    if  form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign in', form = form)

@app.route('/form_test', methods = ['GET', 'POST'])
def form_test():

    form = TestForm()
    if form.validate_on_submit():
        flash('Inserido o registro {}:'.format(form.string_t.data))
        insert(form.string_t.data)
        return redirect('list_db')
    return render_template('form_test.html', title = 'Test', form = form)

@app.route('/list_db')
def list_db():

    items = list_db_sql()
    return render_template('list_db.html', items = items)



def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/uploads', methods=['GET', 'POST'])
def uploads():

    form = UploadForm()
    if form.validate_on_submit() and request.method == 'POST':
        filename = secure_filename(form.file.data.filename)
        if allowed_file(filename):
            form.file.data.save(app.config['UPLOAD_FOLDER'] + filename)
            return redirect(url_for('index'))
        flash('Check the file extension')
    return render_template('uploads.html', form=form)