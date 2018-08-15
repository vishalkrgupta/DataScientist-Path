import pandas as pd
import os
#https://grouplens.org/datasets/movielens/

#movies  = pd.read_csv('C:\\Users\\VGupta\\source\\repos\\pyEdxProject\\pyEdxProject\\ml_dataset_small\\movies.csv',sep=',')
#print(type(movies))
#print(movies.head(15))

gs_ratings  = pd.read_csv('C:\\Users\\VGupta\\source\\repos\\pyEdxProject\\pyEdxProject\\ml_dataset_small\\ratings.csv',sep=',',parse_dates=['timestamp'])
#print(type(gs_ratings))
#print(gs_ratings.head(15))

#describe: returns count mean, st deiation, min, 25%, 50%, 75%, max values from the dataframe
print(gs_ratings['rating'].describe())

#print('gs_ratings[rating].mean: {}'.format(gs_ratings['rating'].mean()))
#3.543608255669773

#print('gs_ratings.mean: {}'.format(gs_ratings.mean()))

print('gs_ratings[rating].mean: {}; max: {}; min: {}'.format(gs_ratings['rating'].mean(), gs_ratings['rating'].max(), gs_ratings['rating'].min()))

print('gs_ratings[rating].std: {}; mode: {}'.format(gs_ratings['rating'].std(), gs_ratings['rating'].mode()))

print('gs_ratings.CORR: {}'.format(gs_ratings.corr()))

filter_1= gs_ratings['rating'] > 5
print('filter_1: {}'.format(filter_1))
filter_1.any()

filter_2= gs_ratings['rating'] > 0
print('filter_2: {}'.format(filter_2))
filter_2.all()

