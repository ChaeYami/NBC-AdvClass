import requests

# POST 요청 보내기

data = {'title' : 'foo', 'body' : 'bar', 'userID':1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data =data)
print(response.text) 
print(response.status_code) # 201
'''
print
{
  "title": "foo",
  "body": "bar",
  "userID": "1",
  "id": 101
}
201

'''

'''
curl test

curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}

'''