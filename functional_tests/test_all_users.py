from selenium import webdriver
import unittest
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class HomeNewVisitorTest(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def get_full_url(self, namespace):
		return self.live_server_url + reverse(namespace)

	#As Jon Doe visits our site, he should see "Classic Man" as the browser title, 
	def test_home_title(self):
		self.browser.get(self.get_full_url("home"))
		self.assertIn("Classic Man", self.browser.title)

	#Jon Doe then sees that the header color is dark red
	def test_h1_css(self):
		self.browser.get(self.get_full_url("home"))
		h1 = self.browser.find_element_by_tag_name("h1")
		self.assertEqual(h1.value_of_css_property("color"), 
						"rgba(178, 34, 34, 1)")

	# When Jon Doe visits the human and robot files, they should not see a file not found
	def test_home_files(self):
		self.browser.get(self.live_server_url + "/robots.txt")
		self.assertNotIn("Page Not Found", self.browser.title)
		self.browser.get(self.live_server_url + "/humans.txt")
		self.assertNotIn("Page Not Found", self.browser.title)

	#def test_home_plain_text(self):
	#	self.browser.get(self.live_server_url + "/robots.txt")
	#	self.assertEqual("text/plain", self.browser.context_te)

 
if __name__ == '__main__':
    unittest.main(warnings='ignore')