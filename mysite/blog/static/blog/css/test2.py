import requests
import re

# header头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.baidu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}
#请求url地址
url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv14&productId=6045059&score=0&sortType=5&page=1&pageSize=10&isShadowSku=4687958&rid=0&fold=1"

# 提交请求爬取信息
response = requests.get(url,headers=headers)

#获取响应码
html = response.text

pat = '"content":"(.*?)"'
items = re.findall(pat,html,re.S)

#print(items)
for v in items:
    print(v)
    print("="*80)