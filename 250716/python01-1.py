import json

data = """
{
    "lastBuildDate": "Wed, 16 Jul 2025 13:20:27 +0900",
    "total": 1261632,
    "start": 1,
    "display": 10,
    "items": [
        {
            "title": "[비비앙] 월넛크릭그린 오 드 퍼퓸 EDP 10ml 20250423-2",
            "link": "https://link.musinsa.com/app/goods/4442601?utm_source=naver_jisicshopping&utm_medium=sh&source=NVSH&utm_term={keyword}&utm_content={ad_group}",
            "image": "https://shopping-phinf.pstatic.net/main_5038779/50387791565.jpg",
            "lprice": "41900",
            "hprice": "",
            "mallName": "무신사",
            "productId": "50387791565",
            "productType": "2",
            "brand": "비비앙",
            "maker": "",
            "category1": "화장품/미용",
            "category2": "향수",
            "category3": "여성향수",
            "category4": ""
        },
         {
            "title": "[보니데] V&amp;A 커버업 랩 수영복 그린(프리) P00000IK",
            "link": "https://link.musinsa.com/app/goods/1968765?utm_source=naver_jisicshopping&utm_medium=sh&source=NVSH&utm_term={keyword}&utm_content={ad_group}",
            "image": "https://shopping-phinf.pstatic.net/main_5280188/52801887678.jpg",
            "lprice": "84990",
            "hprice": "",
            "mallName": "무신사",
            "productId": "52801887678",
            "productType": "2",
            "brand": "보니데",
            "maker": "",
            "category1": "스포츠/레저",
            "category2": "수영",
            "category3": "여성수영복",
            "category4": "원피스수영복"
        },
        {
            "title": "[피지컬가먼츠] P2407 메쉬배색 기능성 오버핏반팔 [블랙] P2407",
            "link": "https://link.musinsa.com/app/goods/4128907?utm_source=naver_jisicshopping&utm_medium=sh&source=NVSH&utm_term={keyword}&utm_content={ad_group}",
            "image": "https://shopping-phinf.pstatic.net/main_4777637/47776373129.jpg",
            "lprice": "26890",
            "hprice": "",
            "mallName": "무신사",
            "productId": "47776373129",
            "productType": "2",
            "brand": "피지컬가먼츠",
            "maker": "",
            "category1": "패션의류",
            "category2": "남성의류",
            "category3": "티셔츠",
            "category4": ""
        }
    ]
}
"""

json_data = json.loads(data)
print(json_data["items"][0]["title"])