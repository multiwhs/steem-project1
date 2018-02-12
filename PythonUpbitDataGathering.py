#-*-coding: utf-8-*-

import urllib.request
import json
#from urllib.parse import urlparse
import codecs
import time

coinName = "steem";
url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days?code=CRIX.UPBIT.KRW-' + coinName +'&count=10';
    
def load_data():
    config_path = 'upbit.txt'
    with codecs.open(config_path, encoding="UTF-8") as fp:
        return json.load(fp)

sdata = ""
fail2GetData = False
failCnt = 0
while True:
    try :
        text  = urllib.request.urlopen(url).read()
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code, ' 5초 대기')
        failCnt += 1
        if ( failCnt > 10 ) :
            fail2GetData = True;
            break;
        time.sleep(5)
    except urllib.error.URLError as e:
        print("URL error")
        exit()
    else:
        failCnt += 1
        if ( failCnt > 10 ) :
            fail2GetData = True;
            break;
        time.sleep(5)
        break;

if ( fail2GetData )  :
    print("Fail to access url")
    exit()

sdata = bytes.decode(text)  # Byte를 텍스트로 만든다.
data = json.loads(sdata)    # json 구조로 변환

#data = load_data()

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