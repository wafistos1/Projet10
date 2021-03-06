from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.urls import reverse
from store.models import Product, Favorite, Categorie
from register.models import Profile
from django.contrib.auth.models import User
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.firefox.options import Options

class MySeleniumTests(LiveServerTestCase):
    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.selenium = WebDriver()
        self.selenium.implicitly_wait(10)        
        self.user = User.objects.create_user('wafistos4', 'wafi@gmail.com', 'djamel2013')
        self.profile = Profile.objects.get_or_create(user=self.user, image='picture/wafi.png')

    
    def tearDown(self):
        self.selenium.quit()

       
    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register/login/'))
        self.selenium.find_element_by_id("id_username").send_keys('wafistos4')
        self.selenium.find_element_by_id("id_password").send_keys('djamel2013')
        self.selenium.find_element_by_id('submitBtn').click()
        self.assertEquals(self.selenium.title, 'Home')


    def test_search(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/store'))
        query = self.selenium.find_element_by_name("q")
        query.send_keys('Pepsi')
        self.selenium.find_element_by_id('submitId').click()
        
        # todo ajouter le test du formulaire 
        


        
        
        
        
        