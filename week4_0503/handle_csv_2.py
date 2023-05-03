# 파이썬에서 csv 파일을 다루기 위해 모듈 import
import csv

csv_path = "sample2.csv"

# csv 파일을 쓸 때는 newline='' 옵션을 줘서 중간에 공백 라인이 생기는 것을 방지합니다.
csv_file = open(csv_path, "a", encoding="utf-8", newline='')

#  파일 객체를 인수로 받아들이고 writer 객체를 반환 
#  writer 객체의 writerow() 메서드를 사용하여 각 행을 쓸 수 있다
csv_writer = csv.writer(csv_file)

# csv에 데이터를 추가합니다.
csv_writer.writerow(["lee@sparta.com", '1989', "lee", "Seoul"])

csv_file.close()

csv_file = open(csv_path, "r", encoding="utf-8")
csv_data = csv.reader(csv_file)
for i in csv_data:
    print(i)

csv_file.close()

# result output
"""
...
['lee@sparta.com', '1989', 'lee', 'Seoul'] # 추가 된 행
"""
# sample2.csv 생성됨