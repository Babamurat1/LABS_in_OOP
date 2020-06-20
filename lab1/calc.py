# Класс калкулятора
class Calc:
    def __init__(self,operand1,operand2,operation):
        self.__operand1=operand1    # Получаем и устанавливаем атрибуты данных
        self.__operand2=operand2
        self.__operation=operation

    def calc(self):     # Метод вычисление в зависимости от оператора

        if self.__operation=='+':
            return self.__operand1+self.__operand2
        elif self.__operation=='-':
            return self.__operand1-self.__operand2
        elif self.__operation=='*':
            return self.__operand1*self.__operand2
        elif self.__operation=='/':
            return self.__operand1/self.__operand2
        elif self.__operation=='%':
            return self.__operand1%self.__operand2

    def set_operand1(self,operand1):    # Метод установки значения операнда1
        self.__operand1=operand1
    def set_operand2(self,operand2):    # Метод установки значения операнда2
        self.__operand2=operand2
    def set_operation(self,operation):  #   Метод установки значения оператора
        self.__operation=operation

    def check_operation(self,operation):    # Метод прверки на правильность оператора
        while operation!='+' and operation!='-'and operation!='*'\
                and operation!='/' and operation!='%':
            operation=input('Введите заново операцию(+ - * / %): ')
        self.__operation=operation

    def __str__(self):  # Метод проверки текущего значения операндов и оператора
        return  'Операнд1: '+str(self.__operand1)+'\nОперанд2: '\
                +str(self.__operand2)+'\nОператор: '+self.__operation


# В функции main в основном взаимодействуем с пользователем
# и обрабатываем исключение
def main ():
    answer='д'
    while answer=='д' or answer=='Д':   # Цикл чтобы программа не завершился без разрешения пользователья
        try:                            # Обрабатываем исключение
            operand1=float(input('Введите операнд1: '))
            operand2=float(input('Введите операнд2: '))
            operation=input('Выберите оперцию (+ - * / %): ')
            calc_object=Calc(operand1,operand2,operation)   # Создаем объект на основе класса Calc
            calc_object.check_operation(operation)      # Проверяем операцию на правильность
            result=calc_object.calc()       # Вычисляем вызовав метод вычисление
            print('Результат:',result)
            answer=input('Хоите продолжит операцию (д-да, все остальное-нет): ')
            while answer=='д' or answer=='Д':   # Чтобы продолжить вычисление над результатом
                calc_object.set_operand1(result)    # Устанавливаем результат как операнд1
                operand2=float(input('Введите операнд2: '))
                operation=input('Выберите операцию(+ - * / %): ')
                calc_object.check_operation(operation)  # Проверка оперции
                calc_object.set_operand2(operand2)      # Установка значении операнда2
                result=calc_object.calc()               # Вычисляем
                print('Результат:',result)
                answer=input('Вы хотите продолжить(д-да) ? ')
            if not answer=='д' or answer=='д':
                answer=input('Вы хотите заново начать(д-да) ?')
        except Exception as err:    # Если было вызвано исключение
            print(err)      # Печатать исключение

main()  # Выполнить программу