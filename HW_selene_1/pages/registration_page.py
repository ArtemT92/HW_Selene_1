from selene import browser, have
import os
from tests.conftest import RESOURCE_PATH


class RegistartionPage:
    def open(self):
        browser.open('/')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value2):
        browser.element('#lastName').type(value2)

    def fill_email(self, value3):
        browser.element('#userEmail').type(value3)

    def fill_gendare(self):
        browser.element('[for="gender-radio-1"').click()
    def fill_number(self, value4):
        browser.element('#userNumber').type(value4)

    def fill_subject(self, value5):
        browser.element('#subjectsInput').type(value5).press_enter()

    def fill_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()

    def choose_picture(self, file_name):
        browser.element('[id="uploadPicture"]').send_keys(os.path.join(RESOURCE_PATH, file_name))

    def fill_adress(self, value6):
        browser.element('#currentAddress').type(value6)

    def fill_state(self, value7):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value7)).click()

    def fill_city(self, value8):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value8)).click()

    def submit(self):
        browser.element('#submit').click()


    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--00{day}').click()

    def assert_registered_user_with(self):
        return browser.element('.table').all('td').even





















