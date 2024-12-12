

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызываю внутреннюю функцию внутри внешней функции
    inner_function()


# Вызываею внешнюю функцию
test_function()

# Пробую вызвать внутреннюю функцию снаружи
inner_function()

