# Домашнее задание: Классы и инициализация
#
# ЗАДАНИЕ 1: Класс Book (Книга)
#
# Создайте класс Book со следующими требованиями:
# 1) В __init__ принимайте параметры: title (название), author (автор), pages (количество страниц)
# 2) Сохраните эти параметры как атрибуты объекта через self
# 3) Создайте метод get_info(), который возвращает строку: "'{title}' автор {author}, {pages} стр."
# 4) Создайте метод is_long(), который возвращает True, если страниц > 300, иначе False
# 5) Создайте 3 объекта книг и выведите информацию о каждой.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def get_info(self):
        return f"Книга '{self.title}', Автор {self.author}, {self.pages} стр."

    def is_long(self):
        return True if self.pages > 300 else False

book1 = Book("Гарри потер", "Некая женщина", 470)
book2 = Book("Война и мир", "Лев Толстой", 1225)
book3 = Book("Богатый папа, бедный папа", "Роберт Кийосаки", 250)
# ЗАДАНИЕ 2: Класс BankAccount (Банковский счёт)
#
# Создайте класс BankAccount:
#
# 1) В __init__ принимайте: owner (владелец), balance (начальный баланс, по умолчанию 0)
# 2) Создайте метод deposit(amount) — пополнение счёта (увеличивает self.balance)
# 3) Создайте метод withdraw(amount) — снятие денег:
# 4) Если денег достаточно — уменьшает баланс и возвращает True
#    Если недостаточно — возвращает False и выводит "Недостаточно средств"
# 5) Создайте метод get_balance() — возвращает текущий баланс
# 6) Создайте счёт, пополните его, попробуйте снять деньги (достаточно и недостаточно), выведите баланс.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнение: {amount}. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снято: {amount}. Остаток: {self.balance}")
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance

my_account = BankAccount("Вадим", 1000)
my_account.deposit(500)
my_account.withdraw(1000)
my_account.withdraw(1000)
print(f"Текущий баланс: {my_account.get_balance()}")
