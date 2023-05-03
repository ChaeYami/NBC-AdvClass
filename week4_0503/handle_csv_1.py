# 파이썬에서 csv 파일을 다루기 위해 모듈 import
import csv

csv_path = "sample.csv"

# csv를 list 자료형으로 읽기
csv_file = open(csv_path, "r", encoding="utf-8")
# csv.reader : 파일 객체를 인수로 받아들여 순회 가능한 reader 객체 반환
csv_data = csv.reader(csv_file)
# print(type(csv_data))
for i in csv_data:
    print(i)

# 작업이 끝난 csv 파일을 닫아줍니다.
csv_file.close()

# result output
"""
['email', 'birthyear', 'name', 'Location']
['laura@example.com', '1996', 'Laura Grey', 'Manchester']
['craig@example.com', '1989', 'Craig Johnson', 'London']
['mary@example.com', '1997', 'Mary Jenkins', 'London']
['jamie@example.com', '1987', 'Jamie Smith', 'Manchester']
['john@example.com', '1998', 'John', 'Manchester']
"""

# csv를 dict 자료형으로 읽기
csv_file = open(csv_path, "r", encoding="utf-8")
csv_data = csv.DictReader(csv_file)
# print(type(csv_data))
for i in csv_data:
    print(i)

csv_file.close()

# result output
"""
{'email': 'laura@example.com', 'birthyear': '1996', 'name': 'Laura Grey', 'Location': 'Manchester'}
{'email': 'craig@example.com', 'birthyear': '1989', 'name': 'Craig Johnson', 'Location': 'London'}
{'email': 'mary@example.com', 'birthyear': '1997', 'name': 'Mary Jenkins', 'Location': 'London'}
{'email': 'jamie@example.com', 'birthyear': '1987', 'name': 'Jamie Smith', 'Location': 'Manchester'}
{'email': 'john@example.com', 'birthyear': '1998', 'name': 'John', 'Location': 'Manchester'}
"""