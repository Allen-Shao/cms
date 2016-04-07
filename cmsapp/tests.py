from django.test import TestCase
from unittest import skip
from django.contrib.auth.models import User, Group
from forms import LoginForm, CallCenterReportForm, NotificationForm, ResourceForm, DecisionForm
from models import CallCenterReport, Crisis, Decision, Notification, Place, Agency, ResourceRequest
from selenium import webdriver

class ObjectCreationHelper:
    @classmethod
    def create_user(self, username):
        user = User.objects.create(username=username)
        user.set_password("cmscz3003")
        user.save()
        return user

    @classmethod
    def create_group_and_user(self, username, group_name):
        group = Group.objects.create(name=group_name)
        user = self.create_user(username)
        user.groups.add(group)

    @classmethod
    def create_report(self):
        return CallCenterReport.objects.create(
            name="Test",
            mobile_number="99999999",
            location="singapore",
            description="help me",
            type_of_crisis=self.create_crisis(),
            type_of_assistance="EA"
        )

    @classmethod
    def create_crisis(self):
        return Crisis.objects.create(type_of_crisis="Haze")

    @classmethod
    def create_decision(self):
        return Decision.objects.create(
            type_of_crisis=self.create_crisis(),
            description="test decision"
        )

    @classmethod
    def create_notification(self):
        return Notification.objects.create(
            decision=self.create_decision(),
            description="test notification",
            agency=self.create_agency()
        )

    @classmethod
    def create_place(self):
        return Place.objects.create(
            name="test place",
            contact="111111"
        )

    @classmethod
    def create_agency(self):
        return Agency.objects.create(
            name = "test agency",
            contact = "11111111"
        )

    @classmethod
    def create_resource_request(self):
        return ResourceRequest.objects.create(
            crisis = self.create_decision(),
            resource = "test resource",
            description = "test description",
        )


class ViewTestCase(TestCase):

    def setUp(self):
        ObjectCreationHelper.create_group_and_user("dm1", "Decision Maker")
        ObjectCreationHelper.create_group_and_user("cmsstaff", "CMS Staff")
        ObjectCreationHelper.create_group_and_user("agency1", "Agency Staff")
        ObjectCreationHelper.create_group_and_user("ccs1", "Call Center Staff")

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
        report = ObjectCreationHelper.create_report()
        agency = ObjectCreationHelper.create_agency()
        self.client.login(username="dm1", password="cmscz3003")
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("dashboard_active", response.context)
        self.assertEqual(response.context["dashboard_active"], "active")
        self.assertIn("form", response.context)
        self.assertEqual(response.context["form"], DecisionForm)
        self.assertIn("form2", response.context)
        self.assertEqual(response.context["form2"], NotificationForm)
        self.assertIn("reports", response.context)
        self.assertEqual([r.__unicode__() for r in response.context["reports"]], [report.__unicode__()])
        self.assertIn("agencies", response.context)
        self.assertEqual([a.__unicode__() for a in response.context["agencies"]], [agency.__unicode__()])

    def test_process_report_page(self):
        crisis = ObjectCreationHelper.create_crisis()
        self.client.login(username="dm1", password="cmscz3003")
        response = self.client.get("/process-reports/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("process_report_active", response.context)
        self.assertEqual(response.context["process_report_active"], "active")
        self.assertIn("type_of_crisis", response.context)
        self.assertEqual([c.__unicode__() for c in response.context["type_of_crisis"]], [crisis.__unicode__()])


    def test_process_request_page(self):
        agency = ObjectCreationHelper.create_agency()
        self.client.login(username="dm1", password="cmscz3003")
        response = self.client.get("/process-requests/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("process_request_active", response.context)
        self.assertEqual(response.context["process_request_active"], "active")
        self.assertIn("agency_list", response.context)
        self.assertEqual([a.__unicode__() for a in response.context["agency_list"]], [agency.__unicode__()])



    def test_notification_page(self):
        agency = ObjectCreationHelper.create_agency()
        self.client.login(username="dm1", password="cmscz3003")
        response = self.client.get("/notification/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("notification_active", response.context)
        self.assertEqual(response.context["notification_active"], "active")
        self.assertIn("form", response.context)
        self.assertEqual(response.context["form"], NotificationForm)
        self.assertIn("agencies", response.context)
        self.assertEqual([a.__unicode__() for a in response.context["agencies"]], [agency.__unicode__()])
        #place not yet tested


    def test_report_page(self):
        self.client.login(username="ccs1", password="cmscz3003")
        response = self.client.get("/report/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("report_active", response.context)
        self.assertEqual(response.context["report_active"], "active")
        self.assertIn("form", response.context)
        self.assertEqual(response.context["form"], CallCenterReportForm)

    def test_resource_page(self):
        self.client.login(username="agency1", password="cmscz3003")
        response = self.client.get("/resource/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("resource_active", response.context)
        self.assertEqual(response.context["resource_active"], "active")
        self.assertIn("form", response.context)
        self.assertEqual(response.context["form"], ResourceForm)

    def test_report_post(self):
        ObjectCreationHelper.create_crisis()
        self.client.login(username="ccs1", password="cmscz3003")
        post_data = {
            "name": "tester",
            "mobile_number": "19230123",
            "location": "singapore",
            "description": "help",
            "type_of_crisis": 1,
            "type_of_assistance": "EA"
        }
        response = self.client.post("/report/", post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/report/")

    def test_request_post(self):
        ObjectCreationHelper.create_decision()
        self.client.login(username="agency1", password="cmscz3003")
        post_data = {
            "crisis": 1,
            "resource": "sand bag",
            "description": "help"
        }
        response = self.client.post("/resource/", post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/resource/")

    @skip("skip posting decision")
    def test_decision_post(self):
        ObjectCreationHelper.create_crisis()
        ObjectCreationHelper.create_agency()
        self.client.login(username="dm1", password="cmscz3003")
        post_data = {
            "type_of_crisis": 1,
            "description": "test description",
            "agency": "test agency"
        }
        response = self.client.post("/dashboard/", post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/dashboard/")

    @skip("skip notification decision")
    def test_notification_post(self):
        ObjectCreationHelper.create_decision()
        ObjectCreationHelper.create_agency()
        self.client.login(username="dm1", password="cmscz3003")
        post_data = {
            "decision": 1,
            "description": "test description",
            "agency": "test agency"
        }
        response = self.client.post("/notification/", post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/notification/")

    def test_login_post(self):
        post_data = {
            "username": "dm1",
            "password": "cmscz3003",
            "next": "/dashboard/"
        }
        response = self.client.post("/login/", post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/dashboard/")

    def test_login_wrong_post(self):
        post_data = {
            "username": "wrong",
            "password": "cms"
        }
        response = self.client.post("/login/", post_data)
        self.assertEqual(response.status_code, 200)

class ModelTestCase(TestCase):

    def test_call_center_report(self):
        report = ObjectCreationHelper.create_report()
        self.assertTrue(isinstance(report, CallCenterReport))
        self.assertEqual(report.__unicode__(), "%s - %s" % (report.id, report.name))

    def test_decision(self):
        decision = ObjectCreationHelper.create_decision()
        self.assertTrue(isinstance(decision, Decision))
        self.assertEqual(decision.__unicode__(), "%s - %s" % (decision.id, decision.type_of_crisis))

    def test_crisis(self):
        crisis = ObjectCreationHelper.create_crisis()
        self.assertTrue(isinstance(crisis, Crisis))
        self.assertEqual(crisis.__unicode__(), crisis.type_of_crisis)

    def test_notification(self):
        notification = ObjectCreationHelper.create_notification()
        self.assertTrue(isinstance(notification, Notification))
        self.assertEqual(notification.__unicode__(), "%s - %s" % (notification.decision, notification.agency))

    def test_place(self):
        place = ObjectCreationHelper.create_place()
        self.assertTrue(isinstance(place, Place))
        self.assertEqual(place.__unicode__(), place.name)

    def test_resource_requests(self):
        resource_request = ObjectCreationHelper.create_resource_request()
        self.assertTrue(isinstance(resource_request, ResourceRequest))
        self.assertEqual(resource_request.__unicode__(), "%s - %s" % (resource_request.crisis, resource_request.resource))

class WebTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sign_in(self):
        self.driver.get("http://localhost:8888/login/")
        self.driver.find_element_by_id("username").send_keys("dm1")
        self.driver.find_element_by_id("password").send_keys("cmscz3003")
        self.driver.find_element_by_id("submit").click()
        self.assertEqual("http://localhost:8888/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit
