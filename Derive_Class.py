import datetime as dt
import pandas as pd
from os import listdir
from os.path import isfile, join
import aqi


class Derive:
    def __init__(self):
        # init does not really do anything for this class
        pass


    def apply_aqi(self, row, aqi_measure, column_name):
        try:
            return aqi.to_iaqi(aqi_measure, str(row[column_name]), algo=aqi.ALGO_EPA)
        except IndexError:
            # the value is too big for the calculator, will calculate the max value instead.
            return 501
        except Exception as e:
            print(e)


    def calc_aqis(self, df_to_add_aqi):
        # get more information from the error...
        df_to_add_aqi['aqi_PM10'] = df_to_add_aqi.apply(lambda row: self.apply_aqi(row, aqi.POLLUTANT_PM10, "PM10"), axis=1)
        df_to_add_aqi['aqi_PM2.5'] = df_to_add_aqi.apply(lambda row: self.apply_aqi(row, aqi.POLLUTANT_PM25, "PM2.5"), axis=1)
        cols = ['aqi_PM10', 'aqi_PM2.5']
        df_to_add_aqi[cols] = df_to_add_aqi[cols].apply(pd.to_numeric, errors='coerce')


    def group_data_by_day(self,df_to_group):
        df_grouped = df_to_group.groupby(['station',"month", "day",'year'], as_index=False)[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3','TEMP','PRES','DEWP','RAIN','WSPM']].max()
        return df_grouped


    def create_date_from_string(self, df_to_clean, month_column, day_column, year_column):
        # add correct data column
        print('**************************')
        print('Creating date column')
        print('**************************')
        df_to_clean['date_string'] = df_to_clean.apply(
            lambda row: str(row[month_column]) + '-' + str(row[day_column]) + '-' + str(row[year_column]), axis=1)
        df_to_clean['date'] = df_to_clean.apply(
            lambda row: dt.datetime(row[year_column], row[month_column], row[day_column]), axis=1)
