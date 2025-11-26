# api/application/copernicus_bridge.py

import xarray as xr
import numpy as np
import pandas as pd
from dataclasses import dataclass

@dataclass(frozen=True)
class NCPoint:
    lat: np.float32
    lon: np.float32
    depth: np.float32
    time: np.datetime64

    def __lt__(self, other: "NCPoint") -> bool:
        """Strict comparison, to facilitate bound checking below."""
        return self.lat < other.lat and self.lon < other.lon and self.depth < other.depth and self.time < other.time

    def __le__(self, other: "NCPoint") -> bool:
        return self.lat <= other.lat and self.lon <= other.lon and self.depth <= other.depth and self.time <= other.time

class CopernicusBridge:
    def __init__(self,
        path: str,
        min_b=NCPoint(30.19, -17.29, 1.018, pd.to_datetime('2025-05-01', format="%Y-%m-%d")),
        max_b=NCPoint(45.98, 36.29, 5.465, pd.to_datetime('2025-09-30', format="%Y-%m-%d"))
    ) -> None:
        self._path = path
        self._data = xr.open_dataset(self._path)
        self._min_b = min_b
        self._max_b = max_b

    def get_sst_at(self, point: NCPoint) -> np.float32:
        thetao = self._data['thetao']
        sst = thetao.sel(
            latitude=point.lat,
            longitude=point.lon,
            depth=point.depth,
            time=point.time,
            method='nearest',
        )
        return sst.values

    def __contains__(self, point: NCPoint) -> bool:
        return self._min_b <= point and point <= self._max_b

if __name__ == "__main__":
    PATH = "../datasets/local/copmed.nc"
    cb = CopernicusBridge(PATH)
    p = NCPoint(37.18, -1.27, 1.018, '2025-08-11')
    q = NCPoint(30.18, -100.27, 1.018, '2025-08-11')
    print(p in cb)
    print(q in cb)
    print(cb.get_sst_at(p))
