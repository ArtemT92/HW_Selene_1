from selene import browser, have
import os
from tests.conftest import RESOURCE_PATH


class RegistartionPage:
    def open(self):
        browser.open('/')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gendare(self):
        browser.element('[for="gender-radio-1"').click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--00{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()

    def choose_picture(self, file_name):
        browser.element('[id="uploadPicture"]').send_keys(os.path.join(RESOURCE_PATH, file_name))

    def fill_adress(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def submit(self):
        browser.element('#submit').click()



    def assert_registered_user_with(self, full_name, email, gender, mobile_number, date_of_birth,
                                    subjects, hobbies, picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city
            )
        )
