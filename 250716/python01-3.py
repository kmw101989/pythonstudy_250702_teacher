import requests
import openpyxl

url = "https://api.themoviedb.org/3/movie/now_playing?language=ko-KR&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYmM4YmQyZGI0NTNkNzQxM2QxYzI4NDRlYzYxN2I2MSIsIm5iZiI6MTY4ODg5NTMxMS4yMTEsInN1YiI6IjY0YWE3ZjRmOWM5N2JkMDBhZGVhZTFiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-21VZjOJOn5x_OGeq_nMzkwrQhgSxFcrC9SeMuuHqJ0"
}

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions["D"].width = 100
excel_sheet.append(["No", "개봉일", "영화제목", "줄거리", "평점"])

res = requests.get(url, headers=headers)
num = 0

if res.status_code == 200 :
    data = res.json()
    for item in data["results"] :
        num += 1
        excel_sheet.append([num, item["release_date"], item["title"], item["overview"], item["vote_average"]])
        print(num, item["release_date"], item["title"], item["overview"], item["vote_average"])
else :
    print("Error Code: ", res.status_code)

excel_file.save("movielist_with_tmdb.xlsx")
excel_file.close()