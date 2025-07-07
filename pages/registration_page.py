import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scroll_and_wait_clickable(driver, locator):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    return element
class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "firstName")
        self.last_name_field = (By.ID, "lastName")
        self.email_field = (By.ID, "userEmail")
        self.male_radio = (By.ID, "gender-radio-1")
        self.female_radio = (By.ID, "gender-radio-2")
        self.mobile_nr_field = (By.ID, "userNumber")
        self.calendar_field = (By.ID, "dateOfBirthInput")
        self.subject_field = (By.ID, "subjectsInput")
        self.hobby_checkboxes = {
            "Sports": (By.XPATH, "//label[@for='hobbies-checkbox-1']"),
            "Reading": (By.XPATH, "//label[@for='hobbies-checkbox-2']"),
            "Music": (By.XPATH, "//label[@for='hobbies-checkbox-3']")
        }

        self.upload_pic_button = (By.ID, "uploadPicture")
        self.current_address_field = (By.ID, "currentAddress")
        self.state_choice = (By.ID, "states")
        self.city_choice = (By.ID, "city")
        self.submit_button = (By.ID, "submit")

    def open(self, url):
        self.driver.get(url)

    def enter_first_name(self, firstName):
        self.driver.find_element(*self.first_name_field).send_keys(firstName)

    def enter_last_name(self, lastName):
        self.driver.find_element(*self.last_name_field).send_keys(lastName)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def choose_gender_ratio(self, gender):
        if gender == "Male":
            label = self.driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
        else:
            label = self.driver.find_element(By.XPATH, "//label[@for='gender-radio-2']")

        label.click()

    def enter_phone_number(self, mobile_number):
        self.driver.find_element(*self.mobile_nr_field).send_keys(mobile_number)

    def choose_date(self, date):
        date_input = self.driver.find_element(*self.calendar_field)
        date_input.click()
        #date_input.send_keys(Keys.CONTROL + "a") # pažymi visą datą
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER) # svarbu! uždaro date picker


    def enter_subject(self, subject):
        subject_input = self.driver.find_element(*self.subject_field)
        subject_input.send_keys(subject)
        subject_input.send_keys(Keys.ENTER)
    def choose_hobby(self, hobby_name):
        locator = self.hobby_checkboxes.get(hobby_name) # lygu locator = (By.ID, "hobby-checkbox-1")
        if locator:
            wait = WebDriverWait(self.driver, 10)
            checkbox = wait.until(EC.element_to_be_clickable(locator))
            if not checkbox.is_selected():
                checkbox.click()

    def upload_photo(self, file_path):
        self.driver.find_element(*self.upload_pic_button).send_keys(file_path)

    def enter_current_adress(self, current_address):
        self.driver.find_element(*self.current_address_field).send_keys(current_address)

    def choose_state_by_visible_text(self, state):
        state_dropdown_locator = (By.ID, "state")
        state_dropdown = scroll_and_wait_clickable(self.driver, state_dropdown_locator)
        state_dropdown.click()
        option = self.driver.find_element(By.XPATH,
                                          f"//div[contains(@id, 'react-select-3-option') and text()='{state}']")
        option.click()
    def choose_city_by_visible_text(self, city):
        city_dropdown = self.driver.find_element(By.ID, "city")
        city_dropdown.click()
        time.sleep(1)
        city_input = self.driver.find_element(By.ID, "react-select-4-input")
        city_input.send_keys(city)
        city_input.send_keys(Keys.ENTER)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def is_result_table_displayed(self):
        try:
            return self.driver.find_element(By.ID, "example-modal-sizes-title-lg").is_displayed()
        except NoSuchElementException:
            return False