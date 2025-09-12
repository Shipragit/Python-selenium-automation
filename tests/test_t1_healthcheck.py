from pages.login_page import LoginPage
from pages.quote_page import QuotePage
from pages.service_location import ServiceLocation


def test_t1_hc_install(browser_instance,request):
    custom_name = f"T1 Install Order test"
    request.node._nodeid = custom_name

    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login("PT.test1@example.com","Brightspeed@123")

    quote_page = QuotePage(driver)
    quote_page.add_mandatory_quote_form_values("12 Months")
    quote_page.initiate_new_location()

    svc_loc_page = ServiceLocation(driver)
    svc_loc_page.search_and_add_address("1913 SALISBURY WAY HINESVILLE, GA, 31313")
    svc_loc_page.add_location_contact_details()
    svc_loc_page.fetch_eligible_services()
    svc_loc_page.add_product_type_and_subtype("VOICE","POTS")
    svc_loc_page.add_primary_price_plans("PP1008")