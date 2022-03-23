#decorator eh uma funcao que retorna uma funcao
#SOBRE :https://peps.python.org/pep-0318/#background



def decor1(func):
    def inner():
        x = func()
        return x*x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    
    return inner

@decor1   #encapsulado baixo pra cima == cebola o msm que fazer decor1(decor(num))
@decor    #
def num():
    return 10

print(num())



@g @f def foo() translates to foo=g(f(foo))
@dec2
@dec1
def func(arg1,arg2, ...):
    pass

#equivalente a

def func(arg1,arg2, ...):
    pass

func = dec2(dec1(func))




@decomaker(argA, argB, ...)
def func(arg1, arg2, ...):
        pass

#equivalente 

func = decomaker(argA,argB, ...)(func)











