def get_integer(prompt) :
    res = int(input(prompt))
    return res

def exchange(ex) :
    k500 = ex // 500
    ex %= 500

    k100 = ex // 100
    ex %= 100

    k50 = ex // 50
    ex %= 50

    k10 = ex // 10
    ex %= 10

    print('500원 동전의 개수:', k500)
    print('100원 동전의 개수:', k100)
    print('50원 동전의 개수:', k50)
    print('10원 동전의 개수:', k10)

k1 = int(get_integer('동전으로 교환하고자 하는 금액은? :'))
exchange(k1)
