from selenium.webdriver.common.by import By

page_link = 'https://qa-scooter.praktikum-services.ru/'

samokat = (By.XPATH, ".//a[descendant::img[@alt='Scooter']]")
yandex = (By.XPATH, ".//a[descendant::img[@alt='Yandex']]")
order_top = (
    By.XPATH, ".//div[button='Статус заказа']/button[text()='Заказать']")
order_bottom = (
    By.XPATH, ".//div/button[last()][text()='Заказать']")

question_1 = (By.XPATH, ".//div[text()[contains(.,'Сколько это стоит?')]]")
question_2 = (By.XPATH, ".//div[text()[contains(.,'Хочу сразу несколько самокатов!')]]")  # noqa
question_3 = (By.XPATH, ".//div[text()[contains(.,'Как рассчитывается время аренды?')]]")  # noqa
question_4 = (By.XPATH, ".//div[text()[contains(.,'Можно ли заказать самокат прямо на сегодня?')]]")  # noqa
question_5 = (By.XPATH, ".//div[text()[contains(.,'Можно ли продлить заказ или вернуть самокат раньше?')]]")  # noqa
question_6 = (By.XPATH, ".//div[text()[contains(.,'Вы привозите зарядку вместе с самокатом?')]]")  # noqa
question_7 = (By.XPATH, ".//div[text()[contains(.,'Можно ли отменить заказ?')]]")  # noqa
question_8 = (By.XPATH, ".//div[text()[contains(.,'Я жизу за МКАДом, привезёте?')]]")  # noqa
answer_1 = (By.XPATH, ".//div/p[text()[contains(.,'Сутки — 400 рублей. Оплата курьеру')]]")  # noqa
answer_2 = (By.XPATH, ".//div/p[text()[contains(.,'Пока что у нас так: один заказ')]]")  # noqa
answer_3 = (By.XPATH, ".//div/p[text()[contains(.,'Допустим, вы оформляете заказ на')]]")  # noqa
answer_4 = (By.XPATH, ".//div/p[text()[contains(.,'Только начиная с завтрашнего')]]")  # noqa
answer_5 = (By.XPATH, ".//div/p[text()[contains(.,'Пока что нет! Но если что-то срочное')]]")  # noqa
answer_6 = (By.XPATH, ".//div/p[text()[contains(.,'Самокат приезжает к вам с полной')]]")  # noqa
answer_7 = (By.XPATH, ".//div/p[text()[contains(.,'Да, пока самокат не привезли')]]")  # noqa
answer_8 = (By.XPATH, ".//div/p[text()[contains(.,'Всем самокатов! И Москве')]]")  # noqa
cookie_consent_button = (By.XPATH, ".//button[text()='да все привыкли']")
