def sort_float_validation(a: list) -> tuple [bool, str] :
    """
    валидация списка, состоящего из чисел с точкой

    :param a: список, пришедший на вход от пользователя
    :return: tuple [bool, str] - результат проерки и сообщение об ошибке
    """
    try:
        wrong_input = []
        for i in a:
            if  not(float(i)>=0 and float(i)<1):
                wrong_input.append(i)
        if wrong_input:
            return False, f"Не выполнено условия '0<=x<1' для {wrong_input}"
        return True, ""
    except ValueError:
            return False, "Не все элементы списка являются числами"
