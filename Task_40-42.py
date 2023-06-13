Задача 40
Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)


import pandas as pd
     

file_path = '/content/sample_data/california_housing_train.csv'
df = pd.read_csv(file_path, sep=',')
     

df['population'].min()
     
3.0

df[df['population'] < 500].median_house_value.mean()
     
206683.83635227982
Задача 42
Узнать какая максимальная households в зоне минимального значения population


df[df['population'] == df['population'].min()].households.max()
     
4.0