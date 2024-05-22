from time import sleep


class LogInPage:
    def __init__(self, driver):
        self.driver = driver

        self.xpath_menuBar = "//android.view.ViewGroup[@content-desc='open menu']/android.widget.ImageView"
        self.xpath_logIn_btn = "//android.view.ViewGroup[@content-desc='menu item log in']"
        self.xpath_title_login = "(//android.widget.TextView[@text='Login'])[1]"
        self.xpath_username = "//android.widget.EditText[@content-desc='Username input field']"
        self.xpath_password = "//android.widget.EditText[@content-desc='Password input field']"
        self.xpath_login_btn = "//android.view.ViewGroup[@content-desc='Login button']"
        self.xpath_wrong_auth_msg = "//android.view.ViewGroup[@content-desc='generic-error-message']"
    def menuBar_and_login(self):
        menu_bar = self.driver.find_element("xpath", self.xpath_menuBar)
        menu_bar.click()
        sleep(1)
        select_log_in = self.driver.find_element("xpath", self.xpath_logIn_btn)
        select_log_in.click()
        sleep(1)

    def check_loginTitle(self):
        titleLogin = self.driver.find_element("xpath", self.xpath_title_login)
        return titleLogin.text

    def login(self, username, password):
        # self.open_menu_and_select_login()
        userName = self.driver.find_element("xpath", self.xpath_username)
        userName.send_keys(username)
        sleep(1)
        userPassword = self.driver.find_element("xpath", self.xpath_password)
        userPassword.send_keys(password)
        sleep(1)
        login_btn = self.driver.find_element("xpath", self.xpath_login_btn)
        login_btn.click()
        sleep(1)

    def wrongLogin(self, username, password):
        userName = self.driver.find_element("xpath", self.xpath_username)
        userName.send_keys(username)
        sleep(1)
        userPassword = self.driver.find_element("xpath", self.xpath_password)
        userPassword.send_keys(password)
        sleep(1)
        login_btn = self.driver.find_element("xpath", self.xpath_login_btn)
        login_btn.click()
        sleep(1)
        invalidAuth_msg = self.driver.find_element("xpath", self.xpath_wrong_auth_msg)
        return invalidAuth_msg.text

