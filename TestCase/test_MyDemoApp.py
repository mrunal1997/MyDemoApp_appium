import pytest, os, yaml
from time import sleep
from PageObject.LoginPage import LogInPage
from PageObject.BuyProduct import BuyProduct
from PageObject.CheckoutPage import CheckoutDetails
from PageObject.ReviewPage import ReviewPage


@pytest.mark.usefixtures("appium_driver")
class Test_shoppingApp:

    variables = None

    @classmethod
    def setup_class(cls):
        # Load variables from YAML file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        variables_file_path = os.path.join(current_directory, "test_variables.yml")
        with open(variables_file_path, "r") as file:
            cls.variables = yaml.safe_load(file)
            cls.login_valid_credentials = cls.variables["login_valid_credentials"]
            cls.login_invalid_credentials = cls.variables["login_invalid_credentials"]
            cls.full_payment = cls.variables["full_payment"]

    def setup_method(self):
        # Setup login credentials before each test
        self.username = self.login_valid_credentials['username']
        self.password = self.login_valid_credentials['password']
        self.usernameWR = self.login_invalid_credentials['username']
        self.passwordWR = self.login_invalid_credentials['password']
        self.fullName = self.full_payment['fullName']
        self.address = self.full_payment['address']
        self.city = self.full_payment['city']
        self.state = self.full_payment['state']
        self.zipcode = self.full_payment['zipcode']
        self.country = self.full_payment['country']
        self.cardNo = self.full_payment['cardNo']
        self.expDate = self.full_payment['expDate']
        self.securityCode = self.full_payment['securityCode']

    def test_validCredential(self, appium_driver):
        logIn = LogInPage(self.driver)
        logIn.menuBar_and_login()
        sleep(1)
        if "Login" == logIn.check_loginTitle():
            assert True
        else:
            assert False
        sleep(1)
        logIn.login(self.username, self.password)
        sleep(1)

    def test_invalidCredential(self):
        logIn = LogInPage(self.driver)

        logIn.menuBar_and_login()
        sleep(1)
        if "Login" == logIn.check_loginTitle():
            assert True
        else:
            assert False
        sleep(1)
        logIn.wrongLogin(self.usernameWR, self.passwordWR)

    def test_login_and_upTo_addToCart(self, appium_driver):
        logIn = LogInPage(self.driver)
        buyProduct = BuyProduct(self.driver)

        logIn.menuBar_and_login()
        sleep(1)
        logIn.login(self.username, self.password)
        sleep(1)
        if "Products" == buyProduct.check_productTitle():
            assert True
        else:
            assert False
        sleep(1)
        buyProduct.select_and_addToCart()
        sleep(2)

    def test_login_and_upTo_proceedToCheckout(self, appium_driver):
        logIn = LogInPage(self.driver)
        buyProduct = BuyProduct(self.driver)

        logIn.menuBar_and_login()
        sleep(1)
        logIn.login(self.username, self.password)
        sleep(1)
        buyProduct.select_and_addToCart()
        sleep(2)
        buyProduct.viewCart()
        sleep(1)
        if "My Cart" == buyProduct.check_cartTitle():
            assert True
        else:
            assert False
        sleep(1)
        buyProduct.checkout()
        sleep(1)

    def test_buyProduct(self, appium_driver):
        logIn = LogInPage(self.driver)
        buyProduct = BuyProduct(self.driver)
        checkoutPage = CheckoutDetails(self.driver)
        reviewProduct = ReviewPage(self.driver)

        logIn.menuBar_and_login()
        sleep(1)
        logIn.login(self.username, self.password)
        sleep(1)
        buyProduct.select_and_addToCart()
        sleep(2)
        buyProduct.viewCart()
        sleep(1)
        if "My Cart" == buyProduct.check_cartTitle():
            assert True
        else:
            assert False
        sleep(1)
        buyProduct.checkout()
        sleep(1)
        if "Checkout" == checkoutPage.check_checkoutTitle():
            assert True
        else:
            assert False
        sleep(1)
        checkoutPage.details_and_proceedPayment(self.fullName, self.address, self.city, self.state, self.zipcode, self.country)
        sleep(1)
        reviewProduct.paymentDetails(self.fullName, self.cardNo, self.expDate, self.securityCode)
        sleep(1)
        reviewProduct.placedOrder()
        sleep(1)
        if "Checkout Complete" == reviewProduct.check_checkoutComplete_Title():
            assert True
        else:
            assert False
        sleep(1)
        reviewProduct.continueShopping()
        sleep(1)
