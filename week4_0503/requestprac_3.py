import requests


# PUT/DELETE 요청 보내기

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=data)
print(response.text)
print(response.status_code)

response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(response.text)
print(response.status_code)


'''
print
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 1
}
200
{}
200
'''


'''
curl test

$ curl -X PUT -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts/1

{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 1

'''