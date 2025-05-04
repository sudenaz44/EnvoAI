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
pip install sentinelhub
pip install geopy
```

### Project Structure
```
envoai/
├── data/
│ ├── fault_lines.shp
│ ├── map.py
│ ├── ... (other data API)
├── features/
│ ├── elevation.py
│ ├── poi_density.py
│ ├── fault_line_distance.py
│ ├── green_area.py
│ └── ... (other feature scripts)
├── main.py
```

### Feature Information
| Feature                       | Type        | Description                                                    | Used it?  | Data Source                                                               |
| ----------------------------- | ----------- | -------------------------------------------------------------- | --------- | ------------------------------------------------------------------------- |
| `fault_line_distance`         | Location    | Fay hattına olan uzaklık (metre cinsinden)                     | Yes       | https://resourcewatch.org/data/explore/dis016rw1-Active-Fault-Lines_1     |
| `slope_degree`                | Location    | Arazinin eğimi (derece veya yüzde)                             | Yes       |
| `elevation`                   | Location    | Rakım yüksekliği (metre cinsinden)                             | Yes       |                                              |
| `soil_type`                   | Environment | Arazi tipi (tarım, çorak, orman vb.)                           | Yes       | https://viewer.esa-worldcover.org/worldcover |
| `land_use`                    | Location    | Arazi kullanımı (konut, sanayi, tarım...)                      | `No`      |
| `green_area_coverage`         | Environment | Belirli bir yarıçap içinde yeşil alan oranı (%)                | Yes       |
| `water_proximity`             | Environment | En yakın su kaynağına uzaklık                                  | Yes       |
| `climate_zone`                | Environment | Bulunduğu iklim sınıflandırması (Köppen gibi)                  | `No`      |
| `seasonal_accessibility`      | Location    | Yıl boyunca ulaşılabilirlik durumu                             | `No`      |
| `disaster_risk_index`         | Environment | Genel afet riski skoru (deprem, sel, yangın vs.)               | Yes       |
| `biodiversity_index`          | Environment | Biyoçeşitlilik yoğunluğu ve nadir türlerin varlığı             | Yes       |
| `protected_area_proximity`    | Environment | Sit alanı, milli park gibi koruma alanlarına yakınlık          | Yes       | https://resourcewatch.org/data/explore/bio040-Protected-Area-Connectivity |
| `air_quality_index`           | Environment | PM2.5/PM10 gibi hava kalitesi ölçümleri                        | Yes       |
| `noise_pollution_potential`   | Environment | Gürültü kaynağına (trafik, sanayi) yakınlık                    | Yes       |
| `groundwater_pollution_risk`  | Environment | Yeraltı suyu kirliliği riski (tarım/sanayi etkisi)             | `No`      |
| `transport_accessibility`     | Human       | Toplu taşıma, yol, otoyol gibi ağlara erişim kolaylığı         | Yes       |
| `infrastructure_availability` | Human       | Su, elektrik, kanalizasyon gibi altyapı durumu                 | Yes       |
| `zoning_compliance`           | Human       | Mevcut imar planlarına uyumluluk (binary)                      | Yes       |
| `poi_density`                 | Human       | Yakın çevredeki market, okul, eczane gibi noktaların yoğunluğu | Yes       |
| `socioeconomic_score`         | Human       | Bölgenin gelir değeri                                          | Yes       |






