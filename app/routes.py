
import os
from flask import render_template, flash, redirect, url_for, request, jsonify, send_file
from app import app
import glob

@app.route('/')
@app.route('/index')
def index():
    files = glob.glob('/home/ubuntu/inpi_extract/xlsx/*')
    return render_template('index.html', title = 'Home', files = files)

@app.route('/<path>')
def download(path = None):
    return send_file(path, as_attachment=True)