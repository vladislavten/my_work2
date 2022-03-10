import requests, re

my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')

find_data = re.findall(r'(<h3 id=.*>)(.*?)(</h3>)', my_req.text)
result = []
for i in find_data:
    result.append(i[1])

print(result)
