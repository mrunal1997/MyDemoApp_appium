from time import sleep


class BuyProduct:
    def __init__(self, driver):
        self.driver = driver

        self.xpath_title_products = "//android.widget.TextView[@text='Products']"
        self.xpath_mainMenu_product = "(//android.view.ViewGroup[@content-desc='store item'])[1]/android.view.ViewGroup[1]/android.widget.ImageView"
        self.xpath_product_colour = "//android.view.ViewGroup[@content-desc='red circle']/android.view.ViewGroup"
        self.xpath_product_quantity = "//android.view.ViewGroup[@content-desc='counter plus button']"
        self.xpath_addToCart = "//android.view.ViewGroup[@content-desc='Add To Cart button']"
        self.xpath_viewCart = "//android.view.ViewGroup[@content-desc='cart badge']/android.widget.ImageView"
        self.xpath_title_cart = "//android.widget.TextView[@text='My Cart']"
        self.xpath_proceedToCheckout_btn = "//android.widget.TextView[@text='Proceed To Checkout']"

    def check_productTitle(self):
        titleProduct = self.driver.find_element("xpath", self.xpath_title_products)
        return titleProduct.text

    def select_and_addToCart(self):
        selectProduct = self.driver.find_element("xpath", self.xpath_mainMenu_product)
        selectProduct.click()
        sleep(1)
        productColour = self.driver.find_element("xpath", self.xpath_product_colour)
        productColour.click()
        sleep(1)
        productQuantity = self.driver.find_element("xpath", self.xpath_product_quantity)
        productQuantity.click()
        sleep(1)
        addToCart = self.driver.find_element("xpath", self.xpath_addToCart)
        addToCart.click()
        sleep(1)

    def check_cartTitle(self):
        titleCart = self.driver.find_element("xpath", self.xpath_title_cart)
        return titleCart.text

    def viewCart(self):
        viewCart = self.driver.find_element("xpath", self.xpath_viewCart)
        viewCart.click()
        sleep(1)

        titleCart = self.driver.find_element("xpath", self.xpath_title_cart)
        return titleCart.text

    def checkout(self):
        proceedToCheckout = self.driver.find_element("xpath", self.xpath_proceedToCheckout_btn)
        proceedToCheckout.click()
        sleep(1)
