import argparse

class POLI:
    def __init__(self,list):
        self.__list=list

    def process(self):
        lists=list(self.__list.split(','))
        num=len(lists)
        if lists[num-1]=='':
            del lists[num-1]
        self.__list=lists


    def check(self,number):
        try:
            float(number)
            return True
        except Exception:
            return False

    def get_list(self):
        return self.__list

    def nums(self,list):
        n_list=[]
        for x in list:
            n_list.append(float(x))
        return n_list

    def calculate(self,numbers):
        try:
            i=0
            result=0
            while i<len(numbers):
                result+=1/(numbers[i]*2)
                i+=1
            return result
        except Exception as err:
            print(err)
            exit()

def main ():
    parser = argparse.ArgumentParser(description='Strings')
    parser.add_argument('-p', action='store', dest='count', type=str)
    args = parser.parse_args()
    Object1=POLI(args.count)
    Object1.process()
    lists=Object1.get_list()
    for num in lists:
        flag=Object1.check(num)
        if not flag:
            print('Вы ввели неправильные данные')
            exit()
    nums=Object1.nums(lists)
    result=Object1.calculate(nums)
    print(result)

main()