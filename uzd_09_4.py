# 2021.02.18, Uzd 4:
# Izveidot dekoratoru, kas izprintēs funckijas nosaukumu, kad tā tiks izsaukta

def print_function_name(function):
    def wrapper():
        print("Executing:", function.__name__)
        function()
    return wrapper

@print_function_name
def print_ok():
    print("Ok")

print_ok()