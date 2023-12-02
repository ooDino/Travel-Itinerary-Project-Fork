from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options  
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 

class UserLoginLogoutTests(StaticLiveServerTestCase):

    def setUp(self):
        
        options = Options()
        options.add_argument('-headless')  
        self.browser = webdriver.Firefox(options=options)
       
        self.user = User.objects.create_user(username='testing', password='RightPassword')

    def tearDown(self):
       
        self.browser.quit()

    def test_user_can_login_and_logout(self):
  
        self.browser.get(self.live_server_url)
     
        wait = WebDriverWait(self.browser, 10)

        try:
            
            sign_in_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
            sign_in_link.click()
        except TimeoutException:
            print("Login link not found")

        username_input = self.browser.find_element(By.NAME, 'username')
        password_input = self.browser.find_element(By.NAME, 'password')

        username_input.send_keys('testing')
        password_input.send_keys('RightPassword')
        password_input.send_keys(Keys.RETURN)

       
        wait.until_not(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
        wait.until_not(EC.presence_of_element_located((By.LINK_TEXT, 'Sign Up')))

      
        
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Logout'))).click()

  
        self.assertTrue(wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Login'))))
