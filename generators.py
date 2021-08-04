import time


def fibo_gen_min(max_counter):
    a, b = 0, 1
    while a <= max_counter:
        yield a
        a, b = b, a+b


def fibo_gen(max_number):
    n1 = 0
    n2 = 1
    counter = 0
    aux = 0

    while True and aux < max_number:
        aux = n1 + n2
        if counter == 0:
            yield n1

        n1, n2 = n2, aux
        counter += 1
        yield n2


if __name__ == '__main__':
    fibonacci = fibo_gen_min(2)
    for element in fibonacci:
        print(element)
        time.sleep(1)
    for element in fibonacci:
        print(element)
        time.sleep(1)
