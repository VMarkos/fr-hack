# README

## Repository Structure

```
.
├── alert_app
├── api
│   ├── application
│   │   ├── config.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── config.cpython-311.pyc
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── models.cpython-311.pyc
│   │   │   ├── routes.cpython-311.pyc
│   │   │   └── utils.cpython-311.pyc
│   │   ├── routes.py
│   │   └── utils.py
│   ├── __pycache__
│   │   └── wsgi.cpython-311.pyc
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

16 directories, 32 files
 (excluding `venv` directory)

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
http://127.0.0.1:5000/api/fishPreferredTemperature?species=Dicentrarchus labrax
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
http://127.0.0.1:5000/api/fishPreferredTemperature?species=Diplodus vulgaris
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
http://127.0.0.1:5000/api/fishPreferredTemperature?species=Pisces imaginarium
```

a self-explanatory response is returned (with a `404` status code):

```json
{
    "message": "Fish not found!"
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
