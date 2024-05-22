from time import sleep


class ReviewPage:
    def __init__(self, driver):
        self.driver = driver

        self.xpath_fullname = "//android.widget.EditText[@content-desc='Full Name* input field']"
        self.xpath_card_number = "//android.widget.EditText[@content-desc='Card Number* input field']"
        self.xpath_month_and_year = "//android.widget.EditText[@content-desc='Expiration Date* input field']"
        self.xpath_securityCode = "//android.widget.EditText[@content-desc='Security Code* input field']"
        self.xpath_reviewOrder_btn = "//android.view.ViewGroup[@content-desc='Review Order button']"
        self.xpath_placeOrder_btn = "//android.view.ViewGroup[@content-desc='Place Order button']"
        self.xpath_title_checkoutComplete = "//android.widget.TextView[@text='Checkout Complete']"
        self.xpath_continueShopping_btn = "//android.widget.TextView[@text='Continue Shopping']"

    def paymentDetails(self, fullname, cardNo, expDate, securityCode):
        fullName = self.driver.find_element("xpath", self.xpath_fullname)
        fullName.send_keys(fullname)
        sleep(1)
        cardNumber = self.driver.find_element("xpath", self.xpath_card_number)
        cardNumber.send_keys(cardNo)
        sleep(1)
        expiryDate = self.driver.find_element("xpath", self.xpath_month_and_year)
        expiryDate.send_keys(expDate)
        sleep(1)
        cvvNumber = self.driver.find_element("xpath", self.xpath_securityCode)
        cvvNumber.send_keys(securityCode)
        sleep(1)
        reviewOrder = self.driver.find_element("xpath", self.xpath_reviewOrder_btn)
        reviewOrder.click()
        sleep(1)

    def placedOrder(self):
        placedOrder = self.driver.find_element("xpath", self.xpath_placeOrder_btn)
        placedOrder.click()
        sleep(1)

    def check_checkoutComplete_Title(self):
        titleCheckoutComplete = self.driver.find_element("xpath", self.xpath_title_checkoutComplete)
        return titleCheckoutComplete.text

    def continueShopping(self):
        continueShopping = self.driver.find_element("xpath", self.xpath_continueShopping_btn)
        continueShopping.click()
        sleep(1)
