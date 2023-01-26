def fun(lst, trgt):
    for i in lst:
        trgt+=i
    return trgt
lst = [1,3,5,7,8]
trgt= 5
print(fun(lst, trgt))
