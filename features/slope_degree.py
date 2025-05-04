# features/slope_degree.py
import requests
import numpy as np

def get_slope_degree(point, step=0.001):
    """
    Estimates slope degree around a point using elevation differences.
    It samples 3x3 grid and calculates gradient-based slope.
    """

    lon, lat = point

    def get_elev(lat, lon):
        url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()["results"][0]["elevation"]
        return 0

    # Sample grid
    grid = []
    for dy in [-step, 0, step]:
        row = []
        for dx in [-step, 0, step]:
            row.append(get_elev(lat + dy, lon + dx))
        grid.append(row)

    grid = np.array(grid)
    gy, gx = np.gradient(grid, step * 111000)  # convert deg to meters approx.
    slope_rad = np.arctan(np.sqrt(gx**2 + gy**2))
    slope_deg = np.degrees(slope_rad)

    return float(np.mean(slope_deg))
