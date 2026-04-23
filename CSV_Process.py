#!/usr/bin/env python3
# Download this CSV from Kaggle:  https://www.kaggle.com/datasets/markkorvin/large-metal-lyrics-archive-228k-songs 

import pandas as pd
import os

def process_metal_lyrics(file_path):
    """
    Access Technology: Local File I/O via Pandas
    Structure: CSV (Tabular)
    Pros: fast for large datasets; allows for complex filtering.
    Cons: Requires local storage; high memory usage for very large files.
    """
    if not os.path.exists(file_path):
        print("Please download the dataset from Kaggle and place it in the /data folder.")
        return

    # Using chunksize if the file is massive, or just read_csv for 228k rows
    try:
        # We only load the first 5 rows as a sample to save memory
        df = pd.read_csv(file_path, nrows=5)
        
        print("--- Metal Lyrics Archive Sample ---")
        print(df[['song', 'artist', 'genre']].to_string(index=False))
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Path relative to the script location
    data_path = os.path.join('..', 'data', 'metal_lyrics.csv')
    process_metal_lyrics(data_path)


