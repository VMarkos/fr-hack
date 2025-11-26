# preprocess.py

import pandas as pd

class Preprocessor:
    def __init__(self, csv_path: str, encoding='windows-1252') -> None:
        """ `csv_path` should be a valid path towards a `csv` file. The default encoding value
        is just a convenience value for the particular use case."""

        self._data = pd.read_csv(
            csv_path,
            sep=',',
            header=0,
            encoding=encoding
        )

    def summary(self) -> pd.DataFrame:
        if self._data is not None:
            return self._data.describe()
        raise ValueError(f"Data not initialised yet.")


if __name__ == "__main__":
    DATAPATH = "data/GlobalTherm_upload_02_11_17.csv"
    pp = Preprocessor(DATAPATH)
    summary = pp.summary()
    print(summary)

