
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, TestForm
from app.db import insert, list_db_sql
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Samurai'}
    return render_template('index.html', title = 'Home', user = user)

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