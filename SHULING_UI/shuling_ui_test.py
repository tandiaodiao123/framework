import pytest
from playwright.sync_api import sync_playwright, Page, expect

import os
import re


# 使用 yield 关键字创建一个自定义的 page 夹具
@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        # 1. 启动持久化上下文
        # 注意：使用持久化上下文时，不能再调用 browser.new_context()
        context = p.chromium.launch_persistent_context(
            user_data_dir="./my_browser_data",  # 数据保存在当前目录的 my_browser_data 文件夹
            headless=False,  # 必须设为 False，方便你第一次手动登录
            # slow_mo=500                      # 如果觉得跑太快，可以取消注释这行，放慢 500 毫秒
        )

        # 2. 获取 page 对象
        page = context.pages[0] if context.pages else context.new_page()

        # 3. 将 page 提供给测试用例使用
        yield page

        # 4. 测试结束后，关闭上下文
        context.close()


def test_example(page: Page) -> None:
    # 判断是不是第一次运行（如果目录不存在，说明是全新的）
    is_first_run = not os.path.exists("./my_browser_data")

    # 打开登录页或你的目标页
    page.goto("https://www-daily.yuntim.com/bizmodule/bteamLogin/login.htm")

    if is_first_run:
        print("\n" + "=" * 50)
        print("⚠️ 检测到首次运行，请在弹出的浏览器中手动登录！")
        print("你有 30 秒的时间输入手机号并获取验证码...")
        print("=" * 50 + "\n")
        # 留给你 30 秒的时间手动操作登录
        page.wait_for_timeout(30000)

        # 登录成功后，导航到目标工作台
        page.goto("https://www-daily.yuntim.com/bizmodule/bteam/home/chat.htm")
    else:
        print("\n✅ 检测到已保存的登录状态，跳过登录步骤...")
        # 如果已经有登录态，直接去目标页
        page.goto("https://www-daily.yuntim.com/bizmodule/bteam/home/chat.htm")

    # ---------------- 以下是你录制的自动化操作 ----------------

    # 等待页面加载完成
    page.wait_for_load_state("networkidle")

    page.get_by_role("button", name="更多").click()
    page.get_by_role("button", name="书灵AI").click()

    # 正确标准的 iframe 定位方式
    iframe = page.frame_locator("iframe")

    # 1. 点击下拉框
    iframe.get_by_role("combobox", name="题目属性 :").click()

    # 2. 先定位到下拉菜单的容器
    dropdown = iframe.locator(".yt5-antd-select-dropdown")

    # 3. 在这个容器里断言包含“母题”的选项可见
    expect(dropdown.get_by_text("常规题", exact=True)).to_be_visible()


