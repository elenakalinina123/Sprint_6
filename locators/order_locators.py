from selenium.webdriver.common.by import By

order_page_link = 'https://qa-scooter.praktikum-services.ru/order'

first_name = (By.XPATH, ".//input[@placeholder='* Имя']")
last_name = (By.XPATH, ".//input[@placeholder='* Фамилия']")
address = (
    By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
metro = (By.XPATH, ".//input[@placeholder='* Станция метро']")
metro_10_button = (By.XPATH, ".//li[@data-value='10']")
metro_20_button = (By.XPATH, ".//li[@data-value='20']")
phone = (
    By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
next_button = (By.XPATH, ".//button[text()='Далее']")
date = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
date_5th = (By.XPATH, ".//div[text()=5]")
date_10th = (By.XPATH, ".//div[text()=10]")
duration = (By.XPATH, ".//div[text()='* Срок аренды']")
duration_one_day = (By.XPATH, ".//div[text()='сутки']")
duration_two_days = (By.XPATH, ".//div[text()='двое суток']")
black_color = (By.XPATH, ".//div/label[@for='black']")
grey_color = (By.XPATH, ".//div/label[@for='grey']")
comment = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
order_button = (By.XPATH, ".//div[button='Назад']/button[text()='Заказать']")
yes_button = (By.XPATH, ".//button[text()='Да']")
order_confirmation = (By.XPATH, ".//div[div[text()='Заказ оформлен']]")
cookie_consent_button = (By.XPATH, ".//button[text()='да все привыкли']")
