import requests

# GET요청 보내기

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.text)



'''
curl test

curl https://jsonplaceholder.typicode.com/posts

StatusCode        : 200                                                                           StatusDescription : OK                                                                            Content           : [                                                                             
                    X-Ratelimit-Reset: 1680085368
                    Vary: Origin, Accept-Encoding
                    Access-Control-A...
Forms             : {}
Headers           : {[Transfer-Encoding, chunked], [Connection, keep-alive], [X-Ratelimit-Limit,  
                    1000], [X-Ratelimit-Remaining, 997]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 27520

'''