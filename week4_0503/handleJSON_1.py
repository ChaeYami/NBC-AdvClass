import json

# JSON 문자열
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# JSON 문자열을 Python 객체로 변환
data = json.loads(json_data)

# Python 객체 출력
print(data)
print(type(data))

'''
print
{'name': 'John', 'age': 30, 'city': 'New York'}
<class 'dict'>
'''


{
    "employee": {
        "name": "sonoo",
        "salary": 56000,
        "married": True
        }
}

with open('data.json') as file:
    data = json.load(file)
    
print(data['employee'])