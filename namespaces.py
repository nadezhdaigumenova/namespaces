
x = 'Я в области видимости функции test_function'

def test_function():

    def inner_function():
        print(x)

    inner_function()

test_function()













