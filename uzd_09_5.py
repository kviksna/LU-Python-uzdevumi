# 2021.02.18, Uzd 5:
# Izveidot ģeneratora funkciju, kas ģenerē pirmskaitļus (skaitļi kas dalās tikai ar 1 vai ar sevi, 0 un 1 nav pirmskaitļi).
# Samples/ideas:  https://stackoverflow.com/questions/567222/simple-prime-number-generator-in-python

def primes(start, end):
    if start < 2:
        start = 2  # because 0 and 1 is not primes
    for i in range(start, end+1):
        is_prime = True
        for x in range(2, i):
            if i % x == 0:
                is_prime = False
                break
        if is_prime:
            yield i

for i in primes(start=2, end=20):
    print(i)