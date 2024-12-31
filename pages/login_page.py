import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By as LOG
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    # 註冊頁面按鈕
    def register_page_button(self):
        register_page_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((LOG.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/section/div/button[2]"))
        )
        return register_page_button

    # 切換登入頁面
    def click_login_page_button(self):
        login_page_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((LOG.XPATH, "/html/body/div/div/div/div[2]/div/div/section/div/button[1]"))
        )
        login_page_button.click()

    # 電話欄位
    def enter_username(self, username):
        username_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (LOG.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/input"))
        )
        username_input.send_keys(username)

    # 密碼欄位
    def enter_password(self, password):
        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.XPATH,
                                              "/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/div["
                                              "1]/div/div/input"))
        )
        password_input.send_keys(password)

    # 清空密碼欄位
    def clear_password_field_with_keys(self):
        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.XPATH,
                                              "/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/div["
                                              "1]/div/div/input"))
        )

        # 根據作業系統來使用不同的鍵來清空輸入框中的文本
        if platform.system() == "Windows":
            password_input.send_keys(Keys.CONTROL + "a")
        elif platform.system() == "Darwin":  # macOS
            password_input.send_keys(Keys.COMMAND + "a")

        time.sleep(2)

        # 刪除選中的文本
        password_input.send_keys(Keys.DELETE)

    # 登入按鈕
    def click_login_button(self):
        login_button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.XPATH,
                                              "/html/body/div/div/div/div[2]/div/div/div/div/div/section/button[2]"))
        )
        login_button.click()

    # 點擊-忘記密碼
    def click_forget_password(self):
        forget_btn = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.XPATH, '/html/body/div/div/div/div['
                                                         '2]/div/div/div/div/div/section/button[1] '))
        )
        forget_btn.click()

    # 忘記密碼頁-輸入手機號欄位
    def forget_phone(self, username):
        phone = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.CSS_SELECTOR, 'input[placeholder="Tu número de celular"]'))
        )
        phone.send_keys(username)

    # 發送驗證碼
    def send_verifycode(self):
        send_btn = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (LOG.XPATH, "/html/body/div/div/div/div[2]/div/div/div/section/div[2]/div/div/div/button"
                 ))
        )
        send_btn.click()

    # 輸入驗證碼
    def input_verifycode(self, verifycode):
        input_code = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.CSS_SELECTOR, 'input[placeholder="Código de verificação"]'))
        )
        input_code.send_keys(verifycode)

    # 輸入新密碼
    def input_newpassword(self, newpassword):
        input_password = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.CSS_SELECTOR, 'input[placeholder="Senha (4-12 letras e números)"]'))
        )
        input_password.send_keys(newpassword)

    # 更改密碼送出
    def click_reset_password(self):
        reset_btn = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.XPATH, "/html/body/div[1]/div/div/div["
                                                         "2]/div/div/div/section/section/button"))
        )
        reset_btn.click()

    # 登入後用戶頭像
    def user_img(self):
        user_img = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.CSS_SELECTOR, 'img[alt="avatar"]'))
        )
        # 返回找到元素
        return user_img

    # 點擊頭像
    def click_user_img(self):
        user_img = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.CSS_SELECTOR, 'img[alt="avatar"]'))
        )
        user_img.click()

    def click_logout_btn(self):
        logout_btn = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.XPATH, "/html/body/div/div/div/div[2]/div/div[6]/button"))
        )
        logout_btn.click()

    def click_cancelar(self):
        cancelar_btn = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/button[1]"))
        )
        cancelar_btn.click()

    def click_confirme(self):
        confirme_btn = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/button[2]"))
        )
        confirme_btn.click()

    def error_login_msg(self):
        error_msg = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((LOG.XPATH, "/html/body/div[2]/div[1]/div/div/div/div[2]"))
        )
        return error_msg
