# api/application/copernicus_bridge.py

import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import copernicusmarine as cm


DS = cm.read_dataframe(
  dataset_id="cmems_mod_med_phy-tem_anfc_4.2km_P1D-m")
print(DS)
