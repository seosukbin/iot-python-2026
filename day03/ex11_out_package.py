## ex01_out_package.py 외부 라이브러리 사용

import requests
response = requests.get("http://www.google.com")

print(response.status_code)
print(response.content)