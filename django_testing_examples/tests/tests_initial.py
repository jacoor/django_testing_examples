# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver import FirefoxOptions


# class InitialTestCase(StaticLiveServerTestCase):
#     """
#     Example smoke test to check if framework has started, using Selenium.
#     Is this test valuable?
#     - It only starts a page and checks if it runs. 
#     - fails to verify incorrect db setup, like wrong name or password
#     - takes 4 seconds to run
#     Curious case to show, but not much more. Extreme TDD.
#     """
#     def setUp(self):
#         super().setUp()
#         opts = FirefoxOptions()
#         opts.add_argument("--headless")
#         self.selenium = webdriver.Firefox(options=opts)

#     def tearDown(self):
#         self.selenium.quit()
#         super().tearDown()

#     def test_smoke_server_started(self):
#         self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
#         assert 'Django' in self.selenium.title

