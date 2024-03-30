from selenium.webdriver.common.by import By

samokat = (By.XPATH, ".//a[descendant::img[@alt='Scooter']]")
yandex = (By.XPATH, ".//a[descendant::img[@alt='Yandex']]")
order_top = (
    By.XPATH, ".//div[button='Статус заказа']/button[text()='Заказать']")
