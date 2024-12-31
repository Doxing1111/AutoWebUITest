import os
import time
import platform
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.base_page import BasePage

load_dotenv()


@pytest.fixture
def wait_for_seconds():
    def _wait(seconds):
        time.sleep(seconds)

    return _wait


@pytest.fixture
def base_page(browser):
    return BasePage(browser)


@pytest.fixture
def register_page(browser):
    return RegisterPage(browser)


@pytest.fixture
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture
def open_page(browser):
    def _open(url):
        browser.get(url)

    return _open


@pytest.fixture(scope="module")
def browser():
    chrome_options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }

    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-gpu")  # 如果你在 Windows 上运行，可能需要这个参数
    chrome_options.add_argument("--window-size=1920x1080")  # 设置窗口大小，确保元素在可见范围内

    if platform.system() == "Darwin":
        chromedriver_path = "/Users/joe_gou/PycharmProjects/AutoWebUITest/drivers/chromedriver"
    else:
        chromedriver_path = r'C:\Users\Joe\PycharmProjects\AutoWebUITest\drivers\chromedriver.exe'

    service = Service(executable_path=chromedriver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()

    try:
        yield driver
    finally:
        driver.quit()


# 註冊資訊
@pytest.fixture
def registration_info():
    url = os.getenv("QAT_URL")
    username_one = os.getenv("REGISTER_USER_ONE")
    username_two = os.getenv("REGISTER_USER_TWO")
    confirm_one = os.getenv("CONFIRM_USER_ONE")
    confirm_two = os.getenv("CONFIRM_USER_TWO")
    password = os.getenv("REGISTER_PASSWORD")
    security_code = os.getenv("REGISTER_VERIFYCODE")
    return url, username_one, username_two, confirm_one, confirm_two, password, security_code


# 註冊流程
@pytest.fixture
def register_flow(register_page, base_page, wait_for_seconds):
    def _register(phone, number, password, code):
        register_page.enter_phone(phone)
        wait_for_seconds(2)
        register_page.confirm_number(number)
        wait_for_seconds(2)
        register_page.enter_password(password)
        wait_for_seconds(2)
        register_page.enter_verifycode(code)
        wait_for_seconds(2)
        register_page.click_privacy_box()
        wait_for_seconds(2)
        register_page.click_register_button()
        wait_for_seconds(2)
        base_page.click_invite_box()
        wait_for_seconds(2)
        base_page.click_tg_box()
        wait_for_seconds(2)

    return _register


@pytest.fixture
def login_info():
    url = os.getenv('QAT_URL')
    username = os.getenv('LOGIN_USERNAME')
    password = os.getenv('LOGIN_PASSWORD')
    return url, username, password


# 登入流程
@pytest.fixture
def login_flow(login_page, base_page, wait_for_seconds):
    def _login(username, password):
        login_page.click_login_page_button()
        wait_for_seconds(2)
        login_page.enter_username(username)
        wait_for_seconds(2)
        login_page.enter_password(password)
        wait_for_seconds(2)
        login_page.click_login_button()
        wait_for_seconds(2)
        base_page.click_invite_box()
        wait_for_seconds(2)
        base_page.click_tg_box()
        wait_for_seconds(2)

    return _login
