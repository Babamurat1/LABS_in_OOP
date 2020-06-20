import  urllib.request              # Импортируем модуль request из библиотеки urllib
import  matplotlib.pyplot as plt    # Импортируем модуль pyplot из библиотеки matplotlib как plt


class SMA:  # Класс SMA
    def __init__(self,url): # Определьяем атрибуты данных
        self.__price=[] # Цена
        self.__year=[]  # Время
        self.__url=url  # Адрес
        self.__sma_price=[] # SMA цена

    def download(self): # Метод загрузки данных
        file = open('finances.txt', 'w', encoding='utf-8')
        f = urllib.request.urlopen(self.__url)
        s = f.read()
        file.write(str(s))
        file.close()

    def get_year_price(self):   # Метод обработки загруженных данных
        file = open('finances.txt', 'r', encoding='utf-8')
        h = file.readline()
        file.close()
        lsit = h.split('USD/RUR')
        del lsit[0]
        value = lsit[0]
        del lsit
        value = value.split('editsection')
        value = value[0]
        j = value.split(' ')

        del j[57]
        del j[0]
        year = []
        price = []
        num = len(j)
        for x in range(0, num - 1, 2):
            n = j[x]
            year.append(n[:4])

        for x in range(1, num, 2):
            n = j[x]
            n = n[:4]
            price.append(n.rstrip(','))

        real_price = []
        for x in price:
            if ',' in x:
                n = x.find(',')
                real_price.append(x[:n])
            else:
                real_price.append(x)
        Price = []
        for x in real_price:
            Price.append(float(x))
        self.__year=year    # Получаем Год
        self.__price=Price  # Получаем цены

    def calculate(self,value):  # Метод вычисления
        length=len(self.__price)
        i=0
        while i<length:
            calc=0
            while i<value:
                self.__sma_price.append(self.__price[i])
                i+=1

            for y in range(value):
                calc+=self.__price[i-y]
            self.__sma_price.append(calc/value)
            i+=1
        time_list=list(range(0,length))
        return time_list

    def build(self,time_list):      # Метод Графика
        plt.figure(figsize=(15,7))  # Установка ширины и высоты графика
        plt.xlabel("Промежуток времени", fontsize='16', weight='bold')
        plt.title('Курс рубля к 1USD ', fontsize='16', weight='bold')
        plt.xticks(time_list, self.__year, fontsize=6, weight='bold')
        plt.grid()  # Включаем сетку

        plt.plot(time_list, self.__sma_price, color='red', linestyle='solid', \
             label='SMA', marker='o')   # Строим SMA график
        plt.plot(time_list, self.__price, color='blue', linestyle='solid', \
                 label='Стандартные значения', marker='>')  # Строим обычный график
        plt.legend(loc='upper right')

        plt.show()  # Показываем график
def main ():
    url = r"""https://ruxpert.ru/%D0%A1%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0:%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D0%BA%D1%83%D1%80%D1%81%D0%B0_%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0_%D0%BA_%D1%80%D1%83%D0%B1%D0%BB%D1%8E"""
    Object=SMA(url) # Создаем обьект
    Object.download()   # Загружаем данные
    Object.get_year_price() # Обрабатываем данные
    F=True
    while F:    # Обработаем исключенме
        try:
            value=int(input('Введите количество итераций (1-27 ): '))
            time_list = Object.calculate(value)
        except Exception as err:
            print(err)
        else:   # Если не было исклчений
            Object.build(time_list=time_list)
            F=False
main()  # Выполняем программу