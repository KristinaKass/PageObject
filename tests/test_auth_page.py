from pages.auth_page import AuthPage
import time


def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_email("email@gmail.commmmmm")
    page.enter_pass("pass")
    page.btn_click()


    assert page.get_relative_link() != '/all pets', "login error"

    time.sleep(4)