# Python3 샘플 코드 #


import requests
from bs4 import BeautifulSoup 
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth'
params ={'serviceKey' : 'nYP3LqqwTg5GNS52Q4YW6OgTesn898EOaEGsWDGE4nFiAWypzAQyl5Yy80y1uqNdz9RDVTwnhUDaItKUkwHSKw==', 'returnType' : 'xml', 'numOfRows' : '100', 'pageNo' : '1', 'searchDate' : '2020-11-14', 'InformCode' : 'PM10' }

response = requests.get(url, params=params)
print(response.content)
# bs_obj = BeautifulSoup(response.content, "html.parser")
# print(response.content)
# print(bs_obj)
# print(response.text)

# print(response.dataTime)
