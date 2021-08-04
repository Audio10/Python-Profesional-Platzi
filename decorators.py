from datetime import datetime


def execution_time(func):
    def wraper(*args, **kwargs):
        initial_time = datetime.now()
        suma = func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")
        return suma
    
    return wraper


@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a: int, b :int) -> int:
    return a + b

# random_func()
print(suma(4,4))
