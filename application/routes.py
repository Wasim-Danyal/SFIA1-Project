# import render_template function from the flask module
from flask import render_template
# import the app object from the ./application/__init__.py
from application import app
# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')

@app.route('/convert')
def convert():
 return render_template('convert.html', title='Convert')

@app.route('/register')
def register():
 return render_template('register.html', title='Register')

@app.route('/login')
def login():
 return render_template('login.html', title='Login')

@app.route('/about')
def about():
 return render_template('about.html', title='About')
