import pytest
import pandas as pd
from bendras_testavimui import df_from_csv


def test_df_from_csv():
    df_baltic = 'test_Baltic_counrties.csv'
    result = df_from_csv(df_baltic)
    # print(result)
    stulpeliu_kiekis_baltic = len(result.columns)
    print(stulpeliu_kiekis_baltic)
    # expected_result = 9
    # assert stulpeliu_kiekis_baltic == expected_result

    # data = list(csv.reader(f))
    # print("rows:", len(data))
    # print("columns:", len(data[0]))