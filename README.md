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
```

### Project Source Data
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

### Project Structure
```
https://resourcewatch.org/data/explore/dis016rw1-Active-Fault-Lines_1
https://viewer.esa-worldcover.org/worldcover
https://resourcewatch.org/data/explore/bio040-Protected-Area-Connectivity
```

### Feature Information
| Feature                       | Description                                                    | Paramaters                               |
| ----------------------------- | -------------------------------------------------------------- | ---------------------------------------- |
| `fault_line_distance`         | Fay hattına olan uzaklık (metre cinsinden)                     | point: list(lon, lat)                    | 
| `slope_degree`                | Arazinin eğimi (derece veya yüzde)                             | point: list(lon, lat)                    |
| `elevation`                   | Rakım yüksekliği (metre cinsinden)                             | point: list(lon, lat)                    |  
| `soil_type`                   | Arazi tipi (tarım, çorak, orman vb.)                           | point: list(lon, lat)                    |  
| `land_use`                    | Arazi kullanımı (konut, sanayi, tarım...)                      | point: list(lon, lat) , radius: int      |
| `green_area_coverage`         | Belirli bir yarıçap içinde yeşil alan oranı (%)                | point: list(lon, lat) , radius: int      |
| `water_proximity`             | En yakın su kaynağına uzaklık                                  | point: list(lon, lat) , radius: int      |
| `climate_zone`                | Bulunduğu iklim sınıflandırması (Köppen gibi)                  | `No`                                     |
| `seasonal_accessibility`      | Yıl boyunca ulaşılabilirlik durumu                             | `No`                                     |
| `disaster_risk_index`         | Genel afet riski skoru (deprem, sel, yangın vs.)               | point: list(lon, lat)                    |
| `biodiversity_index`          | Biyoçeşitlilik yoğunluğu ve nadir türlerin varlığı             | point: list(lon, lat)                    |
| `protected_area_proximity`    | Sit alanı, milli park gibi koruma alanlarına yakınlık          | point: list(lon, lat)                    |  
| `air_quality_index`           | PM2.5/PM10 gibi hava kalitesi ölçümleri                        | point: list(lon, lat)                    |
| `noise_pollution_potential`   | Gürültü kaynağına (trafik, sanayi) yakınlık                    | point: list(lon, lat) , radius: int      |
| `groundwater_pollution_risk`  | Yeraltı suyu kirliliği riski (tarım/sanayi etkisi)             | `No`                                     |
| `transport_accessibility`     | Toplu taşıma, yol, otoyol gibi ağlara erişim kolaylığı         | point: list(lon, lat) , radius: int      |
| `infrastructure_availability` | Su, elektrik, kanalizasyon gibi altyapı durumu                 | point: list(lon, lat) , radius: int      |
| `zoning_compliance`           | Mevcut imar planlarına uyumluluk (binary)                      | point: list(lon, lat) , radius: int      |
| `poi_density`                 | Yakın çevredeki market, okul, eczane gibi noktaların yoğunluğu | point: list(lon, lat) , radius: int      |
| `socioeconomic_score`         | Bölgenin gelir değeri                                          | point: list(lon, lat)                    |






