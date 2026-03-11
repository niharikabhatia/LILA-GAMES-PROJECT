import pandas as pd
import pyarrow.parquet as pq
import os


def load_parquet_file(file_path):

    table = pq.read_table(file_path)
    df = table.to_pandas()

    # Decode event column
    df["event"] = df["event"].apply(
        lambda x: x.decode("utf-8") if isinstance(x, bytes) else x
    )

    return df


def load_all_data(data_dir):

    dfs = []

    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".nakama-0"):
                path = os.path.join(root, file)
                df = load_parquet_file(path)
                dfs.append(df)

    full_df = pd.concat(dfs)

    # Detect bots
    full_df["player_type"] = full_df["user_id"].apply(
        lambda x: "Human" if "-" in str(x) else "Bot"
    )
    df["ts"] = pd.to_datetime(df["ts"])
    return full_df
  