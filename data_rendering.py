import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pytz as tz
import matplotlib.pyplot as plt

from datetime import datetime
from sklearn.cluster import KMeans

from sklearn.metrics import silhouette_score

# spot_ids = []

# def cut_time:

# for chunk_df in pd.read_csv('Gowalla_totalCheckins.txt', sep='\t', header=None, chunksize=10000):
#     chunk_df.columns = ['userid','timestamp','latitude','longitude','spotid']
# df = pd.read_csv('Gowalla_totalCheckins.txt', sep='\t', header=None, index_col=1)
# df.columns = ['userid','latitude','longitude','spotid']
# df['timestamp']

# df.to_csv("how_many.csv", index=False)

output = {}
# partial dataset 작업
# for chunk_df in pd.read_csv('Gowalla_totalCheckins.txt', sep='\t', header=None, chunksize=10000):
#     chunk_df.columns = ['userid','timestamp','latitude','longitude','spotid']
#     output['timestamp'] = pd.to_datetime(chunk_df.timestamp, format="%Y-%m-%dT%H:%M:%SZ").sort_values()
#     output = pd.DataFrame(output)
#     output.to_csv("test2.csv", index=False)
#     break

# partial dataset 시간 작업
# for chunk_df in pd.read_csv('Gowalla_totalCheckins.txt', sep='\t', header=None, chunksize=10000):
#     chunk_df.columns = ['userid','timestamp','latitude','longitude','spotid']
#     chunk_df.index = pd.to_datetime(chunk_df.timestamp, format="%Y-%m-%dT%H:%M:%SZ").sort_values()
#     output = chunk_df.groupby(pd.Grouper(freq='D'))
#     print(output.first().shape())
#     break


# # # 전체 dataset 작업
# chunk_df = pd.read_csv('Gowalla_totalCheckins.txt', sep='\t', header=None)
# chunk_df.columns = ['userid','timestamp','latitude','longitude','spotid']
# output['spot_id'] = chunk_df['spotid'].drop_duplicates()
# output = pd.DataFrame(output)
# print(output.shape)
# output.to_csv("test2.csv", index=True)

# 전체 dataset 시간 작업
chunk_df = pd.read_csv('Gowalla_totalCheckins.txt', sep='\t', header=None)
chunk_df.columns = ['userid','timestamp','latitude','longitude','spotid']
chunk_df.index = pd.to_datetime(chunk_df.timestamp, format="%Y-%m-%dT%H:%M:%SZ").sort_values()
temp = chunk_df.groupby(pd.Grouper(freq='D'))
sorted = temp.first()
print(sorted.shape())
sorted.to_csv("test2.csv", index=True)