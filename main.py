from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees, employees


print(f'Добрый день, сегодня: {date.today()}')

print(f"Статус:{get_employees('Oleg', employees)}")

print(f"Сотрудник: {calculate_salary('Ivan', 5000, 22)[0]} - зарплата: {calculate_salary('Ivan', 5000, 22)[1]}")

