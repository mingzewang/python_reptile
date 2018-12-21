
#百度翻译爬虫
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi'
param = {
"from": "zh",
"to": "en",
"query": "英雄",
"transtype": "translang",
"simple_means_flag": "3"
}
#将参数转码
param = urllib.parse.urlencode(param)
#将参数转换为bytes类型
param = bytes(param,encoding='utf8')

#发送请求
request = urllib.request.Request(url,data=param)

response =urllib.request.urlopen(request)
#读取返回的数据
data = response.read()
#将bytes类型转换为str类型
data =str(data,encoding="utf8")
result = json.loads(data)
#获取需求的数据

dest = result["trans_result"]["data"][0]["dst"]
print("翻译后的结果："+dest)