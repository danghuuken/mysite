from django.test import Client, TestCase, RequestFactory
from django.core.urlresolvers import reverse, resolve 

class TestHomePage(TestCase):

	def test_index_template(self):	
		response = self.client.get(reverse('home'))
		self.assertTemplateUsed(response, 'mysite/index.html')

	def test_base_template(self):
		response = self.client.get(reverse('home'))
		self.assertTemplateUsed(response, "base.html")
