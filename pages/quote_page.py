import time

from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.API_UTILS import API_UTILS

class QuotePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 120)
        self.move_to_quote()
        # self.switch_to_iFrame()

        self.quote_desc = (By.ID, "sn_ind_tmt_orm_quote.u_quote_description")
        # sn_ind_tmt_orm_quote.u_quote_description
        self.term_dropdown = (By.ID, "sn_ind_tmt_orm_quote.u_term")
        self.new_loc_btn = (By.XPATH, "//button[contains(text(), 'New')]")
        # self.save_btn = (By.CSS_SELECTOR, "span.ui_action_container_primary #sysverb_update_and_stay")
        self.get_new_location_btn_locator = (By.ID, "sysverb_new")
        self.save_btn = (By.ID, "sysverb_update_and_stay")

    def move_to_quote(self):
        api_utils = API_UTILS()
        quote_url = api_utils.create_voip_quote()
        print(f"Received Quote URL is: {quote_url}")
        self.driver.get(quote_url)

    def switch_to_iFrame(self):
        print(self.driver.title)
        shadow_host1_locator = (By.CSS_SELECTOR, "macroponent-f51912f4c700201072b211d4d8c26010")
        self.wait_for_element_visible(shadow_host1_locator)
        shadow_host1 = self.driver.find_element(By.CSS_SELECTOR, "macroponent-f51912f4c700201072b211d4d8c26010")
        shadow_root1 = shadow_host1.shadow_root

        # 2. Second shadow host
        shadow_host2 = shadow_root1.find_element(By.CSS_SELECTOR, "sn-canvas-appshell-root")
        shadow_root2 = shadow_host2.shadow_root

        # 3. First slot inside second shadow DOM
        slot1 = shadow_root2.find_element(By.CSS_SELECTOR, "slot")
        assigned1 = self.driver.execute_script("return arguments[0].assignedNodes({flatten: true})", slot1)

        # 4. Find sn-canvas-appshell-layout from assigned nodes
        layout = next(el for el in assigned1 if el.tag_name.lower() == "sn-canvas-appshell-layout")
        shadow_root3 = layout.shadow_root

        # 5. Second slot inside third shadow DOM
        slot2 = shadow_root3.find_element(By.CSS_SELECTOR, "slot")
        assigned2 = self.driver.execute_script("return arguments[0].assignedNodes({flatten: true})", slot2)

        # 6. Find sn-polaris-layout from assigned nodes
        polaris = next(el for el in assigned2 if el.tag_name.lower() == "sn-polaris-layout")
        polaris_shadow = polaris.shadow_root

        # 7. Third slot inside polaris shadow DOM
        slot3 = polaris_shadow.find_element(By.CSS_SELECTOR, "slot")
        assigned3 = self.driver.execute_script("return arguments[0].assignedNodes({flatten: true})", slot3)

        # 8. Find iframe with id 'gsft_main'
        iframe = next(
            el for el in assigned3
            if el.tag_name.lower() == "iframe" and el.get_attribute("id") == "gsft_main"
        )

        # Switch to the iframe
        self.driver.switch_to.frame(iframe)

        # You are now inside the iframe and can proceed
        print("Switched to iframe: gsft_main")

        # Example usage: print iframe document title
        print(self.driver.title)

    def add_mandatory_quote_form_values(self, term):
        quote_desc = self.wait.until(EC.visibility_of_element_located(self.quote_desc))
        quote_desc.clear()
        quote_desc.send_keys("Test Quote Desc")
        Select(self.driver.find_element(*self.term_dropdown)).select_by_value(term)

        for i in range(3):
            print(f"Trying the save of Quote Form for the {i} time")
            try:
                self.driver.find_element(*self.save_btn).click()
                self.wait.until(EC.staleness_of(self.driver.find_element(*self.save_btn)))
                print("Save button became stale — form is refreshing")
                self.wait.until(EC.element_to_be_clickable(self.new_loc_btn))

                print("New Location button is now clickable.")
                break
            except TimeoutException:
                print("Save did not finish or page did not reload properly.")
                if (i == 3):
                    raise

    def initiate_new_location(self):
        retry = 0
        max_retries = 3

        while retry < max_retries:
            try:
                print(f"Attempt {retry + 1} of {max_retries}")

                # Always re-locate element fresh inside the loop
                new_loc_button = self.wait.until(EC.element_to_be_clickable(self.new_loc_btn))
                new_loc_button.click()
                self.wait.until(EC.title_contains("New Record | Service Location | ServiceNow"))
                print("Clicked 'New Location' button.")

                # Wait until the new page is loaded
                self.wait.until(EC.title_contains("New Record | Service Location | ServiceNow"))
                print("New Service Location page loaded successfully.")
                return  # Exit on success

            except StaleElementReferenceException:
                retry += 1
                print(f"Retry {retry}: Caught stale element. Re-locating in next iteration.")

            except TimeoutException:
                retry += 1
                print(f"Retry {retry}: Page title did not load. Trying again...")

                try:
                    # Optional: check visibility after timeout
                    if self.driver.find_element(*self.new_loc_btn).is_displayed():
                        print("New Location button still visible. Retrying...")
                except StaleElementReferenceException:
                    print("Element went stale again during visibility check.")

        # If all retries failed
        raise TimeoutException("Failed to load 'New Service Location' page after retries.")

    def new_location(self, term):
        quote_desc = self.wait.until(EC.visibility_of_element_located(self.quote_desc))
        quote_desc.clear()
        quote_desc.send_keys("Test Quote Desc")

        dropdown = self.wait.until(EC.visibility_of_element_located(self.term_dropdown))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dd = Select(dropdown)
        dd.select_by_visible_text(term)
        time.sleep(5)
        save_button = self.wait.until(EC.element_to_be_clickable(self.save_btn))
        save_button.click()
        time.sleep(10)

        new_loc_button = self.wait.until(EC.element_to_be_clickable(self.new_loc_btn))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", new_loc_button)
        new_loc_button.click()

    def secondary_location(self):
        new_loc_button = self.wait.until(EC.element_to_be_clickable(self.new_loc_btn))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", new_loc_button)
        new_loc_button.click()





