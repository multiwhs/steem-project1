#-*-coding: utf-8-*-
# pip install requests
# pip install pandas
#
import json
import time
import requests
import codecs
import win32com.client

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

coinName = "steem";
url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days?code=CRIX.UPBIT.KRW-' + coinName +'&count=10';
    
def load_data():
    config_path = 'upbit.txt'
    with codecs.open(config_path, encoding="UTF-8") as fp:
        return json.load(fp)

'''
try:
    res = requests.get(url, headers=headers)
except requests.exceptions.HTTPError as err:
    print (err)
    exit(1)

data = res.json()  # json 구조로 변환
'''
data = load_data()
code = data[0]['code']

excel = 1   # excel로 출력을 원할 때.  console을 원하는 경우에는 0으로 변경
if (excel) :
    # exel 관련
    excel = win32com.client.Dispatch("Excel.Application")  # excel 실행
    excel.Visible = True
    #wb = excel.Workbooks.Create('c:\Temp\\spac.xls')   #  excel 파일 생성하는 방법
    wb = wb = excel.Workbooks.Add()
    ws = wb.ActiveSheet

    ws.Cells(1, 1).Value = code;  # coin code 출력
    #엑셀에 title 출력하기
    title=["Date","open","high","low","final","vol"]
    for i in range(len(title)) :
        ws.Cells(2, i+1).Value = title[i];

    excel_row = 2

    for dailyData in data  :
        excel_row = excel_row + 1
        date = dailyData['candleDateTimeKst']
        onlyDate = date.split('T')   # 날짜정보와 시간정보 분리
        ws.Cells(excel_row, 1).Value = onlyDate
        ws.Cells(excel_row, 2).Value = dailyData['openingPrice']
        ws.Cells(excel_row, 3).Value = dailyData['highPrice']
        ws.Cells(excel_row, 4).Value = dailyData['lowPrice']
        ws.Cells(excel_row, 5).Value = dailyData['tradePrice']
        ws.Cells(excel_row, 6).Value = dailyData['candleAccTradeVolume']

#    wb.SaveAs('c:\\temp\\test.xlsx')  # 저장하고 싶을 때
#    excel.Quit()                       # 끝나고 엑셀을 닫고 싶을 때
else :  # 그냥 콘솔로 출력을 원할때
    print(code)
    print("==========================================")
    print("   date    open high low final    vol")
    print("==========================================")
    for dailyData in data  :
        date = dailyData['candleDateTimeKst']
        onlyDate = date.split('T')   # 날짜정보와 시간정보 분리
        print(onlyDate[0], "%d"%dailyData['openingPrice'], "%d"%dailyData['highPrice'], "%d"%dailyData['lowPrice'], "%d"%dailyData['tradePrice'], "%d"%dailyData['candleAccTradeVolume'])

    print("==========================================")
 
print ("")
print('')
