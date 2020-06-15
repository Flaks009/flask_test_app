
import os
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, TestForm, UploadForm
from app.db import list_rpi, list_marca, list_desenho, list_patente
from werkzeug.utils import secure_filename

@app.route('/')
@app.route('/index')
def index():
    rpi = list_rpi()
    return render_template('index.html', title = 'Home', rpi = rpi)

@app.route('/marca')
def marca():
    marca = list_marca()
    return render_template('marca.html', title = 'Marca', marca = marca)

@app.route('/desenho')
def desenho():
    desenho = list_desenho()
    return render_template('desenho.html', title = 'Desenho', desenho = desenho)

@app.route('/patente')
def patente():
    patente = list_patente()
    return render_template('desenho.html', title = 'Patente', patente = patente)

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