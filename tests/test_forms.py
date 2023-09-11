from hw_selene_1.pages.registration_page import RegistartionPagefrom hw_selene_1.pages import user



def test_registration_form():
    registartion_page = RegistartionPage()
    registartion_page.open()
    student = user.student


    # When
    registartion_page.fill(student)


    # Then
    registartion_page.should_have_registered(student)
