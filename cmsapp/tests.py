from django.test import TestCase
from models import CallCenterReport, Crisis

class HomeViewTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

class ModelTestCase(TestCase):
    def test_call_center_report(self):
        report = CallCenterReport.objects.create(
            name="Test",
            mobile_number="99999999",
            location="singapore",
            description="help me",
            type_of_crisis=Crisis.objects.create(type_of_crisis="Haze"),
            type_of_assistance="EA",
        )
        self.assertTrue(isinstance(report, CallCenterReport))
        self.assertEqual(report.__unicode__(), "%s - %s" % (report.id, report.name))
