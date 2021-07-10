import re

text = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'

pattern = re.compile(r'\\wwood\+\?,')
res = re.findall(pattern, text)
print(res)
