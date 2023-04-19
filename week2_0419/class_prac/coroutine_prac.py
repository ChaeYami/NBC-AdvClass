# ================= coroutine ================= 

# --------- next --------- 
def my_coroutine():
    while True:
        value = yield
        print('Received value:', value)

# 코루틴 객체 생성
co = my_coroutine()

# 코루틴 실행 준비
next(co)

# 값을 보내기
co.send('Hello, world!')

# --------- yield --------- 
def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3


# --------- send --------- 
def my_coroutine():
    while True:
        x = yield
        print('Received:', x)

co = my_coroutine()
next(co)

co.send(10) # Received: 10
co.send(20) # Received: 20
co.send(30) # Received: 30


# 
phone_book = {"John":"123-4567", "Jane":"234-5678" , "Max":"345-6789"}

def search ():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
            
        else : 
            phone_number = "찾을 수 없음"
        
        name = yield phone_number
# 코루틴 객체 생성
search_coroutine = search()
next(search_coroutine)

# 검색 예시
result = search_coroutine.send("John")
print(result) # 123-4567
 
result = search_coroutine.send("Jane")
print(result) # 234-5678

result = search_coroutine.send("Sarah")
print(result) # 찾을 수 없음




