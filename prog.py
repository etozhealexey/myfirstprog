def prog():
    a = int(input('Введите число '))
    work = True
    while work:
        if a < 10:
            print('Число меньше или равно 10')
            if input("Again or stop? ") == 'stop':
                work = False
            else:
                prog()


        elif a == 10:
            print('число  равно 10')
            if input("Again or stop? ") == 'stop':
                work = False
            else:
                prog()

        else:
            print("Введите число в диапозоне от 1 до 10")
            prog()


prog()
dasda
