from django.test import TestCase
from django.contrib.auth.models import User, Group
from forms import LoginForm, CallCenterReportForm, NotificationForm, ResourceForm, DecisionForm
from models import CallCenterReport, Crisis, Decision, Notification, Place, Agency, ResourceRequest

class ViewTestCase(TestCase):

    self.mt = ModelTestCase()

    def setUp(self):
        self.create_group_and_user("dm1", "Decision Maker")
        self.create_group_and_user("cmsstaff", "CMS Staff")
        self.create_group_and_user("agency1", "Agency Staff")
        self.create_group_and_user("ccs1", "Call Center Staff")

    def create_user(self, username, password):
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_group_and_user(self, username, group_name):
        group = Group.objects.create(name=group_name)
        user = self.create_user(username, "cmscz3003")
        user.groups.add(group)

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 302)

    def test_login_nexturl(self):
        response = self.client.get("/login/?next=/dashboard/")
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page(self):
        report = self.mt.create_report(self.mt.create_crisis())
        agency = self.mt.create_agency()
        self.client.login(username="dm1", password="cmscz3003")
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("dashboard_active", response.context)
        self.assertEqual(response.context["dashboard_active"], "active")
        self.assertIn("form", response.context)
        self.assertEqual(response.context["form"], DesicionForm)
        self.assertIn("form2", response.context)
        self.assertEqual(response.context["form2"], NotificationForm)
        self.assertIn("report", response.context)
        self.assertEqual(response.context["report"], report)
        self.assertIn("agency", response.context)
        self.assertEqual(response.context["agency"], agency)


    def test_process_report_page(self):
        self.client.login(username="dm1", password="cmscz3003")
        response = self.client.get("/process-reports/")
        self.assertEqual(response.status_code, 200)

    def test_process_request_page(self):
        self.client.login(username="dm1", password="cmscz3003")
        response = self.client.get("/process-requests/")
        self.assertEqual(response.status_code, 200)

    def test_notification_page(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/notification/")
        self.assertEqual(response.status_code, 200)

    def test_report_page(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/report/")
        self.assertEqual(response.status_code, 200)

    def test_resource_page(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/resource/")
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

    def create_agency(self):
        return Agency.objects.create(
            name = "test agency",
            contact = "11111111"
        )


    def create_resource_request(self):
        return ResourceRequest.objects.create(
            crisis = self.create_decision(self.create_crisis()),
            resource = "test resource",
            description = "test description",
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

    def test_resource_requests(self):
        resource_request = self.create_resource_request()
        self.assertTrue(isinstance(resource_request, ResourceRequest))
        self.assertEqual(resource_request.__unicode__(), "%s - %s" % (resource_request.crisis, resource_request.resource))
