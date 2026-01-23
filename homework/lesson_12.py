# ЗАДАЧА 1: Система учета сотрудников

employees = {
    "Иван": {"возраст": 30, "отдел": "IT", "зарплата": 80000},
    "Мария": {"возраст": 25, "отдел": "HR", "зарплата": 60000},
    "Петр": {"возраст": 35, "отдел": "ITR", "зарплата": 90000},
}

# 1. Добавьте нового сотрудника "Анна"

employees["Анна"] = {"возраст": 28, "отдел": "IT", "зарплата": 75000}

# 2 Создайте список всех имен сотрудников

names = list(employees.keys())

# 3. Найдите среднюю зарплату всех сотрудников

total_salary = 0

for data in employees.values():
    total_salary += data["зарплата"]

average_salary = total_salary / len(employees)

# 4. Создайте множество всех отделов

departments = set()

for data in employees.values():
    departments.add(data["отдел"])

# 5. Удалите сотрудника "Петр" и сохраните его данные

petr_data = employees.pop("Петр")

# 6. Создайте словарь, где ключ - отдел, а значение - список имен сотрудников

department_employees = {}

for name, data in employees.items():
    department = data["отдел"]

    if department not in department_employees:
        department_employees[department] = []

    department_employees[department].append(name)
print(department_employees)
