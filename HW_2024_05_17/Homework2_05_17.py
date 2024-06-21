# Разрешения в операционной системе  это права доступа, которые определяют, какие действия могут быть выполнены в рамках системы.
# Разрешения могут ограничивать использование определенного программного обеспечения, доступ к файлам и настройки системы безопасности.
# Создайте миксин, который имитирует управления правами доступами.

# Для этого создайте класс PermissionMixin, который будет иметь следующие методы:
# 	__init__(self): метод инициализации, который создает множество permissions для хранения разрешений. В него 
# 	мы будем сохранять действия, которые будут доступны пользователям, например Чтение, Запись, Выполнение и т.д.
 
# 	grant_permission(self, permission): метод для назначения разрешения.
# 	Добавляет переданное разрешение в множество permissions
 
# 	revoke_permission(self, permission): метод для отмены разрешения.
# 	Удаляет переданное разрешение из множества permissions
 
# 	has_permission(self, permission): метод для проверки наличия разрешения.
# 	Возвращает True, если переданное разрешение присутствует в множестве permissions, и False в противном случае.

# Создайте класс User, который будет наследоваться от PermissionMixin и иметь следующие атрибуты:
# 	name: имя пользователя.
# 	email: email пользователя.


class PermissionMixin:
    def __init__(self):
        self.permissions = set()

    def grant_permission(self, permission):
        self.permissions.add(permission)

    def revoke_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)

    def has_permission(self, permission):
        return permission in self.permissions

class User(PermissionMixin):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email