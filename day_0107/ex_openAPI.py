import requests
# arr = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=종로구&dataTerm=month&pageNo=1&numOfRows=100&returnType=json&serviceKey=nYP3LqqwTg5GNS52Q4YW6OgTesn898EOaEGsWDGE4nFiAWypzAQyl5Yy80y1uqNdz9RDVTwnhUDaItKUkwHSKw%3D%3D'

# response = requests.get(arr)
# print(response.content)
# # 일반 인증키
# # (Encoding)
# #nYP3LqqwTg5GNS52Q4YW6OgTesn898EOaEGsWDGE4nFiAWypzAQyl5Yy80y1uqNdz9RDVTwnhUDaItKUkwHSKw%3D%3D 

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
api_decode = requests.utils.unquote(url)
params ={'serviceKey' : api_decode, 'returnType' : 'xml', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '서울', 'ver' : '1.0' }

response = requests.get(url, params=params)
print("아래")
print(response.content)

#url 방식

# arr1 = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustWeekFrcstDspth?searchDate=2020-11-09&returnType=xml&serviceKey=nYP3LqqwTg5GNS52Q4YW6OgTesn898EOaEGsWDGE4nFiAWypzAQyl5Yy80y1uqNdz9RDVTwnhUDaItKUkwHSKw%3D%3D&numOfRows=100&pageNo=1'
# response = requests.get(arr1)
# print(response.content)

url = 'http://openapi.seoul.go.kr:8088/sample/xml/CardSubwayStatsNew/1/5/20220301'

response = requests.get(url)
print(response.content)