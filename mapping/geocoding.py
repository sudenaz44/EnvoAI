# geocoding.py
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

# Test etmek için:
if __name__ == "__main__":
    adres = input("Bir adres girin: ")
    lat, lon = adresi_koordinata_cevir(adres)
    print(f"Enlem: {lat}, Boylam: {lon}")
