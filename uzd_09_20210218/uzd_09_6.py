# 2021.02.18, Uzd 6:
# Izveidot range() analogu, argumentu secībai nav nozīmes.
# https://docs.python.org/3/library/functions.html#func-range
# https://github.com/dcrosta/xrange/blob/master/xrange.py
# https://github.com/python/cpython/blob/master/Objects/rangeobject.c

# def my_range(start=0, stop=10, step=1):
#     for i in range(start, stop, step):
#         yield i

def my_range(start=0, stop=10, step=1):
    i = start
    while i != stop:
        i += step
        yield i

for i in my_range(start=2, stop=20, step=1):
    print(i)
for i in my_range(start=2, stop=20, step=2):
    print(i)
for i in my_range(start=20, stop=2, step=-1):
    print(i)
