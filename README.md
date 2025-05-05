# EnvoAI

### Project Objective
An artificial intelligence-supported sustainability project that analyzes the potential impacts of public/private sector projects on nature according to location, sector, scale and environmental parameters.

<img src="https://github.com/user-attachments/assets/d3486592-162e-4399-b6bb-7160d0dd8071" style="width:75%;"></img>

### Project Library
```
pip install geopandas
pip install shapely
pip install rasterio
pip install osmnx
pip install geopy
pip install scikit-learn=1.1.3
```

### Project Structure 
```
envoai/
├── data/
│ ├── fault_lines.shp
│ ├── protected_area.shp
│ ├── ... (other data API)
├── features/
│ ├── elevation.py
│ ├── poi_density.py
│ ├── fault_line_distance.py
│ ├── green_area.py
│ └── ... (other feature scripts)
├── main.py
```

### Project Source Data
```
https://resourcewatch.org/data/explore/dis016rw1-Active-Fault-Lines_1
https://viewer.esa-worldcover.org/worldcover
https://resourcewatch.org/data/explore/bio040-Protected-Area-Connectivity
```

### Feature Information
| Feature                       | Description                          | Kütüphaneler                       | Fonksiyon Parametreleri                | Çıktı Değeri                     | Değer Tipi |
| ----------------------------- | ------------------------------------ | ---------------------------------- | -------------------------------------- | -------------------------------- | ---------- |
| `fault_line_distance`         | Fay hattına olan uzaklık (metre)     | `geopandas`, `shapely`             | `point: list[lon, lat]`                | float (metre)                    | Sayısal    |
| `slope_degree`                | Arazinin eğimi (derece)              | `rasterio`, `numpy`                | `point: list[lon, lat]`                | float (derece)                   | Sayısal    |
| `elevation`                   | Rakım yüksekliği (metre)             | `elevation`, `SRTM`, `rasterio`    | `point: list[lon, lat]`                | float (metre)                    | Sayısal    |
| `soil_type`                   | Arazi tipi (tarım, çorak vb.)        | `geopandas`                        | `point: list[lon, lat]`                | string                           | Kategorik  |
| `land_use`                    | Arazi kullanımı (konut, tarım vs.)   | `geopandas`, `osmnx`               | `point: list[lon, lat]`, `radius: int` | string                           | Kategorik  |
| `green_area_coverage`         | Belirli yarıçapta yeşil alan yüzdesi | `geopandas`, `osmnx`               | `point: list[lon, lat]`, `radius: int` | float (%)                        | Sayısal    |
| `water_proximity`             | Su kaynağına uzaklık                 | `geopandas`, `osmnx`               | `point: list[lon, lat]`, `radius: int` | float (metre)                    | Sayısal    |
| `climate_zone`                | İklim sınıfı (Köppen-Geiger)         | `geopandas`, `rasterio`            | Yok                                    | string                           | Kategorik  |
| `seasonal_accessibility`      | Tüm yıl boyunca erişilebilirlik      | `geopandas`                        | Yok                                    | string / boolean                 | Kategorik  |
| `disaster_risk_index`         | Afet riski skoru (deprem, sel...)    | `geopandas`, `custom_risk_data`    | `point: list[lon, lat]`                | float (0-1 arası skor)           | Sayısal    |
| `biodiversity_index`          | Biyoçeşitlilik skoru                 | `geopandas`, `biodiversity_data`   | `point: list[lon, lat]`                | float                            | Sayısal    |
| `protected_area_proximity`    | Koruma alanına uzaklık               | `geopandas`, `shapely`             | `point: list[lon, lat]`                | float (metre)                    | Sayısal    |
| `air_quality_index`           | Hava kalitesi (PM2.5, PM10)          | `openaq`, `requests`, `geopandas`  | `point: list[lon, lat]`                | float (AQI skoru)                | Sayısal    |
| `noise_pollution_potential`   | Gürültü kaynağına yakınlık           | `geopandas`, `osmnx`               | `point: list[lon, lat]`, `radius: int` | float (metre)                    | Sayısal    |
| `groundwater_pollution_risk`  | Yeraltı suyu kirliliği riski         | `geopandas`, `environmental_data`  | Yok                                    | float / string (low/medium/high) | Kategorik  |
| `transport_accessibility`     | Ulaşım altyapısına yakınlık          | `osmnx`, `networkx`                | `point: list[lon, lat]`, `radius: int` | float (mesafe veya erişim skoru) | Sayısal    |
| `infrastructure_availability` | Altyapı varlığı                      | `geopandas`, `infrastructure_data` | `point: list[lon, lat]`, `radius: int` | boolean / string                 | Kategorik  |
| `zoning_compliance`           | İmar planına uyum                    | `geopandas`, `zoning_data`         | `point: list[lon, lat]`, `radius: int` | boolean                          | Kategorik  |
| `poi_density`                 | Market, okul vb. POI yoğunluğu       | `osmnx`, `geopandas`               | `point: list[lon, lat]`, `radius: int` | int / float                      | Sayısal    |
| `socioeconomic_score`         | Gelir düzeyi ve sosyal seviye        | `geopandas`, `socioeconomic_data`  | `point: list[lon, lat]`                | float (skor)                     | Sayısal    |




