import os

import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture
def browser_instance(request):
    global driver
    browser_name = request.config.getoption("browser_name").lower()

    if browser_name == "chrome":
        # Selenium Manager handles ChromeDriver automatically
        driver = webdriver.Chrome()
        print("Launched Chrome using Selenium Manager")

    elif browser_name == "firefox":
        # Selenium Manager handles GeckoDriver automatically
        driver = webdriver.Firefox()
        print("Launched Firefox using Selenium Manager")

    elif browser_name == "edge":
        # Edge still needs manual driver path
        edge_options = EdgeOptions()
        edge_options.add_argument(
            r"user-data-dir=C:\Users\sudhirb\AppData\Local\Microsoft\Edge\User Data"
        )
        edge_options.add_argument("profile-directory=Default")  # Change to Profile 1 if needed

        service_obj = EdgeService(
            r"C:\Users\sudhirb\Downloads\VoipAutomation_selenium\newselenium 13\PythonSeleniumProject\drivers\msedgedriver.exe"
        )
        driver = webdriver.Edge(service=service_obj, options=edge_options)
        print("Launched Edge with manual msedgedriver path")

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    print(f"Closing {browser_name} browser")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('browserInstance')
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_file = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_file)

            # Use relative path for HTML report
            report_path = item.config.option.htmlpath or "report.html"
            report_dir = os.path.dirname(report_path)
            rel_path = os.path.relpath(screenshot_file, start=report_dir or ".")

            extras_list = getattr(report, "extras", [])
            extras_list.append(extras.image(rel_path))
            extras_list.append(extras.url(driver.current_url))
            report.extras = extras_list