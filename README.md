# README

## Repository Structure

```
.
├── alert_app
├── api
│   ├── application
│   │   ├── config.py
│   │   ├── copernicus_bridge.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   └── copernicus_bridge.cpython-311.pyc
│   │   ├── routes.py
│   │   └── utils.py
│   └── wsgi.py
├── datasets
│   ├── FishBase
│   │   ├── medfish.csv
│   │   └── medfish.py
│   ├── GlobTherm
│   │   ├── data
│   │   │   ├── GlobalTherm_upload_02_11_17.csv
│   │   │   └── GlobalTherm_upload_10_11_17.xlsx
│   │   ├── metadata
│   │   │   ├── a_acclimation_Bennett.txt
│   │   │   ├── a_cold_Bennett.txt
│   │   │   ├── a_heat_Bennett.txt
│   │   │   ├── i_Investigation.txt
│   │   │   └── s_study_Bennett.txt
│   │   └── preprocess.py
│   ├── local
│   │   ├── copmed.nc
│   │   └── medfishtemp.csv
│   └── MedFaunaTp
│       └── MedTemp.csv
├── existing_approaches
│   └── bononi_et_al
│       └── MLtechniques.ipynb
├── implementation_log.md
├── literature
│   ├── mhw_review.pdf
│   ├── ml_solutions.pdf
│   └── references.bib
├── notes.md
├── README.md
└── requirements.txt
```

15 directories, 29 files (excluding `venv` directory)

## Requirements

All requirements are kept in `requirements.txt`, installable using pip[3].

Also, the corresponding `.gitignore` file intentionally ignores the `venv` directory, where to local virtual environment should be kept - modify adequately if needed.

## API

To get the API live and running, simply navigate to the `api` directory and run:

```
python[3] -m flask run
```

or, simply:

```
flask run
```

Prefer the first option in case you are using a virtual environment, to make sure all dependencies are configured correctly.

By default, the API is available through port 5000.

### Endpoints

The API offers the following endpoints:


#### `api/fishPreferredTemperature` (`GET`)

This endpoint, given the `species` parameter which corresponds to the desired fish species yields a JSON object including, if available:

* `species`: the species name;
* `taxon`: the species taxon;
* `pref_temp`: the species preferred temperature;
* `t_min`: the minimum survival temperature according to some metric;
* `min_metric`: the metric used to determine `t_min`;
* `t_max`: the maximum survival temperature according to some metric;
* `max_metric`: the metric used to determine `t_max`.

All data for Med Sea fish preferred temperatures come from [(MedFaunaTP, 2024)](#MedFaunaTP), enhanced with additional
information about minimum and maximum temperatures from various sources. An indicative list migh be found in [Data Sources](#DataSources).

For instance, the following `GET` request:

```
/api/fishPreferredTemperature?species=Dicentrarchus labrax
```

yields the following JSON response:

```json
{
    "max_metric": "ctmax",
    "min_metric": "ctmin",
    "pref_temp": 15.81,
    "species": "dicentrarchus labrax",
    "t_max": 34.59,
    "t_min": 5.44,
    "taxon": "fish"
}
```

Similarly, the following request:

```
/api/fishPreferredTemperature?species=Diplodus vulgaris
```

yields this response, in which min and max thermal tolerance data are missing:

```json
{
    "max_metric": "",
    "min_metric": "",
    "pref_temp": 17.9,
    "species": "diplodus vulgaris",
    "t_max": null,
    "t_min": null,
    "taxon": "fish"
}
```

Also, in case of a species not listed in our database, such as:

```
/api/fishPreferredTemperature?species=Pisces imaginarium
```

a self-explanatory response is returned (with a `404` status code):

```json
{
    "message": "Fish not found!"
}
```

#### `api/sstAt` (`GET`)

This endpoint, given lat, lon and datetime, returns the temerature at this point in space time or a corresponding error. Valid values for the above coordinates include:

* `lat`: 30.19 - 45.98
* `lon`: -17.29 - 36.29
* `time`: 2025-05-01 - 2025-09-30

For testing purposes, the API is currently sharing data from a static dataset, as downloaded from [https://data.marine.copernicus.eu/product/MEDSEA_ANALYSISFORECAST_PHY_006_013/download?dataset=cmems_mod_med_phy-tem_anfc_4.2km_P1D-m_202511](https://data.marine.copernicus.eu/product/MEDSEA_ANALYSISFORECAST_PHY_006_013/download?dataset=cmems_mod_med_phy-tem_anfc_4.2km_P1D-m_202511) using the following query:

```
copernicusmarine subset --dataset-id cmems_mod_med_phy-tem_anfc_4.2km_P1D-m --variable bottomT --variable thetao --start-datetime 2025-05-01T00:00:00 --end-datetime 2025-09-30T00:00:00 --minimum-longitude -17.29166603088379 --maximum-longitude 36.29166793823242 --minimum-latitude 30.1875 --maximum-latitude 45.97916793823242 --minimum-depth 1.0182366371154785 --maximum-depth 5.464963436126709
```

This can be directly substituted with live data, provided sufficient data availability.

For instance, the following request:

```
/api/sstAt?lat=37.18&lon=-1.27&time=2025-08-11
```

should return something along the following lines:

```json
{
  "depth": 1.018,
  "lat": 37.18000030517578,
  "lon": -1.2699999809265137,
  "sst": 27.02207374572754,
  "time": "2025-08-11 00:00:00"
}
```

## Data Sources

<a id="DataSources">Data sources</a> utilised to populate our databases.

### Fish Thermal Tolerance

While data for thermal tolerance for various species are, in general, available, we have encounted several difficulties in finding
appropriate data for Med Sea fish, even in vast databases like GlobTherm. To that end, we have utilised the resources shown below
for particular species, mostly for demonstration purposes.

| Species 		| Source								|
| --------------------- | --------------------------------------------------------------------- |
| Dicentrarchus labrax  | [https://doi.org/10.1016/j.jtherbio.2011.11.003](https://doi.org/10.1016/j.jtherbio.2011.11.003) |

## References

<a id="MedFaunaTP">MedFaunaTP</a> Valente, Salvatore; Colloca, Francesco (2024). MedFaunaTP: a dataset of thermal preferences for Mediterranean demersal and benthic macrofauna. figshare. Collection. [https://doi.org/10.6084/m9.figshare.c.6904042.v1](https://doi.org/10.6084/m9.figshare.c.6904042.v1)
