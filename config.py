import yfinance as yf
import numpy as np
import pandas as pd


#Debt to Equity
class indicator1:
    
    def __init__(self):
        # Config debt as a class attribute, accessible via self
        self.config = {
            "industry": "Technology",
            "benchmarks": {
                "Debt-Free or Minimal Debt": {"min": 0, "max": 0.25, "trend": "Positive"},
                "Low Debt": {"min": 0.25, "max": 0.5, "trend": "Positive"},
                "Moderate Debt": {"min": 0.5, "max": 0.75, "trend": "Neutral"},
                "Balanced Capital Structure": {"min": 0.75, "max": 1.25, "trend": "Positive"},
                "Increasing Leverage": {"min": 1.25, "max": 1.75, "trend": "Negative"},
                "Highly Leveraged": {"min": 1.75, "max": 2.5, "trend": "Negative"},
                "Significant Debt Risk": {"min": 2.5, "max": 3.5, "trend": "Negative"},
                "Potential Financial Strain": {"min": 3.5, "max": 5, "trend": "Negative"},
                "Severe Debt Load": {"min": 5, "max": 7, "trend": "Negative"},
                "Imminent Bankruptcy Risk": {"min": 7, "max": float('inf'), "trend": "Negative"},
            }
        }
    
    
    def get_value(self,stock_name):
        
        try:
            stock = yf.Ticker(stock_name)  
            debt_ratio= stock.balance_sheet.T['Total Debt'][-4]/stock.balance_sheet.T['Stockholders Equity'][-4]
            return round(debt_ratio,2)
        except Exception as e:
            debt_ratio = "error"
            return "error"
        


    def predict(self,debt_ratio):
        benchmarks = self.config['benchmarks']

        for category, benchmark in benchmarks.items():
            if benchmark["min"] <= debt_ratio <= benchmark["max"]:
                return {
                    "category": category,
                    "trend": benchmark["trend"]
                }

        return {
            "category": "Unknown Category",
            "trend": "Unknown Trend"
        }



#PB_ratio
class indicator2:
    
    def __init__(self):
        # Config debt as a class attribute, accessible via self
        self.config = {
                "industry": "Technology",
                "benchmarks": {
                    "Deep Undervaluation": {"min": 0, "max": 2, "trend": "Positive"},
                    "Undervaluation": {"min": 2, "max": 3.5, "trend": "Positive"},
                    "Fair Value": {"min": 3.5, "max": 6, "trend": "Neutral"},
                    "Overvaluation": {"min": 6, "max": 8, "trend": "Negative"},
                    "Significant Overvaluation": {"min": 8, "max": 12, "trend": "Negative"},
                    "Extreme Overvaluation": {"min": 12, "max": float('inf'), "trend": "Negative"},
                }
                }
    
    
    def predict(self,pb_ratio):
        
        benchmarks = self.config['benchmarks']

        for category, range in benchmarks.items():
            if range["min"] <= pb_ratio <= range["max"]:
                return {
                    "category": category,
                    "trend": range["trend"]
                }

        return {
            "category": "Unknown Category",
            "trend": "Unknown Trend"
        }   
        


    def get_value(self,stock_name):
        try:
         
            stock = yf.Ticker(stock_name)  
            Stockholder_equity= stock.balance_sheet.T['Stockholders Equity'][-4]
            market_price = stock.info['currentPrice']
            total_shares_outstanding = stock.info['sharesOutstanding']
            pb_ratio= market_price / (Stockholder_equity / total_shares_outstanding)
          
            return round(pb_ratio,2)
        except Exception as e:
            pb_ratio = "error"
            return "error"







#Return of equity change
class indicator3:
    
    def __init__(self):
        # Config debt as a class attribute, accessible via self
        self.config = {
            "industry": "Technology",
            "benchmarks": {
                "Significant Losses": {"min": float('-inf'), "max": -0.5, "trend": "Extremely Negative"},
                "Substantial Losses": {"min": -0.5, "max": -0.2, "trend": "Very Negative"},
                "Moderate Losses": {"min": -0.2, "max": 0, "trend": "Negative"},
                "Break-Even": {"min": 0, "max": 0.1, "trend": "Neutral"},
                "Low Profitability": {"min": 0.1, "max": 0.3, "trend": "Mildly Positive"},
                "Adequate Profitability": {"min": 0.3, "max": 0.5, "trend": "Positive"},
                "Strong Profitability": {"min": 0.5, "max": 0.8, "trend": "Very Positive"},
                "Exceptional Profitability": {"min": 0.8, "max": 1, "trend": "Extremely Positive"},
                "Outstanding Performance": {"min": 1, "max": float('inf'), "trend": "Exceptional"},
            }
        }
    
    
    def predict(self,roe):
        benchmarks = self.config['benchmarks']

        for category, range in benchmarks.items():
            if range["min"] <= roe <= range["max"]:
                return {
                    "category": category,
                    "trend": range["trend"]
                }

        return {
            "category": "Unknown Category",
            "trend": "Unknown Trend"
        }
   
        


    def get_value(self,stock_name):
        try:
            stock = yf.Ticker(stock_name)
            #print(stock)
            # ROE LAST QUARTER
            Net_Income_current = stock.financials.T['Net Income'][0]
            #print(Net_Income_current)
            
            Stockholders_Equity_current = stock.balance_sheet.T['Stockholders Equity'][0]
            ROE_current = Net_Income_current / Stockholders_Equity_current
            
            Net_Income_last = stock.financials.T['Net Income'][-4]
            Stockholders_Equity_last = stock.balance_sheet.T['Stockholders Equity'][-4]
            ROE_last = Net_Income_last / Stockholders_Equity_last
            
            ROE_change = ((ROE_current - ROE_last) / ROE_last) * 100
            
            if np.isnan(ROE_current) or np.isnan(ROE_change):
                return  "error"
            
            return round(ROE_current, 2)
            
        except Exception as e:
            print(f"Error: {e}")
            return  "error"




# Simple moving averages
class indicator4:
    
    def __init__(self):
        # Config debt as a class attribute, acces
        # sible via self
        self.config = {
                "industry": "Technology",
                "benchmarks": {
                    "Major Downtrend Indicates Selling Pressure": {"min": -float('inf'), "max": 20, "trend": "Extremely Negative"},
                    "Strong Downtrend with Risk of Further Decline": {"min": 20, "max": 40, "trend": "Very Negative"},
                    "Downtrend Suggests Weakening Performance": {"min": 40, "max": 50, "trend": "Negative"},
                    "Neutral Zone Limited Momentum": {"min": 50, "max": 70, "trend": "Neutral"},
                    "Uptrend Signals Gradual Improvement": {"min": 70, "max": 90, "trend": "Positive"},
                    "Early Uptrend with Growth Potential": {"min": 90, "max": 110, "trend": "Very Positive"},
                    "Consistent Uptrend Reflects Strength": {"min": 110, "max": 130, "trend": "Strong Positive"},
                    "Solid Uptrend with Positive Outlook": {"min": 130, "max": 150, "trend": "Strong Positive"},
                    "Accelerated Uptrend Suggests Strong Growth": {"min": 150, "max": 200, "trend": "Exceptional"},
                    "Rapid Growth with Elevated Volatility": {"min": 200, "max": float('inf'), "trend": "Exceptional"},
                }
            }
    
    
    def predict(self,sma_50):
            benchmarks = self.config['benchmarks']

            for category, range in benchmarks.items():
                if range["min"] <= sma_50 <= range["max"]:
                    return {
                        "category": category,
                        "trend": range["trend"]
                    }

            return {
                "category": "Unknown Category",
                "trend": "Unknown Trend"
            }
   
    def get_value(self,stock_name):
        try:
            stock = yf.Ticker(stock_name)
            data = stock.history(period="1y")
            sma_50_last= data['Close'].rolling(window=200).mean()[-1]
            return round(sma_50_last,2)
        except Exception as e:
            sma_50_last = "error"
            return "error"





# Upgrade downgrade signals
class indicator5:
    
    def __init__(self):
        # Config debt as a class attribute, acces
        # sible via self
        self.config = {"industry": "General",
                "benchmarks": {
                    "Extreme Sell Downgrade Momentum": {"down": 80, "up": 5, "main": 250, "reit": 25, "init": 25, "trend": "Negative"},
                    "Strong Sell Downgrade Momentum": {"down": 60, "up": 10, "main": 200, "reit": 20, "init": 20, "trend": "Negative"},
                    "Moderate Sell Downgrade Momentum": {"down": 40, "up": 20, "main": 150, "reit": 15, "init": 15, "trend": "Negative"},
                    "Mild Sell Downgrade Momentum": {"down": 30, "up": 25, "main": 100, "reit": 10, "init": 10, "trend": "Negative"},
                    "Hold Neutral Trend": {"down": 25, "up": 25, "main": 50, "reit": 5, "init": 5, "trend": "Neutral"},
                    "Mild Buy Upgrade Momentum": {"up": 30, "down": 20, "main": 100, "reit": 10, "init": 10, "trend": "Positive"},
                    "Moderate Buy Upgrade Momentum": {"up": 40, "down": 15, "main": 150, "reit": 15, "init": 15, "trend": "Positive"},
                    "Strong Buy Upgrade Momentum": {"up": 60, "down": 10, "main": 200, "reit": 20, "init": 20, "trend": "Positive"},
                    "Exceptional Buy Upgrade Momentum": {"up": 80, "down": 5, "main": 250, "reit": 25, "init": 25, "trend": "Positive"},
                    "Stable": {"down": 20, "up": 20, "main": 50, "reit": 5, "init": 5, "trend": "Neutral"},
                    "Increasing Optimism": {"up": 50, "down": 15, "main": 100, "reit": 10, "init": 10, "trend": "Positive"},
                    "Decreasing Optimism": {"down": 50, "up": 15, "main": 100, "reit": 10, "init": 10, "trend": "Negative"},
                    "Cautious Optimism": {"up": 40, "down": 25, "main": 75, "reit": 7, "init": 7, "trend": "Positive"},
                    "Cautious Pessimism": {"down": 40, "up": 25, "main": 75, "reit": 7, "init": 7, "trend": "Negative"},
                }
            }
    
    
    def predict(self,upgrades_dict):
            industry = self.config['industry']
            benchmarks = self.config['benchmarks']

            upgrade_counts_dict = {
                'main': upgrades_dict['main'],
                'reit': upgrades_dict['reit'],
                'init': upgrades_dict['init'],
                'up': upgrades_dict['up'],
                'down': upgrades_dict['down']
            }

            for category, benchmark in benchmarks.items():
                match = True
                for action, target in benchmark.items():
                    if action != "trend" and upgrade_counts_dict[action] < target:
                        match = False
                        break
                if match:
                    return {
                        "category": category,
                        "trend": benchmark["trend"]
                    }

            return {
                "category": "Unknown Upgrade Category",
                "trend": "Unknown Trend"
            }

   
    def get_value(self,stock_name):
        try:
            stock = yf.Ticker(stock_name)
            data = dict(stock.upgrades_downgrades['Action'].value_counts().T)
            return data
        except Exception as e:
            data = "error"
            return data
 
 #IMP half point


       
# EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization)
class indicator6:
    
    def __init__(self):
        # Config debt as a class attribute, acces
        # sible via self
        self.config = {
                    "industry": "General",
                    "benchmarks": {
                        "Extreme Contraction": {"min": -float('inf'), "max": -150, "trend": "Negative"},
                        "Severe Decline": {"min": -150, "max": -100, "trend": "Negative"},
                        "Significant Decline": {"min": -100, "max": -60, "trend": "Negative"},
                        "Moderate Decline High": {"min": -60, "max": -40, "trend": "Negative"},
                        "Moderate Decline Medium": {"min": -40, "max": -25, "trend": "Negative"},
                        "Moderate Decline Low": {"min": -25, "max": -15, "trend": "Negative"},
                        "Mild Decline": {"min": -15, "max": -5, "trend": "Negative"},
                        "Stable": {"min": -5, "max": 5, "trend": "Neutral"},
                        "Slight Growth": {"min": 5, "max": 15, "trend": "Positive"},
                        "Low Growth": {"min": 15, "max": 30, "trend": "Positive"},
                        "Moderate Growth": {"min": 30, "max": 60, "trend": "Positive"},
                        "Strong Growth": {"min": 60, "max": 100, "trend": "Positive"},
                        "Exceptional Growth": {"min": 100, "max": 222, "trend": "Positive"},
                        "Hyper Growth": {"min": 222, "max": float('inf'), "trend": "Positive"},
                    }
                }
    
    
    def predict(self,qoq_growth):
        benchmarks = self.config['benchmarks']

        for category, range in benchmarks.items():
            if range["min"] <= qoq_growth <= range["max"]:
                return {
                    "category": category,
                    "trend": range["trend"]
                }

        return {
            "category": "Unknown Category",
            "trend": "Unknown Trend"
        }
        
   
    def get_value(self,stock_name):
        try:
            stock = yf.Ticker(stock_name)
            df=stock.quarterly_income_stmt.T
            df['EBITDA'] = df['Net Income'] + df['Interest Expense'] + df['Tax Provision'] + df['Reconciled Depreciation']
            df=df[["EBITDA",'Total Revenue']]
            df = df.reset_index()
            df['EBITDA'] = pd.to_numeric(df['EBITDA'].fillna(method='ffill'), downcast='integer')
            df['Total Revenue'] = pd.to_numeric(df['Total Revenue'].fillna(method='ffill'), downcast='integer')
            # Handle missing values
            df['EBITDA'] = df['EBITDA'].interpolate(method='linear')

            # Handle missing values
            df['Total Revenue'] = df['Total Revenue'].interpolate(method='linear')

            # Calculate QoQ growth rate
            df['QoQ Growth Rate'] = (df['EBITDA'].pct_change(periods=1)) * 100

            # Calculate YoY growth rate
            df['YoY Growth Rate'] = (df['EBITDA'].pct_change(periods=4)) * 100

            # Calculate EBITDA margin
            df['EBITDA Margin'] = (df['EBITDA'] / df['Total Revenue']) * 10
            cols = ['EBITDA', 'Total Revenue', 'QoQ Growth Rate', 'YoY Growth Rate', 'EBITDA Margin']
            df[cols] = df[cols].fillna(method='ffill').apply(pd.to_numeric, downcast='integer', errors='coerce')
            df[cols] = df[cols].fillna(method='bfill').apply(pd.to_numeric, downcast='integer', errors='coerce')
            #print(df[["QoQ Growth Rate"]].mean())
            data = round(df[["QoQ Growth Rate"]].mean(),3)[0]
            return data
        except Exception as e:
            data = "error"
            return data
        
    





# Diluted EPS (Earnings Per Share)
class indicator7:
    
    def __init__(self):
        # Config debt as a class attribute, acces
        # sible via self
        self.config = {
                "industry": "General",
                "benchmarks": {
                    "Extreme Volatility, Declining": {"min": -float('inf'), "max": -20, "trend": "Negative"},
                    "High Volatility, Declining": {"min": -20, "max": -15, "trend": "Negative"},
                    "Moderate Volatility, Declining": {"min": -15, "max": -10, "trend": "Negative"},
                    "Low Volatility, Declining": {"min": -10, "max": -5, "trend": "Negative"},
                    "Stable": {"min": -5, "max": 5, "trend": "Neutral"},
                    "Low Volatility, Growing": {"min": 5, "max": 10, "trend": "Positive"},
                    "Moderate Growth": {"min": 10, "max": 15, "trend": "Positive"},
                    "High Growth": {"min": 15, "max": 25, "trend": "Positive"},
                    "Exceptional Growth": {"min": 25, "max": float('inf'), "trend": "Positive"},
                }
            }
    
    
    def predict(self,qoq_change):
            benchmarks = self.config['benchmarks']

            for category, range in benchmarks.items():
                if range["min"] <= qoq_change <= range["max"]:
                    return {
                        "category": category,
                        "trend": range["trend"]
                    }

            return {
                "category": "Unknown Category",
                "trend": "Unknown Trend"
            }

   
    def get_value(self,stock_name):
        try:
            stock = yf.Ticker(stock_name)
            df = stock.quarterly_income_stmt.T[['Diluted EPS']].dropna()
            #print(df.shape, df.columns)
            # Calculate Quarterly (QoQ) Change
            df['QoQ Change'] = df['Diluted EPS'].pct_change(periods=1)
        
            

            # Convert percentage changes to decimal format
            df['QoQ Change (%)'] = df['QoQ Change'] * 100

            #print(df[['QoQ Change (%)']].mean())
            data = round(df[['QoQ Change (%)']].mean(),3)[0]
            return data
        except Exception as e:
            data = "error"
            return data







# Revenue Growth
class indicator8:
    
    def __init__(self):
        # Config debt as a class attribute, acces
        # sible via self
        self.config = {
            "industry": "General",
                "benchmarks": {
                    "Severe Contraction": {"min": -float('inf'), "max": -30, "trend": "Negative"},
                    "Extreme Decline": {"min": -30, "max": -20, "trend": "Negative"},
                    "Significant Decline": {"min": -20, "max": -15, "trend": "Negative"},
                    "Moderate Decline": {"min": -15, "max": -10, "trend": "Negative"},
                    "Mild Decline": {"min": -10, "max": -5, "trend": "Negative"},
                    "Slight Decline": {"min": -5, "max": -2, "trend": "Negative"},
                    "Flat": {"min": -2, "max": 2, "trend": "Neutral"},
                    "Mild Growth": {"min": 2, "max": 5, "trend": "Positive"},
                    "Moderate Growth": {"min": 5, "max": 10, "trend": "Positive"},
                    "Steady Growth": {"min": 10, "max": 15, "trend": "Positive"},
                    "High Growth": {"min": 15, "max": 25, "trend": "Positive"},
                    "Exceptional Growth": {"min": 25, "max": float('inf'), "trend": "Positive"},
                     }
            }
    
    
    def predict(self,qoq_change):
        benchmarks = self.config['benchmarks']

        for category, range in benchmarks.items():
            if range["min"] <= qoq_change <= range["max"]:
                return {
                    "category": category,
                    "trend": range["trend"]
                }

        return {
            "category": "Unknown Category",
            "trend": "Unknown Trend"
        }

   
   
    def get_value(self,stock_name):
        try:
            stock = yf.Ticker(stock_name)
            df = stock.quarterly_income_stmt.T[['Total Revenue']].dropna()
            #print(df.shape, df.columns)
            # Calculate Quarterly (QoQ) Change
            df['QoQ Change'] = df['Total Revenue'].pct_change(periods=1)
        
            

            # Convert percentage changes to decimal format
            df['QoQ Change (%)'] = df['QoQ Change'] * 100

            #print(df[['QoQ Change (%)']].mean())
            data = round(df[['QoQ Change (%)']].mean(),3)[0]
            return data
        except Exception as e:
            data = "error"
            return data






# Gross Profit 
class indicator9:
    
    def __init__(self):
        # Config debt as a class attribute, acces
        # sible via self
        self.config = {
            "industry": "General",
            "benchmarks": {
                "Extreme Contraction": {"min": -float('inf'), "max": -30, "trend": "Negative"},
                "Severe Contraction": {"min": -30, "max": -20, "trend": "Negative"},
                "Significant Decline": {"min": -20, "max": -15, "trend": "Negative"},
                "Moderate Decline": {"min": -15, "max": -10, "trend": "Negative"},
                "Mild Decline": {"min": -10, "max": -5, "trend": "Negative"},
                "Slight Decline": {"min": -5, "max": -2, "trend": "Negative"},
                "Stable": {"min": -2, "max": 2, "trend": "Neutral"},
                "Low Growth": {"min": 2, "max": 5, "trend": "Positive"},
                "Moderate Growth": {"min": 5, "max": 10, "trend": "Positive"},
                "Steady Growth": {"min": 10, "max": 15, "trend": "Positive"},
                "High Growth": {"min": 15, "max": 25, "trend": "Positive"},
                "Exceptional Growth": {"min": 25, "max": float('inf'), "trend": "Positive"},
                            }
            }
    
    
    def predict(self,qoq_change):
        benchmarks = self.config['benchmarks']

        for category, range in benchmarks.items():
            if range["min"] <= qoq_change <= range["max"]:
                return {
                    "category": category,
                    "trend": range["trend"]
                }

        return {
            "category": "Unknown Category",
            "trend": "Unknown Trend"
        }

   
   
    def get_value(self,stock_name):
        try:
            stock = yf.Ticker(stock_name)
            
            df = stock.quarterly_income_stmt.T
            # List of required columns
            required_columns = ['Total Revenue', 'Selling General And Administration', 'Selling And Marketing Expense', 'Salaries And Wages']

            # Check if the columns exist before filling NaNs
            available_columns = [col for col in required_columns if col in df.columns]

            # Only apply fillna(0) to columns that are available
            df[available_columns] = df[available_columns].fillna(0)

            # Initialize Gross Profit to Total Revenue if available, else set to 0
            df['Gross Profit'] = df['Total Revenue'] if 'Total Revenue' in df.columns else 0

            # Check for each column and subtract it from Gross Profit if it exists
            if 'Selling General And Administration' in df.columns:
                df['Gross Profit'] -= df['Selling General And Administration'].fillna(0)
            if 'Selling And Marketing Expense' in df.columns:
                df['Gross Profit'] -= df['Selling And Marketing Expense'].fillna(0)
            if 'Salaries And Wages' in df.columns:
                df['Gross Profit'] -= df['Salaries And Wages'].fillna(0)

            # Display the Gross Profit column
            #print(df[['Gross Profit']])
        
            #print(df.shape)
            # Calculate Quarterly (QoQ) Change
            df=df[['Gross Profit']].dropna()
            df['QoQ Change'] = df["Gross Profit"].pct_change(periods=1)
        
            

            # Convert percentage changes to decimal format
            df['QoQ Change (%)'] = df['QoQ Change'] * 100

            #print(df[['QoQ Change (%)']].mean())
            data = round(df[['QoQ Change (%)']].mean(),3)[0]
            return data
        except Exception as e:
            data = "error"
            return data



