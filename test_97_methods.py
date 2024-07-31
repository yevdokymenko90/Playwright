'''
import pytest
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext: # type: ignore
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com",
        extra_http_headers={'Content-Type': 'application/json'},
    )
    yield api_context
    api_context.dispose()

def test_create_user(api_context: APIRequestContext):
    response = api_context.post(
        "users/add",
        data={
            "firstName": "Damien",
            "lastName": "Smith",
            "age": 27
        }
    )
    user_data = response.json()

    # Check if the id field exists
    assert "id" in user_data, "The 'id' field is missing in the response"
    
    # Check if the firstName and lastName are as expected
    assert user_data["firstName"] == "Damien", f"Expected firstName 'Damien' but got {user_data['firstName']}"
    assert user_data["lastName"] == "Smith", f"Expected lastName 'Smith' but got {user_data['lastName']}"

def test_update_user(api_context: APIRequestContext):
    response = api_context.put(
        "users/1",
        data={
            "lastName": "Smith",
            "age": 20,
        }
    )
    user_data = response.json()

    assert user_data["lastName"] == "Smith", f"Expected lastName 'Smith' but got {user_data['lastName']}"
    assert user_data["age"] == 20, f"Expected age '20' but got {user_data['age']}"

def test_remove_user(api_context: APIRequestContext):
    response = api_context.delete("users/1")

    user_data = response.json()

    assert user_data.get("isDeleted") is True, "Expected 'isDeleted' to be True but got {user_data.get('isDeleted')}"

def run_test():
    with sync_playwright() as playwright: # type: ignore
        test_create_user(playwright.request.new_context(base_url="https://dummyjson.com"))
        test_update_user(playwright.request.new_context(base_url="https://dummyjson.com"))
        test_remove_user(playwright.request.new_context(base_url="https://dummyjson.com"))

if __name__ == "__main__":
    run_test()
'''

import pytest
from playwright.sync_api import Playwright, APIRequestContext

# Фикстура для создания и удаления контекста API
@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext: # type: ignore
    # Создаем новый контекст API с базовым URL и дополнительными HTTP заголовками
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com",
        extra_http_headers={'Content-Type': 'application/json'},
    )
    yield api_context  # Возвращаем контекст API для использования в тестах
    api_context.dispose()  # Закрываем контекст API после завершения тестов

# Тест для создания нового пользователя
def test_create_user(api_context: APIRequestContext):
    # Отправляем POST-запрос для создания нового пользователя
    response = api_context.post(
        "users/add",
        data={
            "firstName": "Damien",  # Имя пользователя
            "lastName": "Smith",    # Фамилия пользователя
            "age": 27               # Возраст пользователя
        }
    )
    # Извлекаем данные пользователя из ответа в формате JSON
    user_data = response.json()

    # Проверяем, что поле 'id' существует в ответе
    assert "id" in user_data, "The 'id' field is missing in the response"
    
    # Проверяем, что имя и фамилия соответствуют ожидаемым значениям
    assert user_data["firstName"] == "Damien", f"Expected firstName 'Damien' but got {user_data['firstName']}"
    assert user_data["lastName"] == "Smith", f"Expected lastName 'Smith' but got {user_data['lastName']}"

# Тест для обновления данных пользователя
def test_update_user(api_context: APIRequestContext):
    # Отправляем PUT-запрос для обновления данных пользователя
    response = api_context.put(
        "users/1",
        data={
            "lastName": "Smith",  # Новая фамилия пользователя
            "age": 20,            # Новый возраст пользователя
        }
    )
    # Извлекаем обновленные данные пользователя из ответа в формате JSON
    user_data = response.json()

    # Проверяем, что фамилия и возраст соответствуют ожидаемым значениям
    assert user_data["lastName"] == "Smith", f"Expected lastName 'Smith' but got {user_data['lastName']}"
    assert user_data["age"] == 20, f"Expected age '20' but got {user_data['age']}"

# Тест для удаления пользователя
def test_remove_user(api_context: APIRequestContext):
    # Отправляем DELETE-запрос для удаления пользователя
    response = api_context.delete("users/1")

    # Извлекаем данные из ответа в формате JSON
    user_data = response.json()

    # Проверяем, что пользователь помечен как удаленный
    assert user_data.get("isDeleted") is True, "Expected 'isDeleted' to be True but got {user_data.get('isDeleted')}"

# Функция для запуска тестов вручную
def run_test():
    with sync_playwright() as playwright: # type: ignore
        # Создаем новый контекст API и запускаем тесты вручную
        test_create_user(playwright.request.new_context(base_url="https://dummyjson.com"))
        test_update_user(playwright.request.new_context(base_url="https://dummyjson.com"))
        test_remove_user(playwright.request.new_context(base_url="https://dummyjson.com"))

# Точка входа для выполнения скрипта напрямую
if __name__ == "__main__":
    run_test()
