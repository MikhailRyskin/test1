import re
text = 'AV is largest Analytics community of India '

res = re.findall(r'\b[aoieywAOIEYW]\w+', text)
print(res)
#

text_1 = 'Even if they are djinns, I will get djinns that can outdjinn them.'

pattern_1 = r'\b[aoieyAOIEY]\w*'
res_1 = re.findall(pattern_1, text_1)
print(res_1)

pattern_2 = r'\b[^\ \.\,aoieyAOIEY]\w*'
res_2 = re.findall(pattern_2, text_1)
print(res_2)
