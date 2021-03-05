# 2021.03.04, Uzd 4:
# Izveidot dekoratoru, kas skaita cik reizes funkcija tika izsaukta.

def call_counter(function):
    def wrapper():
        fn = function.__name__
        global log
        if fn in log:
            log[fn] += 1
        else:
            log[fn] = 1
        print(fn, "call count:", log[fn])
        function()
    return wrapper

@call_counter
def print_ok():
    print("Ok")

@call_counter
def print_hi():
    print("Hi")


log = {}

print_ok()
print_ok()
print_hi()
print_ok()
