import os
import logging
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ---------- Logging Setup ----------
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

log_file = os.path.join(LOG_DIR, "automation.log")

# Configure root logger once
logger = logging.getLogger(__name__)
if not logger.hasHandlers():   # Prevent duplicate logs if re-imported
    logger.setLevel(logging.DEBUG)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    ch.setFormatter(ch_formatter)

    # File handler
    fh = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    fh.setFormatter(fh_formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)


# ---------- BasePage ----------
class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # ---------- Waits ----------
    def wait_for_element_visible(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Element {locator} not visible after {self.timeout}s")
            raise

    def wait_for_element_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            logger.error(f"Element {locator} not clickable after {self.timeout}s")
            raise

    # ---------- Common Actions ----------
    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()
        logger.info(f"Clicked on element {locator}")

    def type_text(self, locator, text, clear_first=True):
        element = self.wait_for_element_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)
        logger.info(f"Typed '{text}' into element {locator}")

    def get_text(self, locator):
        element = self.wait_for_element_visible(locator)
        text = element.text
        logger.info(f"Got text '{text}' from element {locator}")
        return text

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            logger.info(f"Element {locator} is present")
            return True
        except NoSuchElementException:
            logger.warning(f"Element {locator} not found")
            return False

    # ---------- Dropdowns ----------
    def select_by_visible_text(self, locator, text):
        element = self.wait_for_element_visible(locator)
        Select(element).select_by_visible_text(text)
        logger.info(f"Selected '{text}' from dropdown {locator}")

    def select_by_index(self, locator, index):
        element = self.wait_for_element_visible(locator)
        Select(element).select_by_index(index)
        logger.info(f"Selected index {index} from dropdown {locator}")

    def select_by_value(self, locator, value):
        element = self.wait_for_element_visible(locator)
        Select(element).select_by_value(value)
        logger.info(f"Selected value '{value}' from dropdown {locator}")

    # ---------- JS Helpers ----------
    def js_click(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)
        logger.info(f"Clicked (JS) on element {locator}")

    def scroll_into_view(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.info(f"Scrolled into view {locator}")

    # ---------- Browser ----------
    def get_page_title(self):
        title = self.driver.title
        logger.info(f"Page title: {title}")
        return title

    def get_current_url(self):
        url = self.driver.current_url
        logger.info(f"Current URL: {url}")
        return url
