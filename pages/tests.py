from django.test import SimpleTestCase


class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    def test_login_page_status_code(self):
        response = self.client.get("/log-in/")
        self.assertEqual(response.status_code, 200)
