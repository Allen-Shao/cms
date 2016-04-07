from rest_framework.test import APITestCase
from cmsapp.tests import ObjectCreationHelper

# Create your tests here.

class ViewAPITestCase(APITestCase):

    def test_report_view_set(self):
        url = "/api/reports/"
        data = {"get" : "list"}
        response = self.client.get(url, data, format = "json")
        self.assertEqual(response.status_code, 200)

    def test_report_view_detail(self):
        ObjectCreationHelper.create_report()
        url = "/api/reports/1/"
        response = self.client.patch(url, format = "json")
        self.assertEqual(response.status_code, 200)

    def test_decision_view_set(self):
        url = "/api/decisions/"
        data = {"get" : "list"}
        response = self.client.get(url, data, format = "json")
        self.assertEqual(response.status_code, 200)

    def test_decision_view_detail(self):
        ObjectCreationHelper.create_decision()
        url = "/api/decisions/1/"
        response = self.client.patch(url, format = "json")
        self.assertEqual(response.status_code, 200)

    def test_resource_request_view_set(self):
        url = "/api/requests/"
        data = {"get" : "list"}
        response = self.client.get(url, data, format = "json")
        self.assertEqual(response.status_code, 200)

    def test_resource_request_view_detail(self):
        ObjectCreationHelper.create_resource_request()
        url = "/api/requests/1/"
        response = self.client.patch(url, format = "json")
        self.assertEqual(response.status_code, 200)
