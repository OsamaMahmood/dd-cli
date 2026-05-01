from enum import Enum


class UsersListOItem(str, Enum):
    DATE_JOINED = "date_joined"
    EMAIL = "email"
    FIRST_NAME = "first_name"
    IS_ACTIVE = "is_active"
    IS_SUPERUSER = "is_superuser"
    LAST_LOGIN = "last_login"
    LAST_NAME = "last_name"
    USERNAME = "username"
    VALUE_0 = "-date_joined"
    VALUE_1 = "-email"
    VALUE_2 = "-first_name"
    VALUE_3 = "-is_active"
    VALUE_4 = "-is_superuser"
    VALUE_5 = "-last_login"
    VALUE_6 = "-last_name"
    VALUE_7 = "-username"

    def __str__(self) -> str:
        return str(self.value)
