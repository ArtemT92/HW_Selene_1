from selene import browser, have
from hw_selene_1.pages.registration_page import RegistartionPage


def test_registration_form():
    registartion_page = RegistartionPage()
    registartion_page.open()

    # When
    registartion_page.fill_first_name('Артем')
    registartion_page.fill_last_name('Трунилин')
    registartion_page.fill_email('trunilin@mail.com')
    registartion_page.fill_gendare()
    registartion_page.fill_number('8910787986')
    registartion_page.fill_date_of_birth('1992', 'April', '6')
    registartion_page.fill_subject('English')
    registartion_page.fill_hobbies()
    registartion_page.choose_picture('photo.jpg')
    registartion_page.fill_adress('Мирная 186 д1')
    registartion_page.fill_state('NCR')
    registartion_page.fill_city('Delhi')
    registartion_page.submit()

    # Then
    registartion_page.assert_registered_user_with(
        'Артем Трунилин',
        'trunilin@mail.com',
        'Male',
        '8910787986',
        '06 April,1992',
        'English',
        'Sports',
        'photo.jpg',
        'Мирная 186 д1',
        'NCR Delhi',
    )
