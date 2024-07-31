from playwright.sync_api import *

# Функция для обработки вызова API
def on_api_call(route: Route):
    # Выполняем оригинальный запрос и получаем ответ
    response = route.fetch()
    # Извлекаем данные пользователя из ответа в формате JSON
    user_data = response.json()

    # Изменяем данные пользователя
    user_data["lastName"] = "Smith"
    user_data["age"] = 20

    # Выполняем возврат измененных данных в ответе
    route.fulfill(
        response=response,
        json=user_data,
    )

# Тестовая функция для проверки API пользователя
def test_user_api(page: Page):
    # URL для доступа к API пользователей
    USERS_API_URL = "https://dummyjson.com/users/1"

    # Устанавливаем обработчик маршрута для заданного URL
    page.route(USERS_API_URL, on_api_call)

    # Переходим по URL и получаем ответ
    response = page.goto(USERS_API_URL)
    # Печатаем данные пользователя, полученные из ответа
    print("Got data:", response.json())
