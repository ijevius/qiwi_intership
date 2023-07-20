import sys
import xml.etree.ElementTree as ET

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--code", help="Код валюты в формате ISO 4217")
parser.add_argument("--date", help="Дата в формате YYYY-MM-DD")

args = parser.parse_args()
args_dict = vars(args)
print(f"Got: {args_dict}")

#переводим дату из yyyy-mm-dd в dd/mm/yyyy
def transform_date(original_date):
    parsed_date = original_date.split("-")[::-1]
    date_for_cb = "/".join(parsed_date)
    # print(date_for_cb)
    return date_for_cb

'''
Здесь отправляем запрос к ЦБ. 
Требуется: дата в уже правильном формате dd/mm/yyyy
'''
def get_xml_currency(date):
    api_link = "https://www.cbr.ru/scripts/XML_daily.asp?date_req="
    req = requests.get(api_link + date)
    if not req.status_code == 200:
        print("!!! API ВЕРНУЛО КОД: ", req.status_code)
    currency_response = req.text

    return currency_response

'''
Функция парсит XML от ЦБ и выбирает нужные значения по коду валюты
'''
def get_rate_by_date(currency_code, date):
    right_date = transform_date(date)
    currency_response = get_xml_currency(right_date)

    root = ET.fromstring(currency_response)
    found = 0
    for child in root:
        #тут хранится CharCode -- по которому смотрим нужную валюту
        currency_name = child.getchildren()[1].text
        if currency_name == currency_code:
            found = 1
            nominal = child.getchildren()[2].text #номинал -- сколько единиц той валюты
            rus_currency_name = child.getchildren()[3].text #название по-русски
            value = child.getchildren()[4].text #рублей
            return (nominal, currency_name, rus_currency_name, value.rstrip('0'))
            #summary = f"{nominal} {currency_name} ({rus_currency_name}): {value.rstrip('0')}"
            #print(summary)

    if found == 0:
        print("Такой валюты нет в списке на заданную дату")
        sys.exit(-1)


if __name__ == "__main__":
    result = get_rate_by_date(args_dict["code"], args_dict["date"])
    s = f"{result[0]} {result[1]} ({result[2]}): {result[3]}"
    print(s)

