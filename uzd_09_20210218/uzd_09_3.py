# 2021.02.18, Uzd 3:
# Izveidot ģeneratora funkciju, kas ģenerē skaitļa reizinājumus ar skaitļiem no 0 līdz 10

def num_mult(num, start, end):
    for i in range(start, end+1):
        yield num * i

try:
    num = int(input("Enter number: "))
except ValueError:
    exit("Non integer value")

for i in num_mult(num=num, start=0, end=10):
    print(i)

# Short:
print([i * num for i in range(1, 10+1)])

# Another:
for i in range(0, 10+1):
    print(f"{num} * {i} = {num * i}")