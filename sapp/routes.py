from sapp import app
from flask import render_template, request, redirect, url_for
from sapp.Search import main

@app.route('/')
def my_form():
	return render_template('my-form.html')

@app.route('/search')
def search():
	search = request.args.get('search')
	result = main(search)
	return render_template('index.html', results = result)

# @app.route('/index')
# def index():
# 	results = main()
# 	return render_template('index.html', results = results)
