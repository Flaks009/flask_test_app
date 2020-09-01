
import os
from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')