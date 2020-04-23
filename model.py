from data_cleaning import Data_cleaning
import pandas as pd


class Model:
    def main(self):
        df = pd.read_csv("data/twitter-airline-sentiment/Tweets.csv")
        
        df = dc.select_col(df,"text","negativereason_confidence")
        
        
if __name__ == "__main__":
    dc = Data_cleaning()