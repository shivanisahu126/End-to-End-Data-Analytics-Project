#import libraries and import csv file

import pandas as pd
import numpy as np


app= pd.read_csv("C:/Users/91913/Desktop/ps.csv")
df= pd.DataFrame(app) #convert csv file into dataframe using pandas

#exploring data

print(app.head())
print(app.info())
print(app.describe())
print(df.isnull().sum())


# handling null values and fix them with mean and mode
rating_mean =df["Rating"].mean()
content_mode =df["Content Rating"].mode()[0]
df["Rating"] = df["Rating"].replace(np.nan,rating_mean)
print(df.isnull().sum())
df["Content Rating"] = df["Content Rating"].fillna(content_mode)
print(df.isnull().sum())
currentvar_mode =df["Current Ver"].mode()[0]
df["Current Ver"] = df["Current Ver"].fillna(currentvar_mode)
andvar_mode =df["Android Ver"].mode()[0]
df["Android Ver"] = df["Android Ver"].fillna(andvar_mode)

print(df.isnull().sum())

#change case type of columns name

df.columns = df.columns.str.lower() 
df.columns = df.columns.str.replace(" ","_")
df.rename(columns={"price_(usd)":"price"},inplace=True)
print(df.info())

#install psycopg2-binary for transfer the dataframe into postgresql
""" 
here we transfer our dataframe to postgresql
to find some insights
through this process the engine load our dataframe and create a new table

"""

from sqlalchemy import create_engine

username = "postgres"
password = "admin"
host = "localhost"
port = "5432"
database = "playstore"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# this table will generated into postgresql

table_name = "application"

df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"Data sucessfully loaded")











