from time import sleep


class CheckoutDetails:
    def __init__(self, driver):
        self.driver = driver

        self.xpath_title_checkout = "//android.widget.TextView[@text='Checkout']"
        self.xpath_fullName = "//android.widget.EditText[@content-desc='Full Name* input field']"
        self.xpath_addressLine = "//android.widget.EditText[@content-desc='Address Line 1* input field']"
        self.xpath_cityName = "//android.widget.EditText[@content-desc='City* input field']"
        self.xpath_stateName = "//android.widget.EditText[@content-desc='State/Region input field']"
        self.xpath_zipCode = "//android.widget.EditText[@content-desc='Zip Code* input field']"
        self.xpath_countryName = "//android.widget.EditText[@content-desc='Country* input field']"
        self.xpath_toPayment_btn = "//android.view.ViewGroup[@content-desc='To Payment button']"

    def check_checkoutTitle(self):
        titleCheckout = self.driver.find_element("xpath", self.xpath_title_checkout)
        return titleCheckout.text

    def details_and_proceedPayment(self, fullname, address, city, state, zipcode, country):
        fullName = self.driver.find_element("xpath", self.xpath_fullName)
        fullName.send_keys(fullname)
        sleep(1)
        addressLine = self.driver.find_element("xpath", self.xpath_addressLine)
        addressLine.send_keys(address)
        sleep(1)
        cityName = self.driver.find_element("xpath", self.xpath_cityName)
        cityName.send_keys(city)
        sleep(1)
        stateName = self.driver.find_element("xpath", self.xpath_stateName)
        stateName.send_keys(state)
        sleep(1)
        zipCode = self.driver.find_element("xpath", self.xpath_zipCode)
        zipCode.send_keys(zipcode)
        sleep(1)
        countryName = self.driver.find_element("xpath", self.xpath_countryName)
        countryName.send_keys(country)
        sleep(1)
        toPayment = self.driver.find_element("xpath", self.xpath_toPayment_btn)
        toPayment.click()
