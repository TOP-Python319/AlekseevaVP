##############################
1. Если мы хотим заставить пользователя ввести целое число и при этом чтобы оно сохранилось в переменную b, какой из предложенных команд нам нужно воспользоваться?
______________________________
[] b = input()
[+] b = float(input())
[] b = int(input())
[] b = map(int, input().split())
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
2. Как называется параметр в функции print, который отвечает за разделяющие символы?
______________________________
[] math
[] key
[+] sep
[] end
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
3. У нас есть переменная s, в которой хранится строка "Messi". Как правильно получить символ "e"?
______________________________
[] s(1)
[+] s[1]
[] s[0]
[] s{0}
[] s(0)
[] s{1}
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
4. Строка — это:
______________________________
[+] неизменяемый тип данных
[] изменяемый тип данных
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
5. Какой метод позволяет удалить все элементы из списка?
______________________________
[] delete
[] drop
[] clear
[] clean
[+] remove
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
6. Какой список сформируется, если выполнить команду list(range(4))?
______________________________
[] [1, 2, 3, 4]
[] [1, 2, 3]
[+] [0, 1, 2, 3]
[] [0, 1, 2, 3, 4]
[] [1, 2, 3, 4, 5]
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
7. Что выведет следующий код?
def square(x):
    print(x**2)
a = square(6)
print(a)
______________________________
[] 36, а потом случится ошибка
[+] 36, а потом None
[] None
[] будет ошибка
[] 36
[] None, а потом 36
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
8. Какие числа будут выведены на экран в ходе выполнения следующего кода?
def example():
    print(1)
    return 2
    print(3)
example()
______________________________
[] 1, 3
[] 1, 2, 3
[+] 1
[] Будет ошибка
[] 2
[] 1, 2
[] 3
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
9. Для добавления глобальной переменной в локальную область видимости с возможностью изменения используется ключевое слово:
______________________________
[] globals
[] local
[+] global
[] locals
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
10. Сколько раз можно вызывать функцию после её создания?
______________________________
[] Только один раз, без каких-либо исключений
[] Не более 5 раз для каждой функции
[] Ниразу, как говорится "Не для тебя моя роза цвела!"
[+] Сколько угодно раз
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
11. В какой последовательности должны идти определение функции и главная программа?
______________________________
[] Разницы нет, т.к. код будет работать в любом случае
[+] Сначала определение функций, а после главная программа
[] Сначала главная программа, а потом определение
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
12. Что появится на экране после выполнения следующей программы?
a = 4
print(a, 'a')
______________________________
[] a a
[+] 4 a
[] a 4
[] 4 4
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
13. Выберите верное утверждение:
______________________________
[+] Имя переменной может начинаться с символа подчёркивания (_)
[] Имя переменной может начинаться с цифры
[] Имя переменной может оканчиваться цифрой
[] Имя переменной может совпадать с ключевым (зарезервированным) словом



##############################
14. Какую последовательность чисел даст вам вызов функции range(8)?
______________________________
[] пустая последовательность
[] 1, 2, 3, 4, 5, 6, 7, 8
[+] 0, 1, 2, 3, 4, 5, 6, 7
[] 0, 1, 2, 3, 4, 5, 6, 7, 8
[] 1, 2, 3, 4, 5, 6, 7
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
15. Какую последовательность чисел даст вам вызов функции range(3, 11, 2)?
______________________________
[+] 3, 5, 7, 9
[] пустая последовательность
[] 3, 4, 5, 6, 7, 8, 9, 10, 11
[] 3, 5, 7, 9, 11
[] 3, 4, 5, 6, 7, 8, 9, 10
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
16. Сколько итераций сделает цикл?
for _ in range(1, 6):
   print('Python rocks!')
______________________________
[] 1
[] 4
[+] 5
[] 6
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
17. Когда цикл while проверяет свое условие: до или после того, как он выполнит итерацию?
______________________________
[+] до
[] после
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
18. Что покажет приведенный ниже фрагмент кода?
s = 'abcdefg'
print(s[2:5])
______________________________
[] abc
[] bcd
[+] cde
[] def
[] efg
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
19. Какой индекс у числа 17 в списке numbers?
numbers = [1, 100, 7, 20, 17, 37, 22]
______________________________
[] 3
[] 6
[+] 4
[] 5
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
20. Может ли список в Python содержать значения разных типов данных?
______________________________
[] нет
[+] да
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
21. Какой из приведенных методов добавляет значение в конец существующего списка?
______________________________
[+] append()
[] add()
[] increase()
[] extend()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
22. Отдельная функционально независимая часть программы, решающая определенную задачу, называется:
______________________________
[] параметром
[] блоком
[+] функцией
[] выражением
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
23. Какое из имён недопустимо для названия функции в Python?
______________________________
[+] _myfunction
[] print_numbers
[] draw_triangle
[] 1check_condition
[] is_valid
[] find_sum_1
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
24. Для чего используется оператор pass?
______________________________
[] для возврата значения из функции
[] для прерывания функции
[+] для создания заглушки
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
25. Закрытие файлового объекта после его использования лучше осуществить с помощью:
______________________________
[] использования менеджера контекста with
[] использования блока try/finally
[] без разницы
[] вызова метода close()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
26. Текстовый файл с именем dog_breeds.txt находится в той же папке, где и исполняемая программа. Каким способом можно открыть данный файл для чтения в текстовом режиме?
______________________________
[] open('dog_breeds.txt', 'w')
[] open('dog_breeds.txt', 'r')
[] open('dog_breeds.txt', 'wb')
[] open('dog_breeds.txt', 'rb')
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
27. С помощью какого файлового метода можно прочитать полностью содержимое текстового файла в виде строки?
______________________________
[] read()
[] readline()
[] read_file_to_str()
[] readlines()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
28. Какой тип данных возвращает файловый метод readlines()?
______________________________
[] список целых чисел
[] список строк
[] кортеж строк
[] строку
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
29. Верно ли, что в Python функции всегда возвращают значения?
______________________________
[] нет
[] да
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
30. Какой из следующих заголовков функции func() правильный?
______________________________
[] def func(a=2, b=3, c):
[] def func(a, b, c=3, d):
[] def func(a, b=2, c=3):
[] def func(a=2, b, c=3):
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
31. Анонимная функция – это функция:
______________________________
[] у которой есть тело, но нет имени
[] у которой нет ни тела, ни имени
[] у которой есть тело и есть имя
[] у которой нет тела, но есть имя
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
32. Выберите правильный вариант написания лямбда-выражения для функции f(x)=2x+1.
______________________________
[] f = lambda f(x): 2*x + 1
[] f = lambda x: 2*x + 1
[] ​lambda f(x): 2*x + 1
[] f = lambda x: return 2*x + 1
[] нет правильного ответа
[] f = lambda (x): 2*x + 1
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
33. Встроенная функция map() возвращает:
______________________________
[] словарь
[] итератор
[] список
[] строку
[] множество
[] кортеж
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
34. Какая функция позволяет получить список элементов, преобразованных в соответствии с заданной функцией?
______________________________
[] map()
[] filter()
[] reduce()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
35. Какое количество аргументов может принять следующая функция?
______________________________
[] def func(x, y, *args):
[] сколько угодно
[] три
[] два и больше
[] один и больше
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
36. Аргументы функции, которые передаются без указания имен, называются:
______________________________
[] позиционными
[] особенными
[] именованными
[] обычными
[] необязательными
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
37. Где при вызове функции нужно указывать именованные аргументы?
______________________________
[] перед первым позиционным
[] после позиционных аргументов
[] в любом месте перечня аргументов
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
38. Параметры функции, имеющие значения по умолчанию, называются:
______________________________
[] позиционными
[] обычными
[] особенными
[] именованными
[] необязательными
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
39. Какая функция возвращает случайное целое число внутри заданного диапазона значений?
______________________________
[] random()
[] randint()
[] random_integer()
[] uniform()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
40. Какая функция возвращает случайное число с плавающей точкой в диапазоне [0.0;1.0)?
______________________________
[] random_integer()
[] random()
[] randrange()
[] randint()
[] uniform()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
41. Словари (тип данных dict) являются:
______________________________
[] неизменяемыми
[] изменяемыми
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
42. Какая часть элемента словаря ключ: значение должна быть неизменяемой?
______________________________
[] значение
[] ключ
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
43. Для проверки наличия ключа в словаре используется оператор:
______________________________
[] in
[] &
[] ^
[] ?
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
44. Какой словарный метод возвращает все ключи словаря и связанные с ними значения в виде последовательности кортежей?
______________________________
[] keys_values()
[] get()
[] values()
[] keys()
[] items()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
45. Какой метод возвращает последний добавленный в словарь элемент (удаляя его из словаря) в виде кортежа (ключ, значение)?
______________________________
[] random()
[] pop()
[] popitem()
[] rand_pop()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
46. Какой метод возвращает значение, связанное с заданным ключом, и удаляет из словаря пару ключ / значение?
______________________________
[] random()
[] popitem()
[] randpop()
[] pop()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
47. Какой метод возвращает значение, связанное с заданным ключом? Если ключ не найден, то он возвращает значение по умолчанию.
______________________________
[] get()
[] key()
[] рор()
[] value()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
48. Позволяет ли множество хранить повторяющиеся элементы?
______________________________
[] нет
[] да
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
49. Какими являются элементы множества?
______________________________
[] упорядоченными
[] неупорядоченными
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
50. Может ли элементом множества быть список?
______________________________
[] да
[] нет
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
51. Может ли элементом множества быть множество?
______________________________
[] да
[] нет
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
52. Может ли элементом множества быть кортеж?
______________________________
[] нет
[] да
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
53. Как можно добавить значение нового элемента item в уже существующее множество myset?
______________________________
[] myset.update(item)
[] myset.insert(item)
[] myset.append(item)
[] myset.add(item)
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
54. Что произойдет, если в рекурсивной функции не будет условия выхода?
______________________________
[] RecursionError: maximum recursion
[] Бесконечный цикл
[] Ничего
[] Бесконечный вызов функции самой себя
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
55. Выберите верное утверждение:
______________________________
[] Рекурсивная функция при большом числе повторов оптимальна за счёт автоматизации вызова.
[] Рекурсивная функция при большом числе повторов неоптимальна из-за высокой нагрузки.
[] Рекурсивная функция - функция, которую можно вызвать бесчисленное количество раз.
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
56. Что такое декоратор в Python?
______________________________
[] Тип данных, используемая для хранения нескольких значений
[] Ключевое слово, используемое для определения переменных
[] Функция, которая принимает другую функцию в качестве аргумента и добавляет к ней некоторую функциональность
[] Тип цикла в Python
[] Разновидность моржа
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
57. Какова цель использования декоратора в Python?
______________________________
[] Преобразовать функцию в класс
[] Создать новую функцию из существующей
[] Чтобы удалить функцию из памяти
[] Чтобы изменить поведение функции без изменения ее исходного кода
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
58. В каком порядке декораторы применяются к функции в Python?
@timer
@logger
def say_hello():
   print("Hello")
______________________________
[] Произвольно, в зависимости от порядка выполнения
[] Снизу вверх
[] От самого верхнего к самому низу
[] Нет фиксированного порядка применения декораторов.
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
59. Как согласно правилам наименования необходимо называть параметр функции, предназначенный для получения произвольного количества именованных аргументов?
______________________________
[] **args
[] **arguments
[] **kwargs
[] *arguments
[] *args
[] *kwargs
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾



##############################
60. Какова цель функции wraps из модуля functools?
______________________________
[] Чтобы изменить поведение исходной функции
[] Чтобы создать новый функциональный объект
[+] Чтобы сохранить имя и docstring исходной функции при использовании в качестве декоратора
[] Чтобы замерить время выполнения функции
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾