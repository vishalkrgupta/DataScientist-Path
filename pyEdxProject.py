import pandas as pd
import os
#https://grouplens.org/datasets/movielens/

#movies  = pd.read_csv('C:\\Users\\VGupta\\source\\repos\\pyEdxProject\\pyEdxProject\\ml_dataset_small\\movies.csv',sep=',')
#print(type(movies))
#print(movies.head(15))

gs_ratings  = pd.read_csv('C:\\Users\\VGupta\\source\\repos\\pyEdxProject\\pyEdxProject\\ml_dataset_small\\ratings.csv',sep=',',parse_dates=['timestamp'])
print(type(gs_ratings))
print(gs_ratings.head(15))

