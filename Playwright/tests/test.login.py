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

        # Проверка успешного входа
        assert "You logged into a secure area!" in page.text_content("div#flash")

        # Закрытие браузера
        browser.close()

if __name__ == "__main__":
    test_login()
    
    
    
'''
The active selection is a Python script that 
uses the Playwright library to automate browser actions for testing purposes. 
This script specifically tests the login functionality of a web application.

The script starts by importing the `sync_playwright` function 
from the `playwright.sync_api` module. 
This function provides a synchronous API to interact with the Playwright library.

The `test_login` function is defined to perform the login test. 
It uses the `sync_playwright` function 
as a context manager to ensure that resources are 
properly cleaned up when the test is done.

Inside the `test_login` function, 
a browser instance is launched using `p.chromium.launch(headless=False)`. 
The `headless=False` argument means the browser will be visible during the test. 
If you want the browser to run in the background, you can set `headless=True`.

A new page is opened in the browser using `browser.new_page()`. 
The script then navigates to the test website using 
`page.goto("https://the-internet.herokuapp.com/")`.

The script simulates a user clicking on the 
"Form Authentication" link to navigate to the login page, 
filling in the username and password fields, 
and clicking the submit button to log in.

After the login action, 
the script checks whether the login was successful by asserting that the text 
"You logged into a secure area!" is present in the page's text content.

Finally, the browser is closed using `browser.close()` 
to clean up resources.

The `if __name__ == "__main__":` 
block at the end of the script allows the `test_login` function 
to be run when the script is executed directly, 
but not when it's imported as a module. 
This is a common pattern in Python scripts that are 
intended to be used both as standalone scripts and as modules.



Активный выбор - это Python-скрипт, который использует библиотеку Playwright 
для автоматизации действий в браузере для тестирования. 
Этот скрипт конкретно тестирует функциональность входа в веб-приложение.

Скрипт начинается с импорта функции `sync_playwright` 
из модуля `playwright.sync_api`. 
Эта функция предоставляет синхронный API 
для взаимодействия с библиотекой Playwright.

Функция `test_login` определена для выполнения теста входа. 
Она использует функцию `sync_playwright` 
в качестве менеджера контекста, 
чтобы гарантировать правильное освобождение ресурсов после теста.

Внутри функции `test_login` запускается экземпляр браузера с помощью 
`p.chromium.launch(headless=False)`. 
Аргумент `headless=False` означает, 
что браузер будет видимым во время теста. 
Если вы хотите, чтобы браузер работал в фоновом режиме, 
вы можете установить `headless=True`.

В браузере открывается новая страница с помощью `browser.new_page()`. 
Затем скрипт переходит на тестовый сайт с помощью `page.goto("https://the-internet.herokuapp.com/")`.

Скрипт имитирует действия пользователя, 
кликая на ссылку "Form Authentication" для перехода на страницу входа, 
заполняя поля имени пользователя и пароля, 
и нажимая кнопку отправки для входа.

После действия входа скрипт проверяет, 
был ли вход успешным, утверждая, 
что текст "You logged into a secure area!" 
присутствует в текстовом содержимом страницы.

Наконец, браузер закрывается с помощью 
`browser.close()` 
для освобождения ресурсов.

Блок `if __name__ == "__main__":` 
в конце скрипта позволяет функции `test_login` запускаться при прямом выполнении скрипта, 
но не при его импорте в качестве модуля. 
Это общий шаблон в Python-скриптах, 
которые предназначены для использования как самостоятельные скрипты и как модули.
'''

