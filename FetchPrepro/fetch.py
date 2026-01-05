import requests
import json
import time


API_KEY = #["Masukkan API KEY"] 
LIMIT_PAGES = 10  



def get_popular_movies(page):
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "page": page
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Gagal ambil page {page}: {response.status_code}")
        return []


def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


print("🚀 Memulai proses pengambilan data...")
all_movies_data = []


for page in range(1, LIMIT_PAGES + 1):
    print(f"Sedang mengambil halaman {page} dari {LIMIT_PAGES}...")
    movies_list = get_popular_movies(page)
    

    for movie in movies_list:
        movie_id = movie['id']
        
        
        details = get_movie_details(movie_id)
        
        if details:
            
            filtered_data = {
                "id": details.get("id"),
                "title": details.get("title"),
                "release_date": details.get("release_date"),
                "budget": details.get("budget"),
                "revenue": details.get("revenue"),
                "genres": [g['name'] for g in details.get("genres", [])], 
                "popularity": details.get("popularity"),
                "vote_average": details.get("vote_average"),
                "runtime": details.get("runtime"),
                "production_companies": [p['name'] for p in details.get("production_companies", [])]
            }
            all_movies_data.append(filtered_data)
        
        
        time.sleep(0.1)


filename = "movies_raw_data.json"
with open(filename, "w") as f:
    json.dump(all_movies_data, f, indent=2)

print(f"\n✅ Selesai! Data {len(all_movies_data)} film tersimpan di '{filename}'")

#KODE FETCH DATA