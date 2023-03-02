def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    :param collection: Словарь для поиска значения по ключу
    :param key: Ключ для поиска в словаре
    :param default: Слово, которое вернётся, если значение не найдено
    :return:
    """
    # Если словарь пустой или ключа нет - возврат default
    if not collection or key not in collection:
        return default
    #  В противном случае, если ключ есть - вернуть значение
    elif key in collection:
        return collection.get(key)
    # Заглушка - не удалось предусмотреть все варианты
    # если мы здесь - что-то пошло не так.
    # Конструкция написана в учебных целях.
    # Результат - покрытие только 83% :)
    else:
        print("Exception in get_val function of dicts.py module - ATTENTION!!!")
