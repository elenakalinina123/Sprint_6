from selenium.webdriver.common.by import By

index_page_link = 'https://qa-scooter.praktikum-services.ru/'

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
text_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой'
text_2 = (
    'Пока что у нас так: один заказ — один самокат. Если хотите' +
    ' покататься с друзьями, можете просто сделать несколько заказов' +
    ' — один за другим.')
text_3 = (
    'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая' +
    ' в течение дня. Отсчёт времени аренды начинается с момента, когда' +
    ' вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в' +
    ' 20:30, суточная аренда закончится 9 мая в 20:30.')
text_4 = (
    'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')
text_5 = (
    'Пока что нет! Но если что-то срочное — всегда можно позвонить в' +
    ' поддержку по красивому номеру 1010.')
text_6 = (
    'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь' +
    ' суток — даже если будете кататься без передышек и во сне. Зарядка' +
    ' не понадобится.')
text_7 = (
    'Да, пока самокат не привезли. Штрафа не будет, объяснительной' +
    ' записки тоже не попросим. Все же свои.')
text_8 = (
    'Да, обязательно. Всем самокатов! И Москве, и Московской области.')

answer_1 = (By.XPATH, f".//div[text()[contains(.,'{text_1}')]]")
answer_2 = (By.XPATH, f".//div[text()[contains(.,'{text_2}')]]")
answer_3 = (By.XPATH, f".//div[text()[contains(.,'{text_3}')]]")
answer_4 = (By.XPATH, f".//div[text()[contains(.,'{text_4}')]]")
answer_5 = (By.XPATH, f".//div[text()[contains(.,'{text_5}')]]")
answer_6 = (By.XPATH, f".//div[text()[contains(.,'{text_6}')]]")
answer_7 = (By.XPATH, f".//div[text()[contains(.,'{text_7}')]]")
answer_8 = (By.XPATH, f".//div[text()[contains(.,'{text_8}')]]")
