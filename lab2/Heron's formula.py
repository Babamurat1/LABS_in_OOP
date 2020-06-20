# Класс для вычисления по формуле Герона
class Heron_formula:
    def __init__(self,number):  # Создаем и устанавливаем значение атрибута данных
        self.__number=number

    def calc(self):     # Метод вычисление
        if self.__number==0:
            print('Результат: ',self.__number)
            exit()
        elif self.__number<0:
            print('Неверное значение !')
            exit()
        elif self.__number>0:   # Если больше нулья
            result=None
            x=100         # Случайное число
            flag=True
            while flag:     # Цикл продолжится до тех пор пока не будет получен правильный результат
                result=0.5*(x+(self.__number/x))
                if result==x:   # Если одно и тоже
                    flag=False  # Цикл остановится
                x=result
            return result       # Возвращаем результат

# В функции main получаем данные, проверяем, создаем объект
# и вычисляем вызывав метод calc объекта c_object
def main ():
    flag=True
    while flag: # Цикл продолжится пока не будет введено число
        try:    # Обрабатываем исключение
            number=float(input('Введите число: '))
        except Exception as error:
            print(error)
        else:   # Если не было вызвано исключений
            flag=False
            c_object=Heron_formula(number)  # Создаем объект
            print('Результат: ',format(c_object.calc(),'.2f'))

main() # Выполняем функцию