import shutil
import pytest
import os
import re
import json
from dotenv import load_dotenv
from utils.email_utils import send_email, get_email_config

load_dotenv()


def set_report_name(allure_html_path, new_name):
    title_filepath = os.path.join(allure_html_path, "widgets", "summary.json")
    # 读取summary.json中的json数据，并改写reportName
    with open(title_filepath, 'r', encoding='utf-8') as f:
        # 加载json文件中的内容给params
        params = json.load(f)
        # 修改内容
        params['reportName'] = new_name
    # 往summary.json中，覆盖写入新的json数据
    with open(title_filepath, 'w', encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=4)


def generate_allure_report(results_directory, report_directory, report_title=None):
    # 使用 os 模块删除旧的报告目录，不需要分开为不同的操作系统编写不同的代码
    if os.path.exists(report_directory):
        shutil.rmtree(report_directory)

    # 生成 Allure 报告
    command = f'allure generate {results_directory} -o {report_directory}'
    os.system(command)

    # 检查报告文件是否存在，更改报告的网页标题
    report_path = os.path.join(report_directory, 'index.html')
    if os.path.exists(report_path):
        with open(report_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            content = re.sub(r'<title>Allure Report</title>', f'<title>{report_title}</title>', content)
            f.seek(0)
            f.write(content)
            f.truncate()
        print("Allure report title changed successfully:", report_path)
    else:
        print("Failed to change Allure report title.")

    # 修改 Allure 报告的标题文案
    set_report_name(report_directory, report_title)

    # 返回报告路径
    return report_path


def run_tests(test_path=None):
    report_title = os.getenv("REPORT_TITLE")

    # 获取邮件配置信息
    email_from, email_to, smtp_server, smtp_port, email_password, server_link, body, subject = get_email_config()

    # 指定报告目录
    report_directory = './allure-report'

    # 运行测试并生成 Allure 报告
    results_directory = './allure-results'

    # 默认的 pytest 参数
    pytest_args = ['-vs', f'--alluredir={results_directory}', '--clean-alluredir']
    if test_path:
        pytest_args.append(test_path)

    pytest.main(pytest_args)

    # 生成 Allure 报告
    generate_allure_report(results_directory, report_directory, report_title)

    # 发送邮件
    send_email(email_from, email_to, smtp_server, smtp_port, email_password, subject, body, server_link)


if __name__ == "__main__":
    run_tests("tests/web_tests")
