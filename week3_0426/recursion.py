'''
def rec(n):
    print (n)
    rec(n+1)

rec(1)

error : 

RecursionError: maximum recursion depth exceeded while calling a Python object

'''

# #재귀함수 사용해서 팩토리얼 구하기
# def fac(n):
#     if(n <= 1):
#         return 1
#     else:
#         return n * fac(n - 1)

# print(fac(0))
# print(fac(6))
# print(fac(1))


#피보나치
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(12))