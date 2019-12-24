from sapp import app
from flask import render_template
from sapp.Search import main

@app.route('/')
@app.route('/index')
def index():
	results = main()
	return render_template('index.html', results = results)
