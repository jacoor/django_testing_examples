from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import FirefoxOptions
from selenium import webdriver

class InitialTestCase(StaticLiveServerTestCase):
    """
    Example smoke test to check if framework has started, using Selenium.
    Is this test valuable?
    - It only starts a page and checks if it runs. 
    - fails to verify incorrect db setup, like wrong name or password
    - takes 4 seconds to run
    Curious case to show, but not much more. Extreme TDD.
    """
    def setUp(self):
        super().setUp()
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.selenium = webdriver.Firefox(options=opts)

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_smoke_server_started(self):
        # for some weird reason / returns 404 while admin works. 
        # interesting, as ./manage.py runserver works flawlessly.
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        assert 'Django' in self.selenium.title