class IncorrectVinNumber(Exception):
    '''Исключение для обработки корректности Vin номера'''
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    '''Исключение для обработки корректности номера'''

    def __init__(self, message):
        self.message = message


class Car:

    def __init__(self, model, vin, numbers):

        try:
            self.__is_valid_numbers(numbers)
            self.model = model
            self.__is_valid_vin(vin)
        except (IncorrectVinNumber, IncorrectCarNumbers) as exc:
            raise exc

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип данных для vin номера')

        # Проверяем длину номера
        if vin_number > 9999999 or vin_number < 1000000:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        return True

    def __is_valid_numbers(self, numbers):

        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        # Проверяем длину номера
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

try:
    four = Car('Model4', 2020202, 123)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{four.model} успешно создан')


try:
    five = Car('Model5', '2020202', 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{five.model} успешно создан')
