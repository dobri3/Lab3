def fibo_factorial_validation(n:int)-> tuple [bool, str]:
    """
    валидация для Фибоначчи и факториала
    
    :param n: число для проверки
    :return: tuple [bool, str] - результат проерки и сообщение об ошибкее
    """
    
    try:
        int(n)
        if int(n)<0:
             return False, f"Элемент {n} должен быть неотрицательным"
    except ValueError as e:
            return False, f"Элемент '{n}' не является целым числом"
    return True, ""