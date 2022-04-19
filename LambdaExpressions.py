def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
ucle = lambda a : a * 3

print(ucle(11))

print(mydoubler(11))
print(mytripler(11))


num =[1,2,3,4,5,9]

result = list(map(mydoubler,num))
print(result)



result = list(map(lambda a : a*2 ,num))
print(result)

result = list(map(ucle ,num))
print(result)

def check_even(n):
    return n%2==0

result =list(filter(check_even, num))
print(result)

result =list(filter(lambda n: n%2==0, num))
print(result)

