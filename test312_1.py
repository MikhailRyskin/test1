import re


text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

pattern = re.compile(r'wo')
res_1 = re.match(pattern, text)
print(res_1)
res_2 = re.search(pattern, text)
print(res_2)
print(res_2.group())
print(res_2.start())
print(res_2.end())
print(re.findall(pattern, text))
print(re.sub(pattern, 'ЗАМЕНА', text))

