# Создать систему управления библиотекой.
# Библиотека состоит из отделов
# (например, отдел художественной литературы, отдел научной литературы и т.д.).
# В каждом отделе есть свой набор книг.
# Книги могут перемещаться между отделами.
# Читатели могут брать книги в отделе и возвращать их обратно.


# Добавить пользовательский класс ошибок.
# Например на остутствие книги в отделе.

# Проверять существует ли такая книга вообще в библиотеке

# Создать класс читателя.
# В нём может пригодиться использование метода is_available из класса Book


from dataclasses import dataclass


@dataclass
class Book:
    name: str
    author: str
    pages: int
    year: int
    is_available: bool = True

    def take(self):
        self.is_available = False

    def return_back(self):
        self.is_available = True


class Library:
    class Department:
        def __init__(self, name: str):
            self.name = name
            self.books = []

        def __str__(self):
            result = f'Отдел {self.name} имеет книги:'
            for book in self.books:
                result += f'\n{book.name} by {book.author}, available {"Yes" if book.is_available else "No"}'
            return result

        def add_book(self, book: Book):
            self.books.append(book)

        def del_book(self, book: Book):
            self.books.remove(book)

    def __init__(self, name: str):
        self.name = name
        self.departments = {}

    def __str__(self):
        result = f'{self.name} имеет отделы:\n'
        for department in self.departments:
            result += f'\t{department}:\n'
            for book in self.departments[department].books:
                result += f'\t\t{book.name} автора {book.author},{" " if book.is_available else " не "}доступна\n'
        return result

    def add_department(self, name: str):
        self.departments[name] = self.__class__.Department(name)

    def move_book(self,
                  book: Book,
                  department_from: Department,
                  department_to: Department):
        department_from.del_book(book)
        department_to.add_book(book)


library = Library('Ленинская библиотека')
FICTION_BOOKS = 'Художественная литература'
SCIENCE_BOOKS = 'Научная литература'
library.add_department(FICTION_BOOKS)
library.add_department(SCIENCE_BOOKS)

brave_new_world = Book('Brave New World', 'Aldous Huxley', 311, 1932)
anna_karenina = Book('Anna Karenina', 'Leo Tolstoy', 864, 1877)
fight_club = Book('Fight Club', 'Chuck Palahniuk', 366, 1996)
universe_in_a_nutshell = Book('Universe in a nutshell', 'Stephen Hawking', 480, 1976)

library.departments[FICTION_BOOKS].add_book(brave_new_world)
library.departments[FICTION_BOOKS].add_book(anna_karenina)
library.departments[FICTION_BOOKS].add_book(fight_club)
library.departments[FICTION_BOOKS].add_book(universe_in_a_nutshell)

library.move_book(universe_in_a_nutshell, library.departments[FICTION_BOOKS], library.departments[SCIENCE_BOOKS])

anna_karenina.take()

print(library)


# Комментарий преподавателя:

# 1. Код читабельный и структурированный
# 2. Использованы dataclass для определения класса Book
# 3. Реализована возможность перемещения книг между отделами
# 4. Реализована возможность взятия книги читателем и возврата ее обратно

# Что можно улучшить:
# 1. Добавить класс Читатель, который будет хранить информацию о взятых книгах и возможность их возврата
# 2. Добавить пользовательский класс ошибок для обработки ситуаций, когда книга отсутствует в отделе или ее нет в библиотеке вообще
# 3. Реализовать проверку на существование книги в библиотеке при ее перемещении между отделами
# 4. Добавить возможность добавления книг в библиотеку через консоль или файл
# 5. Добавить возможность удаления книг из библиотеки
# 6. Добавить возможность поиска книг по названию или автору
# 7. Добавить возможность сортировки книг по годам издания, количеству страниц или автору
# 8. Добавить возможность вывода информации о конкретной книге по ее названию или автору.