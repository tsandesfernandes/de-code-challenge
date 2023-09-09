
import boto3
import os

import pandas as pd
from pyarrow import parquet as pq
import awswrangler as wr

file = "part-00000-26160df0-1827-4787-a515-95ecaa2c9688.c000.gz.parquet"

parquet_file = pq.ParquetFile(file)
for i in parquet_file.iter_batches(batch_size=10):
    
    # print(i.to_pandas()['fetch_time'])
    df = i.to_pandas()
    df['fetch_time'] = df['fetch_time'].astype(str)
    # print(df['url_surtkey'])
    
    
    wr.dynamodb.put_df(
        df=df,
        table_name='challenge'
    )
    break

