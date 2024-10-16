# Sprint_6

В проекте написаны автотесты для учебного сервиса «Яндекс.Самокат».

Описание структуры проекта: 
Папки:
1. allure_results - allure-отчёты по прогону тестов;
2. locators - хранятся файлы с локаторами для отдельных страниц; 
3. pages - хранятся файлы с page object для отдельных страниц;
4. tests - хранятся файлы с автотестами, в каждом файле тесты для отдельной страницы.

Файлы:
1. confest.py - файл, в котором хранятся фикстуры по проекту;
2. data.py - файл, в котором хранятся наборы тестовых данных;
3. requirements.txt - файл с внешними зависимостями.

Основа для написания автотестов: 
1. Selenium
2. WebDriver Firefox 
3. Pytest

Для запуска всех тестов проекта: 
pytest -v tests/