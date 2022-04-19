def cube():
    for i in range(5):
        yield i ** 3

print(cube())

print(next(cube()))
print(next(cube()))
print(next(cube()))


for i in cube():
    print(i)