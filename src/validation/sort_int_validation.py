def sort_int_validation(a: list) -> tuple [bool, str] :
    """
    валидация списка, состоящего из целых чисел

    :param a: список, пришедший на вход от пользователя
    :return: tuple [bool, str] - результат проерки и сообщение об ошибке
    """
    for i in a:
        try:
            int(i)
        except ValueError:
            return False, f"Элемент '{i}' не является целым числом"
    return True, ""
