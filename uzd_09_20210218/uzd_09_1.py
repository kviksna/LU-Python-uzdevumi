# 2021.02.18, Uzd 1:
# Izveidot sarakstu, kur ir skaitļi no 1 līdz 100, kas nedalās ar 3.

def nums_div(start, end, div):
    for i in range(start, end):
        if i % div == 0:
            yield i

for i in nums_div(start=1, end=100, div=3):
    print(i)

# Short:
print([i for i in range(1,100) if i % 3 == 0])
