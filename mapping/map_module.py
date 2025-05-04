# map_module.py

import requests

def adresi_koordinata_cevir(adres):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": adres,
        "format": "json",
        "limit": 1
    }
    response = requests.get(url, params=params, headers={'User-Agent': 'envoai-app'})
    data = response.json()

    if data:
        return float(data[0]["lat"]), float(data[0]["lon"])
    else:
        return None, None


if __name__ == "__main__":
    adres = input("Bir adres girin (örn. Üsküdar, İstanbul): ")
    lat, lon = adresi_koordinata_cevir(adres)
    if lat and lon:
        print(f"Enlem: {lat}, Boylam: {lon}")
    else:
        print("Koordinatlar alınamadı.")


# def yesil_alan_var_mi(lat, lon, yaricap=500):
#     import requests
#     overpass_url = "http://overpass-api.de/api/interpreter"
#     query = f"""
#     [out:json];
#     (
#       node["leisure"="park"](around:{yaricap},{lat},{lon});
#       way["leisure"="park"](around:{yaricap},{lat},{lon});
#       relation["leisure"="park"](around:{yaricap},{lat},{lon});
#     );
#     out center;
#     """
#     response = requests.post(overpass_url, data=query)
#     data = response.json()
#     return len(data.get('elements', [])) > 0


# def fay_hattina_yakin_mi(lat, lon, dosya_yolu="fay_hatlari.geojson", max_mesafe_km=5):
#     import geopandas as gpd
#     from shapely.geometry import Point

#     proje_noktasi = Point(lon, lat)
#     gdf = gpd.read_file(dosya_yolu)
#     gdf = gdf.to_crs(epsg=3857)
#     proje_noktasi_proj = gpd.GeoSeries([proje_noktasi], crs="EPSG:4326").to_crs(epsg=3857)
#     gdf["mesafe"] = gdf.distance(proje_noktasi_proj[0]) / 1000
#     return (gdf["mesafe"] < max_mesafe_km).any()




# def koruma_alani_var_mi(lat, lon, dosya="koruma_alanlari.geojson", yaricap_km=2):
#     import geopandas as gpd
#     from shapely.geometry import Point

#     proje_noktasi = Point(lon, lat)
#     gdf = gpd.read_file(dosya).to_crs(epsg=3857)
#     proje_noktasi_proj = gpd.GeoSeries([proje_noktasi], crs="EPSG:4326").to_crs(epsg=3857)
#     gdf["mesafe"] = gdf.distance(proje_noktasi_proj[0]) / 1000
#     return (gdf["mesafe"] < yaricap_km).any()




# def ulasim_noktasi_var_mi(lat, lon, yaricap=500):
#     import requests
#     overpass_url = "http://overpass-api.de/api/interpreter"
#     query = f"""
#     [out:json];
#     (
#       node["public_transport"="station"](around:{yaricap},{lat},{lon});
#       node["highway"="bus_stop"](around:{yaricap},{lat},{lon});
#     );
#     out;
#     """
#     response = requests.post(overpass_url, data=query)
#     data = response.json()
#     return len(data.get('elements', [])) > 0



# lat, lon = 40.9912955, 29.0245631  # Örnek: Kadıköy

# print("Yeşil Alan:", yesil_alan_var_mi(lat, lon))
# print("Fay Hattına Yakınlık:", fay_hattina_yakin_mi(lat, lon))
# print("Koruma Alanı:", koruma_alani_var_mi(lat, lon))
# print("Ulaşım Noktası:", ulasim_noktasi_var_mi(lat, lon))


