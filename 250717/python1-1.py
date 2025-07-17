
import requests

url = "https://apis.data.go.kr/B551011/GoCamping/basedList"
request_params = {
    'numOfRows':'50',
    'pageNo':'1',
    'MobileOS':'ETC',
    'MobileApp':'camping',
    'serviceKey':'RGzR0pEvB08eGZWqjj0mYonhz1%2Bkj6rzw2MBbGWGY99AroOuOwtjHo8LOJESQ8Q6jyV9jhaIcfndl%2BG6pi4v0A%3D%3D',
    '_type':'xml'
}

res = requests.get(url, params=request_params)
print(res)