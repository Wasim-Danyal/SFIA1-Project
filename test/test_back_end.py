import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Posts
from os import getenv

class TestBase(TestCase):

	def create_app(self):

		# pass in configurations for test database
		config_name = 'testing'
		app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
				SECRET_KEY=getenv('TEST_SECRET_KEY'),
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

	def test_homepage_view(self):
		"""
		Test that homepage is accessible without login
		"""
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)

	def test_about_view(self):
		"""
		Test that the About page is accessible without login
		"""
		response = self.client.get(url_for('about'))
		self.assertEqual(response.status_code, 200)
