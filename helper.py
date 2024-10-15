import os
import google.generativeai as genai
import pandas as pd
from config import *





os.environ['GOOGLE_API_KEY'] = 'AIzaSyDxW-Zqxk3sUAegVDJnNW_UaRhSWbzU8N8'
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')


class modelanalysis:
    def indicator_summary(self,indicator, indicator_meaning, current_analysys,trend):

        prompt = f'you are a financial analyst in 3 lines summerize using this financial indicator\
            {indicator} which means\
            {indicator_meaning} has a current data analysis of {current_analysys} \
                and suggested trend of {trend}'
        summary= model.generate_content(prompt).text
        
        return summary

tickers = [
    # Technology
    'AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META', 'NFLX', 'PYPL', 'INTC', 'CSCO', 'ORCL',
    
    # Finance
    'JPM', 'BAC', 'WFC', 'GS', 'MS', 'V', 'MA', 'AXP', 'COF', 'C',
    
    # Healthcare
    'JNJ', 'PFE', 'MRK', 'UNH', 'ABT', 'LLY', 'NVO', 'BMY', 'GILD', 'BIIB',
    
    # Consumer Goods
    'PG', 'PEP', 'KO', 'MCD', 'DIS', 'HD', 'WMT', 'CMCSA', 'GIS', 'K',
    
    # Energy
    'XOM', 'CVX', 'COP', 'EOG', 'OXY', 'SLB', 'HAL', 'BKR', 'VLO', 'PSX'
]

financial_indicators = [
    "Debt-to-Equity Ratio",
    "Price-to-Book (P/B) Ratio",
    "Return on Equity (ROE)",
    "Simple Moving Average (SMA)",
    "Upgrades and Downgrades",
    "EBITDA",
    "Diluted EPS (Earnings Per Share)",
    "Revenue Growth",
    "Gross Profit"
]

financial_indicators_explanation = [
    "Debt-to-Equity Ratio: Calculated as Total Debt / Shareholders' Equity. It measures a company's financial leverage and indicates the proportion of debt used to finance the company. A high ratio suggests a higher risk of default.",
    
    "Price-to-Book (P/B) Ratio: Calculated as Market Price per Share / Book Value per Share. It compares a company's market value to its book value, often used to evaluate whether a stock is over or undervalued.",
    
    "Return on Equity (ROE): Calculated as Net Income / Shareholders' Equity. It shows how effectively a company is using its equity to generate profit. A higher ROE indicates more efficient use of equity to drive earnings.",
    
    "Simple Moving Average (SMA): Calculated by averaging a stock’s closing price over a specific period (e.g., 50 or 200 days). It helps smooth out price data to identify trends and signals potential buy or sell points.",
    
    "Upgrades and Downgrades: Analysts' recommendations based on fundamental or technical analysis. Upgrades suggest improving stock performance, while downgrades indicate expected declines in financial health or stock price.",
    
    "EBITDA: Calculated as Earnings Before Interest, Taxes, Depreciation, and Amortization. It reflects the core profitability of a company by excluding the impact of financing and non-cash expenses, making it useful for comparing companies.",
    
    "Diluted EPS (Earnings Per Share): Calculated as Net Income / Total Diluted Shares Outstanding. It measures profitability per share after accounting for all possible dilution from stock options, convertible debt, etc., providing a more conservative earnings figure.",
    
    "Revenue Growth: Calculated as (Current Period Revenue - Previous Period Revenue) / Previous Period Revenue * 100. It reflects the percentage increase in sales over a specific period and is crucial for assessing a company’s expansion potential.",
    
    "Gross Profit: Calculated as Total Revenue - Cost of Goods Sold (COGS). It measures how efficiently a company produces its goods and services by showing the profit made after covering production costs."
]

import random

indicator_df= pd.DataFrame({
    "Indicators":financial_indicators ,
    "Indicator_Meaning":financial_indicators_explanation ,
}, columns=["Indicators","Indicator_Meaning"])

#Select Tickers
random.shuffle(tickers), "shuffle"
four_tickers= tickers[:4]
#print(f'Will give analysis of these Tickers: \n{four_tickers[0]}')

class_mapping= {
    0 :indicator1(),
    1 :indicator2(),
    2 :indicator3(),
    3 :indicator4(),
    4 :indicator5(),
    5 :indicator6(),
    6 :indicator7(),
    7 :indicator8(),
    8 :indicator9(),
}
