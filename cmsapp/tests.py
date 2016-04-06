from django.test import TestCase
from models import CallCenterReport, Crisis, Decision, Notification, Place

class HomeViewTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

class ModelTestCase(TestCase):
    def create_report(self, crisis):
        return CallCenterReport.objects.create(
            name="Test",
            mobile_number="99999999",
            location="singapore",
            description="help me",
            type_of_crisis=crisis,
            type_of_assistance="EA"
        )

    def create_crisis(self):
        return Crisis.objects.create(type_of_crisis="Haze")

    def create_decision(self, crisis):
        return Decision.objects.create(
            type_of_crisis=crisis,
            description="test decision"
        )

    def create_notification(self, decision, place):
        return Notification.objects.create(
            decision=decision,
            description="test notification",
            place=place
        )

    def create_place(self):
        return Place.objects.create(
            name="test place",
            contact="111111"
        )

    def test_call_center_report(self):
        crisis = self.create_crisis()
        report = self.create_report(crisis)
        self.assertTrue(isinstance(report, CallCenterReport))
        self.assertEqual(report.__unicode__(), "%s - %s" % (report.id, report.name))

    def test_decision(self):
        crisis = self.create_crisis()
        decision = self.create_decision(crisis)
        self.assertTrue(isinstance(decision, Decision))
        self.assertEqual(decision.__unicode__(), "%s - %s" % (decision.id, decision.type_of_crisis))

    def test_crisis(self):
        crisis = self.create_crisis()
        self.assertTrue(isinstance(crisis, Crisis))
        self.assertEqual(crisis.__unicode__(), crisis.type_of_crisis)

    def test_notification(self):
        crisis = self.create_crisis()
        decision = self.create_decision(crisis)
        place = self.create_place()
        notification = self.create_notification(decision, place)
        self.assertTrue(isinstance(notification, Notification))
        self.assertEqual(notification.__unicode__(), "%s - %s" % (notification.decision, notification.place))

    def test_place(self):
        place = self.create_place()
        self.assertTrue(isinstance(place, Place))
        self.assertEqual(place.__unicode__(), place.name)
