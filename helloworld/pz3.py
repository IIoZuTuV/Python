from helloworld.pz2 import *


def newParser():
    functions = {
        'hello': hello,
        'shout_on_me': shout_on_me,
        'addCalc': addCalc
    }
    flag = True
    while True:
        stringWithFunction = input('Введите название функции:')
        for x in functions.keys():
            if x == stringWithFunction:
                flag = False
        if not flag:
            functions[stringWithFunction]()
        else:
            print('Данной функции в словаре нет!')



if __name__ == '__main__':
    newParser()
