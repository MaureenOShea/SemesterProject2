import unittest
from Cleaner_Class import *
from Derive_Class import *
import aqi

class Cleaning_Derive_TestCase(unittest.TestCase): # inherit from unittest.TestCase


    # Unit test to determine if the fee has been assigned correclty
    def test_load_csv_data_correctly(self):
        print("Testing Load correctly")
        cleaner = Cleaner() # create Cleaner object
        df = cleaner.load_csv_data('data')
        df_size = len(df.index)

        self.assertGreater(df_size, 0) # make sure the datframe has at least some rows.

    def test_create_timestamp_correctly(self):
        print("Testing timestamp correctly")
        deriver = Derive()  # create Cleaner object
        cleaner = Cleaner()  # create Cleaner object
        df = cleaner.load_csv_data('data')
        deriver.create_date_from_string(df, 'month', 'day', 'year')
        timestamp = df.iloc[10]['date']
        month = df.iloc[10]['month']
        day = df.iloc[10]['day']
        year = df.iloc[10]['year']

        test_ts = dt.datetime(year, month, day)

        self.assertEqual(timestamp, test_ts)  # make sure the datframe has at least some rows.

    def test_create_aqis_correctly(self):
        print("Testing aqis correctly")
        deriver = Derive()  # create Cleaner object
        cleaner = Cleaner()  # create Cleaner object
        df = cleaner.load_csv_data('data')
        cleaner.clean_data(df)
        df_group = deriver.group_data_by_day(df)
        deriver.create_date_from_string(df_group, 'month', 'day', 'year')
        deriver.calc_aqis(df)

        aqi_value = df.iloc[10]['aqi_PM10']
        PM10_value = df.iloc[10]['PM10']
        test_aqi_value = aqi.to_iaqi(aqi.POLLUTANT_PM10, PM10_value, algo=aqi.ALGO_EPA)

        self.assertEqual(aqi_value, test_aqi_value)  # make sure the datframe has at least some rows.








if __name__ == '__main__':
    unittest.main()            