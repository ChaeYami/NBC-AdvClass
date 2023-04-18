
# ============== String method ============== 

# count : 문자열 내에서 특정 문자가 몇 개나 있는지 세는 메서드
text = "Hello, Chaenii!"
cnt = text.count('e')
print("count : ", end="") 
print(cnt) # 2

# find: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드 (없을 경우 -1 return)
text = "Hello, Chaenii!"
position = text.find("Chaenii")
print("position : ", end="") 
print(position) # 7

# index: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드 (없을 경우 ValueError)
text = "Hello, Chaenii!"
try:
    position = text.find("Chaenii")
    print("index : ", end="") 
    print(position) # 7
except ValueError:
    print("문자열 없음")
    
# join: 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메서드
chaeyeon = ["cutie", "pretty", "lovely"]
joined_chaeyeon = ", ".join(chaeyeon)
print("join :",joined_chaeyeon) # cutie, pretty, lovely

'''
upper: 문자열 내의 모든 소문자를 대문자로 바꾸는 메서드
lower: 문자열 내의 모든 대문자를 소문자로 바꾸는 메서드
'''
text = "Hello, Chaenii!"
upper_text = text.upper()
lower_text = text.lower()

print("upper : " + upper_text) # upper : HELLO, CHAENII!
print("lower : " + lower_text) # lower : hello, chaenii!

# replace: 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메서드
text = "Hello, Chaenii!"
replaced_text = text.replace("Hello", "Hi")
print("replace : " + replaced_text) # Hi, Chaenii!

# split: 문자열을 특정 문자를 기준으로 나누는 메서드(결과는 리스트 형태로 반환)
chaeyeon = "cutie,pretty,lovely"
chaenii = chaeyeon.split(",")
print("split : ", end="") 
print(chaenii)
# split : ['cutie', 'pretty', 'lovely']

# len: 리스트의 길이를 반환하는 내장 함수
nums = [1,2,3,4,5,6,7]
print("len : ", end="") 
print(len(nums)) # 7

# del: 리스트에서 특정 요소를 삭제하는 연산자
nums = [1,2,3,4,5,6,7]
del nums[4]
print("del : ", end="")
print(nums) 
# del : [1, 2, 3, 4, 6, 7]

# append: 리스트의 맨 뒤에 새로운 요소를 추가하는 메서드
nums = [1,2,3,4,5,6,7]
nums.append(8)
print("append : ", end="")
print(nums) 
# append : [1, 2, 3, 4, 5, 6, 7, 8]

# sort: 리스트를 오름차순으로 정렬하는 메서드
cy = [1,3,4,2,5,7,6]
cy.sort()
print("sort : ", end="")
print(cy)
#sort : [1, 2, 3, 4, 5, 6, 7]

# reverse: 리스트의 요소 순서를 반대로 뒤집는 메서드
nums = [1,2,3,4,5,6,7]
nums.reverse()
print("reverse : ", end="")
print(nums) 
#reverse : [7, 6, 5, 4, 3, 2, 1]

# index: 리스트에서 특정 요소의 인덱스를 반환하는 메서드
chaeyeon = ["cutie", "pretty", "lovely"]
print("index : ", end="")
print(chaeyeon.index("lovely")) # index : 2

# insert: 리스트의 특정 위치에 요소를 삽입하는 메서드
nums = [1,2,3,4,5,6,7]
nums.insert(3,20)
print("insert : ", end="")
print(nums) # insert : [1, 2, 3, 20, 4, 5, 6, 7]

# remove: 리스트에서 특정 요소를 제거하는 메서드
nums = [1,2,3,4,5,6,7]
nums.remove(4)
print("remove : ", end="")
print(nums) #  [1, 2, 3, 5, 6, 7]

# pop: 리스트에서 마지막 요소를 빼낸 뒤, 그 요소를 삭제하는 메서드 (인덱스를 정해주면 그 요소)
nums = [1,2,3,4,5,6,7]
nums.pop(2)
print("pop : ", end="")
print(nums) # [1, 2, 4, 5, 6, 7]

# count: 리스트에서 특정 요소의 개수를 세는 메서드
nums = [1,1,1,1,1,1,2,3,4,5,6,7]
print("count : ", end="")
print(nums.count(1)) # 6

# extend: 리스트를 확장하여 새로운 요소들을 추가하는 메서드
nums = [1,2,3,4]
nums.extend([5,6,7])
print("extend : ", end="")
print(nums) # extend : [1, 2, 3, 4, 5, 6, 7]

# += 연산자 사용하기
nums = [1,2,3,4]
nums += ([5,6,7])
print("+=사용하기 : ", end="")
print(nums) # [1, 2, 3, 4, 5, 6, 7]


# ============== Dictionary method ============== 

# 딕셔너리 초기화 - 빈 딕셔너리를 만들고 싶을 때
empty_dict = {}
# 딕셔너리 초기화 - 딕셔너리를 초기화하고 싶을 때
chaenii_dict = {"cutie" : 1, "pretty" : 2}
print(chaenii_dict) # {'cutie': 1, 'pretty': 2}

#딕셔너리 쌍 추가
chaenii_dict = {"cutie" : 1, "pretty" : 2}
chaenii_dict["lovely"] = 3
print(chaenii_dict) # {'cutie': 1, 'pretty': 2, 'lovely': 3}

# del : 딕셔너리에서 특정 요소 삭제
chaenii_dict = {'cutie': 1, 'pretty': 2, 'lovely': 3}
del chaenii_dict["pretty"]
print(chaenii_dict) # {'cutie': 1, 'lovely': 3}

'''
딕셔너리에서 특정 Key에 해당하는 Value를 얻는 방법
(딕셔너리에 Key가 없는 경우 KeyError)
'''
chaenii_dict = {'cutie': 1, 'pretty': 2, 'lovely': 3}
print(chaenii_dict["pretty"]) # 2

# keys: 딕셔너리에서 모든 Key를 리스트로 만들기
chaenii_dict = {'cutie': 1, 'pretty': 2, 'lovely': 3}
key_list = list(chaenii_dict.keys())
print("keys : ", end="")
print(key_list) # keys : ['cutie', 'pretty', 'lovely']

# values: 딕셔너리에서 모든 Value를 리스트로 만들기
chaenii_dict = {'cutie': 1, 'pretty': 2, 'lovely': 3}
value_list = list(chaenii_dict.values())
print("values : ", end="")
print(value_list) # values : [1, 2, 3]

# items: 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
chaeyeon = {'name' : 'chaenii',
            'age' : 27,
            'race' : 'fairy'}
items = chaeyeon.items()
print("items : ", end="")
print(items) 
# items : dict_items([('name', 'chaenii'), ('age', 27), ('race', 'fairy')])

# clear: 딕셔너리의 모든 요소를 삭제
chaeyeon = {'name' : 'chaenii',
            'age' : 27,
            'race' : 'fairy'}
chaeyeon.clear()
print("clear : ", end="")
print(chaeyeon) # clear : {}

'''
get: 딕셔너리에서 지정한 키에 대응하는 값을 반환
(딕셔너리에 Key가 없는 경우 None 반환)
'''
chaeyeon = {'name' : 'chaenii',
            'age' : 27,
            'race' : 'fairy'}

print('--get--')
name = chaeyeon.get('name')
print(name) # chaenii

gender = chaeyeon.get('gender')
print("None : ", end="")
print(gender) # None : None
# 기본값 설정 가능
gender = chaeyeon.get('gender', 'unknown')
print("default : ", end="")
print(gender) # default : unknown

# in: 해당 키가 딕셔너리 안에 있는지 확인
chaeyeon = {'name' : 'chaenii',
            'age' : 27,
            'race' : 'fairy'}
print('--in--')
print('name' in chaeyeon) # True
print('gender' in chaeyeon) # False




