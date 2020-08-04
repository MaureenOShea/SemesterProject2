import datetime as dt
import pandas as pd
from os import listdir
from os.path import isfile, join


class Cleaner:
    def __init__(self):
        # init does not really do anything for this class
        pass


    def remove_duplicates(self,df_to_clean):
        print('**************************')
        print('Removing Duplicates')
        print('**************************')
        duplicate_rows_df = df_to_clean[df_to_clean.duplicated()]
        print('number of duplicate rows: ', len(duplicate_rows_df.index))
        df_to_clean.drop_duplicates(inplace=True)


    def drop_nulls_from_df(self,df_to_clean, drop_rows, column_names=[]):
        if column_names == []:
            column_names == column_names.append(df_to_clean.columns)
        print('**************************')
        print('Removing Nulls')
        print('**************************')

        print('- - - - - - - - - - - - - ')
        print('Before removing nulls')
        print('- - - - - - - - - - - - - ')
        print(df_to_clean.isnull().sum())  # Number of rows with nulls that we are dropping

        if (drop_rows):
            df_to_clean.dropna(inplace=True, subset=column_names)

        print('- - - - - - - - - - - - - ')
        print('After removing nulls')
        print('- - - - - - - - - - - - - ')
        print(df_to_clean.count())  # number of total rows after drop.


    def clean_data(self,df_to_clean):
        # self.create_date_from_string(df_to_clean, 'month', 'day', 'year')
        self.remove_duplicates(df_to_clean)
        # self.drop_nulls_from_df(df_to_clean, True, ['No', 'year', 'month', 'day', 'hour', 'PM2.5', 'PM10', 'SO2', 'NO2',
#                                               'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'wd', 'WSPM', 'station',
#                                               'date'])

        self.drop_nulls_from_df(df_to_clean, True, ['No', 'year', 'month', 'day', 'hour', 'PM2.5', 'PM10', 'SO2', 'NO2',
                                                  'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'wd', 'WSPM', 'station'])


    def load_csv_data(self,data_directory):
        #get the data files from the directory
        data_files = [f for f in listdir(data_directory) if isfile(join(data_directory, f)) and f.endswith(".csv")]
        df = pd.DataFrame() #initialize an empty dataframe
        for data_file in data_files:
            df_per_file = pd.read_csv(join(data_directory, data_file))
            #concatonate the df_weekly dataframe we just generated with the others
            df = pd.concat([df, df_per_file])

        # self.clean_data(df)
        return df

