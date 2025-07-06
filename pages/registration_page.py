from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "firstName")
        self.last_name_field = (By.ID, "lastName")
        self.email_field = (By.ID, "userEmail")
        self.male_radio = (By.ID, "gender-radio-1")
        self.mobile_nr_field = (By.ID, "userNumber")
        self.calendar_field = (By.ID, "dateOfBirthInput")
        self.subject_field = (By.ID, "subjectsContainer")
        self.hobbies_checkbox = (By.ID, "hobbies-checkbox-1")
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

    def choose_gender_ratio(self):
        if not self.driver.find_element(*self.male_radio).is_selected():
            self.driver.find_element(*self.male_radio).click()

    def enter_phone_number(self, mobile_number):
        self.driver.find_element(*self.mobile_nr_field).send_keys(mobile_number)

    def choose_date(self, date):
        self.driver.find_element(*self.calendar_field).send_keys(date)

    def enter_subject(self, subject):
        self.driver.find_element(*self.subject_field).send_keys(subject)

    def choose_hobby(self):
        if not self.driver.find_element(*self.hobbies_checkbox).is_selected():
            self.driver.find_element(*self.hobbies_checkbox).click()

    def upload_photo(self, file_path):
        self.driver.find_element(*self.upload_pic_button).send_keys(file_path)

    def enter_current_adress(self, current_address):
        self.driver.find_element(*self.current_address_field).send_keys(current_address)

    def choose_state_by_visible_text(self, state):
        self.driver.find_element(*self.state_choice).select_by_visible_text(state)

    def choose_city_by_visible_text(self, city):
        self.driver.find_element(*self.city_choice).select_by_visible_text(city)

    def push_submit(self, submit_button):
        self.driver.find_element(*self.submit_button).select_by_visible_text(submit_button)