import pandas as pd


def add_pickup_day(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["pickup_day"] = df["tpep_pickup_datetime"].dt.strftime("%Y-%m-%d")
    return df


def tip_percentage(df: pd.DataFrame) -> pd.Series:
    valid_fares = df["fare_amount"] > 0

    return (
        df.loc[valid_fares, "tip_amount"]
        * 100
        / df.loc[valid_fares, "fare_amount"]
    )
