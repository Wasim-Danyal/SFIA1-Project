import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Users

test_admin_first_name = "admin"
test_admin_last_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"
test_base_currency = "USD"
test_new_currency = "JPY"
test_bid_rate = "1.234"
test_ask_rate = "4.567"
class TestBase(LiveServerTestCase):

	def create_app(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = str('mysql+pymysql://root:1234@35.246.73.168/TestBase')
		app.config['SECRET_KEY'] = 'TEST_SECRET_KEY'
		return app

	def setUp(self):
		"""Setup the test driver and create test users"""
		print("--------------------------NEXT-TEST----------------------------------------------")
		chrome_options = Options()
		chrome_options.binary_location = "/usr/bin/chromium-browser"
		chrome_options.add_argument("--headless")
		self.driver = webdriver.Chrome(executable_path="/home/wasim_danyal1/chromedriver", chrome_options=chrome_options)
		self.driver.get("http://localhost:5000")
		db.session.commit()
		db.drop_all()
		db.create_all()

	def tearDown(self):
		self.driver.quit()
		print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

	def test_server_is_up_and_running(self):
		response = urlopen("http://localhost:5000")
		self.assertEqual(response.code, 200)


class TestAccountFunct(TestBase):

	def test_registration(self):
		self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[3]").click()
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(
			test_admin_first_name)
		self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(
			test_admin_last_name)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
			test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
			test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)

		assert url_for('login') in self.driver.current_url

	def test_login(self):
		self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[3]").click()
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(
			test_admin_first_name)
		self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(
			test_admin_last_name)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
			test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
			test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[4]").click()
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
			test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)

		assert url_for('home') in self.driver.current_url

	def test_newrate(self):

		self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[3]").click()
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(
			test_admin_first_name)
		self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(
			test_admin_last_name)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
			test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
			test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[4]").click()
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
			test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[3]").click()
		time.sleep(1)
		
		assert url_for('home') in self.driver.current_url		



if __name__ == '__main__':
	unittest.main(port=5000)