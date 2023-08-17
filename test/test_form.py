

from selene import browser, have, be
import os



def test_registration():
    browser.open('https://demoqa.com/automation-practice-form')


    browser.element('#firstName').type('Артем')
    browser.element('#lastName').type('Трунилин')
    browser.element('#userEmail').type('trunilin@mail.com')
    browser.element('[for="gender-radio-1"').click()
    browser.element('#userNumber').type('8910787986')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="3"]').click()
    browser.element('.react-datepicker__year-select [value="1992"]').click()
    browser.element('[aria-label="Choose Monday, April 6th, 1992"]').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/zhivotnye_igra_sobaka_19261.jpg'))
    browser.element('#currentAddress').click().type('Мирная 186 д1')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').click()




    # Проверки
    browser.element('.table').should(have.text('Артем'))
    browser.element('.table').should(have.text('Трунилин'))
    browser.element('.table').should(have.text('trunilin@mail.com'))
    browser.element('.table').should(have.text('Male'))
    browser.element('.table').should(have.text('8910787986'))
    browser.element('.table').should(have.text('06 April,1992'))
    browser.element('.table').should(have.text('English'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('zhivotnye_igra_sobaka_19261.jpg'))
    browser.element('.table').should(have.text('Мирная 186 д1'))
    browser.element('.table').should(have.text('NCR'))
    browser.element('.table').should(have.text('Delhi'))



