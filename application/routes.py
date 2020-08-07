from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from application.models import Users, Rates
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, NewRate, UpdateRatesForm


@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')

@app.route('/convert')
def convert():
		ratesData = Rates.query.all()
		return render_template('convert.html', title='Forex Rates', rates=ratesData )

@app.route('/newrate', methods=['GET', 'POST'])
def newrate():
	form = NewRate()
	if form.validate_on_submit():
		ratesData = Rates(
			base_currency=form.base_currency.data,
			new_currency=form.new_currency.data,
			bid_rate=form.bid_rate.data,
			ask_rate=form.ask_rate.data
		)
			
		db.session.add(ratesData)
		db.session.commit()
		
		return redirect(url_for('convert'))
	else:
		print(form.errors)
	return render_template('newrate.html', title='Forex', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data)
		user = Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			email=form.email.data,
			password=hash_pw
			)

		db.session.add(user)
		db.session.commit()

		return redirect(url_for('login'))

	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user=Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
		user = current_user.id
		posts = Posts.query.filter_by(user_id=user)
		for post in posts:
				db.session.delete(post)
		account = Users.query.filter_by(id=user).first()
		logout_user()
		db.session.delete(account)
		db.session.commit()
		return redirect(url_for('register'))


@app.route("/delete/<id>", methods=["GET", "POST"])
@login_required
def delete_rate(id):
	rate = Rates.query.filter_by(id=id).all()
	for rate in rate:
		db.session.delete(rate)
		db.session.commit()
	return redirect(url_for('convert'))

@app.route("/update/<id>", methods=["GET", "POST"])
@login_required
def update_rate(id):
	form = UpdateRatesForm()
	rate = Rates.query.filter_by(id=id).first()
	if form.validate_on_submit():
		rate.base_currency=form.base_currency.data
		rate.new_currency=form.new_currency.data
		rate.bid_rate=form.bid_rate.data
		rate.ask_rate=form.ask_rate.data
		db.session(commit)
		return redirect(url_for('convert'))
	elif request.method == 'GET':
		form.base_currency.data=rate.base_currency
		form.new_currency.data=rate.new_currency
		form.bid_rate.data=rate.bid_rate
		form.ask_rate.data=rate.ask_rate
	return render_template('update.html', title='Manage Rate', form=form, rate=rate)