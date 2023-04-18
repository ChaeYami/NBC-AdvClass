from multiprocessing import Process
import os

# ============== Class ============== 

# print('hello chaenii')
# print('my pid is', os.getpid())
# hello chaenii
# my pid is 9304

'''
def foo():
    print('child process', os.getpid())
    print('my parent is', os.getppid())
  
if __name__ == '__main__':
    print('parent process', os.getpid())
    
    child = Process(target=foo).start() # foo 함수를 실행하는 자식 프로세스

print example
parent process 11844 --> parent process + PID값
child process 15712 --> 자식 프로세스가 foo 함수 실행
my parent is 11844
'''

# ============== Assignment ============== 

def foo():
    print('-----')
    print('This is foo')
    print('my pid is', os.getpid())
    print('my parents pid is', os.getppid())
    
def bar():
    print('-----')
    print('This is bar')
    print('my pid is', os.getpid())
    print('my parents pid is', os.getppid())
    
def baz():
    print('-----')
    print('This is baz')
    print('my pid is', os.getpid())
    print('my parents pid is', os.getppid())
  
if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start() 
    child4 = Process(target=baz).start() # 같은 부모
    child5 = Process(target=baz).start() # 같은 부모
    
'''
print example
-----
This is foo
my pid is 23520
my parents pid is 3024
-----
This is bar
my pid is 12292
my parents pid is 3024
-----
This is baz
my pid is 7100
my parents pid is 3024
-----
This is baz
my pid is 2936
my parents pid is 3024
-----
This is baz
my pid is 17132
my parents pid is 3024
'''