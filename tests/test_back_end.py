import unittest

from flask import url_for
from flask_testing import TestCase
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt
from application.models import Users, Rates
from os import getenv

class TestBase(TestCase):

	def create_app(self):

		# pass in configurations for test database
		config_name = 'testing'
		app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:1234@35.246.73.168/TestBase',
				SECRET_KEY=('TEST_SECRET_KEY'),
				WTF_CSRF_ENABLED=False,
				DEBUG=True
				)
		return app

	def setUp(self):
		"""
		Will be called before every test
		"""
		# ensure there is no data in the test database when the test starts
		db.session.commit()
		db.drop_all()
		db.create_all()

		# create test admin user
		hashed_pw = bcrypt.generate_password_hash('admin2016')
		admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password=hashed_pw)

		# create test non-admin user
		hashed_pw_2 = bcrypt.generate_password_hash('test2016')
		employee = Users(first_name="test", last_name="user", email="test@user.com", password=hashed_pw_2)

		# save users to database
		db.session.add(admin)
		db.session.add(employee)
		db.session.commit()

	def tearDown(self):
		"""
		Will be called after every test
		"""

		db.session.remove()
		db.drop_all()
	

class TestViews(TestBase):
	# testing to see if code 200 is returned upon access to url

	def test_homepage_view(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)
	

	def test_about_view(self):

		response = self.client.get(url_for('about'))
		self.assertEqual(response.status_code, 200)
		
	def test_convert_view(self):
		self.client.post(url_for('login'), data=dict(email="admin@admin.com", password="admin2016"), follow_redirects=True)
		response = self.client.get('/convert')
		self.assertIn(b'Forex Rates', response.data)

	def test_newrate_view(self):
		self.client.post(url_for('login'), data=dict(email="admin@admin.com", password="admin2016"), follow_redirects=True)
		response = self.client.get('/newrate')
		self.assertIn(b'New Rate', response.data)

	def test_accountpage_view(self):
		self.client.post(url_for('login'), data=dict(email="admin@admin.com", password="admin2016"), follow_redirects=True)
		response = self.client.get('/account')
		self.assertIn(b'Account', response.data)

	def test_loggedinhome_view(self):
		self.client.post(url_for('login'), data=dict(email="admin@admin.com", password="admin2016"), follow_redirects=True)
		response = self.client.get('/home')
		self.assertIn(b'Click here to check out current rates', response.data)

	def test_loggedinhomesecond_view(self):
		self.client.post(url_for('login'), data=dict(email="admin@admin.com", password="admin2016"), follow_redirects=True)
		response = self.client.get('/home')
		self.assertIn(b'Click here to logout', response.data)

	def test_loggedinhomethird_view(self):
		response = self.client.get('/home')
		self.assertIn(b'Click here to register', response.data)

	

class TestUserFunctionality(TestBase):

	def test_registeruser(self):
		with self.client:
			response = self.client.post(
				'/register',
				data=dict(
					first_name="Joe",
					last_name="Bloggs",
					email="joebloggs@gmail.com",
					password="password123",
					confirm_password="password123"
				),
				follow_redirects=True
			)
			self.assertTrue(response.status_code, 200)

	def test_loginuser(self):
		with self.client:
			response = self.client.post(
				'/login',
				data=dict(
					email="admin@admin.com",
					password="admin2016"
				),
				follow_redirects=True
			)
			self.assertEqual(current_user.email, "admin@admin.com")

	def test_logout(self):
		with self.client:
			response = self.client.get(
				'/logout',
				follow_redirects=True
			)
			self.assertFalse(current_user.is_authenticated)
		