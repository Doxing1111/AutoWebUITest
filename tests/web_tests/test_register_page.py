import os
import pytest
import allure


@allure.description('执行者：Joe')
@allure.feature('注册功能')
@allure.title('一般连结')
@allure.story('注册成功')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.一般註冊
@pytest.mark.run(order=3)
@pytest.mark.flaky(reruns=1)
def test_register(open_page, register_flow, registration_info, register_page, home_page, wait_for_seconds):
    # 获取注册信息
    url, username_one, username_two, confirm_one, confirm_two, password, security_code = registration_info

    # 开启网页
    open_page(url)
    wait_for_seconds(5)

    register_flow(username_one, confirm_one, password, security_code)

    # 定位登入頭像
    page_img = register_page.user_img()
    assert page_img.is_displayed()


@pytest.mark.skip(reason="QAT邀請連結未調整")
@allure.description('执行者：Joe')
@allure.feature('注册功能')
@allure.title('邀请连结')
@allure.story('注册成功')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.邀請連結註冊
@pytest.mark.run(order=4)
@pytest.mark.flaky(reruns=1)
def test_invite_register(open_page, register_flow, registration_info, register_page, login_page, browser,
                         wait_for_seconds):
    # 获取注册信息
    url, username_one, username_two, confirm_one, confirm_two, password, security_code = registration_info

    register_page.click_convide_amigos_menu()
    wait_for_seconds(2)

    link = register_page.get_convide_amigos_link()
    wait_for_seconds(2)

    login_page.click_user_img()
    wait_for_seconds(2)

    login_page.click_logout_btn()
    wait_for_seconds(2)

    login_page.click_confirme()
    wait_for_seconds(2)

    # 清除浏览器缓存
    browser.execute_script("window.localStorage.clear();")
    browser.execute_script("window.sessionStorage.clear();")
    browser.execute_script("window.location.reload();")

    # 等待一段时间，让页面重新加载
    wait_for_seconds(3)

    # 使用 JavaScript 修改当前页面的 URL
    browser.execute_script("window.location.href = '{}'".format(link))
    wait_for_seconds(3)

    # 使用注册流程进行注册操作
    register_flow(username_two, confirm_two, password, security_code)
    wait_for_seconds(3)

    # 定位登入頭像
    page_img = register_page.user_img()
    assert page_img.is_displayed()


@pytest.mark.skip(reason="QAT邀請連結未調整")
@allure.description('执行者：Joe')
@allure.feature('注册功能')
@allure.title('后台邀请明细')
@allure.story('邀请关系成立')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.確認後台邀請關係建立成功
@pytest.mark.run(order=5)
@pytest.mark.flaky(reruns=1)
def test_verify_relationship(admin_login_info, admin_login_flow, admin_page, wait_for_seconds):
    url, account, pwd, user_id, money, cellphone = admin_login_info

    admin_login_flow(url, account, pwd, user_id, money, cellphone)
    wait_for_seconds(2)

    admin_page.click_invite_list()
    wait_for_seconds(2)

    admin_page.click_invite_detail()
    wait_for_seconds(2)

    admin_page.input_cellphone_search(os.getenv("CELLPHONE_NUMBER"))
    wait_for_seconds(2)

    admin_page.click_search_btn()
    wait_for_seconds(2)

    relationship = admin_page.invite_relationship()
    assert "成立" in relationship
