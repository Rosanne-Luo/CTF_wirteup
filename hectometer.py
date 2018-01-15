# coding:utf-8
# 解题链接： http://ctf5.shiyanbar.com/jia

import requests
import re

url = 'http://ctf5.shiyanbar.com/jia/'
url_check = 'http://ctf5.shiyanbar.com/jia/index.php?action=check_pass'
s = requests.session()  #注意两次访问网页的session要保持，不然表达式会被刷新。
html = s.get(url).content.decode('gbk')
# print(html)
pattern = re.compile(r"name='my_expr'>(.*?) </div>")
text = pattern.findall(html)[0]
text = text.replace('x','*').replace('÷','/')
result = eval(text)
print('{} = {}'.format(text,eval(text)))
data = {'pass_key':result}
html2 = s.post(url_check,data=data).content.decode('gbk')
print(html2)
