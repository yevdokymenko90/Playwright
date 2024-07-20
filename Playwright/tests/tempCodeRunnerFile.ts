import pytest
from playwright.sync_api import sync_playwright

# Пример данных API ответа для успешного получения
expected_response = {
    "id": 1,
    "announcement": "Welcome to project X",
    "completed_on": 1389968184,
    "default_role_id": 3,
    "default_role": "Tester",
    "is_completed": False,
    "name": "Project X",
    "show_announcement": True,
    "suite_mode": 1,
    "url": "https://instance.testrail.io/index.php?/projects/overview/1",
    "users": [
        {
            "id": 3,
            "global_role_id": None,
            "global_role": None,
            "project_role_id": None,
            "project_role": None
        }
    ],
    "groups": []
}

@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

def test_get_project_success(playwright_context):
    response = playwright_context.request.get("https://instance.testrail.io/index.php?/api/v2/get_project/1")
    response_data = response.json()

    assert response.status == 200
    assert response_data == expected_response

def test_get_project_invalid(playwright_context):
    response = playwright_context.request.get("https://instance.testrail.io/index.php?/api/v2/get_project/9999")

    assert response.status == 400
    assert response.json()['error'] == 'Invalid or unknown project'

def test_get_project_no_access(playwright_context):
    response = playwright_context.request.get("https://instance.testrail.io/index.php?/api/v2/get_project/2")

    assert response.status == 403
    assert response.json()['error'] == 'No access to the project'

def test_get_project_rate_limit(playwright_context):
    for _ in range(100):  # Симулируем быстрые запросы для срабатывания ограничения по частоте запросов
        response = playwright_context.request.get("https://instance.testrail.io/index.php?/api/v2/get_project/1")

    assert response.status == 429
    assert response.json()['error'] == 'Too many requests'

if __name__ == "__main__":
    pytest.main(["-v", "test_api.py"])
