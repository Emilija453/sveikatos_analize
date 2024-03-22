import pytest
import pandas as pd
from bendras_testavimui import df_from_csv, baltijos_saliu_indeksas


def test_df_from_csv():
    df_baltic = 'test_Baltic_counrties.csv'
    result = df_from_csv(df_baltic)
    expected_response = 39
    assert len(result) == expected_response


