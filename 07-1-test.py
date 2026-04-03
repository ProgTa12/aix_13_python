from urllib import request
target = request.urlopen("http://www.naver.com")
output = target.read()
print(output)