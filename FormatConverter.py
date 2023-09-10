import pandas as pd

tsv_file_supermarket_train = 'C:/Users/hardc/Desktop/supermarket_train.tsv'
csv_table_supermarket_train = pd.read_table(tsv_file_supermarket_train, sep='\t')
csv_table_supermarket_train.to_csv('supermarket_train.csv', index=False)


tsv_file_supermarket_val = 'C:/Users/hardc/Desktop/supermarket_val.tsv'
csv_table_supermarket_val = pd.read_table(tsv_file_supermarket_val, sep='\t')
csv_table_supermarket_val.to_csv('supermarket_val.csv', index=False)


tsv_file_supermarket_val_target = 'C:/Users/hardc/Desktop/supermarket_val_target.tsv'
csv_table_supermarket_val_target = pd.read_table(tsv_file_supermarket_val_target, sep='\t')
csv_table_supermarket_val_target.to_csv('supermarket_val_target.csv', index=False)

