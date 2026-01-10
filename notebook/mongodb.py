import pandas as pd
import pymongo

df = pd.read_csv('notebook/data.csv')
print(df.head(2))

# df should be converted into dict before we push it to mongodb

data = df.to_dict(orient='records')
# data

DB_NAME = "Proj1"
COLLECTION_NAME = "Proj1-Data"
CONNECTION_URL = "url"
# above, either remove your credentials or delete the mongoDB resource bofore pushing it to github.

client = pymongo.MongoClient(CONNECTION_URL)
data_base = client[DB_NAME]
collection = data_base[COLLECTION_NAME]

# Uploading data to MongoDB
rec = collection.insert_many(data)

# Load back data from mongodb

df = pd.DataFrame(list(collection.find()))
print(df.head(2))