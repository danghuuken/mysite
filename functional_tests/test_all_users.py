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

 
if __name__ == '__main__':
    unittest.main(warnings='ignore')