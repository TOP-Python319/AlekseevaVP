# Напишите суперкласс Publisher (издательство) и два подкласса BookPublisher (книжное издательство) и NewspaperPublisher (газетное издательство).

# Родительский класс Publisher имеет два атрибута name и location (название, расположение) и два метода:
# 	get_info(self) – предоставляет информацию о названии и расположении издательства;
# 	publish(self, message) – выводит информацию об издании, которое находится в печати.

# Подклассы BookPublisher и NewspaperPublisher используют метод super().__init__(name, location) суперкласса для вывода информации о своих названии и расположении, и кроме того, имеют собственные атрибуты:
# 	BookPublisher – num_authors (количество авторов).
# 	NewspaperPublisher– num_pages (количество страниц в газете).


# Пример использования:
# publisher = Publisher("АБВГД Пресс", "Москва")
# publisher.publish("Справочник писателя")

# book_publisher = BookPublisher("Важные Книги", "Самара", 52)
# book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

# newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
# newspaper_publisher.publish("Новая версия Midjourney будет платной")

# Вывод:
# Готовим "Справочник писателя" к публикации в АБВГД Пресс (Москва)
# Передаем рукопись 'Приключения Чебурашки', написанную автором В.И. Пупкин в издательство Важные Книги (Самара)
# Печатаем свежий номер со статьей "Новая версия Midjourney будет платной" на главной странице в издательстве Московские вести (Москва)


class Publisher():
    def __init__(self,name,location):
        self.name = name
        self.location = location

    def get_info(self):
        print( "Издательство под название" + self.name + "находится" + self.location  )


    def publish(self, message):
        print(message + " находится в печати!")

class BookPublisher(Publisher):
    def __init__(self, name, location, num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors

    def get_info(self):
        info = super().get_info()
        print( info + ",количество авторов: "+ self.num_authors )

class NewspaperPublisher(Publisher):
    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages

    def get_info(self):
        info = super().get_info()
        print( info + ",количество страниц: "+ self.num_pages)


publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")
