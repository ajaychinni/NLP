import pandas as pd

class Data_cleaning:
    
    def select_col(self,df,*cols):
        print(cols)
        # removing all other columns
        df1 = df[[cols]]
        # print(df1)
        # print(df1.columns)
        return df1

    def convert_to_0_1(self,df):
        #replacing nans to do
        df1 = df1.fillna(0)
        print(df1)

        #replacing 0 to 0.5 "0"   and 0.5 to 1  "1"
        df1["negativereason_confidence"] = df1["negativereason_confidence"].apply(lambda x : 0 if x<0.5 else 1)
        print(df1)

#
