from django.test import TestCase

class TopPageTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"Hellow World")

# class TopPageViewTest(TestCase):
#     def test_top_returns_200(self):
#         request = HttpRequest()
#         response = top(request)
#         self.assertEqual(response.status_code, 200)

#     def test_top_returns_expected_content(self):
#         request = HttpRequest()
#         response = top(request)
#         self.assertEqual(response.content, b"Hellow World")
# Create your tests here.
