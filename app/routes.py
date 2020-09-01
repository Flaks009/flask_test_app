
import os
from flask import render_template, flash, redirect, url_for, request, jsonify, send_from_directory
from app import app
import glob

UPLOAD_DIRECTORY = "/home/ubuntu/inpi_extract/xlsx/"

@app.route('/')
@app.route('/index')
def index():
    files = glob.glob('/home/ubuntu/inpi_extract/xlsx/*')
    return render_template('index.html', title = 'Home', files = files)

@app.route('/download/<path>')
def download(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)