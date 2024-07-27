def lavash(func):
    def wrapper():
        print('лаваш')
        func()
        print('лаваш')

    return wrapper

def nachinka(func):
    def wrapper():
        print('tomato\ncucumber\n1000 ostrovov\nfench fries')
        func()

    return wrapper



@lavash
@nachinka

def shaurma(meat='goviyadina'):
    print(meat)

shaurma()
