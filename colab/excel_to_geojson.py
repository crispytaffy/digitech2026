import pandas as pd
import json
from pathlib import Path

FILE_NAME = "sample.xlsx"  # ここを変更
SHEET_NAME = 0

path = Path(FILE_NAME)
df = pd.read_csv(path) if path.suffix.lower() == ".csv" else pd.read_excel(path, sheet_name=SHEET_NAME)

required = ["name", "latitude", "longitude"]
missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError(f"必要な列がありません: {missing}")

features = []
for _, row in df.iterrows():
    if pd.isna(row["latitude"]) or pd.isna(row["longitude"]):
        continue

    properties = {}
    for column in df.columns:
        if column not in ["latitude", "longitude"]:
            value = row[column]
            properties[column] = None if pd.isna(value) else value

    features.append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [float(row["longitude"]), float(row["latitude"])]
        },
        "properties": properties
    })

geojson = {"type": "FeatureCollection", "features": features}

with open("mapdata.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2, allow_nan=False)

print(f"{len(features)} 件を mapdata.geojson に変換しました！")
