import pytest
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions


@pytest.fixture(scope="function")
def appium_driver(request):
    # Desired capabilities for the Android device
    capabilities = {
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:deviceName": "emulator-5554",
        "appium:app": "/Users/aw/Downloads/Android-MyDemoAppRN.1.3.0.build-244.apk",
        "appium:automationName": "UiAutomator2",
        "appium:ensureWebviewHavePages": "True",
        "appium:newCommandTimeout": "3600",
        "appium:connectHardwareKeyboard": "True"
    }
    appium_options = AppiumOptions()
    appium_options.load_capabilities(capabilities)
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=appium_options)
    request.cls.driver = driver
    yield driver
    driver.quit()
