import json
import pandas as pd

print("🍳 Sedang memasak data...")

with open("movies_raw_data.json", "r") as f:
    data = json.load(f)

rows = []
for m in data:
    
    primary_genre = m["genres"][0] if m.get("genres") and len(m["genres"]) > 0 else "Unknown"
    
    rows.append({
        "id": m.get("id"),
        "title": m.get("title"),
        "budget": m.get("budget"),
        "revenue": m.get("revenue"),
        "rating": m.get("vote_average"),
        "popularity": m.get("popularity"),
        "genre": primary_genre,
        "release_date": m.get("release_date")
    })

df = pd.DataFrame(rows)


df = df[(df["budget"] > 1000) & (df["revenue"] > 1000)]
df = df.dropna(subset=['release_date'])


df["roi"] = df["revenue"] / df["budget"]


df["release_date"] = pd.to_datetime(df["release_date"])
df["month"] = df["release_date"].dt.month

def get_season(month):
    if month in [12, 1, 2]: return "Winter"
    elif month in [3, 4, 5]: return "Spring"
    elif month in [6, 7, 8]: return "Summer"
    else: return "Fall"

df["season"] = df["month"].apply(get_season)


final_df = df[["title", "budget", "revenue", "roi", "rating", "popularity", "genre", "season", "release_date"]]


final_df.to_csv("movies_clean.csv", index=False)

print(f"✅ Selesai! Data matang tersimpan di 'movies_clean.csv'.")
print(f"📊 Jumlah film layak analisis: {len(final_df)}")

#KODE PREPROCESSING UBAH KE CSV