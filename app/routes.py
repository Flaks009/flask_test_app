
import os
from flask import render_template, flash, redirect, url_for, request, jsonify, send_from_directory
from app import app
import glob

UPLOAD_DIRECTORY = "/home/ubuntu/inpi_extract/xlsx/"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')

def patente():
    files = glob.glob('/home/ubuntu/inpi_extract/xlsx/P*')
    files.sort()
    return render_template('patente.html', title='Patente', files = files)

def desenho_industrial():
    files = glob.glob('/home/ubuntu/inpi_extract/xlsx/D*')
    files.sort()
    return render_template('desenho.html', title='Desenho Industrial', files = files)

def marca():
    files = glob.glob('/home/ubuntu/inpi_extract/xlsx/RM*')
    files.sort()
    return render_template('marca.html', title='Marca', files = files)

@app.route('/download/<path>')
def download(path):
    return send_from_directory(UPLOAD_DIRECTORY, filename=path, as_attachment=True)