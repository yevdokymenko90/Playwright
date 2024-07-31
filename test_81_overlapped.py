from playwright.sync_api import Page, expect


def test_overlapped(page: Page):
    # Переход на целевую страницу
    page.goto("http://uitestingplayground.com/overlapped")
    
    # Поиск элемента ввода по placeholder "Name"
    input = page.get_by_placeholder("Name")

    # Наведение мыши на область прокрутки (родительский элемент)
    div = input.locator("..")
    div.hover()

    # Прокрутка на 200 пикселей по горизонтали
    page.mouse.wheel(0, 200)

    # Небольшая задержка для завершения прокрутки
    page.wait_for_timeout(1000)

    # Проверка видимости элемента ввода
    input.wait_for(state="visible")

    # Ввод данных в элемент
    data = "python"
    input.fill(data)

    # Снятие скриншота области прокрутки
    div.screenshot(path="test-overlapped.jpg")

    # Проверка значения элемента ввода
    expect(input).to_have_value(data)
