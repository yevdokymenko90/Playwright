from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        # Запуск браузера
        browser = p.chromium.launch(headless=False)  # Установите headless=True для запуска в фоновом режиме
        page = browser.new_page()

        # Открытие страницы
        page.goto("https://the-internet.herokuapp.com/")

        # Переход на страницу аутентификации
        page.click("text=Form Authentication")

        # Ввод данных пользователя
        page.fill("input#username", "tomsmith")
        page.fill("input#password", "SuperSecretPassword!")

        # Нажатие кнопки входа
        page.click("button[type='submit']")