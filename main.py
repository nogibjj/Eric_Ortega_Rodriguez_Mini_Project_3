"""
        library file 
"""

# import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
import altair as alt

dataset = (
    "https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv"
)


def load_dataset():
    df = pl.read_csv(dataset)
    return df

def grab_mean(df, col):
    return df[col].mean()

def grab_median(df,col):
    return df[col].median() 

# def grab STD
def grab_std(df,col):
    return df[col].std()

# def grab max
def grab_max(df,col):
    return df[col].max()

def create_histogram(df , col):
    df_pd = df.to_pandas()
    
    plt.hist(df_pd[col], bins=10, edgecolor='black')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

df1 = load_dataset()
df1.head()

mean_mar = grab_mean(df1,"marijuana_use")

median_mar = grab_median(df1,"marijuana_use")

std_mar = grab_std(df1,"marijuana_use")

max_mar = grab_max(df1,"marijuana_use")

create_histogram(df1, "marijuana_use")
