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

