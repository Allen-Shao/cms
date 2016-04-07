from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

# Create your tests here.

class ViewAPITestCase(APITestCase):

	def test_report_view_set(self):
		url = "/api/reports/"
		data = {"get" : "list"}
		response = self.client.get(url, data, format = "json")
		self.assertEqual(response.status_code, 200)

	def test_report_view_detail(self):
		url = "/api/reports/0"
		response = self.client.patch(url, format = "json")
		self.assertEqual(response.status_code, 301)

	def test_decision_view_set(self):
		url = "/api/decisions/"
		data = {"get" : "list"}
		response = self.client.get(url, data, format = "json")
		self.assertEqual(response.status_code, 200)

	def test_decision_view_detail(self):
		url = "/api/decisions/0"
		response = self.client.patch(url, format = "json")
		self.assertEqual(response.status_code, 301)

	def test_resource_request_view_set(self):
		url = "/api/requests/"
		data = {"get" : "list"}
		response = self.client.get(url, data, format = "json")
		self.assertEqual(response.status_code, 200)

	def test_resource_request_view_detail(self):
		url = "/api/requests/0"
		response = self.client.patch(url, format = "json")
		self.assertEqual(response.status_code, 301)



