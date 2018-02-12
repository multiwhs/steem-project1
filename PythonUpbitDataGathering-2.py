
#-*-coding: utf-8-*-
import json
import time
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

coinName = "steem";
url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days?code=CRIX.UPBIT.KRW-' + coinName +'&count=10';
    
def load_data():
    config_path = 'upbit.txt'
    with codecs.open(config_path, encoding="UTF-8") as fp:
        return json.load(fp)

try:
    res = requests.get(url, headers=headers)
except requests.exceptions.HTTPError as err:
    print (err)
    exit(1)

data = res.json()  # json 구조로 변환
code = data[0]['code']
print(code)
print("==========================================")
print("   date    open high low final    vol")
print("==========================================")

for i in range(len(data))  :
    date = data[i]['candleDateTimeKst']
    onlyDate = date.split('T')   # 날짜정보와 시간정보 분리
    print(onlyDate[0], "%d"%data[i]['openingPrice'], "%d"%data[i]['highPrice'], "%d"%data[i]['lowPrice'], "%d"%data[i]['tradePrice'], "%d"%(data[i]['candleAccTradeVolume']));

print("==========================================")
print ("a")