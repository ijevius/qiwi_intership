Утилита для получения курса валют с сайта ЦБ РФ по определенной дате.


ВВОД: код валюты и дату (yyyy-mm-dd). Для API ЦБ нужно: dd/mm/yyyy
ВЫВОД: 1 USD (Доллар): 32


Отправляем http-get и получаем XML
парсим xml -- внимание, дока говорит, что это дверь для уязвимости.

какие тесты нужны?
-- пара позитивных на прошедшие даты, что программа вернула правильное число
-- дата из будущего -- сложно, ЦБ на какое-то время дает котировки. Отказываемся

Не доделал:
-- запуск  тестов
-- правильную обработку если именнованые аргументы ввели с ошибкой (напр. cod, data)

