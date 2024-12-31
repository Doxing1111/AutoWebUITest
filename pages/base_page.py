from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import yaml


# 在BasePage类中导入ActionChains
class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(self.browser)

    def click_invite_box(self):
        invite_box = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[3]/div/div[1]/button'))
        )
        invite_box.click()

    def click_tg_box(self):
        tg_box = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/button'))
        )
        tg_box.click()

    # 点击充值符号 (+)
    def click_add_button(self):
        add_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="add"]'))
        )
        add_button.click()

    # 等待並接受彈出的警示框
    def wait_for_alert_and_accept(self, timeout=10):
        try:
            # 等待对话框出现
            WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            print("对话框已出现")

            # 在这里添加断言，例如：
            # 断言对话框已关闭
            WebDriverWait(self.browser, 10).until_not(EC.alert_is_present())
            print("对话框已关闭")

        except TimeoutException:
            print("超时：未能等待到对话框")


class RechargePage(BasePage):
    pass
