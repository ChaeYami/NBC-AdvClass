import threading
import os

def foo():
    print('This is foo')
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())
 
def bar():
    print('This is bar')
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())
 
def baz():
    print('This is baz')
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())

if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()
    
'''
print example

This is foo
thread id 24904
process id 17684
This is bar
thread id 15616
process id 17684
This is baz
thread id 12632
process id 17684
'''