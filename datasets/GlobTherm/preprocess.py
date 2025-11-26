# preprocess.py

import pandas as pd


class Preprocessor:
    def __init__(self, csv_path: str, encoding="windows-1252") -> None:
        """`csv_path` should be a valid path towards a `csv` file. The default encoding value
        is just a convenience value for the particular use case."""

        self._data = pd.read_csv(csv_path, sep=",", header=0, encoding=encoding)

    def summary(self) -> pd.DataFrame:
        if self._data is not None:
            return self._data.describe()
        raise ValueError(f"Data not initialised yet.")

    def filter(self, cname: str, cvals) -> None:
        clean_vals = {"_".join(x.split(" ")).lower() for x in cvals}
        print(clean_vals)
        self._data = self._data[self._data[cname].isin(clean_vals)]


def _get_csv_dataset(path: str) -> pd.DataFrame:
    medfish = pd.read_csv(
        path,
        sep=",",
        header=0,
    )
    return medfish


if __name__ == "__main__":
    DATAPATH = "data/GlobalTherm_upload_02_11_17.csv"
    MF_PATH = "../FishBase/medfish.csv"
    MFTP_PATH = "../MedFaunaTp/MedTemp.csv"
    MEDFISH = _get_csv_dataset(MF_PATH)
    MEDFAUNA = _get_csv_dataset(MFTP_PATH)
    med_species = MEDFAUNA.get("ScientificName")
    pp = Preprocessor(DATAPATH)
    pp.filter("Species", med_species)
    summary = pp.summary()
    print(summary)
