class LoginPage():
    #Locators of all elements
    testbox_username_id="Email"
    textbox_password_id="Password"
    textbox_login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.testbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.textbox_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()