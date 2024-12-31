from selenium.webdriver.common.by import By as REG
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RegisterPage:
    def __init__(self, browser):
        self.browser = browser

    # 輸入電話欄位
    def enter_phone(self, phone):
        phone_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (REG.CSS_SELECTOR, 'input[placeholder="Tu número de celular"]'))
        )
        phone_input.send_keys(phone)

    # 再次確認欄位
    def confirm_number(self, number):
        number_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((REG.CSS_SELECTOR,
                                              'input[placeholder="Confirme o número do celular"]'))
        )
        number_input.send_keys(number)

    # 密碼欄位
    def enter_password(self, password):
        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((REG.CSS_SELECTOR,
                                              'input[placeholder="Senha (4-12 letras e números)"]'))
        )
        password_input.send_keys(password)

    # 驗證碼欄位
    def enter_verifycode(self, code):
        verifycode_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((REG.CSS_SELECTOR,
                                              'input[placeholder="Código de verificação"]'))
        )
        verifycode_input.send_keys(code)

    # 隱私政策勾選 (加上try except 調適確認定位)
    def click_privacy_box(self):
        try:
            privacy_box = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((REG.CSS_SELECTOR, '#root > div > div > '
                                                                    'div.fixed.bottom-0.right-0.top-0.z-\['
                                                                    '1001\].w-full > div > div > div > section > '
                                                                    'section.flex.flex-row.items-start > div > div > '
                                                                    'div > svg')))
            privacy_box.click()
        except TimeoutException:
            print("Timeout: Failed to locate privacy box")

    # 註冊按鈕
    def click_register_button(self):
        register_button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((REG.XPATH,
                                              "/html/body/div/div/div/div[2]/div/div/div/section/section[1]/button"))
        )
        register_button.click()

    # 登入後用戶頭像
    def user_img(self):
        user_img = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((REG.CSS_SELECTOR, 'img[alt="avatar"]'))
        )
        # 返回找到元素
        return user_img

        # 點擊-邀請好友 選單

    def click_convide_amigos_menu(self):
        convide_amigos = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((REG.XPATH, "/html/body/div/div/div/div[1]/div/section[1]/button[1]"))
        )
        convide_amigos.click()

    # 獲取邀請好友連結
    def get_convide_amigos_link(self):
        convide_link = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((REG.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div["
                                                         "2]/div"))
        )

        # 获取链接的值
        link_value = convide_link.text
        return link_value
