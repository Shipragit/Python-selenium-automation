import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ServiceLocation(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        # self.switch_to_iFrame()
        self.qoute=None
        self.address_input = (By.ID, "sn_ind_tmt_orm_location.u_address")
        self.search_address_btn = (By.XPATH, "//button[@id='search_add' and contains(text(), 'Search address')]")
        self.search_address_table_rows = (By.CSS_SELECTOR, "div.modal-content tbody.list2_body tr")
        self.select_address_btn = (By.CSS_SELECTOR,"button[data-action-label ='Select Address']")

        self.location_contact_tab = (By.CSS_SELECTOR,"#tabs2_section span.tab_header:nth-of-type(2)")
        self.lcon_dropdown = (By.CSS_SELECTOR, "select[id='sys_select.sn_ind_tmt_orm_location.u_location_contact']")

        self.get_eligible_services_btn_locator = (By.CSS_SELECTOR, "span.navbar_ui_actions button#sqe_details")
        self.ptype_dropdown_locator = (By.CSS_SELECTOR, "Select[id*='.u_product_type']")
        self.psubtype_dropdown_locator = (By.CSS_SELECTOR, "Select[id*='.u_product_plan']")
        self.save_btn = (By.XPATH,"//div[@class='container-fluid']//button[contains(text(),'Save')]")
        self.preferred_area_code = (By.ID, "sn_ind_tmt_orm_location.u_preferred_area_code")
        self.package_type = (By.ID,"sn_ind_tmt_orm_location.u_package_type")
        self.is_primary_site = (By.ID, "sn_ind_tmt_orm_location.u_is_primary_site")
        self.component_type = (By.ID, "sn_ind_tmt_orm_location.u_component_type")

        self.next_btn = (By.XPATH, "//div[@class='container-fluid']//button[contains(text(),'Next')]")
        self.get_primary_price_plan_btn_locator = (By.XPATH, "//span[@class='navbar_ui_actions']//button[contains(text(),'Get Primary Priceplans POC')]")
        self.expand_group_btn = (By.CSS_SELECTOR, "div.list_div button.btn[data-dynamic-title='Expand group']")
        self.table_row=(By.CSS_SELECTOR, "div.modal-content tbody.list2_body tr.list_row")
        self.add_products_btn=(By.ID, "add_se")
        self.quantity=(By.CSS_SELECTOR, "div.list_div tbody.list2_body tr.list_row td:nth-of-type(12)")
        self.quantity_change=(By.XPATH, "//input[ @ id = 'cell_edit_value']")
        self.quantity_save=(By.XPATH, "//a[@id='cell_edit_ok']")
        self.add_primary_priceplan_btn = (By.ID, "se_add_on_1")
        self.catagory_unlock=(By.ID, "sn_ind_tmt_orm_location.u_choose_category_unlock")
        self.catagory_lock=(By.ID, "sn_ind_tmt_orm_location.u_choose_category_lock")
        self.select_category=(By.ID, "sys_display.sn_ind_tmt_orm_location.u_choose_category")
        self.lookup_category=(By.ID, "lookup.sn_ind_tmt_orm_location.u_choose_category")
        self.get_addTo_qoute_btn_locator=(By.ID, "add_quote_sloc")
        self.get_generate_quote_btn_locator=(By.ID, "generate_quote")
        self.get_send_quote_btn_locator=(By.CSS_SELECTOR, "button#send_quote")
        self.get_generate_contract_btn_locator=(By.ID, "generate_contract")
        self.get_header_add_attachment_btn_locator=(By.ID, "header_add_attachment")
        self.get_header_attachment_title_locator=(By.ID, "attachment_title")
        self.attach_close=(By.ID, "attachment_closemodal")
        self.contract_signed_dropdown=(By.ID, "sn_ind_tmt_orm_quote.u_contract_signed")
        self.get_save_btn_locator=(By.ID, "sysverb_update_and_stay")
        self.get_createban_btn_locator=(By.ID, "create_ban")
        self.get_banname_field_locator=(By.ID, "sn_ind_tmt_orm_c360_integration.u_ban_name")
        self.ban_address_locator=(By.ID, "sn_ind_tmt_orm_c360_integration.u_address")
        self.ban_postal_code=(By.ID, "sn_ind_tmt_orm_c360_integration.u_zip_postal_code")
        self.ban_email_locator=(By.ID, "sn_ind_tmt_orm_c360_integration.u_email")
        self.ban_phone_locator=(By.ID, "sn_ind_tmt_orm_c360_integration.u_phone")
        self.valid_checkbox_locator=(By.ID, "label.ni.sn_ind_tmt_orm_c360_integration.u_is_validation_required")
        self.get_valid_address_btn_locator=(By.ID, "validate_add_bottom")
        self.ban_address_submit_locator=(By.ID, "sysverb_insert_bottom")
        self.get_winloss_dd_locator=(By.ID, "sn_ind_tmt_orm_quote.u_winloss")
        self.get_createpackage_btn_locator=(By.ID, "create_package")
        self.get_qoute_tab_locator=(By.CSS_SELECTOR, "#tabs2_list span.tab_header:nth-of-type(3)")
        self.get_qoute_link_locator=(By.CSS_SELECTOR, "div.list_div tbody.list2_body tr[record_class='sn_ind_tmt_orm_quote_order'] td:nth-of-type(3)")
        self.get_date_field_locator=(By.ID, "sn_ind_tmt_orm_quote_order.u_crd")
        self.get_remarks_field_locator=(By.ID, "sn_ind_tmt_orm_quote_order.u_remarks")
        self.get_submitboss_btn_locator=(By.ID, "boss_om_VoIP")
        self.get_nopop_btn_locator=(By.CSS_SELECTOR, "button.no-button")
        self.get_address_field_locator=(By.ID, "sn_ind_tmt_orm_location.u_address")
        self.get_site_field_locator=(By.ID, "sn_ind_tmt_orm_location.u_site_name")
        self.primary_location_tab=(By.CSS_SELECTOR,"#tabs2_section span.tab_header:nth-of-type(3)")
        self.primary_tab=(By.CSS_SELECTOR,"select[name = 'sys_select.sn_ind_tmt_orm_quote.u_primary_contact']")
        self.Activity_tab=(By.CSS_SELECTOR,"#tabs2_section span.tab_header:nth-of-type(4)")

    def search_and_add_address(self, address):
        retry = 0
        max_retries = 4

        while retry < max_retries:
            print(f"Attempt {retry + 1}/{max_retries}: Searching for address '{address}'")

            # Enter address and search
            self.driver.find_element(*self.address_input).clear()
            self.driver.find_element(*self.address_input).send_keys(address)
            self.driver.find_element(*self.search_address_btn).click()

            try:
                # Wait for address search results
                address_search_results = self.wait.until(
                    EC.presence_of_all_elements_located(self.search_address_table_rows)
                )

                found = False
                for result in address_search_results:
                    address_name = result.find_element(By.CSS_SELECTOR, "td:nth-of-type(3)").text.strip()
                    print("Address in row: ", address_name)
                    if address_name == address:
                        print("Address match found, selecting checkbox.")
                        result.find_element(By.CSS_SELECTOR, "td:nth-of-type(1) label.checkbox-label").click()
                        found = True
                        break

                if not found:
                    print("Address not found in current results. Retrying...")
                    retry += 1
                    continue

                # Attempt to click 'Select Address'
                self.driver.find_element(*self.select_address_btn).click()

                # Wait for pop-up to disappear
                self.wait.until(EC.invisibility_of_element_located(self.search_address_table_rows))
                print("Address pop-up closed successfully.")
                return  # ✅ Success

            except TimeoutException:
                retry += 1
                print(f"Timeout waiting for search results or popup to close. Retry {retry}/{max_retries}")

        # If all retries fail
        raise TimeoutException(f"Failed to select address '{address}' after {max_retries} attempts.")

    def addingaddress(self,addr):
        driver = self.driver
        get_address_field = self.wait.until(
            EC.visibility_of_element_located(self.get_address_field_locator))
        get_address_field.send_keys(addr)

        new = driver.find_element(By.CSS_SELECTOR, "input[name='sn_ind_tmt_orm_location.u_quote_label']")
        self.qoute = new.get_attribute("value")
        print(self.qoute)

        get_site_field = self.wait.until(
            EC.visibility_of_element_located(self.get_site_field_locator))
        get_site_field.send_keys("test")

        get_serachadd_btn = self.wait.until(
            EC.visibility_of_element_located(self.search_address_btn))
        get_serachadd_btn.click()


        a=True
        while (a==True):
            addressRows = WebDriverWait(driver, 60).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.modal-content tbody.list2_body tr")))

            for row in addressRows:
                if row.find_element(By.CSS_SELECTOR,
                                        "td:nth-of-type(3)").text.strip() == addr:
                    row.find_element(By.CSS_SELECTOR, "td:nth-of-type(1) label.checkbox-label").click()
                    a=False
                    break
            #vcr_next
            if a==False:
                break
            lpage = driver.find_element(By.NAME, "vcr_next")
            driver.execute_script("arguments[0].scrollIntoView(true);", lpage)
            lpage.click()
            if   lpage.is_enabled() and a==True:
                lpage.click()
                time.sleep(5)

        get_selectadd_btn = self.wait.until(
            EC.visibility_of_element_located(self.select_address_btn))
        get_selectadd_btn.click()
        print("Address added successfully.",addr)
        # # Switch to the alert
        # alert = driver.switch_to.alert
        #
        # # Accept the alert
        # alert.accept()
        #
        time.sleep(10)

    def add_location_contact_details(self):
        self.driver.find_element(*self.location_contact_tab).click()
        lconDropDown = Select(self.driver.find_element(*self.lcon_dropdown))
        lconDropDown.select_by_visible_text("Test JulAcc002_Updated")
        #self.driver.find_element(By.ID, "sysverb_update_and_stay").click()
        time.sleep(10)

    def fetch_eligible_services(self):
        get_eligible_services_btn = self.wait.until(EC.visibility_of_element_located(self.get_eligible_services_btn_locator))
        get_eligible_services_btn.click()

    def non_primary_address_add_product_type_and_subtype(self):
        product_type_dropdown = Select(self.wait.until(EC.visibility_of_element_located(self.ptype_dropdown_locator)))

        p_type_options = [opt.text.strip() for opt in product_type_dropdown.options]
        for i in range(3):
            if len(p_type_options) > 1:
                if i > 1:
                    time.sleep(1)
                    print("Waiting after a trial for a second to to get product type")
                product_type_dropdown.select_by_visible_text("VoIP")
                break

        time.sleep(2)
        product_subtype_dropdown = Select(self.driver.find_element(*self.psubtype_dropdown_locator))

        p_subtype_options = [opt.text.strip() for opt in product_subtype_dropdown.options]

        for i in range(3):
            print('Available product subtype options:', p_subtype_options)
            print('Available product type options:', p_type_options)
            if "Voice+" in p_subtype_options:
                product_subtype_dropdown.select_by_visible_text("Voice+")
                break
            else:
                product_type_dropdown = Select(
                    self.wait.until(EC.visibility_of_element_located(self.ptype_dropdown_locator)))
                product_type_dropdown.select_by_visible_text("--None--")
                time.sleep(1)
                product_subtype_dropdown = Select(self.driver.find_element(*self.psubtype_dropdown_locator))
                product_type_dropdown.select_by_visible_text("VoIP")
                time.sleep(1)  # allow time for dropdown to refresh
                p_subtype_options = [opt.text.strip() for opt in product_subtype_dropdown.options]

        self.driver.find_element(*self.preferred_area_code).send_keys("210")

    def add_product_type_and_subtype(self, product_type, product_sub_type):
        product_type_dropdown = Select(self.wait.until(EC.visibility_of_element_located(self.ptype_dropdown_locator)))

        p_type_options = [opt.text.strip() for opt in product_type_dropdown.options]
        for i in range(3):
            if len(p_type_options) > 1:
                if i>1:
                    time.sleep(1)
                    print("Waiting after a trial for a second to to get product type")
                product_type_dropdown.select_by_visible_text(product_type)
                break

        time.sleep(2)
        product_subtype_dropdown = Select(self.driver.find_element(*self.psubtype_dropdown_locator))

        p_subtype_options = [opt.text.strip() for opt in product_subtype_dropdown.options]

        for i in range(3):
            print('Available product subtype options:', p_subtype_options)
            print('Available product type options:', p_type_options)
            if product_sub_type in p_subtype_options:
                product_subtype_dropdown.select_by_visible_text(product_sub_type)
                break
            else:
                product_type_dropdown = Select(self.wait.until(EC.visibility_of_element_located(self.ptype_dropdown_locator)))
                product_type_dropdown.select_by_visible_text("--None--")
                time.sleep(1)
                product_subtype_dropdown = Select(self.driver.find_element(*self.psubtype_dropdown_locator))
                product_type_dropdown.select_by_visible_text(product_type)
                time.sleep(1)  # allow time for dropdown to refresh
                p_subtype_options = [opt.text.strip() for opt in product_subtype_dropdown.options]


    def click_on_next_button(self):
        self.driver.find_element(*self.next_btn).click()

    def add_primary_price_plans(self, priceplan):
        # Wait for the Get Primary Priceplans button and click
        get_price_plans_btn = self.wait.until(EC.element_to_be_clickable(self.get_primary_price_plan_btn_locator))
        get_price_plans_btn.click()

        self.driver.find_element(By.XPATH, "//button[@class='accordion'][contains(text(),'PP1008 ')]").click()

        address_rows = self.wait.until(EC.presence_of_all_elements_located(self.table_row))
        for row in address_rows:
            row.find_element(By.CSS_SELECTOR, "td:nth-of-type(1) label.checkbox-label").click()

        #attempting to clicking add products btn
        self.driver.find_element(*self.add_products_btn).click()

        # waiting untill pop add primay plans pop up disappear
        self.wait.until(EC.invisibility_of_element_located(self.table_row))
        print("Primary price plans added successfully.")

    def increase_priceplan_quantity(self):
        # Step 1: Find the header index for "Quantity"
        product_table_headers = self.driver.find_elements(
            By.XPATH,
            "//table[@id='sn_ind_tmt_orm_location.REL:f87ba88a873ebd547d070fa8cebb352e_table']//thead//tr[1]//th"
        )

        index = 1
        for header in product_table_headers:
            if header.text.strip() == "Quantity":
                break
            index += 1

        # Step 2: Get the target cell (first row in tbody)
        quantity_cell = self.driver.find_element(
            By.XPATH,
            f"//table[@id='sn_ind_tmt_orm_location.REL:f87ba88a873ebd547d070fa8cebb352e_table']//tbody//tr[1]/td[{index}]"
        )

        # Step 3: Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", quantity_cell)

        # Step 4: Double-click to activate the input
        actions = ActionChains(self.driver)
        actions.move_to_element(quantity_cell).double_click().perform()

        # Step 5: Wait for the input field to appear
        quntity_input= self.driver.find_element(By.ID,"cell_edit_value")
        quntity_input.clear()
        quntity_input.send_keys("10")

        # Step 6: Save the quantity
        self.driver.find_element(*self.quantity_save).click()

        # clicking on next btn
        self.click_on_next_button()

        # click on Get Addon Price plans
        # add_priceplans_btn = self.wait.until(EC.element_to_be_clickable(self.add_primary_priceplan_btn))
        # add_priceplans_btn.click()

    def choose_category(self):
        #click unlock button
        choose_category_btn = self.wait.until(EC.element_to_be_clickable(self.catagory_unlock))
        choose_category_btn.click()

        # selecting the catagory
        get_select_catagory = self.wait.until(
            EC.visibility_of_element_located(self.select_category))
        get_select_catagory.send_keys("Service")

        get_lookup_catagory = self.wait.until(
            EC.visibility_of_element_located(self.lookup_category))
        get_lookup_catagory.click()


        #clicking on lock button
        self.driver.find_element(*self.catagory_lock).click()

        #clicing on next button
        self.click_on_next_button()

        #clicking on next button
        self.click_on_next_button()

    def click_on_addTo_qoute(self):

        # click on Add to Quote -- ui action
        time.sleep(5)
        get_addTo_qoute_btn = self.wait.until(
            EC.visibility_of_element_located(self.get_addTo_qoute_btn_locator))
        get_addTo_qoute_btn.click()

        time.sleep(10)

    def generate_send_qoute(self):
        # Then it redirect to quote page click on next -- ui action
        # self.driver.find_element(By.XPATH, "//button[ @ id = 'ew_site']").click()
        # time.sleep(10)
        self.driver.find_element(By.XPATH, "//button[ @ id = 'ew_site']").click()
        time.sleep(10)

        # generate_quote
        get_generate_quote_btn = self.wait.until(
            EC.visibility_of_element_located(self.get_generate_quote_btn_locator))
        get_generate_quote_btn.click()
        print("Quote generated successfully")

        time.sleep(5)

        primary_location_tab = self.wait.until(
            EC.visibility_of_element_located(self.primary_location_tab))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", primary_location_tab)
        primary_location_tab.click()
        time.sleep(5)


        primary_tab = Select(self.driver.find_element(*self.primary_tab))
        primary_tab.select_by_index(1)

        time.sleep(10)

        get_send_quote_btn = self.wait.until(
            EC.visibility_of_element_located(self.get_send_quote_btn_locator))
        get_send_quote_btn.click()
        print("Quote sent successfully")

        self.driver.find_element(By.ID, "check_credit").click()
        time.sleep(10)

        activity_tab = self.wait.until(
            EC.visibility_of_element_located(self.Activity_tab))
        activity_tab.click()

    def click_generatecontract(self):

        # generate_contract UI action
        get_generate_contract_btn = self.wait.until(
            EC.visibility_of_element_located(self.get_generate_contract_btn_locator))
        get_generate_contract_btn.click()
        print("contract successfully")

    def click_attachment(self):
        #click attachment link
        get_header_add_attachment_btn = self.wait.until(
            EC.visibility_of_element_located(self.get_header_add_attachment_btn_locator))
        get_header_add_attachment_btn.click()

    def manual_sign(self):

        #manual sign
        get_header_attachment_title = self.wait.until(
            EC.visibility_of_element_located(self.get_header_attachment_title_locator))
        get_header_attachment_title.click()
        self.driver.find_element(By.CSS_SELECTOR,
                            f"div[id='attachment_dialog_list'] a[aria-label='Rename Brightspeed Contract {self.qoute}.pdf']").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "div[id='attachment_dialog_list'] a[contenteditable='true']")
        self.driver.execute_script(f"arguments[0].innerText =  'Brightspeed Contract {self.qoute}signed.pdf'", element)
        time.sleep(3)
        get_header_attachment_title.click()
        self.driver.find_element(*self.attach_close).click()



        DropDown = Select(self.driver.find_element(*self.contract_signed_dropdown))
        DropDown.select_by_visible_text("Yes")

        # click on save UI action

    def save (self):
        #sysverb_update_and_stay
        get_save_btn = self.wait.until(
            EC.visibility_of_element_located(self.get_save_btn_locator))
        get_save_btn.click()

    def create_associate_ban(self):

        get_createban_btn = self.wait.until(
            EC.visibility_of_element_located(self.get_createban_btn_locator))
        get_createban_btn.click()
        print("manual signed  successfull")
        addressRows = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.modal-content tbody.list2_body tr.list_row")))

        for row in addressRows:
            row.find_element(By.CSS_SELECTOR, "td:nth-of-type(1) label.checkbox-label").click()


        self.driver.find_element(By.ID, "select_ban").click()

    def ordering(self,date1):
        # selecting winloss
        get_winloss_dd = self.wait.until(
            EC.visibility_of_element_located(self.get_winloss_dd_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", get_winloss_dd)
        dd = Select(get_winloss_dd)
        dd.select_by_visible_text("Pricing")
        time.sleep(5)
        # clickimng on order package UI action
        get_createpackage_btn = self.wait.until(
            EC.visibility_of_element_located(self.get_createpackage_btn_locator))
        get_createpackage_btn.click()

        time.sleep(10)
        #Qoute clicking
        get_qoute_tab = self.wait.until(
            EC.visibility_of_element_located(self.get_qoute_tab_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", get_qoute_tab)
        get_qoute_tab.click()

        get_qoute_tab.click()

        #clicking qoute
        # get_qoute_link = self.wait.until(
        #     EC.visibility_of_element_located(self.get_qoute_link_locator))
        # get_qoute_link.click()

        #new step
        #div.list_div tbody.list2_body tr[record_class='sn_ind_tmt_orm_quote_order'] td:nth-of-type(3)
        addressRows = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.list_div tbody.list2_body tr[record_class='sn_ind_tmt_orm_quote_order']")))

        for row in addressRows:

            if row.find_element(By.CSS_SELECTOR,
                                "td:nth-of-type(9)").text.strip() == "Yes":
                row.find_element(By.CSS_SELECTOR, "td:nth-of-type(3)").click()
                break

        #new step

       #entering date in qoute page
        get_date_field = self.wait.until(
            EC.visibility_of_element_located(self.get_date_field_locator))
        get_date_field.send_keys(date1)
        #sysverb_update_and_stay
        #sysverb_update_and_stay
        self.save()
        self.click_on_next_button()

        # sn_ind_tmt_orm_quote_order.u_remarks
        get_remarks_field = self.wait.until(
            EC.visibility_of_element_located(self.get_remarks_field_locator))
        get_remarks_field.send_keys("test1")



        # clicking on submit order button
        # boss_om_VoIP
        get_submitboss_btn = self.wait.until(
            EC.visibility_of_element_located(self.get_submitboss_btn_locator))
        get_submitboss_btn.click()

        # button.no-button
        get_nopop_btn = self.wait.until(
            EC.visibility_of_element_located(self.get_nopop_btn_locator))
        get_nopop_btn.click()
        time.sleep(10)

        new = self.driver.find_element(By.ID, "sys_readonly.sn_ind_tmt_orm_quote_order.u_boss_om_number")
        n1 = new.get_attribute("value")
        print("BOSS OM Order Number:", n1)
        time.sleep(5)