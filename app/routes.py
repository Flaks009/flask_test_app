
import os
from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app
from app.forms import LoginForm, TestForm, UploadForm
from app.db import list_rpi, list_marca, list_desenho, list_patente, rpi_desenho, rpi_marca, rpi_patente, insert_email_desenho
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
    return render_template('patente.html', title = 'Patente', patente = patente)

@app.route('/get_desenho_rpi', methods=['POST', 'GET'])
def get_desenho_rpi():
    if request.method == 'POST':
        desenho = rpi_desenho(request.form['desenho_rpi'])
        return render_template('desenho.html', title = 'Desenho', desenho = desenho)
    elif request.method == 'GET':
        desenho = rpi_desenho(request.args.get('rpi'))
        return render_template('desenho.html', title = 'Desenho', desenho = desenho)

@app.route('/get_marca_rpi', methods=['POST'])
def get_marca_rpi():
    marca = rpi_marca(request.form['marca_rpi'])
    return render_template('marca.html', title = 'Marca', marca = marca)

@app.route('/get_patente_rpi', methods=['POST'])
def get_patente_rpi():
    patente = rpi_patente(request.form['patente_rpi'])
    return render_template('patente.html', title = 'Patente', patente = patente)

@app.route('/post_insert_email', methods=['POST'])
def post_insert_email():
    email = request.json['email']
    num_ped = request.json['num_ped']
    rpi = request.json['rpi']
    insert_email_desenho(num_ped, email)
    return redirect(url_for('get_desenho_rpi', rpi=rpi))