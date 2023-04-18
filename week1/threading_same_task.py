import threading
import os


def foo():
    print('----')
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())
    

if __name__ == '__main__':
    print('process id', os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()
    
'''
process id 5988

thread id 17424
process id 5988
thread id 15656
thread id 14452
process id 5988
process id 5988

---> 다 다른 스레드지만 동일한 프로세스를 공유하고 있다.
'''





