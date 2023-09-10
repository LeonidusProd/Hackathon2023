import pandas as pd
import numpy


df_sp_tr = pd.read_csv('supermarket_train.csv')
df_sp_val = pd.read_csv('supermarket_val.csv')
df_sp_val_tar = pd.read_csv('supermarket_val_target.csv')
#названия всех продуктов список
df_sp_tr_names = df_sp_tr.copy()
df_sp_tr_names.drop(['name', 'device_id', 'receipt_id', 'server_date', 'local_date', 'price', 'quantity', 'my_ckecker'], axis=1, inplace=True)
df_sp_tr_names.drop_duplicates(keep='last', inplace=True)
print(df_sp_tr_names)

#для каждого айди или пар айди или так далее ищем вещь которую с ним/ними брали
df_sp_tr_receipt_mean_users = df_sp_tr.copy(deep=True)
df_sp_tr_receipt_mean_users.drop(['device_id', 'server_date', 'local_date', 'price', 'quantity', 'my_ckecker', 'name'], axis=1, inplace=True)
#print(df_sp_tr_receipt_mean_users)





