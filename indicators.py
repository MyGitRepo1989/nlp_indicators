import json
import pandas as pd
import yfinance as yf
import random
import helper
from helper import *
from config import *
import warnings


# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)
# Suppress specific runtime warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
#initilize genai
final_summary = modelanalysis()



if __name__ == "__main__":
    for i in range(1):
    
        print(f'GETTING ANALYSIS NO: {i} ')
        
        ticket_current =four_tickers[i]
        ticker_name= yf.Ticker(ticket_current)
        company_info = ticker_name.info
        ticker_name= company_info['longName']
        
        sampled_df = indicator_df.sample(n=3)
        indicators_index=sampled_df.index.to_list()
        print(f'Ticker Analysis of: {ticket_current,ticker_name}')

        for n in range(3):
            analysis=class_mapping[indicators_index[n]]
            indicator_value=analysis.get_value(four_tickers[i])
            analysis_indicator = analysis.predict(indicator_value)
            print(f"\n")
            
            print(f'Financial Indicator: {indicator_df["Indicators"][indicators_index[n]]}')
            print(f'Indicator Definition: {indicator_df["Indicator_Meaning"][indicators_index[n]]}')
            print(' ')
            print(f'Analysis: {analysis_indicator["category"]}')
            print(f'Signal: {analysis_indicator["trend"]}')
            f_analysis = final_summary.indicator_summary(indicator_df["Indicators"][indicators_index[n]],\
                indicator_df["Indicator_Meaning"][indicators_index[n]], \
                    analysis_indicator["category"],\
                        analysis_indicator["trend"])
            print(f'Analysis Summary: {f_analysis}')
            print(indicator_value)
        print(f"_______________________________ \n\n\n")
    
        
        









