import pytest
import allure


@allure.description('执行者：Joe')
@allure.feature('登入功能')
@allure.title('输入正确帐密')
@allure.story('登入成功')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.前台登入
@pytest.mark.run(order=6)
@pytest.mark.flaky(reruns=1)
def test_login(open_page, login_flow, login_info, login_page, wait_for_seconds):
    url, username, password = login_info
    open_page(url)
    wait_for_seconds(5)
    login_flow(username, password)

    # 定位登入頭像
    page_img = login_page.user_img()
    assert page_img.is_displayed()


@allure.description('执行者：Joe')
@allure.feature('登出功能')
@allure.title('点击取消')
@allure.story('登出失败')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.前台登出＿取消
@pytest.mark.run(order=7)
@pytest.mark.flaky(reruns=1)
def test_logout_cancel(open_page, login_flow, login_info, login_page, base_page, wait_for_seconds):
    login_page.click_user_img()
    wait_for_seconds(2)

    login_page.click_logout_btn()
    wait_for_seconds(2)

    login_page.click_cancelar()
    wait_for_seconds(2)

    page_img = login_page.user_img()
    assert page_img.is_displayed()


@allure.description('执行者：Joe')
@allure.feature('登出功能')
@allure.title('点击确定')
@allure.story('登出成功')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.前台登出＿確定
@pytest.mark.run(order=8)
@pytest.mark.flaky(reruns=1)
def test_logout_confirm(open_page, login_flow, login_info, login_page, base_page, wait_for_seconds):
    login_page.click_user_img()
    wait_for_seconds(2)

    login_page.click_logout_btn()
    wait_for_seconds(2)

    login_page.click_confirme()
    wait_for_seconds(2)

    register_btn = login_page.register_page_button()
    register_button_text = register_btn.text

    assert "Cadastre-Se" in register_button_text
