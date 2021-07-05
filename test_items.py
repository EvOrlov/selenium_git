from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button(browser):
    browser.get(link)
    sleep(30)
    # button ищет длину списка совпадений селектора. Если совпадение одно- тест пройден
    # если совпадений нет - падает по assert. Аналогично, если совпадений больше 1
    # Это сделано для того, чтобы тест падал строго по assert, а не по "no such element".
    # Использован сложный селектор, поскольку для отсутствющей в продаже книги, используется кнопка
    # "Notify me" с тем же классом, но с другим form id
    # http://selenium1py.pythonanywhere.com/ru/catalogue/hackers-painters_185/
    button = len(browser.find_elements_by_css_selector("form#add_to_basket_form > button.btn-add-to-basket"))
    assert button == 1, "button for basket not found or selector found more than 1 items!"
