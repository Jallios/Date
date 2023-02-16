import calendar
from tabulate import tabulate

base = {
   1:{
        "month":"Январь",
        "day": 172,
    },
    2: {
        "month":"Февраль",
        "day": 154,
        "dayL": 165,
    },
    3: {
        "month":"Март",
        "day": 172,
    },
    4: {
        "month":"Апрель",
        "day": 168,
    },
    5: {
        "month":"Май",
        "day": 172,
    },
    6: {
        "month":"Июнь",
        "day": 168,
    },
    7: {
        "month":"Июль",
        "day": 172,
    },
    8: {
        "month":"Август",
        "day": 172,
    },
    9: {
        "month":"Сентябрь",
        "day": 168,
    },
    10: {
        "month":"Октябрь",
        "day": 172,
    },
    11: {
        "month":"Ноябрь",
        "day": 168,
    },
    12: {
        "month":"Декабрь",
        "day": 172,
    }
}

year = int(input('Введите год: '))

result = 0

if calendar.isleap(year):
    for key in base:
        if key == 2:
            m = (base[key].get("month"))
            d = (base[key].get("dayL"))
            result += d
        else:
            m = (base[key].get("month"))
            d = (base[key].get("day"))
            result += d
        print(f"\n{tabulate([[m,d]], headers=['Месяц', 'Дней'])}")
    print(f"\nГод високосный.\nРезультат: {result}")
   
else:
    for key in base:
        m = (base[key].get("month"))
        d = (base[key].get("day"))
        result += d
        print(f"\n{tabulate([[m,d]], headers=['Месяц', 'Дней'])}")
    print(f"\nГод не високосный.\nРезультат: {result}")

       


