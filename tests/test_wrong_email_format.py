from selenium.webdriver.common.by import By

from pages.registration_page import RegistrationPage

def test_wrong_email_format(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open("https://demoqa.com/automation-practice-form")

    registration_page.enter_first_name("Andrius")
    registration_page.enter_last_name("Gelezevicius")
    registration_page.enter_email("andrius.gelezevicius.com")
    registration_page.choose_gender_ratio("Male")
    registration_page.enter_phone_number("1234567890")
    registration_page.choose_date("10 February 1989")
    registration_page.enter_subject("Maths")
    registration_page.choose_hobby("Sports")
    registration_page.upload_photo("C:/Users/PC/Desktop/ProfilePhoto.jpg")
    registration_page.enter_current_adress("123 Test street")
    registration_page.choose_state_by_visible_text("NCR")
    registration_page.choose_city_by_visible_text("Delhi")
    registration_page.click_submit()

    email_element = driver.find_element(By.ID, "userEmail")
    border_color_email = email_element.value_of_css_property("border-color")

    assert "rgb(220, 53, 69)" in border_color_email, f"Expected red border, got {border_color_email}"
    assert not registration_page.is_result_table_displayed(), "Result modal should not be displayed"